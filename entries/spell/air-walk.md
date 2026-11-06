+++
id = "ref/spell/air-walk"
kind = "spell"
title = "Air Walk"
source_ids = ["core-rulebook", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "air_walk", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature (Gargantuan or smaller) touched" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Cleric, Druid, Hunter, Investigator, Occultist, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level
Saving throw: none
Spell resistance: yes
Target: creature (Gargantuan or smaller) touched
Descriptors: air
:::

**Sources:** PRPG Core Rulebook pg 239

The subject can tread on air as if walking on solid ground. Moving upward is similar to walking up a
hill. The maximum upward or downward angle possible is 45 degrees, at a rate equal to half the air
walker's normal speed.

A strong wind (21+ miles per hour) can push the subject along or hold it back. At the end of a
creature's turn each round, the wind blows the air walker 5 feet for each 5 miles per hour of wind
speed. The creature may be subject to additional penalties in exceptionally strong or turbulent
winds, such as loss of control over movement or physical damage from being buffeted about.

Should the spell duration expire while the subject is still aloft, the magic fails slowly. The
subject floats downward 60 feet per round for 1d6 rounds. If it reaches the ground in that amount of
time, it lands safely. If not, it falls the rest of the distance, taking 1d6 points of damage per 10
feet of fall. Since dispelling a spell effectively ends it, the subject also descends in this way if
the air walk spell is dispelled, but not if it is negated by an antimagic field.

You can cast air walk on a specially trained mount so it can be ridden through the air. You can
train a mount to move with the aid of air walk (counts as a trick; see Handle Animal skill) with 1
week of work and a DC 25 Handle Animal check.

### Communal Air Walk

**Sources:** Ultimate Combat pg 222

This spell functions like air walk, except divide the duration in 10-minute intervals among the
creatures touched.
