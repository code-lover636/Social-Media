from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Tuple
from datetime import datetime
import json
import base64

import postgres as ps

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/",tags=['ROOT'])
async def root():
    return {
        "Name": "Pixel", 
        "Desc": "Social Media Platform"
    }


# Login/Register

class MyLoginData(BaseModel):
    email: str
    password: str

@app.post("/login",tags=['Login'])
async def login(data: MyLoginData):
    text = data.json()
    text = json.loads(text)
    
    name = ps.login_user(text["email"], text["password"])
    if name:
        return {
            "Status": "Success",
            "valid": "Valid",
            "fname": name[0],
            "lname": name[1],
            "image": name[2]
        }
    else:
        return {
                "Status":"Success",
                "valid": "Invalid"
        }


class MyRegisterData(BaseModel):
    fname: str
    lname: str
    dob: str
    email: str
    password: str
    image: str

@app.post("/register",tags=['Login'])
async def register(data: MyRegisterData):
    text = data.json()
    text = json.loads(text)
    image = base64.b64decode(data.image.split(",")[1]) 
    if ps.register_user(text["fname"], text["lname"], text["email"], text["password"], text["dob"], image):
        return {
            "Status": "Success",
            "valid": "Valid"
        }
    else:
        return {
                "Status":"Success",
                "valid": "Invalid"
        }

# Feed
class MyPostsData(BaseModel):
    current_email: str

@app.post("/feed", response_model=List[Tuple[int, datetime, str, str, str, int, str, int, str, str, str]], tags=['Post Related'])
async def get_feed(user_email: MyPostsData):
    user_email = user_email.json()
    user_email = json.loads(user_email)
    data = ps.fetch_all_posts(user_email["current_email"])
    formatted_data = [
        (item[0], item[1].isoformat() if isinstance(item[1], datetime) else item[1], *item[2:]) 
        for item in data
    ]
    return formatted_data


@app.post("/myposts", response_model=List[Tuple[int, datetime, str, str, str, int, str, int, str, str, str]], tags=['Post Related'])
async def get_my_posts(current_email:MyPostsData):
    email = current_email.json()
    email = json.loads(email)["current_email"]
    data = ps.fetch_my_posts(email)
    formatted_data = [
        (item[0], item[1].isoformat() if isinstance(item[1], datetime) else item[1], *item[2:]) 
        for item in data
    ]
    return formatted_data

@app.post("/likedposts", response_model=List[Tuple[int, datetime, str, str, str, int, str, int, str, str, str]], tags=['Post Related'])
async def get_liked_posts(current_email:MyPostsData):
    email = current_email.json()
    email = json.loads(email)["current_email"]
    data = ps.fetch_liked_posts(email)
    formatted_data = [
        (item[0], item[1].isoformat() if isinstance(item[1], datetime) else item[1], *item[2:]) 
        for item in data
    ]
    return data

class MyLikeData(BaseModel):
    email: str
    post_id: int
    liked: int

@app.post("/likeapost", tags=['Post Related'])
async def get_liked_posts(data:MyLikeData):
    data = data.json()
    data = json.loads(data)
    liked = False
    if data['liked']:
        ps.remove_like(data["post_id"], data["email"])
    else:
        ps.like_a_post(data["post_id"], data["email"])
        liked = True
    
    return {
        "Status": "Success",
        "like_status": liked
    }

# Create Posts
@app.post("/create", tags=['Post Related'])
async def create_post(
    title: str = Form(...),
    desc: str = Form(...),
    image: UploadFile = File(...),
    owner_email: str = Form(...),
):
    # Process the image, title, and description here
    image_content = await image.read()
    ps.add_post(title, desc, image_content, owner_email, datetime.now())
    
    return {
        "title": title,
        "desc": desc,
        "filename": image.filename,
        "content_type": image.content_type,
        "message": "Post created successfully!"
    }