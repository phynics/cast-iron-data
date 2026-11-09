+++
id = "ref/spell/bloodbath"
kind = "spell"
title = "Bloodbath"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloodbath", path = "json/spells2.json" },
]
[[sources]]
publication = "horror-adventures"
page = "110"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (a ceremonial dagger)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "up to one living creature/level, no two of which can be more than 30 feet apart" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Bloodrager, Medium\
2: Arcanist, Cleric, Inquisitor, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a ceremonial dagger)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: up to one living creature/level, no two of which can be more than 30 feet apart
:::

You cut yourself with the dagger, dealing yourself 1d6 points of bleed damage. So long as you keep
taking this bleed damage, your targets each bleed for 1d6 points of damage at the beginning of their
turns. The bleed damage on any target ends if that target receives magical healing, or if your bleed
damage ends for any reason. This spell has no effect if you're immune to bleed damage or can
otherwise reduce or ignore the bleed damage to yourself.
