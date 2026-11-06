+++
id = "ref/spell/leshy-swarm"
kind = "spell"
title = "Leshy Swarm"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "leshy_swarm", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, M/DF (a bundle of seeds)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "10-ft.-square swarm of leshys" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Bard, Druid, Hunter, Skald, Sorcerer, Summoner, Wizard
Casting time: 1 round
Components: V, S, M/DF (a bundle of seeds)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Effect: 10-ft.-square swarm of leshys
Subschool: Summoning
:::

**Sources:** Ultimate Wilderness pg 25

> _[Vine leshys](ref/race/vine-leshy) have access to the following spell._

You call out to nearby nature spirits and grant them temporary plant bodies. These creatures are
similar to leshys, except they are Tiny and far more simpleminded. The swarm uses the statistics for
a rat swarm, except it does not carry a disease or have scent. The leshy swarm has
[darkvision](ref/rule/darkvision) with a range of 60 feet and is immune to electricity,
mind-affecting effects, paralysis, poison, polymorph, sleep effects, sonic, and stunning.

You can direct the leshy swarm to move up to its speed along a path for your choice by spending a
standard action to communicate your desires through the spell, or by spending a move action if you
can speak to creatures that understand only Druidic and Sylvan. The leshys are confused by their
sudden possession of new bodies and assume that nearly any creature you direct them toward is a
threat. They attack all creatures within their area except for you and other creatures with the
plant type.
