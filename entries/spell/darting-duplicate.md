+++
id = "ref/spell/darting-duplicate"
kind = "spell"
title = "Darting Duplicate"
aon = "SpellDisplay.aspx?ItemName=Darting%20Duplicate"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darting_duplicate", path = "json/spells3.json" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 swift action"
components = "V, S"
range = "5 ft."
effects = [
  { label = "Effect", value = "visual figment of the caster" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Antipaladin, Arcanist, Bard, Magus, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 swift action
Components: V, S
Range: 5 ft.
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Effect: visual figment of the caster
Subschool: Figment
:::

An illusory duplicate of you steps clumsily into an adjacent square, presenting a tempting target
before winking out of existence. Any creature that threatens that square must succeed at a Will save
or make an attack of opportunity against the image. The image's AC is equal to 10 + 1/2 your caster
level, but as a figment, the image is unaffected by any attack.
