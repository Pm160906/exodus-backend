from model import NarrativeSpec

# history is treated as real-world execution of collapse.
# again, we ignore politics and personalities.

# we only encode the structural stress and outcome.

history = [
    NarrativeSpec(
        name="Fall of Rome",
        category="history",
        sequence=[
            'moral_decay', 'political_instability', 'betrayal',
            'invasion', 'collapse'
        ]
    ),

    NarrativeSpec(
        name="French Revolution",
        category="history",
        sequence=[
            'economic_inequality', 'social_unrest', 'uprising',
            'betrayal', 'execution', 'regime_change'
        ]
    ),

    NarrativeSpec(
        name="Nazi Germany (Rise & Fall)",
        category="history",
        sequence=[
            'national_humiliation', 'propaganda', 'authoritarianism',
            'invasion', 'genocide', 'destruction', 'collapse'
        ]
    ),

    NarrativeSpec(
        name="Partition of India",
        category="history",
        sequence=[
            'foreign_interference', 'political_betrayal', 'mass_migration',
            'violence', 'trauma'
        ]
    )
]