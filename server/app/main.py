
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import users
from .api import dashboard
from .api import child

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*","http://localhost:3000"],  # Change to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "chorechart-api"}


app.include_router(users.router)
app.include_router(dashboard.router)
app.include_router(child.router)
