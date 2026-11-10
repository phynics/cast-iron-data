+++
id = "ref/spell/summon-minor-ally"
kind = "spell"
title = "Summon Minor Ally"
aon = "SpellDisplay.aspx?ItemName=Summon%20Minor%20Ally"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_minor_ally", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-natures-ally-1" },
]
[[sources]]
publication = "ultimate-magic"
page = "241"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "1d3 summoned creatures" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Druid, Hunter, Ranger
Casting time: 1 round
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: 1d3 summoned creatures
Subschool: Summoning
:::

This spell functions as [summon nature's ally I](ref/spell/summon-natures-ally-1), except you can
summon 1d3 Tiny or smaller animals, such as bats, lizards, monkeys, rats, ravens, toads, or weasels.
The summoned animals must all be the same type of creature.
