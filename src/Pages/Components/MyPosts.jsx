import { useState, useEffect } from 'react';
import Post from './Post';

const MyPosts = ({reload, setReload, myPostList}) => {

  return (
    <main>
      {myPostList.length > 0 ? (
        myPostList.map((post, index) => (
          <Post key={index} post={post} reload={reload} setReload={setReload} /> 
        ))
      ) : (
        <div className="loader"></div> 
      )}
    </main>
  );
}

export default MyPosts