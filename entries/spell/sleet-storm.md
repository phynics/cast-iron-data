+++
id = "ref/spell/sleet-storm"
kind = "spell"
title = "Sleet Storm"
aon = "SpellDisplay.aspx?ItemName=Sleet%20Storm"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sleet_storm", path = "json/spells9.json" },
]
[[sources]]
publication = "core-rulebook"
page = "344"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (dust and water)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "cylinder (40-ft. radius, 20 ft. high)" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Bloodrager, Druid, Hunter, Magus, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (dust and water)
Range: long (400 ft. + 40 ft./level)
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Area: cylinder (40-ft. radius, 20 ft. high)
Subschool: Creation
Descriptors: cold
:::

Driving sleet blocks all sight (even [darkvision](ref/rule/darkvision)) within it and causes the
ground in the area to be icy. A creature can walk within or through the area of sleet at half normal
speed with a DC 10 Acrobatics check. Failure means it can't move in that round, while failure by 5
or more means it falls (see the [Acrobatics](ref/skill/acrobatics) skill for details).

The sleet extinguishes torches and small fires.
