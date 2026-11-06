+++
id = "ref/spell/touch-of-fatigue"
kind = "spell"
title = "Touch of Fatigue"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_fatigue", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Adept", level = 0 },
  { class = "Arcanist", level = 0 },
  { class = "Mesmerist", level = 0 },
  { class = "Occultist", level = 0 },
  { class = "Shaman", level = 0 },
  { class = "Sorcerer", level = 0 },
  { class = "Witch", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of sweat)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 0: Adept, Arcanist, Mesmerist, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of sweat)
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
:::

**Sources:** PRPG Core Rulebook pg 360

You channel negative energy through your touch, fatiguing the target. You must succeed on a touch
attack to strike a target. The subject is immediately fatigued for the spell's duration.

This spell has no effect on a creature that is already fatigued. Unlike with normal fatigue, the
effect ends as soon as the spell's duration expires.
