import { useState, useEffect } from 'react';
import Post from './Post';

const Feed = ({reload, setReload, postList}) => {
  // const [postList, setPostList] = useState([]);

  // const current_email = localStorage.getItem('email');

  // useEffect(() => {
  //   fetch('http://127.0.0.1:8000/feed', {
  //     method: 'POST',
  //     headers: {
  //       'Content-Type': 'application/json',
  //       'Access-Control-Allow-Origin': '*',
  //     },
  //     body: JSON.stringify({"current_email": current_email}),
  //   })
  //     .then(res => {
  //       if (!res.ok) {
  //         throw new Error('Network response was not ok');
  //       }
  //       return res.json();
  //     })
  //     .then(data => {
  //       setPostList(data);
  //     })
  //     .catch(error => {
  //       console.error('Error:', error);
  //     });
  // }, [reload]); 

  return (
    <main>
      {postList.length > 0 ? (
        postList.map((post, index) => (
          <Post key={index} post={post} reload={reload} setReload={setReload} />
        ))
      ) : (
        <div className="loader"></div> 
      )}
    </main>
  );
};

export default Feed;
