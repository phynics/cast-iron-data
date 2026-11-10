+++
id = "ref/spell/plague-carrier"
kind = "spell"
title = "Plague Carrier"
aon = "SpellDisplay.aspx?ItemName=Plague%20Carrier"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plague_carrier", path = "json/spells7.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "231"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease", "evil"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Druid, Hunter, Oracle, Warpriest\
5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes
Target: creature touched
Descriptors: disease, evil
:::

The target's natural attacks carry filth fever (DC 10 + 1/2 of the creature's Hit Dice + creature's
Con modifier).
