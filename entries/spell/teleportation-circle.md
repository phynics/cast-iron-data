+++
id = "ref/spell/teleportation-circle"
kind = "spell"
title = "Teleportation Circle"
aon = "SpellDisplay.aspx?ItemName=Teleportation%20Circle"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "teleportation_circle", path = "json/spells10.json" },
]
[[sources]]
publication = "core-rulebook"
page = "359"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "10 minutes"
components = "V, M (amber dust to cover circle worth 1,000 gp)"
range = "0 ft."
effects = [
  { label = "Effect", value = "5-ft.-radius circle that teleports those who activate it" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Summoner\
9: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, M (amber dust to cover circle worth 1,000 gp)
Range: 0 ft.
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: yes
Effect: 5-ft.-radius circle that teleports those who activate it
Subschool: Teleportation
:::

You create a circle on the floor or other horizontal surface that teleports, as
[greater teleport](ref/spell/teleport-greater), any creature who stands on it to a designated spot.
Once you designate the destination for the circle, you can't change it. The spell fails if you
attempt to set the circle to teleport creatures into a solid object, to a place with which you are
not familiar and have no clear description, or to another plane.

The circle itself is subtle and nearly impossible to notice. If you intend to keep creatures from
activating it accidentally, you need to mark the circle in some way.

Teleportation circle can be made permanent with a [permanency](ref/spell/permanency) spell. A
permanent teleportation circle that is disabled becomes inactive for 10 minutes, then can be
triggered again as normal.

Magic traps such as teleportation circle are hard to detect and disable. A character with the
trapfinding class feature can use the Disable Device to disarm magic traps. The DC in each case is
25 + spell level, or 34 in the case of teleportation circle.
