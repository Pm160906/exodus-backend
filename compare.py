# measures how much two sequences overlap.
class SimilarityEngine:
    def jaccard(self, seq1, seq2):
        set1 = set(seq1)
        set2 = set(seq2)

        intersection = set1.intersection(set2)
        union = set1.union(set2)

        if not union:
            return 0.0

        return len(intersection) / len(union)

    def ordered(self, seq1, seq2):
        matches = 0
        min_len = min(len(seq1), len(seq2))

        for i in range(min_len):
            if seq1[i] == seq2[i]:
                matches += 1

        if min_len == 0:
            return 0.0

        return matches / min_len


# converts raw events into structural shapes.
class LifecycleAnalyzer:
    def __init__(self, phases):
        self.phases = phases

    def signature(self, sequence):
        signature = []

        for phase, data in self.phases.items():
            triggers = data["triggers"]

            if any(event in triggers for event in sequence):
                signature.append(phase)

        return signature