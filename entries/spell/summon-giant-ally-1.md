+++
id = "ref/spell/summon-giant-ally-1"
kind = "spell"
title = "Summon Giant Ally I"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_giant_ally_1", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-natures-ally-6" },
]
[[sources]]
publication = "inner-sea-races"
page = "223"

[fields]
kind = "spell"
school = "conjuration [see text]"
subschools = ["Summoning"]
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (bit of cloth from a giant's bag)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one or more giants" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 6: Druid, Hunter
Casting time: 1 standard action
Components: V, S, F/DF (bit of cloth from a giant's bag)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one or more giants
Subschool: Summoning
:::

> _The following spells are available to the indicated race or ethnicity: Kellid_

This spell functions as [summon nature's ally VI](ref/spell/summon-natures-ally-6), except its
casting time is shorter and you can summon one cave, hill, marsh, river, slag, stone, or wood giant.
