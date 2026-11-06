+++
id = "ref/spell/retrocognition"
kind = "spell"
title = "Retrocognition"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "retrocognition", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Medium", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 minute"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "concentration, up to 1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium, Occultist\
5: Psychic\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S
Range: personal
Duration: concentration, up to 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Occult Adventures pg 185

This spell allows you to gain psychic impressions from past events that occurred in your current
location. Retrocognition reveals psychic impressions from events that occurred over the course of
the last hour throughout the first minute of the duration, followed by impressions from the next
hour back the next minute you concentrate, and so on. If a psychically traumatic or turbulent event
happened during that time period, you must succeed at a [concentration](ref/rule/concentration)
check (DC = 20, 30, or 40, depending on the severity of the psychic disturbance) or lose
concentration on the spell.

At caster level 13th and higher, you can choose to collect impressions from over the course of a
longer interval of time than an hour, beginning at 1 week per minute of concentration (as listed on
the table below). The amount of detail you receive diminishes, so this eventually makes it harder to
distinguish impressions left by anything but the most major events.

|Caster Level|Time Period|
| --- | --- |
|13th-15th|1 week per minute|
|16th-18th|1 year per minute|
|19th+|1 century per minute|
