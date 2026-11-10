+++
id = "ref/spell/summon-swarm"
kind = "spell"
title = "Summon Swarm"
aon = "SpellDisplay.aspx?ItemName=Summon%20Swarm"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_swarm", path = "json/spells16.json" },
]
[[sources]]
publication = "core-rulebook"
page = "354"

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

You summon a swarm of [bats](ref/monster/bat-bat-swarm), [rats](ref/monster/rat-rat-swarm), or
[spiders](ref/monster/spider-spider-swarm) (your choice), which attacks all other creatures within
its area. (You may summon the swarm so that it shares the area of other creatures.) If no living
creatures are within its area, the swarm attacks or pursues the nearest creature as best it can. The
caster has no control over its target or direction of travel.
