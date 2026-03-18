from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"status": "FastAPI is running", "user":"Saurabh"}