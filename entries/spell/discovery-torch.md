+++
id = "ref/spell/discovery-torch"
kind = "spell"
title = "Discovery Torch"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "discovery_torch", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "228"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Bard, Inquisitor, Skald\
3: Cleric, Oracle, Warpriest
Casting time: 1 round
Components: V, S
Range: touch
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: object touched
Descriptors: light
:::

An object you touch emanates a 20-foot radius of bright light. The effect looks like a regular flame
but creates no heat and uses no oxygen. Allies within the area of this light gain a +2 enhancement
bonus on Perception and Sense Motive checks, as well as on Knowledge checks to identify monsters
that are also within the area and their special powers and vulnerabilities.

When an inquisitor casts this spell, the light emanation doubles (40-ft.-radius emanation) while
that inquisitor has a judgment active.

Light spells counter and dispel darkness spells of an equal or lower level.
