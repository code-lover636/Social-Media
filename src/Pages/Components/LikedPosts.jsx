import { useState, useEffect } from 'react';
import Post from './Post';

const LikedPosts = ({reload, setReload, likedPostList}) => {

  // const [likedPostList, setLikedPostList] = useState([]);
  // const current_email = localStorage.getItem('email');

  // useEffect(() => {
  //   fetch('http://127.0.0.1:8000/likedposts', {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Access-Control-Allow-Origin': '*',
  //     },
  //     body: JSON.stringify({current_email}),
  //   })
  //     .then(res => {
  //       if (!res.ok) {
  //         throw new Error('Network response was not ok');
  //       }
  //       return res.json();
  //     })
  //     .then(data => {
  //       setLikedPostList(data);
  //       console.log(data);
  //     })
  //     .catch(error => {
  //       console.error('Error:', error);
  //     });
  // }, [reload]); 

  return (
    <main>
      {likedPostList.length > 0 ? (
        likedPostList.map((post, index) => (
          <Post key={index} post={post} reload={reload} setReload={setReload} /> // Use a key prop for each item
        ))
      ) : (
        <div className="loader"></div> 
      )}
    </main>
  );
}

export default LikedPosts