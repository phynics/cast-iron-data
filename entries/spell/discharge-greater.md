+++
id = "ref/spell/discharge-greater"
kind = "spell"
title = "Greater Discharge"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "discharge_greater", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/discharge" },
]
[[sources]]
publication = "technology-guide"
page = "9"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Magus", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target or Area", value = "one creature or technological object, or a 20-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 6: Arcanist, Bard, Cleric, Magus, Oracle, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Target or Area: one creature or technological object, or a 20-ft.-radius burst
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: no
:::

### Greater Discharge

This spell functions as [discharge](ref/spell/discharge), except it can discharge multiple
technological objects and can be used to target an area.

You choose to use greater discharge in one of two ways: an area discharge or a targeted discharge.

_Area Discharge:_ When greater discharge is used in this way, the spell affects everything within a
20-foot-radius burst. Each creature in the area is affected as though by discharge (affecting only
one object in the creature's possession), and each unattended object is similarly affected.

_Targeted Discharge:_ This spell functions as discharge, but if the target is a creature, it can
discharge one randomly determined object from the target's charged or electrically powered
possessions for every 4 caster levels you possess.
