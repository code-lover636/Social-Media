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
        <div className="no-post">
          <h2 className='no-post-msg'>No Posts Found</h2>
        </div> 
      )}
    </main>
  );
}

export default MyPosts