# these categories define the types of stresses that can exist in a civilization.
# we intentionally ignore names, places, and characters and only care about structural pressures.


# core event types
power = {'succession_dispute', 'authoritarianism', 'political_betrayal'}
moral = {'moral_decay', 'hubris', 'national_humiliation', 'prophecy_ignored' }
divine = {'prophecy', 'divine_intervention', 'cosmic_disorder'}
social = {'economic_inequality', 'social_unrest', 'uprising', 'mass_migration', 'exile'}
violence = {'war', 'invasion', 'genocide', 'violence', 'execution'}
political = {'political_instability', 'foreign_interference', 'propaganda', 'betrayal'}
outcome = {'collapse', 'destruction', 'regime_change', 'rebirth', 'restoration_of_order',
           'trauma'}
identity = {'abduction'}

# category map
category_map = {'power': power, 'moral': moral, 'divine': divine, 'social': social,
    'violence': violence, 'political': political, 'outcome': outcome, 'identity': identity
}

# full ontology = everything we allow to exist in our universe
ontology = set().union(*category_map.values())

''' 
lifecycle phases define HOW collapse unfolds over time.
this is our model of civilizational breakdown.
'''
phases = {
    "decay": {
        "description": "Internal moral, social, or economic deterioration that weakens the stability of the system.",
        "triggers": ["economic_inequality", "moral_decay", "national_humiliation"]
    },
    "rupture": {
        "description": "A breaking point where latent tensions surface through betrayal, uprising, or power struggle.",
        "triggers": ["uprising", "betrayal", "succession_dispute"]
    },
    "violence": {
        "description": "Open conflict or mass harm through war, invasion, or systemic brutality.",
        "triggers": ["war", "invasion", "genocide", "violence"]
    },
    "collapse": {
        "description": "Structural breakdown of political or social order.",
        "triggers": ["collapse", "destruction"]
    },
    "reconstruction": {
        "description": "Reorganization or rebirth of order following breakdown.",
        "triggers": ["rebirth", "restoration_of_order", "regime_change"]
    }
}

class OntologyManager:
    def __init__(self, ontology, phases, category_map):
        self.ontology = ontology
        self.phases = phases
        self.category_map = category_map

        self.validate_phase_map()

    def validate_sequence(self, sequence, source='unknown'):
        invalid = [x for x in sequence if x not in self.ontology]
        if invalid:
            raise ValueError(f'Invalid ontology terms in {source}: {invalid}')

    def validate_phase_map(self):
        invalid = []
        
        for phase, data in self.phases.items():
            triggers = data.get("triggers", [])

        for trigger in triggers:
            if trigger not in self.ontology:
                invalid.append((phase, trigger))
                
        if invalid:
            raise ValueError(f'Invalid phase mappings found: {invalid}')

    def get_event_category(self, event):
        for category, event_set in self.category_map.items():
            if event in event_set:
                return category
        return 'unknown'

ontology_manager = OntologyManager(ontology, phases, category_map)