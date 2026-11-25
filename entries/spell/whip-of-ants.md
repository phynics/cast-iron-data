+++
id = "ref/spell/whip-of-ants"
kind = "spell"
title = "Whip of Ants"
aon = "SpellDisplay.aspx?ItemName=Whip%20of%20Ants"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "whip_of_ants", path = "json/spells11.json" },
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
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 6 },
  { class = "Unchained Summoner", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
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
Level: 6: Arcanist, Bard, Druid, Hunter, Skald, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a square of red cloth)
Range: 0 ft.
Duration: 1 round/level (d (see text)
Saving throw: none
Spell resistance: yes
Effect: whip-like swarm
Subschool: summoning
:::

### Whip of Ants

This spell functions as [whip of spiders](ref/spell/whip-of-spiders), except it summons army ants,
and any creature you strike with the whip takes swarm damage as if it were attacked by an
[army ant swarm](ref/monster/ant-army-ant-swarm) (3d6 points of damage plus poison and distraction).
If you transform the whip into an army ant swarm, it has 16 hit points.
