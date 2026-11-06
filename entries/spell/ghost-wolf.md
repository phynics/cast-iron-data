+++
id = "ref/spell/ghost-wolf"
kind = "spell"
title = "Ghost Wolf"
source_ids = ["advanced-race-guide", "orcs-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ghost_wolf", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, F (dire wolf tooth)"
range = "0 ft."
effects = [
  { label = "Target", value = "one quasi-real wolf-like creature" },
]
duration = "1 hour/level (d) or 1 round/level; see text"
saving_throw = "none (see description)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Summoner, Unchained Summoner\
4: Arcanist, Bloodrager, Psychic, Sorcerer, Wizard
Casting time: 10 minutes
Components: V, S, F (dire wolf tooth)
Range: 0 ft.
Duration: 1 hour/level (d) or 1 round/level; see text
Saving throw: none (see description)
Spell resistance: no
Target: one quasi-real wolf-like creature
Subschool: Creation
:::

**Sources:** Advanced Race Guide pg 58, Orcs of Golarion pg 28

> _[Half-orcs](ref/race/half-orc) have access to the following spell._

This spell conjures a Large, quasi-real, wolf-like creature made of roiling black smoke. It
functions as [phantom steed](ref/spell/phantom-steed), except as noted above. In addition, the
creature radiates an aura of fear. Any creature with fewer than 6 Hit Dice within 30 feet (except
the ghost wolf's rider) must make a Will save or become shaken for 1d4 rounds (this is a
mind-affecting fear effect). A creature that makes its Will save is unaffected by the steed's fear
aura for 24 hours.

The ghost wolf may also be used in combat. Once per round, the rider may direct the ghost wolf to
attack in battle as a free action (bite +10, 1d8+6 points of damage); unlike an animal mount, this
does not require a Ride check or any training. Once the ghost wolf attacks, it lasts for only 1
round per level thereafter.
