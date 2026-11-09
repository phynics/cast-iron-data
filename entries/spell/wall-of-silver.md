+++
id = "ref/spell/wall-of-silver"
kind = "spell"
title = "Wall of Silver"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wall_of_silver", path = "json/spells11.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "177"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "transparent wall 20 ft. high by up to 20 ft. long/level" },
]
duration = "1 round/leve"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Bard, Inquisitor, Skald\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/leve
Saving throw: see text
Spell resistance: yes
Effect: transparent wall 20 ft. high by up to 20 ft. long/level
Descriptors: good
:::

You create a wall of translucent silver energy that hums and vibrates at the slightest touch.
Objects and nonevil creatures can pass through this wall without difficulty. However, spells and
effects with the evil descriptor treat this barrier as a wall of force, which blocks line of effect.

Evil creatures that pass through the wall take 3d6 points of damage + 1 point of damage per caster
level (maximum 3d6+20) and are blinded for 1 round. Creatures of any alignment that are particularly
vulnerable to silver (such as those with [damage reduction](ref/rule/damage-reduction) bypassed by
silver, like devils or lycanthropes) instead take 1d6 points of damage per caster level (maximum
15d6), are staggered for 1 round, and are permanently blinded. A creature that succeeds at a Will
save reduces the damage by half and negates the blinding and staggering effects.

If you create a wall of silver so that it appears where creatures are, each creature takes damage as
if passing through the wall. Each such creature can avoid the wall (ending up on the side of its
choice) and thus take no damage by succeeding at a Reflex save.
