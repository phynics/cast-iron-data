+++
id = "ref/spell/slow"
kind = "spell"
title = "Slow"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "slow", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of molasses)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Medium, Summoner\
3: Arcanist, Bloodrager, Bard, Magus, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Spiritualist, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of molasses)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Targets: one creature/level, no two of which can be more than 30 ft. apart
:::

**Sources:** PRPG Core Rulebook pg 344

An affected creature moves and attacks at a drastically slowed rate. Creatures affected by this
spell are staggered and can take only a single move action or standard action each turn, but not
both (nor may it take full-round actions). Additionally, it takes a -1 penalty on attack rolls, AC,
and Reflex saves. A slowed creature moves at half its normal speed (round down to the next 5-foot
increment), which affects the creature's jumping distance as normal for decreased speed.

Multiple slow effects don't stack. Slow counters and dispels [haste](ref/spell/haste).
