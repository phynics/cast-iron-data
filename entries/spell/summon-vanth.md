+++
id = "ref/spell/summon-vanth"
kind = "spell"
title = "Summon Vanth"
source_ids = ["pathfinder-80-empty-graves"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_vanth", path = "json/spells16.json" },
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
components = "V, S, F/DF (a vulture skull funerary mask)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one summoned vanth psychopomp" },
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
Components: V, S, F/DF (a vulture skull funerary mask)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned vanth psychopomp
Subschool: Summoning
:::

**Sources:** Pathfinder \#80: Empty Graves pg 28

This spell functions like summon monster, except that it summons a single
[vanth psychopomp](ref/monster/psychopomp-vanth).
