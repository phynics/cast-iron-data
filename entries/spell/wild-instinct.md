+++
id = "ref/spell/wild-instinct"
kind = "spell"
title = "Wild Instinct"
source_ids = ["heroes-of-the-wild"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_instinct", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "8 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Bloodrager, Druid, Hunter, Ranger, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 8 hours
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Heroes of the Wild pg 31

This spell sharpens your senses, allowing you to perceive threats you would otherwise miss. You
become aware of sounds and smells you would normally overlook, and even retain the ability to detect
threats when soundly asleep. For the duration of the spell, you gain a +5 bonus on Perception checks
to act in a surprise round. Additionally, you don't take a penalty on Perception checks while
sleeping, and can choose to wake if you notice a threat while asleep.
