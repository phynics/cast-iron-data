+++
id = "ref/spell/invisibility-alarm"
kind = "spell"
title = "Invisibility Alarm"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_alarm", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/alarm" },
]
[[sources]]
publication = "advanced-class-guide"
page = "185"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a tiny bell and a piece of very fine silver wire)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on a point in space" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Alchemist, Arcanist, Bard, Hunter, Inquisitor, Investigator, Psychic, Ranger, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a tiny bell and a piece of very fine silver wire)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Area: 20-ft.-radius emanation centered on a point in space
:::

This spell functions as [alarm](ref/spell/alarm), except it is triggered only by invisible creatures
entering or leaving the warded area. The spell has a different mental alarm depending on whether the
invisible creature is entering or leaving the area. This spell does not aid you in sensing or
pinpointing the location of an invisible creature within the spell's area.

Invisibility alarm can be made permanent with a [permanency](ref/spell/permanency) spell by a caster
of 9th level or higher at a cost of 2,500 gp.
