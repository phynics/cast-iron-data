+++
id = "ref/spell/dazzling-blade-mass"
kind = "spell"
title = "Mass Dazzling Blade"
source_ids = ["rival-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dazzling_blade_mass", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dazzling-blade" },
]
[[sources]]
publication = "rival-guide"
page = "5"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Pattern"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 swift action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one metal weapon/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes (harmless, object)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 swift action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one metal weapon/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates (see text)
Spell resistance: yes (harmless, object)
Subschool: Pattern
:::

### Mass Dazzling Blade

This spell functions like [dazzling blade](ref/spell/dazzling-blade), except that it affects
multiple weapons. Each wielder of a dazzling blade can discharge the weapon's effect to attempt to
blind a foe independently of the others.
