import { useState } from "react";

const CreatePosts = ({setPage, reload, setReload, setNavSelect}) => {
  const [title, setTitle] = useState("");
  const [desc, setDesc] = useState("");
  const [image, setImage] = useState(null); // Change to null to better handle file input
  
  const current_email = localStorage.getItem("email");
  const validate = async (e) => {
    console.log("hello")
    e.preventDefault();

    if (!title || !desc || !image) {
      alert("Please fill in all fields and upload an image.");
      return;
    }
    
    if (desc.length > 200) {
      alert("Description cannot exceed 200 characters.");
      return;
    }

    const formData = new FormData();
    formData.append("title", title);
    formData.append("desc", desc);
    formData.append("image", image);
    formData.append("owner_email", current_email);
  
    try {
      const response = await fetch("http://127.0.0.1:8000/create", {
        method: "POST",
        body: formData,
      });
  
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
  
      const result = await response.json();
      console.log("Post created:", result);
      setReload(!reload);
      setPage('feed');
      setNavSelect(0);

    } catch (error) {
      console.error("Error posting data:", error);
      alert("There was an error creating the post. Please try again.");
    }

    console.log("Post created:", { title, desc, image });
  };

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    const allowedTypes = ["image/jpeg", "image/png", "image/gif"];
    if (!allowedTypes.includes(file.type)) {
      alert("Please upload a valid image file (JPEG, PNG, GIF).");
      return;
    }
    // if (file.size > 3 * 1024 * 1024) {
    //   // 2MB limit
    //   alert("File size exceeds 3MB. Please upload a smaller image.");
    //   return;
    // }
    setImage(file);
  };

  return (
    <form className="create-post-container">
      <h2 className="createpost">Create Post</h2>
      <input
        type="text"
        placeholder='Post title'
        name="title"
        required
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        name="desc"
        id="desc"
        placeholder='Description max(200 characters)'
        required
        maxLength={200} // Limit to 200 characters
        onChange={(e) => setDesc(e.target.value)}
      ></textarea>
      <input
        className="file-upload"
        type="file"
        name="file"
        accept="image/*"
        required
        onChange={handleFileChange} // Use the new handler
      />
      <button type='submit' onClick={(e)=>validate(e)}>Post</button>
    </form>
  );
};

export default CreatePosts;
