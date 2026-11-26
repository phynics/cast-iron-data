+++
id = "ref/spell/summon-natures-ally-6"
kind = "spell"
title = "Summon Nature's Ally VI"
aon = "SpellDisplay.aspx?ItemName=Summon%20Nature%27s%20Ally%206"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_natures_ally_6", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-natures-ally-1" },
]
[[sources]]
publication = "core-rulebook"
page = "354"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["summoning"]
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Shaman", level = 6 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one summoned creature" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration \[see text\]
Level: 6: Druid, Hunter, Shaman
Casting time: 1 round
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: summoning
:::

### Summon Nature's Ally VI

This spell functions like [summon nature's ally I](ref/spell/summon-natures-ally-1), except that you
can summon one 6th-level creature, 1d3 5th-level creatures of the same kind, or 1d4+1 lower-level
creatures of the same kind.
