+++
id = "ref/spell/rain-of-frogs"
kind = "spell"
title = "Rain of Frogs"
aon = "SpellDisplay.aspx?ItemName=Rain%20of%20Frogs"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rain_of_frogs", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-swarm" },
]
[[sources]]
publication = "ultimate-magic"
page = "233"

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

### Rain of Frogs

This spell functions as [summon swarm](ref/spell/summon-swarm), except you summon a swarm of
poisonous frogs. This swarm has the statistics of a
[centipede swarm](ref/monster/centipede-centipede-swarm), except it has the animal type and its
poison deals Constitution damage instead of Dexterity damage.
