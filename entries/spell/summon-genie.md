+++
id = "ref/spell/summon-genie"
kind = "spell"
title = "Summon Genie"
aon = "SpellDisplay.aspx?ItemName=Summon%20Genie"
source_ids = ["people-of-the-sands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_genie", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-genie-lesser" },
]
[[sources]]
publication = "people-of-the-sands"
page = "11"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["summoning"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
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
Level: 4: Summoner, Unchained Summoner\
5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (an oil lamp worth at least 50 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned genie
Subschool: summoning
:::

### Summon Genie

This spell functions like [lesser summon genie](ref/spell/summon-genie-lesser), except you can
summon one djnni or 1d3 jann.
