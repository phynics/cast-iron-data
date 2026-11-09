+++
id = "ref/spell/burst-with-light"
kind = "spell"
title = "Burst with Light"
source_ids = ["demon-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burst_with_light", path = "json/spells2.json" },
]
[[sources]]
publication = "demon-hunters-handbook"
page = "26"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/4 levels"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/4 levels
Saving throw: see text
Spell resistance: yes
Target: one creature
Descriptors: light
:::

The target becomes filled with intense magical light, taking 2d6 points of damage as the light
bursts from its wounds and orifices (if the target is an undead creature, it instead takes 2d8
points of damage). In addition, the creature radiates bright light in a 30-foot radius and increases
the light level by one step for an additional 30 feet beyond that area-darkness becomes dim light,
dim light becomes normal light, and normal light becomes bright light. Creatures that take penalties
in bright light take them while within the 30-foot radius of this magical light. A successful Will
save halves the damage and negates the light effect.

For every 4 character levels you possess, the light continues to fill the creature for another round
(to a maximum of 5 rounds at 20th level), though the target may make a Will save each round to halve
the damage and end the effect. Any creature adjacent to the target that fails its save and takes
damage takes half as much damage and is blinded for 1 round. A successful Reflex save halves this
damage (to a total of one-quarter the damage taken by the target) and negates the blindness effect.
