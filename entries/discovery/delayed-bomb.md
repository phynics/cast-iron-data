+++
id = "ref/discovery/delayed-bomb"
kind = "rule"
title = "Delayed Bomb"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "delayed_bomb", path = "json/class_ability_discoveries.json" },
]

[fields]
kind = "none"
+++

**Delayed Bomb**

**Ability:** The alchemist can place a bomb so that it explodes a number of rounds after the
alchemist ceases contact with the bomb. This delay can be any number of rounds as chosen by the
alchemist, up to a number of rounds equal to his level. If at any point the alchemist reclaims
possession of the _delayed bomb,_ he can end the timer and prevent the bomb's detonation. A _delayed
bomb_ detonates immediately if any other creature attempts to touch or move it, or if the bomb's
contents are removed from the vial (such as if the vial breaks).

The bomb deals damage as if it scored a direct hit to any creature in the square with the bomb when
it detonates, and splash damage to all adjacent creatures as normal.

**Prereq:** 8th-level alchemist

**Special:** An alchemist cannot have more than one _delayed bomb_ at one time. If he creates
another _delayed bomb,_ the previous bomb becomes inert. [Dispel magic](ref/spell/dispel-magic) can
neutralize a _delayed bomb,_ as can a successful [Disable Device](ref/skill/disable-device) check
(DC equals 10 + the alchemist's level + the alchemist's Intelligence modifier).
