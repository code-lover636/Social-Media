import '../styles/login.css'
import { useState } from 'react';

const LoginValidation = (e, email, password) => {
  e.preventDefault();
  if(email=="" || password==""){
    alert("All fields should be filled")
  }
  else{
    fetch('http://127.0.0.1:8000/login', {
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
            window.location.replace("/home")
        }
        
      })
      .catch(error => {console.error('Error:', error); });
  };
  
}

const RegisterValidation = (e, fname, lname, dob, email, password, confirmPassword) => {
  e.preventDefault();
  if(email=="" || password=="" || fname=="" || lname=="" || confirmPassword=="" || dob==""){
    alert("All fields should be filled")
  }
  else if(password !== confirmPassword){
    alert("Passwords doesn't match");
  }
  else{
    fetch('http://127.0.0.1:8000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': "*"
      },
      body: JSON.stringify({fname, lname, dob, email, password}),
      })
      .then(res => res.json())
      .then(res=>{
        if(res.Status !== "Success"){
          alert("Login Failed");
        }
        else if(res.valid == "Invalid"){
          alert("Email Id Already Exists");
        }
        else{
            localStorage.setItem('email', email);
            localStorage.setItem('fname', fname);
            localStorage.setItem('lname', lname);
            window.location.replace("/home")
        }
        
      })
      .catch(error => {console.error('Error:', error); });
  }
}

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
      <input className="file-upload" type="file" name="file" accept="image/*" placeholder="Upload profile picture"/>
      <button className="submit" type="submit" onClick={e => RegisterValidation(e, fname, lname, dob, email, password, confirmPassword)}>Register</button>
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