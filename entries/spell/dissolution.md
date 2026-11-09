+++
id = "ref/spell/dissolution"
kind = "spell"
title = "Dissolution"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dissolution", path = "json/spells13.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "19"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Investigator", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (vial of alchemical reagents worth 50 gp)"
range = "touch"
effects = [
  { label = "Target", value = "Tiny or smaller object touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Fortitude negates (object)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Investigator\
5: Arcanist, Sorcerer, Wizard\
6: Spiritualist, Summoner
Casting time: 1 standard action
Components: V, S, M (vial of alchemical reagents worth 50 gp)
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Fortitude negates (object)
Spell resistance: no
Target: Tiny or smaller object touched
:::

You touch a Tiny or smaller item, causing the item to vanish as if it did not exist at all. The item
doesn't take damage or otherwise gain any condition; it simply ceases to be visible to or interact
with the world in any way, as if it no longer existed. The oil vanishes with the item and leaves no
residue, nor does it affect surfaces that handle or hold the item during its application. No spell
or ability short of miracle or wish can locate or affect the item while it is under the effect of
this spell. Though the item seems to not exist while under the effects of this spell, its own
reality is consistent (it ages normally, and any ongoing effects upon it continue normally). The
target object can be one size larger than Tiny for every 5 caster levels above 5th you possess.

The target item returns to existence when the spell's duration expires. An item returns to existence
in exactly the same location and condition it left. If the location no longer has room for the item,
the item takes 1d0 points of damage (bypassing [hardness](ref/umr/hardness)) and is teleported to
the nearest location that has room for it. If that location is more than 5 feet from the original
location, there is a 25% chance the item is instead shifted to a randomly determined alternate
plane.
