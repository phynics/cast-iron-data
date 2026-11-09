+++
id = "ref/spell/healing-warmth"
kind = "spell"
title = "Healing Warmth"
aon = "SpellDisplay.aspx?ItemName=Healing%20Warmth"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "healing_warmth", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "131"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Alchemist, Cleric, Druid, Hunter, Inquisitor, Investigator, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

> _[Ifrits](ref/race/ifrit) have access to the following spell._

This spell grants you temporary immunity to fire damage as protection from energy. As a standard
action, you may sacrifice 12 points of remaining energy absorption from the spell to heal a touched
creature of 1d8 points of damage. Healing a creature provokes an attack of opportunity. When the
spell has absorbed 12 points of fire damage per caster level (to a maximum of 120 points at 10th
level), it is discharged.
