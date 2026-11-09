+++
id = "ref/spell/fury-of-the-sun"
kind = "spell"
title = "Fury of the Sun"
aon = "SpellDisplay.aspx?ItemName=Fury%20of%20the%20Sun"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fury_of_the_sun", path = "json/spells13.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "131"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse", "fire"]
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Fortitude negates
Spell resistance: yes
Targets: one creature
Descriptors: curse, fire
:::

> _[Ifrits](ref/race/ifrit) have access to the following spell._

You curse the target to suffer unbearable heat. On a failed saving throw, the target is immediately
subjected to severe heat, takes 1d4 points of nonlethal damage, and is suffering from heatstroke
(fatigued). The target must save every 10 minutes as normal for severe heat (starting at DC 15
rather than the DC of this spell). Because this heat is internal, the target cannot avoid it using
the normal methods for escaping heat dangers such as Survival checks or finding shade.
