+++
id = "ref/arc-bard/phrenologist"
kind = "archetype"
title = "Phrenologist"
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
replaces = ["Bardic knowledge", "Well-versed", "Jack-of-all-trades", "Inspire courage", "Inspire competence"]
alters = ["Fascinate"]
+++

The phrenologist is an expert at reading creatures' skulls, and he learns to use this knowledge to
his benefit.

**Phrenological Knowledge (Ex)**

**Ability:** A phrenologist is an expert at reading creatures' skulls. He gains
[Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus feat, and he can use the phrenology
skill unlock even if he is untrained in [Knowledge (arcana)](ref/skill/knowledge-arcana).

**Passive:** He adds [half](ref/misc/fractions-and-rounding) his class level (minimum 1) on all
Knowledge (arcana) checks for the phrenology occult skill unlock.

**Replaces:** Bardic knowledge

**Skull-Versed (Ex)**

**Ability:** A phrenologist can use knowledge gleaned from a creature's skull to tailor a
performance. All creatures on which the phrenologist has successfully used his phrenology skill
unlock take a -2 penalty on all saving throws against the phrenologist's bardic performances.

**Gained:** At 2nd Level

**Replaces:** Well-versed

**Phrenological Savant**

**Ability:** A phrenologist gains either [Psychic Maestro](ref/feat/psychic-maestro) or
[Psychic Virtuoso](ref/feat/psychic-virtuoso) as a bonus feat. If he chooses Psychic Maestro, he
must select phrenology as one of his two skill unlocks to use an additional time.

**Gained:** At 10th Level

**Replaces:** Jack-of-all-trades

**Bardic Performance**

**Info:** A phrenologist gains the following types of bardic performance.

**Skull Sonata (Su)**

**Ability:** A phrenologist learns to use the resonance of other creatures' skulls to increase sonic
damage. All enemies within 30 feet of the phrenologist that have skulls take an amount of additional
sonic damage equal to half the phrenologist's bard level (minimum 1) each time they take sonic
damage.

**Replaces:** Inspire courage

**Special:** _Skull sonata_ relies on audible components.

**In Your Head (Sp)**

**At 11th Level:** This performance's duration increases to 10 minutes per bard level.

**At 19th Level:** The duration increases to 1 hour per bard level.

**At 3rd Level:** A phrenologist can use his performance to send his own senses into another's
skull, as the spell [witness](ref/spell/witness) (DC = 10 + 1/2 the phrenologist's class level + his
Charisma modifier).

**Replaces:** Inspire competence

**Special:** _In your head_ relies on audible components.

**Fingers of Fascination (Su)**

**Ability:** When a phrenologist uses the [fascinate](ref/performance/fascinate) bardic performance,
he can send forth psychic fingers along with his performance, allowing him to study one of the
fascinated creatures with his phrenology skill unlock without touching its head physically and
without it being helpless, willing, or paralyzed. This does not spend his daily use of the
phrenology skill unlock.

**Alters:** Fascinate
