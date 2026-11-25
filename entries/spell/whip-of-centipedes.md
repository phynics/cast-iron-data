+++
id = "ref/spell/whip-of-centipedes"
kind = "spell"
title = "Whip of Centipedes"
aon = "SpellDisplay.aspx?ItemName=Whip%20of%20Centipedes"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "whip_of_centipedes", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/whip-of-spiders" },
]
[[sources]]
publication = "advanced-class-guide"
page = "199"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["summoning"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a square of red cloth)"
range = "0 ft."
effects = [
  { label = "Effect", value = "whip-like swarm" },
]
duration = "1 round/level (d (see text)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Bard, Druid, Hunter, Skald, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a square of red cloth)
Range: 0 ft.
Duration: 1 round/level (d (see text)
Saving throw: none
Spell resistance: yes
Effect: whip-like swarm
Subschool: summoning
:::

### Whip of Centipedes

This spell functions as [whip of spiders](ref/spell/whip-of-spiders), except it summons centipedes,
and any creature you strike with the whip takes swarm damage as if it were attacked by a
[centipede swarm](ref/monster/centipede-centipede-swarm) (2d6 points of damage plus poison and
distraction). If you transform the whip into a centipede swarm, it has 10 hit points.
