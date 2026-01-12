from compare import SimilarityEngine, LifecycleAnalyzer
from ontology import phases

# takes all narratives (myth + history) and compares ONLY myth ↔ history pairs.
def run_pipeline(narratives):
    similarity_engine = SimilarityEngine()
    lifecycle_analyzer = LifecycleAnalyzer(phases)

    results = []

    for n1 in narratives:
        for n2 in narratives:
            if n1.category != n2.category:
                event_sim = similarity_engine.jaccard(n1.sequence, n2.sequence)

                life1 = lifecycle_analyzer.signature(n1.sequence)
                life2 = lifecycle_analyzer.signature(n2.sequence)

                lifecycle_sim = similarity_engine.jaccard(life1, life2)

                results.append({
                    "n1": n1,
                    "n2": n2,
                    "event_similarity": event_sim,
                    "lifecycle_similarity": lifecycle_sim,
                    "life1": life1,
                    "life2": life2
                })

    return results