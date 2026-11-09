+++
id = "ref/spell/curse-water"
kind = "spell"
title = "Curse Water"
aon = "SpellDisplay.aspx?ItemName=Curse%20Water"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_water", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "263"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 minute"
components = "V, S, M (5 lbs. of powdered silver worth 25 gp)"
range = "touch"
effects = [
  { label = "Target", value = "flask of water touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 minute
Components: V, S, M (5 lbs. of powdered silver worth 25 gp)
Range: touch
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: flask of water touched
Descriptors: evil
:::

This spell imbues a flask (1 pint) of water with negative energy, turning it into unholy water.
Unholy water damages good outsiders the way [holy water](ref/eq-weapon/holy-water) damages undead
and evil outsiders.
