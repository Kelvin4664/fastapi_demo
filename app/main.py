from fastapi import FastAPI
from app.api.endpoints import user

app = FastAPI(title="FastAPI Demo")

app.include_router(user.router, prefix="/users", tags=["users"])

#to run directly with python app/main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
