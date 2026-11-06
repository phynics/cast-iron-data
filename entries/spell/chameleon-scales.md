+++
id = "ref/spell/chameleon-scales"
kind = "spell"
title = "Chameleon Scales"
source_ids = ["kobolds-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chameleon_scales", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 0 },
  { class = "Druid", level = 0 },
  { class = "Hunter", level = 0 },
  { class = "Investigator", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Sorcerer", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 0: Arcanist, Druid, Hunter, Sorcerer, Wizard\
1: Alchemist, Investigator, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Kobolds of Golarion pg 26

You temporarily alter the color of your skin, hide, or scales to another option legal for your race.
You take no penalty for using Disguise to appear as a member of a different race as long as that
race has the same type and color of skin, hide, or scales as you.
