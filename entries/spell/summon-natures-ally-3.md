+++
id = "ref/spell/summon-natures-ally-3"
kind = "spell"
title = "Summon Nature's Ally III"
aon = "SpellDisplay.aspx?ItemName=Summon%20Nature%27s%20Ally%203"
source_ids = ["core-rulebook", "inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_natures_ally_3", path = "json/spells16.json" },
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
subschools = ["Summoning"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
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
School: conjuration
Level: 1: Druid, Hunter, Ranger, Shaman
Casting time: 1 round
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: Summoning
:::

### Summon Nature's Ally III

This spell functions like [summon nature's ally I](ref/spell/summon-natures-ally-1), except that you
can summon one 3rd-level creature, 1d3 2nd-level creatures of the same kind, or 1d4+1 1st-level
creatures of the same kind.
