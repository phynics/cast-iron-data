+++
id = "ref/rule/radiation"
kind = "rule"
title = "Radiation"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "radiation", path = "json/rules_campaign_types10.json" },
]
[[sources]]
publication = "technology-guide"
page = "55"

[fields]
kind = "none"
+++

Radiation is a very real threat to those who explore the technological ruins of Numeria. Radiation
is a poison effect whose initial effect causes Constitution drain and secondary effect causes
Strength damage. Radiation poisoning dangers are organized into four categories: low, medium, high,
and severe.

**Area of Effect:** Radiation suffuses a spherical area of effect that can extend into solid
objects. The closer one gets to the center of an area of radiation, the stronger the radiation
effect becomes. Radiation entries list the maximum level of radiation in an area, as well as the
radius out to which this radiation level applies. Each increment up to an equal length beyond that
radius degrades the radiation strength by one level. For example, a spherical area of high radiation
with a radius of 20 feet creates a zone of medium radiation 21 feet to 40 feet from the center in
all directions, and a similar zone of low radiation from 41 to 60 feet.

**Initial Effect:** Radiation initially deals Constitution drain unless the affected character
succeeds at a Fortitude save. A new saving throw must be attempted to resist radiation's initial
damage each round a victim remains exposed to it.

**Secondary Effect:** Secondary effects from radiation deal Strength damage at a much slower rate
than most poisons. This secondary effect ends only after a character succeeds at two consecutive
Fortitude saving throws to resist secondary radiation damage. If a character has Strength damage
equal to his current Strength score, further damage dealt by a secondary effect is instead
Constitution damage.

**Removing Radiation Effects:** All radiation damage is a poison effect, and as such it can be
removed with any effect that neutralizes poison.
[Ability damage and drain](ref/rule/ability-damage-drain) caused by radiation damage can be healed
normally

|Radiation Level|Fort DC|Initial Effect|Secondary Effect|
| --- | --- | --- | --- |
|Low|13|1 Con drain|1 Str damage/day|
|Medium|17|1d4 Con drain|1d4 Str damage/day|
|High|22|2d4 Con drain|1d6 Str damage/day|
|Severe|30|4d6 Con drain|2d6 Str damage/day|
