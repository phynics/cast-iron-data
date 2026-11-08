+++
id = "ref/spell/dimension-door"
kind = "spell"
title = "Dimension Door"
source_ids = ["core-rulebook", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dimension_door", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "you and touched objects or other touched willing creatures" },
]
duration = "instantaneous"
saving_throw = "none and Will negates (object)"
spell_resistance = "no and yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Medium, Summoner\
4: Arcanist, Bard, Magus, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: none and Will negates (object)
Spell resistance: no and yes (object)
Target: you and touched objects or other touched willing creatures
Subschool: Teleportation
:::

**Sources:** PRPG Core Rulebook pg 269

You instantly transfer yourself from your current location to any other spot within range. You
always arrive at exactly the spot desired - whether by simply visualizing the area or by stating
direction. After using this spell, you can't take any other actions until your next turn. You can
bring along objects as long as their weight doesn't exceed your maximum load. You may also bring one
additional willing Medium or smaller creature (carrying gear or objects up to its maximum load) or
its equivalent per three caster levels. A Large creature counts as two Medium creatures, a Huge
creature counts as two Large creatures, and so forth. All creatures to be transported must be in
contact with one another, and at least one of those creatures must be in contact with you.

If you arrive in a place that is already occupied by a solid body, you and each creature traveling
with you take 1d6 points of damage and are shunted to a random open space on a suitable surface
within 100 feet of the intended location.

If there is no free space within 100 feet, you and each creature traveling with you take an
additional 2d6 points of damage and are shunted to a free space within 1,000 feet. If there is no
free space within 1,000 feet, you and each creature travelling with you take an additional 4d6
points of damage and the spell simply fails.
