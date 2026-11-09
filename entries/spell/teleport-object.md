+++
id = "ref/spell/teleport-object"
kind = "spell"
title = "Teleport Object"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "teleport_object", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/teleport" },
]
[[sources]]
publication = "core-rulebook"
page = "359"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "one touched object of up to 50 lbs./level and 3 cu. ft./level" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one touched object of up to 50 lbs./level and 3 cu. ft./level
Subschool: Teleportation
:::

This spell functions like [teleport](ref/spell/teleport), except that it teleports an object, not
you. Creatures and magical forces cannot be teleported.

If desired, the target object can be sent to a distant location on the Ethereal Plane. In this case,
the point from which the object was teleported remains faintly magical until the item is retrieved.
A successful targeted [dispel magic](ref/spell/dispel-magic) spell cast on that point brings the
vanished item back from the Ethereal Plane.
