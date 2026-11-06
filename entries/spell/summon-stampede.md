+++
id = "ref/spell/summon-stampede"
kind = "spell"
title = "Summon Stampede"
source_ids = ["chronicle-of-the-righteous"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_stampede", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 round"
components = "V, S, M (piece of fur from a herd animal)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "20-ft.-radius herd of animals" },
]
duration = "1 round/level"
saving_throw = "Reflex halves (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Summoner, Unchained Summoner\
6: Cleric, Druid, Hunter, Oracle, Warpriest
Casting time: 1 round
Components: V, S, M (piece of fur from a herd animal)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Reflex halves (see text)
Spell resistance: no
Effect: 20-ft.-radius herd of animals
Subschool: Summoning
:::

**Sources:** Chronicle of the Righteous pg 51

You conjure a herd of aurochs or similar herd animal that immediately stampedes in the direction you
indicate. The herd takes up a 20-foot-radius space and moves at a rate of 120 feet per round in a
straight line. Any creatures caught in the herd's path take 4d6+9 points of damage that round as
they are trampled beneath dozens of animals' hooves. A successful Reflex save halves this damage.

If the stampede's path would put it in an obviously dangerous area (such as over a cliff or through
a fire) or force it to move through a solid barrier, the herd stops at the obstacle and moves in a
new randomly determined direction until it reaches another obstacle or the spell's duration ends.
