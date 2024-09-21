import { useState } from 'react';
import { SuitHeart, SuitHeartFill } from 'react-bootstrap-icons';

const Post = ({ post, reload, setReload }) => {
  const [liked, setLiked] = useState(post[7]); // Changed to boolean for clarity

  const current_email = localStorage.getItem('email');
  const handleLikeToggle = () => {
    setLiked(!liked);

    if(liked)
      post[5] -= 1
    else
      post[5] += 1

    fetch('https://social-media-u5pv.onrender.com/likeapost', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify({"email": current_email, "post_id": post[0]}),
    })
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json(); // Parse JSON from response
      })
      .then(data => {
        if(data.like_status){
          setLiked(true)
        }
        else{
          setLiked(false)
        }
        setReload(!reload)
      })
      .catch(error => {
        console.error('Error:', error);
      });
  };
  return (
    <div className="post-container">
      <div className="owner-container">
        <img
          src="https://play-lh.googleusercontent.com/_qUtBpMVsGY-CLPx2DreAENHAbr4KHwBGn2w_3jhGSzoRVFRKn0SXUaK0wXSU0SJ7A=w240-h480-rw"
          alt=""
          className="profile-pic"
        />
        <div className="name-grp">
          <h2 className="owner-name">John Wick</h2>
          <h2 className="owner-handle">{post[4]}</h2>
        </div>
      </div>
      <img
        src={`data:image/png;base64,${post[6]}`}
        alt="post image"
        className="post-img"
      />
      <div className="controls">
        <p className="date">{new Date(post[1]).toLocaleDateString(undefined, {day: 'numeric', month: 'long', year: 'numeric'})}</p>
        <p className="like-count">{post[5]} people liked</p>
        <button className="like-btn" onClick={handleLikeToggle}>
          {liked ? <SuitHeartFill className="icon" /> : <SuitHeart className="icon" />}
          Like
        </button>
      </div>
      <h2 className="post-title">{post[2]}</h2>
      <p className="post-desc">{post[3]}</p>
    </div>
  );
};

export default Post;

