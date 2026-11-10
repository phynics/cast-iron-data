+++
id = "ref/spell/resilient-sphere"
kind = "spell"
title = "Resilient Sphere"
aon = "SpellDisplay.aspx?ItemName=Resilient%20Sphere"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "resilient_sphere", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/wall-of-force" },
]
[[sources]]
publication = "core-rulebook"
page = "333"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (a crystal sphere)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "1-ft.-diameter/level sphere, centered around a creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Reflex negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Arcanist, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a crystal sphere)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Reflex negates
Spell resistance: yes
Effect: 1-ft.-diameter/level sphere, centered around a creature
Descriptors: force
:::

A globe of shimmering force encloses a creature, provided the creature is small enough to fit within
the diameter of the sphere. The sphere contains its subject for the spell's duration. The sphere
functions as a [wall of force](ref/spell/wall-of-force), except that it can be negated by
[dispel magic](ref/spell/dispel-magic). A subject inside the sphere can breathe normally. The sphere
cannot be physically moved either by people outside it or by the struggles of those within.
