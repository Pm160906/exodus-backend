from model import NarrativeSpec

# myths are treated as symbolic memories of collapse.
# we are not preserving gods, heroes, or magic.

# we are preserving the failure pattern underneath.

myths = [
    NarrativeSpec(
        name="Mahabharata",
        category="myth",
        sequence=[
            'succession_dispute', 'betrayal',
            'exile', 'moral_decay',
            'war', 'divine_intervention',
            'destruction'
        ]
    ),

    NarrativeSpec(
        name="Ramayana",
        category="myth",
        sequence=[
            'succession_dispute', 'exile', 'abduction',
            'war', 'divine_intervention', 'restoration_of_order'
        ]
    ),

    NarrativeSpec(
        name="Trojan War",
        category="myth",
        sequence=[
            'prophecy', 'divine_intervention', 'abduction',
            'betrayal', 'war', 'destruction'
        ]
    ),

    NarrativeSpec(
        name="Ragnarok",
        category="myth",
        sequence=[
            'moral_decay', 'betrayal', 'cosmic_disorder',
            'war', 'destruction', 'rebirth'
        ]
    )
]