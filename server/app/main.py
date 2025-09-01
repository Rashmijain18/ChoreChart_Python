from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello Rashmi 🚀, FastAPI is running with Python 3!"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "chorechart-api"}
