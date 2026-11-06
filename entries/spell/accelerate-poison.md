+++
id = "ref/spell/accelerate-poison"
kind = "spell"
title = "Accelerate Poison"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "accelerate_poison", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a thorn)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Druid, Hunter, Occultist, Ranger, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a thorn)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Descriptors: poison
:::

**Sources:** Advanced Player's Guide pg 201

You hasten the onset of poison in the target. If the poison normally has an onset time, its effects
begin immediately. If the poison has no onset time, its frequency is doubled, requiring two saving
throws and inflicting damage twice per round or minute, though its duration is halved. Accelerate
poison does not change the cure condition for the poison. If the target is affected by more than one
poison, you may choose which is affected if you administered the poison; otherwise, randomly
determine which poison is affected.
