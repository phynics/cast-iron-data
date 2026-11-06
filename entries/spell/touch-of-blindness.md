+++
id = "ref/spell/touch-of-blindness"
kind = "spell"
title = "Touch of Blindness"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_blindness", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["darkness", "shadow"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "creature or creatures touched (up to one/level)" },
]
duration = "1 round/level (see text)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Arcanist, Bard, Cleric, Oracle, Shaman, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: touch
Duration: 1 round/level (see text)
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature or creatures touched (up to one/level)
Descriptors: darkness, shadow
:::

**Sources:** Blood of Shadows pg 29

A touch from your hand, which is engulfed in darkness, disrupts a creature's vision by coating its
eyes in supernatural darkness. Each touch causes the target to become blinded for 1 round unless it
makes a successful Fortitude saving throw. You can use this melee touch attack up to one time per
caster level. Any touch attack not used after 1 round per caster level is lost.
