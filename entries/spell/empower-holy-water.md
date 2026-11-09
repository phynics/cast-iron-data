+++
id = "ref/spell/empower-holy-water"
kind = "spell"
title = "Empower Holy Water"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "empower_holy_water", path = "json/spells4.json" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "26"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one or more vials of holy water" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Paladin\
2: Alchemist, Bard, Investigator, Skald
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: one or more vials of holy water
Descriptors: good
:::

You empower a vial of holy water to deal additional damage to undead creatures. You can empower one
vial of holy water at 4th level, two at 8th level, and three at 12th level. When thrown at an undead
creature, the affected vial of holy water deals an amount of bonus damage equal to your caster level
(maximum +10) on a direct hit, and half that amount of bonus damage (maximum +5) to creatures caught
in the splash area. This additional damage is positive energy damage, and has no effect on living
creatures.
