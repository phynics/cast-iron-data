+++
id = "ref/spell/thorn-javelin"
kind = "spell"
title = "Thorn Javelin"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thorn_javelin", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["poison"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "javelin-like thorn" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Druid, Hunter, Ranger, Shaman
Casting time: 1 standard action
Components: V, S
Range: 0 ft.
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Effect: javelin-like thorn
Subschool: Creation
Descriptors: poison
:::

**Sources:** Advanced Class Guide pg 196

A wooden thorn the size of a javelin (appropriate for your size) appears in your open hand. You can
wield this thorn as a javelin, and you are proficient in its use. Any creature struck by the javelin
must succeed at a Fortitude save or be sickened for 1 round. If you throw the javelin, another one
appears in your hand. Any javelin that leaves your grasp disappears at the end of your turn. Each
javelin attack you make reduces the spell's remaining duration by 1 minute. If an attack reduces the
remaining duration to 0 minutes or less, the spell ends after that attack resolves.
