# judgement_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from model import NarrativeSpec
from pipeline import run_pipeline
from services import all_narratives

app = FastAPI()

Archive = all_narratives.copy()

class JudgementRequest(BaseModel):
    text: str

@app.post("/judge")
def judge_narrative(req: JudgementRequest):
    new_narrative = NarrativeSpec(
        name=f"User Narrative {len(Archive)+1}",
        category="user",
        sequence=[req.text]
    )

    Archive.append(new_narrative)

    results = run_pipeline(Archive)
    last = results[-1]

    judgement = {
        "lifecycle_phase": last["life1"][-1] if last["life1"] else "undefined",
        "triggers": last["life1"],
        "collapse_trajectory": " → ".join(last["life1"])
    }

    return judgement

