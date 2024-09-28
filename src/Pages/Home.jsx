import { useEffect, useState } from 'react'

import { Feed, MyPosts, LikedPosts, CreatePosts, SideBar } from './Components'
import '../styles/home.css'


const Home = () => {
  const [page, setPage] = useState('feed');
  const [reload, setReload] = useState(false);
  const [navSelect, setNavSelect] = useState(0);

  if (!localStorage.getItem('email')) {
    window.location.replace("/login");
  }

  const current_email = localStorage.getItem('email');
  const [postList, setPostList] = useState([]);
  const [myPostList, setMyPostList] = useState([]);
  const [likedPostList, setLikedPostList] = useState([]);

  // Fetch functions
  const fetchFeed = () => {
    fetch('http://0.0.0.0:8000/feed', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ current_email }),
    })
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then(data => {
        setPostList(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const fetchMyPosts = () => {
    fetch('http://0.0.0.0:8000/myposts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ current_email }),
    })
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then(data => {
        setMyPostList(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  const fetchLikedPosts = () => {
    fetch('http://0.0.0.0:8000/likedposts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ current_email }),
    })
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json();
      })
      .then(data => {
        setLikedPostList(data);
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };

  // useEffect to fetch data based on reload
  useEffect(() => {
    fetchFeed();
    fetchMyPosts();
    fetchLikedPosts();
  }, [reload]);


  const renderComponent = () => {
    switch (page) {
      case 'feed':
        return <Feed reload={reload} setReload={setReload} postList={postList} />;
      case 'myPosts':
        return <MyPosts reload={reload} setReload={setReload} myPostList={myPostList}/>;
      case 'likedPosts':
        return <LikedPosts reload={reload} setReload={setReload} likedPostList={likedPostList}/>;
      case 'createPosts':
        return <CreatePosts setPage={setPage} reload={reload} setReload={setReload} setNavSelect={setNavSelect}/>;
      default:
        return <Feed />;
    }
  };

  return (
    <div className="home-body">
      <button className="create-post" onClick={()=>{setPage('createPosts')}}>+ Create Post</button>
      <SideBar setPage={setPage} Feed={Feed} MyPosts={MyPosts} LikedPosts={LikedPosts} navSelect={navSelect} setNavSelect={setNavSelect}/>
      {renderComponent()}
    </div>
  )
}

export default Home