
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/about")
def about():
    return {"app": "FastAPI Tutorial", "author": "You"}





@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id == 1551:
        return {
            "user_id": user_id,
            "message": "Welcome! Access granted"
        }
    else:
        # Proper API way to block access
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )


