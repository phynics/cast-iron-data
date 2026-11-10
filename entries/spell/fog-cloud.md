+++
id = "ref/spell/fog-cloud"
kind = "spell"
title = "Fog Cloud"
aon = "SpellDisplay.aspx?ItemName=Fog%20Cloud"
source_ids = ["core-rulebook", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fog_cloud", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "284"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "fog spreads in 20-ft. radius" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Druid, Hunter, Magus, Shaman, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Effect: fog spreads in 20-ft. radius
Subschool: Creation
:::

A bank of fog billows out from the point you designate. The fog obscures all sight, including
[darkvision](ref/rule/darkvision), beyond 5 feet. A creature within 5 feet has concealment (attacks
have a 20% miss chance). Creatures farther away have total concealment (50% miss chance, and the
attacker can't use sight to locate the target).

A moderate wind (11+ mph) disperses the fog in 4 rounds; a strong wind (21+ mph) disperses the fog
in 1 round.

The spell does not function underwater.
