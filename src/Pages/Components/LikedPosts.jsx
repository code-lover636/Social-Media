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
        <div className="no-post">
          <h2 className='no-post-msg'>No Posts Found</h2>
        </div> 
      )}
    </main>
  );
}

export default LikedPosts