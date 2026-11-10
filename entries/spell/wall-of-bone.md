+++
id = "ref/spell/wall-of-bone"
kind = "spell"
title = "Wall of Bone"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wall_of_bone", path = "json/spells11.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "13"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a polished humanoid femur)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "solid wall of humanoid bones with an area of up to one 5-ft. square/level" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes; see text"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Arcanist, Bloodrager, Cleric, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a polished humanoid femur)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes; see text
Effect: solid wall of humanoid bones with an area of up to one 5-ft. square/level
:::

This spell creates a vertical wall of skeletal arms that attaches itself to any solid surface. The
wall of bone works identically to wall of stone except as noted above and in this spell description.
The wall of bone is 1 inch thick per 4 caster levels and composed of up to one 5-foot square per
level. The wall created must be vertical, and must rest upon a firm foundation. It cannot be used to
bridge a chasm, for instance, or to act as a ramp. Each 5-foot square of the wall has
[hardness](ref/umr/hardness) 4 and 7 hit points per inch of thickness. A section of wall whose hit
points drops to 0 is breached. If a creature tries to break through the wall with a single attack,
the DC of the Strength check is equal to 15 + 2 per inch of thickness.

For each creature adjacent to the wall, the skeletal hands attempt a combat maneuver check to
grapple it. The skeletal hands do not provoke attacks of opportunity. They make their attacks at the
start of your turn, when the wall is summoned, or when an enemy first moves adjacent to the wall.
The skeletal hands' CMB is equal to your caster level, and they can grapple a Huge or smaller
creature with no penalty.

If the wall successfully grapples a foe, that foe takes 1d6 points of damage and gains the grappled
condition. Grappled opponents cannot move without first breaking the grapple. All other movement is
prohibited unless the creature breaks the grapple first. The wall cannot move or pin foes. Each
round the wall succeeds at a grapple combat maneuver check, it deals 1d6 additional points of
damage. The CMD of the wall, for the purposes of escaping the grapple, is equal to 10 + its CMB.
