import { SuitHeart, SuitHeartFill } from 'react-bootstrap-icons';

const Post = ({ post, reload, setReload }) => {
  // console.log(post[2], post[7])
  const current_email = localStorage.getItem('email');
  const handleLikeToggle = () => {
    console.log("clicked like")
    if(post[7])
      post[5] -= 1
    else
      post[5] += 1

    fetch('http://0.0.0.0:8000/likeapost', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify({"email": current_email, "post_id": post[0], 'liked': post[7]}),
    })
      .then(res => {
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        return res.json(); // Parse JSON from response
      })
      .then(data => {
        console.log(data.like_status)
        if(data.like_status){
          post[7] = true
        }
        else{
          post[7] = false
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
          src={`data:image/png;base64,${post[10]}`}
          alt="profile picture"
          className="profile-pic"
        />
        <div className="name-grp">
          <h2 className="owner-name">{`${post[8]} ${post[9]}`}</h2>
          <h2 className="owner-handle">@{`${post[8].toLowerCase()}${post[9].toLowerCase()}`}</h2>
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
        <button className="like-btn" onClick={() => handleLikeToggle()}>
          {post[7]? <SuitHeartFill className="icon" /> : <SuitHeart className="icon" />}
          Like
        </button>
      </div>
      <h2 className="post-title">{post[2]}</h2>
      <p className="post-desc">{post[3]}</p>
    </div>
  );
};

export default Post;

