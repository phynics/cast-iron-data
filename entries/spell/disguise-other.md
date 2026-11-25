+++
id = "ref/spell/disguise-other"
kind = "spell"
title = "Disguise Other"
aon = "SpellDisplay.aspx?ItemName=Disguise%20Other"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disguise_other", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/disguise-self" },
]
[[sources]]
publication = "ultimate-magic"
page = "217"

[fields]
kind = "spell"
school = "illusion"
subschools = ["glamer"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Bard, Inquisitor, Medium, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: creature touched
Subschool: glamer
:::

### Disguise Other

This spell functions as [disguise self](ref/spell/disguise-self), except you can disguise either
yourself or another creature.
