+++
id = "ref/spell/wind-walk"
kind = "spell"
title = "Wind Walk"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wind_walk", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["air"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 7 },
  { class = "Investigator", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 7 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "you and one touched creature per three levels" },
]
duration = "1 hour/level (d); see text"
saving_throw = "no and Will negates (harmless)"
spell_resistance = "no and yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Alchemist, Cleric, Investigator, Oracle, Warpriest\
7: Druid, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 hour/level (d); see text
Saving throw: no and Will negates (harmless)
Spell resistance: no and yes (harmless)
Targets: you and one touched creature per three levels
Descriptors: air
:::

**Sources:** PRPG Core Rulebook pg 369

You alter the substance of your body to a cloud-like vapor (as the
[gaseous form](ref/spell/gaseous-form) spell) and move through the air, possibly at great speed. You
can take other creatures with you, each of which acts independently.

Normally, a wind walker flies at a speed of 10 feet with perfect maneuverability. If desired by the
subject, a magical wind wafts a wind walker along at up to 600 feet per round (60 mph) with poor
maneuverability. Wind walkers are not invisible but rather appear misty and translucent. If fully
clothed in white, they are 80% likely to be mistaken for clouds, fog, vapors, or the like.

A wind walker can regain its physical form as desired and later resume the cloud form. Each change
to and from vaporous form takes 5 rounds, which counts toward the duration of the spell (as does any
time spent in physical form). As noted above, you can dismiss the spell, and you can even dismiss it
for individual wind walkers and not others.

For the last minute of the spell's duration, a wind walker in cloud form automatically descends 60
feet per round (for a total of 600 feet), though it may descend faster if it wishes. This descent
serves as a warning that the spell is about to end.
