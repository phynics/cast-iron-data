+++
id = "ref/spell/poisonous-cloud"
kind = "spell"
title = "Poisonous Cloud"
aon = "SpellDisplay.aspx?ItemName=Poisonous%20Cloud"
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
subschools = ["creation"]
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (small drop of poison)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "cloud spreads in 20-ft. radius, 20 ft. high" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates; see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Arcanist, Bloodrager, Magus, Shaman, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (small drop of poison)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Fortitude negates; see text
Spell resistance: no
Effect: cloud spreads in 20-ft. radius, 20 ft. high
Subschool: creation
Descriptors: poison
:::

### Poisonous Cloud

Poisonous cloud creates a bank of fog like that created by [fog cloud](ref/spell/fog-cloud), except
that the vapors are toxic. The cloud deals 1d2 points of Constitution damage per round to living
creatures that fail their Fortitude saves. A creature that succeeds at its save but remains in the
cloud must continue to attempt a new saving throw each round on your turn.

Poisonous cloud can be made permanent with a [permanency](ref/spell/permanency) spell cast by a
caster of 13th level or higher, at a cost of 12,500 gp. A permanent poisonous cloud dispersed by
wind re-forms in 10 minutes.
