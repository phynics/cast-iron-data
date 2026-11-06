+++
id = "ref/spell/telekinetic-projectile"
kind = "spell"
title = "Telekinetic Projectile"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telekinetic_projectile", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Occultist", level = 0 },
  { class = "Psychic", level = 0 },
  { class = "Spiritualist", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "N/A (not listed in spell, assumed one creature or object)" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 0: Occultist, Psychic, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: N/A (not listed in spell, assumed one creature or object)
:::

**Sources:** Occult Adventures pg 188

You fling an object weighing up to 5 pounds at the target. You must succeed at a ranged attack (not
a ranged touch attack) to hit your target; if you hit, you deal 1d6 points of bludgeoning damage to
both the target and the object. The type of object thrown doesn't change the damage type or any
other properties of the attack, even if you throw a weapon or magic item in this way.
