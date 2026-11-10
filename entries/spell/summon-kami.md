+++
id = "ref/spell/summon-kami"
kind = "spell"
title = "Summon Kami"
aon = "SpellDisplay.aspx?ItemName=Summon%20Kami"
source_ids = ["core-rulebook", "inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_kami", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-natures-ally-5" },
]
[[sources]]
publication = "inner-sea-races"
page = "223"

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

### Summon Kami

> _The following spell is available to the indicated race or ethnicity: Tian_

This spell functions as [summon nature's ally V](ref/spell/summon-natures-ally-5), except you can
summon one kodama, 1d3 fukujin, or 1d4+1 shikigami.
