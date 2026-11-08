+++
id = "ref/spell/rain-of-frogs"
kind = "spell"
title = "Rain of Frogs"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rain_of_frogs", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-swarm" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 round"
components = "V, S, M/DF (a square of red cloth)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one swarm of bats, rats, or spiders" },
]
duration = "concentration+ 2 rounds"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Bard, Druid, Hunter, Shaman, Skald, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 round
Components: V, S, M/DF (a square of red cloth)
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration+ 2 rounds
Saving throw: none
Spell resistance: no
Effect: one swarm of bats, rats, or spiders
Subschool: Summoning
:::

### Mythic Summon Swarm

**Sources:** Mythic Adventures pg 109

The swarm has the advanced simple template. A swarm of rats or spiders leaves behind a trail of
filth or ichor when it moves, which has the effects of a [grease](ref/spell/grease) spell for 1
round after the swarm passes through an area. Any creature that moves through the affected area is
also subject to the swarm's disease or poison, as if attacked by the swarm. A prone creature in the
affected area takes a -4 penalty on its saving throw against this affliction. A bat swarm leaves
behind a similar trail that lasts for 2 rounds but doesn't have a disease or poison effect.

### Rain of Frogs

**Sources:** Ultimate Magic pg 233

This spell functions as [summon swarm](ref/spell/summon-swarm), except you summon a swarm of
poisonous frogs. This swarm has the statistics of a
[centipede swarm](ref/monster/centipede-centipede-swarm), except it has the animal type and its
poison deals Constitution damage instead of Dexterity damage.
