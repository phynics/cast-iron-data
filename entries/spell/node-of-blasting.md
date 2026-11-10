+++
id = "ref/spell/node-of-blasting"
kind = "spell"
title = "Node of Blasting"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "node_of_blasting", path = "json/spells7.json" },
]
[[sources]]
publication = "occult-adventures"
page = "178"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["mind-affecting"]
levels = [
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 3 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "one touched object weighing no more than 10 lbs." },
]
duration = "permanent until discharged (D)"
saving_throw = "Will partial, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Occultist\
3: Medium, Mesmerist, Psychic
Casting time: 1 standard action
Components: V
Range: touch
Duration: permanent until discharged (D)
Saving throw: Will partial, see text
Spell resistance: no
Target: one touched object weighing no more than 10 lbs.
Descriptors: mind-affecting
:::

You imbue an object with psychic energy. The node of blasting unleashes a mental blast when a
creature with a mind touches the object, dealing 6d6 points of damage to the creature touching the
object and causing the creature to be staggered for 1 minute. A successful saving throw halves the
damage and negates the staggered condition.

Magic traps such as node of blasting are hard to detect and disable. A character with the
trapfinding class feature can use Disable Device to thwart node of blasting. The DCs to find a node
of blasting using Perception and to disable it using Disable Device are both equal to 25 + the
spell's level. Additionally, a creature with the read aura occult skill unlock can attempt the same
Perception check to notice a node of blasting.
