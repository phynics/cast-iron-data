+++
id = "ref/spell/summon-greater-demon"
kind = "spell"
title = "Summon Greater Demon"
source_ids = ["pathfinder-74-sword-of-valor"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_greater_demon", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-monster" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
descriptors = ["chaotic", "evil"]
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
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
Level: 9: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, F/DF (a tiny bag and a small candle)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: Summoning
Descriptors: chaotic, evil
:::

**Sources:** Pathfinder \#74: Sword of Valor pg 75

This spell functions like [summon monster](ref/spell/summon-monster), except it allows you to summon
a single coloxus, an omox demon, or 1d3 kalavakus demons.
