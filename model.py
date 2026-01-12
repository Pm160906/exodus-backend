from dataclasses import dataclass
from typing import List
from ontology import ontology_manager

@dataclass
class NarrativeSpec:
    name: str
    category: str         # myth or history
    sequence: List[str]

    def __post_init__(self):
        # every narrative is validated against the ontology.
        ontology_manager.validate_sequence(self.sequence, source=self.name)