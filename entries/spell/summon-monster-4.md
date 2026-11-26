+++
id = "ref/spell/summon-monster-4"
kind = "spell"
title = "Summon Monster IV"
aon = "SpellDisplay.aspx?ItemName=Summon%20Monster%204"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_monster_4", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-monster-1" },
]
[[sources]]
publication = "core-rulebook"
page = "352"
[[expanded_in]]
publication = "monster-summoners-handbook"
page = "18"
via = "ref/feat/versatile-summon-monster"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["summoning"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, F/DF (a tiny bag and a small candle)"
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
Level: 3: Medium, Summoner, Unchained Summoner\
4: Antipaladin, Arcanist, Bard, Cleric, Oracle, Psychic, Skald, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (a tiny bag and a small candle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: summoning
:::

### Summon Monster IV

This spell functions like [summon monster I](ref/spell/summon-monster-1), except that you can summon
one creature from the 4th-level list, 1d3 creatures of the same kind from the 3rd-level list, or
1d4+1 creatures of the same kind from a lower-level list.
