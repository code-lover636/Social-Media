import '../styles/login.css'
import { useState } from 'react';

const LoginValidation = (e, email, password) => {
  e.preventDefault();
  if(email=="" || password==""){
    alert("All fields should be filled")
  }
  else{
    fetch('http://0.0.0.0:8000/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': "*"
      },
      body: JSON.stringify({"email":email, "password":password,}),
      })
      .then(res => res.json())
      .then(res=>{
        if(res.Status !== "Success"){
          alert("Login Failed");
        }
        else if(res.valid == "Invalid"){
          alert("Invalid Email Id or Password");
        }
        else{
            localStorage.setItem('email', email);
            localStorage.setItem('fname', res.fname);
            localStorage.setItem('lname', res.lname);
            localStorage.setItem('image', `data:image/png;base64,${res.image}`);
            window.location.replace("/home");
        }
        
      })
      .catch(error => {console.error('Error:', error); });
  };
  
}

const RegisterValidation = (e, fname, lname, dob, email, password, confirmPassword, image) => {
  e.preventDefault();
  
  // Validation for empty fields
  if (email === "" || password === "" || fname === "" || lname === "" || confirmPassword === "" || dob === "") {
    alert("All fields should be filled");
    return;
  }
  
  // Validation for password match
  if (password !== confirmPassword) {
    alert("Passwords don't match");
    return;
  }

  // Convert the image file to Base64 before sending it or storing it
  const reader = new FileReader();
  reader.onloadend = () => {
    const base64Image = reader.result; // Base64 string of the image
    
    // Send data to the backend
    fetch('https://social-media-u5pv.onrender.com/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': "*"
      },
      body: JSON.stringify({ fname, lname, dob, email, password, image: base64Image }),
    })
    .then(res => res.json())
    .then(res => {
      if (res.Status !== "Success") {
        alert("Registration Failed");
      } else if (res.valid === "Invalid") {
        alert("Email ID already exists");
      } else {
        // Store data in localStorage
        localStorage.setItem('email', email);
        localStorage.setItem('fname', fname);
        localStorage.setItem('lname', lname);
        localStorage.setItem('image', base64Image);  // Store Base64 image in localStorage
        window.location.replace("/home");
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  if (image) {
    reader.readAsDataURL(image); // Convert image file to Base64
  } else {
    alert("Please upload an image");
  }
};


const LoginSection = ({setCurrentPage}) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  return(
    <form className="login-form">
      <h1 className="heading">Login</h1>
      <input type="text" placeholder="Email" className="name" required onChange={(e)=>{setEmail(e.target.value)}} />
      <input type="password" placeholder="Password" className="name" required onChange={(e)=>{setPassword(e.target.value)}} />
      <button className="submit" type="submit" onClick={e => LoginValidation(e, email, password )}>Login</button>
      <small>New User? 
        <div id="register" onClick = {()=>{
          setCurrentPage(0);
        }}>Create account</div>
      </small>
    </form>
  );
}

const RegisterSection = ({setCurrentPage}) => {
  const [fname, setFname] = useState("");
  const [lname, setLname] = useState("");
  const [dob, setDob] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [image, setImage] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    const allowedTypes = ["image/jpeg", "image/png", "image/gif"];
    if (!allowedTypes.includes(file.type)) {
      alert("Please upload a valid image file (JPEG, PNG, GIF).");
      return;
    }
    // if (file.size > 3 * 1024 * 1024) {
    //   // 2MB limit
    //   alert("File size exceeds 3MB. Please upload a smaller image.");
    //   return;
    // }
    setImage(file);
  };

  return(
    <form className="login-form register-form">
      <h1 className="heading">Register</h1>
      <input type="text" placeholder="First Name" className="name" required onChange={(e)=>{setFname(e.target.value)}}/>
      <input type="text" placeholder="Second Name" className="name" required onChange={(e)=>{setLname(e.target.value)}}/>
      <input type="email" placeholder="Email ID" className="name" required onChange={(e)=>{setEmail(e.target.value)}}/>
      <input type="date" placeholder="Date Of Birth" className="name" required onChange={(e)=>{setDob(e.target.value)}}/>
      <input type="password" placeholder="Password" className="name" required onChange={(e)=>{setPassword(e.target.value)}}/>
      <input type="password" placeholder="Confirm Password" className="name" required onChange={(e)=>{setConfirmPassword(e.target.value)}}/>
      <label htmlFor="file">Upload profile picture</label>
      <input className="file-upload" type="file" name="file" accept="image/*" placeholder="Upload profile picture" onChange={handleFileChange} />
      <button className="submit" type="submit" onClick={e => RegisterValidation(e, fname, lname, dob, email, password, confirmPassword, image)}>Register</button>
      <small>Already a memeber? <div id="login" onClick={()=>{
        setCurrentPage(1);
      }}>Log in</div> </small>
    </form>
  );
}


const Login = ({}) => {
  const [currentPage, setCurrentPage] = useState(1);

  return (
    <div className="login-body">
      <section className="login-sec">
            <img src="https://t3.ftcdn.net/jpg/03/88/34/96/360_F_388349679_22fgWbI5QO72gPO7LqZHF08v0Cyvb37U.jpg" alt="side-image" />
            {currentPage?<LoginSection setCurrentPage={setCurrentPage} />: <RegisterSection setCurrentPage={setCurrentPage} />}            
      </section>
    </div>
  );
}

export default Login;