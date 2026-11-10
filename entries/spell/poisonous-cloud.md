+++
id = "ref/spell/poisonous-cloud"
kind = "spell"
title = "Poisonous Cloud"
source_ids = ["core-rulebook", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poisonous_cloud", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fog-cloud" },
]
[[sources]]
publication = "potions-and-poisons"
page = "11"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "fog spreads in 20-ft. radius" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Druid, Hunter, Magus, Shaman, Sorcerer, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Effect: fog spreads in 20-ft. radius
Subschool: Creation
:::

### Poisonous Cloud

Poisonous cloud creates a bank of fog like that created by [fog cloud](ref/spell/fog-cloud), except
that the vapors are toxic. The cloud deals 1d2 points of Constitution damage per round to living
creatures that fail their Fortitude saves. A creature that succeeds at its save but remains in the
cloud must continue to attempt a new saving throw each round on your turn.

Poisonous cloud can be made permanent with a [permanency](ref/spell/permanency) spell cast by a
caster of 13th level or higher, at a cost of 12,500 gp. A permanent poisonous cloud dispersed by
wind re-forms in 10 minutes.
