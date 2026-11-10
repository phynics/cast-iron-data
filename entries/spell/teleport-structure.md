+++
id = "ref/spell/teleport-structure"
kind = "spell"
title = "Teleport Structure"
source_ids = ["quests-and-campaigns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "teleport_structure", path = "json/spells10.json" },
]
[[sources]]
publication = "quests-and-campaigns"
page = "29"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "8 hours"
components = "V, M (gold dust worth 50 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one building" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Arcanist, Sorcerer, Wizard
Casting time: 8 hours
Components: V, M (gold dust worth 50 gp)
Range: touch
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one building
Subschool: Teleportation
:::

You instantly teleport a building in a settlement you control to another lot or series of lots in
the same settlement district. The building to be teleported must be unoccupied, and the area to
which you wish to move the building must be cleared and unoccupied during the casting of this spell.
A building cannot be teleported to an area it would not normally be able to occupy, such as an area
adjacent to a prohibited building type. If you don't wholly own the structure, all of the
structure's owners must consent to the structure's teleportation before the spell is cast;
otherwise, it fails immediately.

This spell only functions on buildings that occupy a number of lots equal to one-fourth your caster
level (so, for instance, a 16th-level caster could use this spell on a building that occupies up to
4 lots).
