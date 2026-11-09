+++
id = "ref/spell/aqueous-orb"
kind = "spell"
title = "Aqueous Orb"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aqueous_orb", path = "json/spells.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "202"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of water and a glass bead)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft.-diameter sphere" },
]
duration = "1 round/level"
saving_throw = "Reflex negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Bloodrager, Druid, Hunter, Magus, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of water and a glass bead)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Reflex negates
Spell resistance: no
Effect: 10-ft.-diameter sphere
Subschool: Creation
Descriptors: water
:::

You create a rolling sphere of churning water that can engulf those it strikes. The aqueous orb can
move up to 30 feet per round, rolling over barriers less than 10 feet tall. It automatically
quenches any nonmagical fires and functions as [dispel magic](ref/spell/dispel-magic) against
magical fires as long as those fires are size Large or less.

Any creature in the path of the aqueous orb takes 2d6 points of nonlethal damage. A successful
Reflex save negates this damage, but a large or smaller creature that fails its save must make a
second save or be engulfed by the aqueous orb and carried along with it. Engulfed creatures are
immersed in water and must [hold their breath](ref/misc/hold-your-breath) unless capable of
breathing water. They gain cover against attacks from outside the aqueous orb but are considered
entangled by its churning currents, takes 2d6 points of nonlethal damage at the beginning of their
turn each round they remain trapped. Creatures within the orb may attempt a new Reflex save each
round to escape into a random square adjacent to the aqueous orb. The orb may hold one Large
creature, 4 Medium, or 16 Small or smaller creatures within it.

The sphere moves as long as you actively direct it (a move action for you); otherwise, it merely
stays at rest and churns in place. An aqueous orb stops if it moves outside the spell's range.
