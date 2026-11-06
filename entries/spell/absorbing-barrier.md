+++
id = "ref/spell/absorbing-barrier"
kind = "spell"
title = "Absorbing Barrier"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "absorbing_barrier", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (a jagged scrap of metal)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "40-ft.-radius sphere; see text (S)" },
]
duration = "1 hour/level or until discharged"
saving_throw = "none"
spell_resistance = "no (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Alchemist, Arcanist, Investigator, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, F (a jagged scrap of metal)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level or until discharged
Saving throw: none
Spell resistance: no (harmless)
Area: 40-ft.-radius sphere; see text (S)
:::

**Sources:** People of the Wastes pg 28

You ward all creatures and objects in the area from ranged weapons. The spell's area of effect is
often a sphere, although you can shape it to be smaller than the maximum area or to exclude certain
adjacent areas or objects (for example, if you are warding a specific structure, or if you are
roughly warding the front lines of a battlefield). This spell's area is also up to 40 feet in
height, so flying creatures benefit as long as they are in this area of effect.

Creatures and objects in the warded area gain [damage reduction](ref/rule/damage-reduction) 20/magic
against ranged weapons. Once the spell has prevented a total of 20 points of damage per caster level
(maximum 200 points) to creatures and objects in the area, it is discharged.
