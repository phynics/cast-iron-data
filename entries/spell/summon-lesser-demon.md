+++
id = "ref/spell/summon-lesser-demon"
kind = "spell"
title = "Summon Lesser Demon"
aon = "SpellDisplay.aspx?ItemName=Summon%20Lesser%20Demon"
source_ids = ["pathfinder-74-sword-of-valor"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_lesser_demon", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-monster" },
]
[[sources]]
publication = "pathfinder-74-sword-of-valor"
page = "75"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
descriptors = ["chaotic", "evil"]
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
Level: 4: Summoner, Unchained Summoner\
5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
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

This spell functions like [summon monster](ref/spell/summon-monster), except it allows you to summon
a single brimorak, one incubus, one thoxel demon, 1d3 schir demons, or 1d4+1 vermlek demons.
