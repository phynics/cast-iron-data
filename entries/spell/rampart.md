+++
id = "ref/spell/rampart"
kind = "spell"
title = "Rampart"
aon = "SpellDisplay.aspx?ItemName=Rampart"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rampart", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "237"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["earth"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of earth)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft.-high earthen wall, in a line up to 10 ft. long/2 levels, or a circle with radius of up to 3 ft. + 1 ft./level" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 7: Arcanist, Druid, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a handful of earth)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: 10-ft.-high earthen wall, in a line up to 10 ft. long/2 levels, or a circle with radius of up to 3 ft. + 1 ft./level
Subschool: Creation
Descriptors: earth
:::

You create a massive rampart of hard-packed earth and stone 5 feet thick. The rampart cannot be
conjured so that it occupies the same space as another creature or object. Each 5-foot-wide section
of the rampart has [hardness](ref/umr/hardness) 0 and 180 hit points. A section of the rampart whose
hit points drop to 0 is breached. If a creature tries to break through the rampart with a single
attack, the DC for the Strength check is 60. A creature can climb over the rampart with a DC 20
Climb check.
