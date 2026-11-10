+++
id = "ref/spell/flashfire"
kind = "spell"
title = "Flashfire"
aon = "SpellDisplay.aspx?ItemName=Flashfire"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flashfire", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "231"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Shaman", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "one 5-ft. square/2 levels" },
]
duration = "1 round/level"
saving_throw = "Reflex negates (object) and Fortitude negates"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Reflex negates (object) and Fortitude negates
Spell resistance: yes (object)
Area: one 5-ft. square/2 levels
Descriptors: fire
:::

You cause flames to spring up in the area of effect. These flames deal 1d6 points of fire damage for
every 3 caster levels you have (maximum 5d6) to each creature that enters a burning area or begins
its turn in the area; these creatures also catch on fire. A creature that succeeds at a Reflex save
negates the damage and avoids catching on fire. The area and all adjacent 5-foot squares are smoky,
providing [concealment](ref/rule/concealment) within. You can concentrate as a standard action to
ignite one 5-foot square adjacent to a currently burning square. Heavy precipitation (including
sleet storm) ends the spell. Strong and severe winds spread each square of flashfire downwind by one
square each round, but windstorm-force or stronger winds extinguish the fires.
