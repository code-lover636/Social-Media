import uvicorn
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use the PORT environment variable
    uvicorn.run("app.app:app", host="0.0.0.0", port=port)