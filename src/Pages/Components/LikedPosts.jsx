import { useState, useEffect } from 'react';
import Post from './Post';

const LikedPosts = ({reload, setReload, likedPostList}) => {

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