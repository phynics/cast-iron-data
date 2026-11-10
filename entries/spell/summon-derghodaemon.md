+++
id = "ref/spell/summon-derghodaemon"
kind = "spell"
title = "Summon Derghodaemon"
source_ids = ["book-of-the-damned-volume-3-horsemen-of-the-apocalypse"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_derghodaemon", path = "json/spells16.json" },
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
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 round"
components = "V, S, F (a handful of bug carapaces)"
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
Components: V, S, F (a handful of bug carapaces)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Effect: one summoned creature
Subschool: Summoning
Descriptors: evil
:::

This spell functions like [summon monster](ref/spell/summon-monster), except it summons a single
derghodaemon.
