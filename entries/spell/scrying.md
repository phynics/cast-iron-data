+++
id = "ref/spell/scrying"
kind = "spell"
title = "Scrying"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scrying", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 hour"
components = "V, S, F (a silver mirror worth 1,000 gp), M/DF (a pool of water)"
range = "see text"
effects = [
  { label = "Effect", value = "magical sensor" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Bard, Medium, Mesmerist, Skald\
4: Arcanist, Druid, Hunter, Occultist, Psychic, Shaman, Sorcerer, Witch, Wizard\
5: Cleric, Oracle, Spiritualist, Warpriest
Casting time: 1 hour
Components: V, S, F (a silver mirror worth 1,000 gp), M/DF (a pool of water)
Range: see text
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Effect: magical sensor
Subschool: Scrying
:::

**Sources:** PRPG Core Rulebook pg 337

You can observe a creature at any distance. If the subject succeeds on a Will save, the spell fails.
The difficulty of the save depends on how well your knowledge of the subject and what sort of
physical connection (if any) you have to that creature. Furthermore, if the subject is on another
plane, it gets a +5 bonus on its Will save.

|Knowledge|Will Save Modifier|
| --- | --- |
|None\*|+10|
|Secondhand (you have heard of the subject)|+5|
|Firsthand (you have met the subject)|+0|
|Familiar (you know the subject well)|-5|

\*You must have some sort of connection (see below) to a creature of which you have no knowledge.

|Connection|Will Save Modifier|
| --- | --- |
|Likeness or picture|-2|
|Possession or garment|-4|
|Body part, lock of hair, bit of nail, etc.|-10|

If the save fails, you can see and hear the subject and its surroundings (approximately 10 feet in
all directions of the subject). If the subject moves, the sensor follows at a speed of up to 150
feet.

As with all divination (scrying) spells, the sensor has your full visual acuity, including any
magical effects. In addition, the following spells have a 5% chance per caster level of operating
through the sensor: [detect chaos](ref/spell/detect-chaos), [detect evil](ref/spell/detect-evil),
[detect good](ref/spell/detect-good), [detect law](ref/spell/detect-law),
[detect magic](ref/spell/detect-magic), and [message](ref/spell/message).

If the save succeeds, you can't attempt to scry on that subject again for at least 24 hours.

### Greater Scrying

**Sources:** PRPG Core Rulebook pg 337

This spell functions like scrying, except as noted above. Additionally, all of the following spells
function reliably through the sensor: [detect chaos](ref/spell/detect-chaos),
[detect evil](ref/spell/detect-evil), [detect good](ref/spell/detect-good),
[detect law](ref/spell/detect-law), [detect magic](ref/spell/detect-magic),
[message](ref/spell/message), [read magic](ref/spell/read-magic), and [tongues](ref/spell/tongues).
