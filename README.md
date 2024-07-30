# Overview
This project entails the development of a simplified social networking platform centered around the creation and sharing of user-generated content. The platform will facilitate user interaction through post creation, liking, and viewing. To ensure a seamless user experience, the platform will incorporate user registration and authentication mechanisms. The core functionalities will include posting, liking, and displaying content in a user-friendly format. The project will focus on building a robust foundation for understanding the underlying database management principles required for such platforms.

# Features
### User-related functionalities:
- User Registration: New users can create accounts on the platform.
- Authentication: Registered users can log in to access their accounts.

### Post-related functionalities:
- Post Creation: Users can create new posts with a title, description, and image.
- Post Display: Users can view all posts, their own posts, and posts they have liked.
- Post Interaction: Users can like other users' posts.
- Post Management: Users can update or delete their own posts.

### Feed-related functionalities:
- Feed Display: The platform will show a feed of posts.
- Feed Ordering: Posts in the feed will be ordered by date and number of likes.

# Technologies used
*Read documentation*
- [Python](https://www.w3schools.com/python/) (backend)
- [Streamlit](https://docs.streamlit.io/) (frontend)
- [MySQL](https://www.w3schools.com/MySQL/default.asp) (database)

# Installation and Setup

1. Download and install Python, MySQL and Git
2. Clone this repository
   
   ```
   git clone https://github.com/code-lover636/Social-Media.git
   ```
4. Creating virtual environment
   ```
   python -m venv <venv name>
   ```
5. Activating virtual environment
   
   - For linux
   ```
   . <venv name>/bin/activate
   ```
   - For windows
   ```
   <venv name>\Scripts\activate
   ```
7. Install libraries and dependencies
   ```
   pip install -r requirements.txt
   ```
8. Create a .env file with the following content
   ```
   MYSQL_DB_PASSWORD=<your MySQL password>
   ```
9. Run the following command and click the link (if not already opened)
   ```
   streamlit run main.py
   ```

# Screenshot of website

![image](https://github.com/user-attachments/assets/b7995c24-1ad2-433a-9721-eb25d8e7973b)

![image](https://github.com/user-attachments/assets/a5fb57c9-04b1-416f-a1a1-23dee5abcd17)


