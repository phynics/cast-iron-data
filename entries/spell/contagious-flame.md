+++
id = "ref/spell/contagious-flame"
kind = "spell"
title = "Contagious Flame"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contagious_flame", path = "json/spells12.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "212"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "three or more rays" },
]
duration = "3 rounds"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Magus, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 3 rounds
Saving throw: none
Spell resistance: yes
Target: three or more rays
Descriptors: fire
:::

You blast several enemies with beams of fire. You may fire three rays, plus one additional ray for
every four levels beyond 11th (to a maximum of five rays at 19th level). Each ray requires a ranged
touch attack to hit and deals 4d6 points of fire damage. The rays may be fired at the same or
different targets, but all rays must be aimed at targets within 30 feet of each other and fired
simultaneously.

Every round on your turn, a new ray of fire launches from each creature who took damage from the
spell in the previous round - these new rays attack as if you fired them, but their point of origin
is the previous creature damaged. You can choose the new targets as a free action, all of whom must
be within close range (25 ft. + 5 ft./2 levels) of their new starting point. This contagion of flame
continues for a total of three rounds - a creature can be struck more than once by this spell over
the course of these three rounds, although never by a ray of fire that launches from itself.
