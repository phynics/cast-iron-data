+++
id = "ref/spell/summon-lesser-psychopomp"
kind = "spell"
title = "Summon Lesser Psychopomp"
aon = "SpellDisplay.aspx?ItemName=Summon%20Lesser%20Psychopomp"
source_ids = ["pathfinder-80-empty-graves"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_lesser_psychopomp", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-monster" },
]
[[sources]]
publication = "pathfinder-80-empty-graves"
page = "28"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
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
components = "V, S, F/DF (a crocodile skull funerary mask)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one or more summoned psychopomps (see text)" },
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
Components: V, S, F/DF (a crocodile skull funerary mask)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one or more summoned psychopomps (see text)
Subschool: Summoning
:::

This spell functions like [summon monster](ref/spell/summon-monster), except that it summons 1d3
[esobok psychopomps](ref/monster/psychopomp-esobok) or 1d4+1
[nosoi psychopomps](ref/monster/psychopomp-nosoi).
