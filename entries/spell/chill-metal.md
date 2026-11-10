+++
id = "ref/spell/chill-metal"
kind = "spell"
title = "Chill Metal"
aon = "SpellDisplay.aspx?ItemName=Chill%20Metal"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chill_metal", path = "json/spells2.json" },
]
[[sources]]
publication = "core-rulebook"
page = "254"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["cold"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "metal equipment of one creature per two levels, no two of which can be more than 30 ft. apart; or 25 lbs. of metal/level, none of which can be more than 30 ft. away from any of the rest" },
]
duration = "7 rounds"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Occultist, Psychic
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 7 rounds
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: metal equipment of one creature per two levels, no two of which can be more than 30 ft. apart; or 25 lbs. of metal/level, none of which can be more than 30 ft. away from any of the rest
Descriptors: cold
:::

Chill metal makes metal extremely cold. Unattended, nonmagical metal gets no saving throw. Magical
metal is allowed a saving throw against the spell. An item in a creature's possession uses the
creature's saving throw bonus unless its own is higher.

A creature takes cold damage if its equipment is chilled. It takes full damage if its armor, shield,
or weapon is affected. The creature takes minimum damage (1 point or 2 points; see the table) if
it's not wearing or wielding such an item.

On the first round of the spell, the metal becomes chilly and uncomfortable to touch but deals no
damage. The same effect also occurs on the last round of the spell's duration. During the second
(and also the next-to-last) round, icy coldness causes pain and damage. In the third, fourth, and
fifth rounds, the metal is freezing cold, and causes more damage, as shown on the table below.

|Round|Metal Temperature|Damage|
| --- | --- | --- |
|1|Cold|None|
|2|Icy|1d4 points|
|3-5|Freezing|2d4 points|
|6|Icy|1d4 points|
|7|Cold|None|

Any heat intense enough to damage the creature negates cold damage from the spell (and vice versa)
on a point-for-point basis. Underwater, chill metal deals no damage, but ice immediately forms
around the affected metal, making it float if unattended.

Chill metal counters and dispels [heat metal](ref/spell/heat-metal).
