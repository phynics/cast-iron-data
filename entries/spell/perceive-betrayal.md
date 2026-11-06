+++
id = "ref/spell/perceive-betrayal"
kind = "spell"
title = "Perceive Betrayal"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "perceive_betrayal", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 4 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 minute"
components = "V, S, M (12 drops of blood), F (a silver circlet worth 500 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Inquisitor\
6: Cleric, Witch\
7: Sorcerer, Wizard
Casting time: 1 minute
Components: V, S, M (12 drops of blood), F (a silver circlet worth 500 gp)
Range: personal
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Heroes of the High Court pg 25

By donning a silver circlet anointed with blood, you gain the ability to sense traitorous intent
toward a single person to whom you defer, designated when you cast the spell. The spell alerts you
when a creature with traitorous intent is within 200 feet, although it doesn't identify the source.
By concentrating, you can learn the strength of the greatest threat, based on the following
categories.

_Ill Will:_ Someone dislikes your liege, but isn't planning to act against her.

_Plotting:_ Someone is actively conspiring against your liege.

_Imminent:_ Someone is in the process of carrying out a plot against your liege.

Creatures that are immune to mind-affecting or thought-detecting effects cannot have their intent
detected by perceive betrayal.
