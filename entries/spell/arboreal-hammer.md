+++
id = "ref/spell/arboreal-hammer"
kind = "spell"
title = "Arboreal Hammer"
source_ids = ["ultimate-magic", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arboreal_hammer", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one Huge or larger tree" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Druid, Hunter
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: one Huge or larger tree
:::

**Sources:** Ultimate Magic pg 206

This spell animates a tree's branch and directs it against your foes. At caster level 10th or lower,
you can target a Huge tree. At caster level 11th-15th, you can target a Gargantuan tree, and at
caster level 16th or higher you can target a Colossal tree. The animated branch makes slam attacks
with a Strength score equal to 10 + your caster level. The branch strikes once per round with an
attack bonus equal to your caster level + the branch's Strength modifier, adjusted by the
appropriate size modifier (-2 for Huge, -4 for Gargantuan, -8 for Colossal). A Huge tree's slam
deals 2d6 points of damage, a Gargantuan tree's slam deals 3d6 points of damage, and a Colossal
tree's slam deals 4d6 points of damage; the tree adds 1-1/2 times its Strength modifier to this
damage. A Huge tree has reach 15 feet, a Gargantuan has reach 20 feet, and a Colossal has reach 30
feet. The tree attacks the creature you designate when you cast the spell, and is unable to move.
You can direct the tree against a new target as a move action. The tree does not gain a bonus for
flanking, nor can it help another combatant flank. It cannot attack a foe you cannot see.

### Mythic Arboreal Hammer

**Sources:** Mythic Adventures pg 84\
You animate two branches instead of one, allowing the tree to attack twice per round. Add your tier
to your caster level when determining the tree's Strength score. A creature struck by both slam
attacks in the same round must succeed at a Fortitude save against the spell's DC or be staggered
for 1 round.

_Augmented (7th):_ If you expend two uses of mythic power, the tree attempts three slam attacks per
round and its slams bypass all [damage reduction](ref/rule/damage-reduction). A creature struck by
all three slam attacks in the same round is stunned for 1 round and staggered for 1d4 rounds after
the stun ends. A successful Fortitude save negates the stun and reduces the duration of being
staggered by half.
