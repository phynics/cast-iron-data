+++
id = "ref/arc-bard/phrenologist"
kind = "archetype"
title = "Phrenologist"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Phrenologist"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phrenologist", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "occult-adventures"
page = "114"

[fields]
kind = "archetype"
features = [
  { anchor = "phrenological-knowledge", level = 1 },
  { anchor = "skull-versed", level = 2 },
  { anchor = "phrenological-savant", level = 10 },
  { anchor = "skull-sonata", level = 1 },
  { anchor = "in-your-head", level = 3 },
  { anchor = "fingers-of-fascination", level = 1 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["phrenological-knowledge"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["skull-versed"] },
  { replaces = "Jack-of-all-trades", feature = "jack-of-all-trades", by = ["phrenological-savant"] },
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["skull-sonata"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["in-your-head"] },
  { alters = "Fascinate", feature = "bardic-performance", power = "fascinate", by = ["fingers-of-fascination"] },
]
+++

The phrenologist is an expert at reading creatures' skulls, and he learns to use this knowledge to
his benefit.

## Phrenological Knowledge (Ex) {#phrenological-knowledge}

A phrenologist is an expert at reading creatures' skulls. He gains
[Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus feat, and he can use the phrenology
skill unlock even if he is untrained in [Knowledge (arcana)](ref/skill/knowledge-arcana). He adds
[half](ref/misc/fractions-and-rounding) his class level (minimum 1) on all Knowledge (arcana) checks
for the phrenology occult skill unlock. This ability replaces bardic knowledge.

## Skull-Versed (Ex) {#skull-versed}

Starting at 2nd level, a phrenologist can use knowledge gleaned from a creature's skull to tailor a
performance. All creatures on which the phrenologist has successfully used his phrenology skill
unlock take a -2 penalty on all saving throws against the phrenologist's bardic performances. This
ability replaces well-versed.

## Phrenological Savant {#phrenological-savant}

At 10th level, a phrenologist gains either [Psychic Maestro](ref/feat/psychic-maestro) or
[Psychic Virtuoso](ref/feat/psychic-virtuoso) as a bonus feat. If he chooses Psychic Maestro, he
must select phrenology as one of his two skill unlocks to use an additional time. This ability
replaces jack-of-all-trades.

## Bardic Performance {#bardic-performance}

A phrenologist gains the following types of bardic performance.

## Skull Sonata (Su) {#skull-sonata}

At 1st level, a phrenologist learns to use the resonance of other creatures' skulls to increase
sonic damage. All enemies within 30 feet of the phrenologist that have skulls take an amount of
additional sonic damage equal to half the phrenologist's bard level (minimum 1) each time they take
sonic damage. Skull sonata relies on audible components. This ability replaces inspire courage.

## In Your Head (Sp) {#in-your-head}

At 3rd level, a phrenologist can use his performance to send his own senses into another's skull, as
the spell _[witness](ref/spell/witness)_ (DC = 10 + 1/2 the phrenologist's class level + his
Charisma modifier). At 11th level, this performance's duration increases to 10 minutes per bard
level, and at 19th level, the duration increases to 1 hour per bard level. In your head relies on
audible components. This ability replaces inspire competence.

## Fingers of Fascination (Su) {#fingers-of-fascination}

When a phrenologist uses the [fascinate](ref/performance/fascinate) bardic performance, he can send
forth psychic fingers along with his performance, allowing him to study one of the fascinated
creatures with his phrenology skill unlock without touching its head physically and without it being
helpless, willing, or paralyzed. This does not spend his daily use of the phrenology skill unlock.
This ability alters fascinate.
