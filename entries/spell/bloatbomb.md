+++
id = "ref/spell/bloatbomb"
kind = "spell"
title = "Bloatbomb"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloatbomb", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["acid", "death"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous and 1 minute/level (see text)"
saving_throw = "Fortitude negates or Reflex half (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous and 1 minute/level (see text)
Saving throw: Fortitude negates or Reflex half (see text)
Spell resistance: yes
Target: living creature touched
Descriptors: acid, death
:::

**Sources:** Advanced Class Guide pg 175

The target creature dies if it fails a Fortitude saving throw and its Hit Dice are no more than half
your caster level. If it dies, its corpse rapidly putrefies. The next creature to touch the corpse
within 1 minute per level of the target's death causes the corpse to explode in a 10-foot-radius
burst, dealing 3d6 points of acid damage (Reflex half).
