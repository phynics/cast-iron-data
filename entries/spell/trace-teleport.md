+++
id = "ref/spell/trace-teleport"
kind = "spell"
title = "Trace Teleport"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "trace_teleport", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "226"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a magnifying lens)"
range = "40 ft."
effects = [
  { label = "Area", value = "40-ft.-radius emanation centered on you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Psychic\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a magnifying lens)
Range: 40 ft.
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Area: 40-ft.-radius emanation centered on you
:::

You immediately become aware of any teleportation effects that begin or end within the spell's area.
The spell's area radiates from you and moves as you move. You know the exact origin point of any
teleportation effect that originates within the spell's area, and the exact end point of any
teleportation effect that terminates within the spell's area. Further, you can detect the lingering
traces of any teleportation effect that occurred up to 1 hour previously, in the same fashion. You
intuitively know, to the nearest minute, when the teleportation effect occurred.

Whenever you detect the origin point or termination point of any teleportation effect with this
spell, you can study that origin point or termination point for 1 round. If you do, you can attempt
a caster level check (DC = 11 + the teleportation effect's caster level), taking a -5 penalty if the
effect occurred more than 1 minute ago. If you succeed, you gain a glimpse of the teleportation
effect's termination point (if you detected an origin point) or origin point (if you detected a
termination point). This glimpse lasts long enough for you to get a brief look at the area, but not
long enough to scrutinize it in detail. It doesn't come with any geographic knowledge of the
location, so it is not sufficient for teleport or similar magic. You can't retry the caster level
check, even if you cast trace teleport again.
