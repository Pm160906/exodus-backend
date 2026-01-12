from services import all_narratives
from pipeline import run_pipeline
from report import ReportPrinter

if __name__ == "__main__":
    results = run_pipeline(all_narratives)

    printer = ReportPrinter(results)
    printer.print_structural_parallels(threshold=0.6)
    printer.print_lifecycles()
    printer.print_phase_dictionary()