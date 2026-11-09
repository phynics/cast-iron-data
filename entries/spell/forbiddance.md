+++
id = "ref/spell/forbiddance"
kind = "spell"
title = "Forbiddance"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forbiddance", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "285"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Warpriest", level = 6 },
]
casting_time = "6 rounds"
components = "V, S, DF, M (holy water and incense worth 1,500 gp, plus 1,500 gp per 60-foot cube)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "60-ft. cube/level (S)" },
]
duration = "permanent"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Cleric, Inquisitor, Occultist, Oracle, Warpriest
Casting time: 6 rounds
Components: V, S, DF, M (holy water and incense worth 1,500 gp, plus 1,500 gp per 60-foot cube)
Range: medium (100 ft. + 10 ft./level)
Duration: permanent
Saving throw: see text
Spell resistance: yes
Area: 60-ft. cube/level (S)
:::

Forbiddance seals an area against all planar travel into or within it. This includes all
teleportation spells (such as dimension door and teleport), plane shifting, astral travel, ethereal
travel, and all summoning spells. Such effects simply fail automatically.

In addition, it damages entering creatures whose alignments are different from yours. The effect on
those attempting to enter the warded area is based on their alignment relative to yours (see below).
A creature inside the area when the spell is cast takes no damage unless it exits the area and
attempts to reenter, at which time it is affected as normal.

_Alignments identical:_ No effect. The creature may enter the area freely (although not by planar
travel).

Alignments different with respect to either law/chaos or good/evil: The creature takes 6d6 points of
damage. A successful Will save halves the damage, and [spell resistance](ref/rule/spell-resistance)
applies.

Alignments different with respect to both law/chaos and good/evil: The creature takes 12d6 points of
damage. A successful Will save halves the damage, and [spell resistance](ref/rule/spell-resistance)
applies.

At your option, the abjuration can include a password, in which case creatures of alignments
different from yours can avoid the damage by speaking the password as they enter the area. You must
select this option (and the password) at the time of casting. Adding a password requires the burning
of additional rare incenses worth at least 1,000 gp, plus 1,000 gp per 60-foot cube.

[Dispel magic](ref/spell/dispel-magic) does not dispel a forbiddance effect unless the dispeller's
level is at least as high as your caster level.

You can't have multiple overlapping forbiddance effects. In such a case, the more recent effect
stops at the boundary of the older effect.
