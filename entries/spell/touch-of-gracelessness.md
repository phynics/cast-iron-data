+++
id = "ref/spell/touch-of-gracelessness"
kind = "spell"
title = "Touch of Gracelessness"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_gracelessness", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bloodrager, Bard, Mesmerist, Red Mantis Assassin, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Fortitude partial
Spell resistance: yes
Target: creature touched
:::

**Sources:** Advanced Player's Guide pg 249

With a single touch, you reduce a creature to a fumbling clown. The target takes a penalty to its
Dexterity equal to 1d6+1 per two caster levels (maximum 1d6+5). This penalty cannot drop the
target's Dexterity score below 1.

In addition, if the subject moves more than half its speed, it falls prone. If the subject flies,
its maneuverability is reduced by one step (perfect maneuverability becomes good, good becomes
average, and so on).

A successful Fortitude save halves the penalty to Dexterity and negates the possibility of falling
prone or the reduction to fly maneuverabilities.
