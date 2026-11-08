+++
id = "ref/spell/summon-genie-greater"
kind = "spell"
title = "Greater Summon Genie"
source_ids = ["people-of-the-sands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_genie_greater", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-genie-lesser" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Summoner", level = 5 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 round"
components = "V, S, F/DF (an oil lamp worth at least 50 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one summoned genie" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Summoner, Unchained Summoner\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (an oil lamp worth at least 50 gp)
Range: close (25 ft. + 5 ft./2 levels)
Effect: one summoned genie
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Subschool: Summoning
:::

### Greater Summon Genie

**Sources:** People of the Sands pg 11

This spell functions like [lesser summon genie](ref/spell/summon-genie-lesser), except you can
summon one shaitan, 1d3 djnn or 1d4+1 jann.
