+++
id = "ref/spell/grease"
kind = "spell"
title = "Grease"
source_ids = ["core-rulebook", "dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grease", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (butter)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one object or 10-ft. square" },
]
duration = "1 minute/level (D)"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Bard, Magus, Mesmerist, Skald, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (butter)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: see text
Spell resistance: no
Target: one object or 10-ft. square
Subschool: Creation
:::

**Sources:** PRPG Core Rulebook pg 291

A grease spell covers a solid surface with a layer of slippery grease. Any creature in the area when
the spell is cast must make a successful Reflex save or fall. A creature can walk within or through
the area of grease at half normal speed with a DC 10 Acrobatics check. Failure means it can't move
that round (and must then make a Reflex save or fall), while failure by 5 or more means it falls
(see the [Acrobatics](ref/skill/acrobatics) skill for details). Creatures that do not move on their
turn do not need to make this check and are not considered flat-footed.

The spell can also be used to create a greasy coating on an item. Material objects not in use are
always affected by this spell, while an object wielded or employed by a creature requires its bearer
to make a Reflex saving throw to avoid the effect. If the initial saving throw fails, the creature
immediately drops the item. A saving throw must be made in each round that the creature attempts to
pick up or use the greased item. A creature wearing greased armor or clothing gains a +10
circumstance bonus on Escape Artist checks and combat maneuver checks made to escape a grapple, and
to their CMD to avoid being grappled.
