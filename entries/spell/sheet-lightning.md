+++
id = "ref/spell/sheet-lightning"
kind = "spell"
title = "Sheet Lightning"
aon = "SpellDisplay.aspx?ItemName=Sheet%20Lightning"
source_ids = ["rival-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sheet_lightning", path = "json/spells9.json" },
]
[[sources]]
publication = "rival-guide"
page = "23"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "20-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Druid, Hunter, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: 20-ft.-radius spread
Descriptors: electricity
:::

You create a dazzling flash of electricity that fills the target area. Sheet lightning inflicts 1
point of electricity damage to all creatures within the area of effect (no save). The true power of
the spell, though, lies not in the damage it inflicts but in the overwhelming pain the lightning
creates. The sudden flash and jolt dazes living creatures for 1 round if they fail a saving throw.
Creatures that save are instead dazzled for 1 round. Any creature wearing metal armor takes a -2
penalty to its saving throw against this spell.
