+++
id = "ref/spell/divine-favor"
kind = "spell"
title = "Divine Favor"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_favor", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "273"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 minute
Saving throw: none
Spell resistance: no
Target: you
:::

Calling upon the strength and wisdom of a deity, you gain a +1 luck bonus on attack and weapon
damage rolls for every three caster levels you have (at least +1, maximum +3). The bonus doesn't
apply to spell damage.
