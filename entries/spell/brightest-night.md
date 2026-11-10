+++
id = "ref/spell/brightest-night"
kind = "spell"
title = "Brightest Night"
aon = "SpellDisplay.aspx?ItemName=Brightest%20Night"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brightest_night", path = "json/spells2.json" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "15"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one willing creature plus one additional willing creature per 3 levels, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bard, Cleric, Druid, Hunter, Oracle, Paladin, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Targets: one willing creature plus one additional willing creature per 3 levels, no two of which can be more than 30 ft. apart
:::

You grant [low-light vision](ref/rule/low-light-vision) to the affected creatures. Creatures that
already have low-light vision have their existing low-light vision enhanced so that they can see
four times as far in conditions of dim light. Creatures within 10 feet of someone under the effects
of brightest night do not gain concealment from dim light.
