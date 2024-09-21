import '../styles/welcome.css'

const Welcome = () => {
  return (
    <div className="welcome-body">
            {/* <img src="https://4kwallpapers.com/images/wallpapers/dark-background-abstract-background-network-3d-background-3840x2160-8324.png" alt="bg" class="bg" /> */}
            <main>
                <h1>
                    PIXEL
                </h1>
            </main>
            <a href={localStorage.getItem('email') ? "/home": "/login"}>Explore</a>
    </div>
  )
}

export default Welcome