+++
id = "ref/spell/giant-vermin"
kind = "spell"
title = "Giant Vermin"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "giant_vermin", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "1 or more vermin, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Druid, Hunter, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes
Targets: 1 or more vermin, no two of which can be more than 30 ft. apart
:::

**Sources:** PRPG Core Rulebook pg 290

You turn a number of normal-sized centipedes, scorpions, or spiders into their giant counterparts.
Only one type of vermin can be transmuted (so a single casting cannot affect both a centipede and a
spider). The number of vermin which can be affected by this spell depends on your caster level, as
noted on the table below.

Giant vermin created by this spell do not attempt to harm you, but your control of such creatures is
limited to simple commands ("Attack," "Defend," "Stop," and so forth). Orders to attack a certain
creature when it appears or guard against a particular occurrence are too complex for the vermin to
understand. Unless commanded to do otherwise, the giant vermin attack whomever or whatever is near
them.

|Caster Level|Centipedes|Scorpions|Spiders|
| --- | --- | --- | --- |
|9th or lower|3|1|2|
|10th-13th|4|2|3|
|14th-17th|6|3|4|
|18th-19th|8|4|5|
|20th or higher|12|6|8|

### Mythic Giant Vermin

**Sources:** Mythic Adventures pg 96\
The vermin you transform with this spell gain DR 5/magic and either the advanced creature template
or the giant creature template.

_Augmented (6th):_ If you expend two uses of mythic power, any vermin you transform also gains
either the agile or savage [mythic template](ref/rule/mythic-simple-templates) while the spell
lasts.

If you're at least 9th tier and expend three uses of mythic power, the duration changes to
instantaneous, meaning the vermin retain their giant size. After a number of days equal to your
tier, you lose control over the vermin unless you have some other way of controlling them, and they
lose the agile or savage mythic template but retain the advanced or giant creature template.
