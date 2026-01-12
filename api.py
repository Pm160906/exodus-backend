from fastapi import FastAPI
from archive_api import app as archive_app
from judgement_api import app as judgement_app

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Exodus backend alive"}

app.mount("/archive", archive_app)
app.mount("/judge", judgement_app)