+++
id = "ref/spell/carrion-compass"
kind = "spell"
title = "Carrion Compass"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "carrion_compass", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one undead creature" },
]
duration = "10 minutes/level"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Cleric, Hunter, Oracle, Ranger, Warpriest, Witch\
2: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: no
Target: one undead creature
:::

**Sources:** Undead Slayer's Handbook pg 26

You animate one of the target's fetid organs so that it leads you to the undead creature's most
recent controller or the cause of the creature's undeath. The organ (typically the heart, the brain,
or an eyeball) floats in front of you at chest level and slowly leads you to the undead creature's
most recent controller at a rate of 30 feet per round, always staying within your range of vision.
If the creature from which the organ originated had no controller, but rather was created
deliberately by another creature, the organ instead leads you to that creator. If the undead was
animated by an effect or event at a particular location, the organ leads you to that location. If
the creature was animated by none of the methods above, if it was self-created, or if the creature's
most recent controller no longer exists, the spell fails. Once the organ is within 10 feet of its
intended destination, the spell ends, and the organ falls to the ground.

The organ cannot engage in combat or execute any other task aside from leading you to its intended
target. It may pass through small slits and crevices, though it will not leave your range of vision.
The organ cannot travel more than 5 miles from the spot where you cast the spell. If the undead
creature to which the organ belonged is destroyed, the spell ends and the organ falls to the ground.
