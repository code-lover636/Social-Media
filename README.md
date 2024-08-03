![image](https://github.com/user-attachments/assets/08f2359a-d12c-4a49-beb3-e960b1cabc43)
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
   ```
   cd Social-Media
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
   streamlit run Login.py
   ```

# Screenshot of website

![image](https://github.com/user-attachments/assets/6c6e36ad-38fc-4aae-97ea-d20bd0bcac9f)

![image](https://github.com/user-attachments/assets/753edd9a-886e-4378-9dc3-defcbd6f6dc7)

![image](https://github.com/user-attachments/assets/a18bce90-bdf9-4f5b-94a8-7c269bf2851d)

![image](https://github.com/user-attachments/assets/91e5dce3-51f0-4d03-bd83-a4afc309465a)

