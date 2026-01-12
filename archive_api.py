from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services import (
    get_structural_parallels,
    get_lifecycle_signatures,
    get_phase_dictionary
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/parallels")
def parallels():
    return get_structural_parallels()


@app.get("/lifecycles")
def lifecycles():
    return get_lifecycle_signatures()


@app.get("/phases")
def phases():
    return get_phase_dictionary()