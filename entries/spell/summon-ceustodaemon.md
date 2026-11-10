+++
id = "ref/spell/summon-ceustodaemon"
kind = "spell"
title = "Summon Ceustodaemon"
aon = "SpellDisplay.aspx?ItemName=Summon%20Ceustodaemon"
source_ids = ["book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_ceustodaemon", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/summon-monster" },
]
[[sources]]
publication = "book-of-the-damned-volume-3-horsemen-of-the-apocalypse"
page = "39"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
descriptors = ["evil"]
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
components = "V, S, F (ashes of a dead animal)"
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
Components: V, S, F (ashes of a dead animal)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: Summoning
Descriptors: evil
:::

This spell functions like [summon monster](ref/spell/summon-monster), except it summons a single
ceustodaemon.
