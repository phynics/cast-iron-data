+++
id = "ref/spell/calm-air"
kind = "spell"
title = "Calm Air"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calm_air", path = "json/spells2.json" },
]
[[sources]]
publication = "ranged-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["air"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "cylinder (5-ft./level radius, 40 ft. high)" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Druid, Hunter, Summoner, Unchained Summoner\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no (object)
Area: cylinder (5-ft./level radius, 40 ft. high)
Descriptors: air
:::

This spell calms the air and disperses fog, dust, and other particles. The wind force in the area is
reduced in strength by one step per 4 caster levels (to a minimum wind force of light) and clouds
are dispersed, although parts of nonmagical clouds that extend beyond the area are not affected. If
a magical cloud or wind's point of origin is inside the area of a calm air spell, the whole effect
is suppressed; otherwise, only the part inside the area is suppressed. Suppression still counts
against the duration of a wind or cloud effect. Magical wind and cloud effects are suppressed only
if you succeed at a caster level check (DC 11 + effect's caster level). You can move the calm air
effect by concentrating as a standard action.
