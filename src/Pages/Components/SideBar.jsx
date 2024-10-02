import { useState } from 'react';
import { House, Pen, Heart, BoxArrowLeft } from 'react-bootstrap-icons';

const SideBar = ({setPage, Feed, MyPosts, LikedPosts, navSelect, setNavSelect}) => {
    return(
      <div className="side-bar">
        <div className="logo-container">
          <a className="logo-name" href="/">PIXEL</a>
        </div>
  
        <div className="user-details">
          <img className="profile-pic" src={localStorage.getItem('image')} alt="profile-pic" />
          <h1 className="name">{localStorage.getItem('fname')}</h1>
          <h1 className="handle">@{`${(localStorage.getItem('fname')).toLowerCase()}${localStorage.getItem('lname').toLocaleLowerCase()}`}</h1>
        </div>
  
        <nav>
          <ul>
            <li className={navSelect===0? "active": ""} onClick={()=>{setNavSelect(0); setPage('feed')}} ><House className='icon' />Feed</li>
            <li className={navSelect===1? "active": ""} onClick={()=>{setNavSelect(1); setPage('myPosts')}}><Pen  className='icon' /> My Posts</li>
            <li className={navSelect===2? "active": ""} onClick={()=>{setNavSelect(2); setPage('likedPosts')}}><Heart  className='icon' /> Liked Posts</li>
            <li className={navSelect===3? "active": ""} onClick={() => {
                                                                        setNavSelect(3);
                                                                        setPage('feed');
                                                                        localStorage.removeItem('fname');
                                                                        localStorage.removeItem('lname');
                                                                        localStorage.removeItem('image');
                                                                        localStorage.removeItem('email');
                                                                        window.location.replace('/login');                                                                  
                                                                      }
                                                                      }>
                                                                        <BoxArrowLeft  className='icon' />Logout</li>
          </ul>
        </nav>
      </div>
    );
}

export default SideBar;