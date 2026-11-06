+++
id = "ref/spell/summon-minor-monster"
kind = "spell"
title = "Summon Minor Monster"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_minor_monster", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S, F/DF (a tiny bag and a small candle)"
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
Level: 1: Antipaladin, Arcanist, Bard, Cleric, Medium, Oracle, Psychic, Skald, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (a tiny bag and a small candle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: 1d3 summoned creatures
Subschool: Summoning
:::

**Sources:** Ultimate Magic pg 241

This spell functions as [summon monster I](ref/spell/summon-monster-1), except you can summon 1d3
Tiny or smaller animals, such as bats, lizards, monkeys, rats, ravens, toads, or weasels. The
summoned animals must all be the same type of creature. As with animals summoned with summon monster
I, you may apply one alignment-appropriate template to these animals.
