+++
id = "ref/spell/shield-of-fortification"
kind = "spell"
title = "Shield of Fortification"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shield_of_fortification", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "192"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Warpriest", level = 2 },
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
Level: 1: Inquisitor, Paladin\
2: Cleric, Oracle, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You create a magical barrier that protects a target's vital areas. When the target is struck by a
critical hit or a sneak attack, there is a 25% chance that the critical hit or sneak attack is
negated and damage is instead rolled normally. This benefit does not stack with other effects that
can turn critical hits or sneak attacks into normal attacks, such as the fortification armor special
ability.
