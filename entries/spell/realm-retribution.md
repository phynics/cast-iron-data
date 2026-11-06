+++
id = "ref/spell/realm-retribution"
kind = "spell"
title = "Realm Retribution"
source_ids = ["chronicle-of-legends"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "realm_retribution", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 8 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Will negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Inquisitor, Warpriest\
8: Cleric, Oracle
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Will negates (see text)
Spell resistance: no
Target: creature touched
Subschool: Teleportation
:::

**Sources:** Chronicle of Legends pg 14

All attacks made by the target match your alignment, counting as either chaotic, evil, good, or
lawful as appropriate. If your alignment includes multiple alignment components, such as lawful
good, you select one alignment component to impart to the target. Whenever the target confirms a
critical hit against or takes damage from a creature, that creature must attempt a Will save. On a
failed save, the creature is sent to the Outer Plane matching your alignment, as per
[plane shift](ref/spell/plane-shift), and the spell ends. A warpriest treats this spell as a
6th-level cleric spell for the purposes of preparing the spell, determining DCs, and so forth.
