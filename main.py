from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import routes

app = FastAPI()

# Serve the static directory under /static
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include your API routes
app.include_router(routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CV Summarization API"}
