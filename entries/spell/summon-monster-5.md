+++
id = "ref/spell/summon-monster-5"
kind = "spell"
title = "Summon Monster V"
aon = "SpellDisplay.aspx?ItemName=Summon%20Monster%205"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_monster_5", path = "json/spells16.json" },
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
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
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
Level: 4: Medium, Summoner, Unchained Summoner\
5: Arcanist, Bard, Cleric, Oracle, Psychic, Skald, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (a tiny bag and a small candle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: summoning
:::

### Summon Monster V

This spell functions like [summon monster I](ref/spell/summon-monster-1), except that you can summon
one creature from the 5th-level list, 1d3 creatures of the same kind from the 4th-level list, or
1d4+1 creatures of the same kind from a lower-level list.
