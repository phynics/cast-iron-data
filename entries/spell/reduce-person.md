+++
id = "ref/spell/reduce-person"
kind = "spell"
title = "Reduce Person"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reduce_person", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S, M (a pinch of powdered iron)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Arcanist, Bloodrager, Investigator, Magus, Medium, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 round
Components: V, S, M (a pinch of powdered iron)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one humanoid creature
:::

**Sources:** PRPG Core Rulebook pg 330

This spell causes instant diminution of a humanoid creature, halving its height, length, and width
and dividing its weight by 8. This decrease changes the creature's size category to the next smaller
one. The target gains a +2 size bonus to Dexterity, a -2 size penalty to Strength (to a minimum of
1), and a +1 bonus on attack rolls and AC due to its reduced size.

A Small humanoid creature whose size decreases to Tiny has a space of 2-1/2 feet and a natural reach
of 0 feet (meaning that it must enter an opponent's square to attack). A Large humanoid creature
whose size decreases to Medium has a space of 5 feet and a natural reach of 5 feet. This spell
doesn't change the target's speed.

All equipment worn or carried by a creature is similarly reduced by the spell.

Melee and projectile weapons [deal less damage](ref/misc/damage-die-adjustments). Other magical
properties are not affected by this spell. Any reduced item that leaves the reduced creature's
possession (including a projectile or thrown weapon) instantly returns to its normal size. This
means that thrown weapons deal their normal damage (projectiles deal damage based on the size of the
weapon that fired them).

Multiple magical effects that reduce size do not stack. Reduce person counters and dispels
[enlarge person](ref/spell/enlarge-person).

Reduce person can be made permanent with a [permanency](ref/spell/permanency) spell.

### Mythic Reduce Person

**Sources:** Mythic Adventures pg 105

You can decrease the target's size by up to two categories, to a minimum of Tiny. If the target
shrinks two sizes, its weight decreases by a factor of 16 and it gains a +4 size bonus to Dexterity,
a -4 size penalty to Strength, and a +2 bonus on attack rolls and to AC because of its decreased
size. A Medium or Small humanoid creature whose size decreases to Tiny has a space of 2-1/2 feet and
a natural reach of 0 feet.

Mythic reduce person counters and dispels mythic [enlarge person](ref/spell/enlarge-person).
