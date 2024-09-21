import { useState, useEffect } from 'react';
import Post from './Post';

const Feed = ({reload, setReload, postList}) => {

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
