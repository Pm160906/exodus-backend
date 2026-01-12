from myths import myths
from history import history
from pipeline import run_pipeline
from ontology import phases

all_narratives = myths + history

def get_all_results():
    return run_pipeline(all_narratives)


def get_structural_parallels(threshold=0.6):
    results = get_all_results()
    parallels = []

    for r in results:
        if r["lifecycle_similarity"] >= threshold:
            parallels.append({
                "myth": r["n1"].name,
                "history": r["n2"].name,
                "lifecycle_similarity": r["lifecycle_similarity"],
                "life1": r["life1"],
                "life2": r["life2"]
            })

    return parallels


def get_lifecycle_signatures():
    results = get_all_results()
    signatures = {}

    for r in results:
        name = r["n1"].name

        if name not in signatures:
            signatures[name] = {
                "category": r["n1"].category,
                "signature": r["life1"]
            }

    return signatures


def get_phase_dictionary():
    return {
        phase: {
            "description": data["description"]
        }
        for phase, data in phases.items()
    }