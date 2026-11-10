+++
id = "ref/spell/alchemical-tinkering"
kind = "spell"
title = "Alchemical Tinkering"
aon = "SpellDisplay.aspx?ItemName=Alchemical%20Tinkering"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alchemical_tinkering", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "155"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "firearm or alchemical item touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Red Mantis Assassin, Sorcerer, Witch, Wizard\
2: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (object)
Spell resistance: yes
Target: firearm or alchemical item touched
:::

> _[Ratfolk](ref/race/ratfolk) have access to the following spell._

You transform one alchemical item or firearm into another alchemical item or firearm of the same or
lesser cost. Magic items are unaffected by this spell. At the end of the spell's duration,
alchemical items used while transformed are destroyed and do not return to a usable state and
firearms transformed revert back to their original type.
