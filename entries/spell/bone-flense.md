+++
id = "ref/spell/bone-flense"
kind = "spell"
title = "Bone Flense"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bone_flense", path = "json/spells2.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "160"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "M/F (a jagged shard of bone from a humanoid creature)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Bloodrager\
3: Arcanist, Cleric, Druid, Hunter, Inquisitor, Magus, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: M/F (a jagged shard of bone from a humanoid creature)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates
Spell resistance: no
Target: one living creature
:::

Choose a creature that you can see. When that creature is struck by a weapon wielded by a member of
the [Red Mantis](ref/rule/aff-assassins), a sawtooth sabre, or by the claw of a giant mantis, the
bone nearest to the wound instantly sprouts jagged, razor-sharp spurs that flense the muscle and
flesh from the inside out unless the target succeeds at a Fortitude save. The creature takes 1d6
points of piercing damage per caster level. While the bone returns to normal immediately after
dealing damage, the creature takes 1d4 points of bleed damage for 1 round per 2 caster levels. The
victim is sickened by the pain for the duration of the bleeding. If the target creature has no
bones, this spell has no effect.
