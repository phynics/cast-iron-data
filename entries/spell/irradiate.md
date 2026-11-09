+++
id = "ref/spell/irradiate"
kind = "spell"
title = "Irradiate"
aon = "SpellDisplay.aspx?ItemName=Irradiate"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "irradiate", path = "json/spells6.json" },
]
[[sources]]
publication = "technology-guide"
page = "9"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Magus", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "special (see below)" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial (see below)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Arcanist, Cleric, Magus, Oracle, Sorcerer, Summoner, Unchained Summoner, Warpriest, Witch, Wizard\
4: Druid, Hunter
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude partial (see below)
Spell resistance: no
Effect: special (see below)
Subschool: Creation
:::

The spell's area of effect floods with dangerous radiation. The strength of the radiation you create
depends on your caster level, as detailed below. The central irradiated area is always a
10-foot-radius spread that expands normally per the rules for [radiation](ref/rule/radiation) areas
of effect. Creatures within the area are exposed to the radiation only once; the radiation does not
linger in the area. The save to resist the radiation effects is set by the spell, not the standard
save DC for radiation.

|Caster Level|Radiation Level|
| --- | --- |
|6th or lower|Low|
|7th-9th|Medium|
|10th-16th|High|
|17th or higher|Severe|
