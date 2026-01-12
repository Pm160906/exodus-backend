from services import get_phase_dictionary

class ReportPrinter:
    def __init__(self, results):
        self.results = results

    def print_structural_parallels(self, threshold=0.6):
        print("\n--- Structural Parallels (Myth ↔ History) ---")

        for r in self.results:
            # only show strong matches & avoid false parallels; keeps output meaningful
            if r["lifecycle_similarity"] >= threshold:
                print(
                    f'{r["n1"].name}  <-->  {r["n2"].name}  | '
                    f'lifecycle similarity = {round(r["lifecycle_similarity"], 2)}'
                )

    def print_lifecycles(self):
        print("\n--- Lifecycle Signatures ---")

        seen = set()

        for r in self.results:
            n = r["n1"]
            if n.name not in seen:
                # shows the collapse shape of each narrative.
                # allows visual inspection of how different stories break.
                print(f'{n.name} ({n.category}) → {r["life1"]}')
                seen.add(n.name)

    def print_phase_dictionary(self):
        print("\n--- Phase Dictionary ---\n")
        
        phases = get_phase_dictionary()
        for phase, info in phases.items():
            print(f'{phase.upper()}')
            print(f'  {info["description"]}\n')
