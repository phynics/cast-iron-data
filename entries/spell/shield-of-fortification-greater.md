+++
id = "ref/spell/shield-of-fortification-greater"
kind = "spell"
title = "Greater Shield of Fortification"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_of_fortification_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shield-of-fortification" },
]
[[sources]]
publication = "advanced-class-guide"
page = "192"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Inquisitor, Paladin\
4: Cleric, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Target: creature touched
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Shield of Fortification

This spell functions as [shield of fortification](ref/spell/shield-of-fortification), except there
is a 50% chance that the critical hit or sneak attack is negated and damage is instead be rolled
normally, rather than 25%.
