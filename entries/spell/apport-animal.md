+++
id = "ref/spell/apport-animal"
kind = "spell"
title = "Apport Animal"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "apport_animal", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/apport-object" },
]
[[sources]]
publication = "occult-adventures"
page = "157"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "one touched animal of Tiny or smaller size" },
]
duration = "instantaneous or 1 hour/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Druid, Hunter, Medium, Mesmerist, Psychic, Ranger, Sorcerer, Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: instantaneous or 1 hour/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one touched animal of Tiny or smaller size
Subschool: Teleportation
:::

This spell functions like [apport object](ref/spell/apport-object) except the target is an animal.
Only normal, nonmagical creatures of the animal type can be teleported.
