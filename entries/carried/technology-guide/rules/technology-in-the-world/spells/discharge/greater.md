+++
id = "ref/carried/technology-guide/rules/technology-in-the-world/spells/discharge/greater"
kind = "spell"
title = "Discharge, Greater"
source_ids = ["technology-guide"]
section = ["Rules", "Technology in the world", "Spells", "Discharge"]
tags = ["abjuration"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Technology Guide/Rules/Technology in the world/Spells/Discharge/Greater", path = "technology_guide/spell/discharge_greater.json" },
]

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
effects = [
  { label = "Target or Area", value = "one creature or technological object, or a 20-ft.-radius burst" },
]
+++

::: statblock
School: abjuration
Level: 6: Arcanist, Bard, Cleric, Magus, Oracle, Skald, Sorcerer, Warpriest, Witch, Wizard
Target or Area: one creature or technological object, or a 20-ft.-radius burst
:::

This spell functions as _[discharge](ref/spell/discharge)_, except it can discharge multiple
technological objects and can be used to target an area.

You choose to use _[greater discharge](ref/spell/discharge-greater)_ in one of two ways: an area
discharge or a targeted discharge.

## Area Discharge {#area-discharge}

When _[greater discharge](ref/spell/discharge-greater)_ is used in this way, the spell affects
everything within a 20-foot-radius burst. Each creature in the area is affected as though by
_[discharge](ref/spell/discharge)_ (affecting only one object in the creature's possession), and
each unattended object is similarly affected.

## Targeted Discharge {#targeted-discharge}

This spell functions as _[discharge](ref/spell/discharge)_, but if the target is a creature, it can
discharge one randomly determined object from the target's charged or electrically powered
possessions for every 4 caster levels you possess.
