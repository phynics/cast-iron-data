+++
id = "ref/spell/enlarge-person-mass"
kind = "spell"
title = "Mass Enlarge Person"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enlarge_person_mass", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/enlarge-person" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (powdered iron)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "One humanoid creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Summoner\
4: Arcanist, Bloodrager, Magus, Psychic, Red Mantis Assassin, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 round
Components: V, S, M (powdered iron)
Range: close (25 ft. + 5 ft./2 levels)
Target: One humanoid creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
:::

## Enlarge Person

**Sources:** PRPG Core Rulebook pg 277

This spell causes instant growth of a humanoid creature, doubling its height and multiplying its
weight by 8. This increase changes the creature's size category to the next larger one. The target
gains a +2 size bonus to Strength, a -2 size penalty to Dexterity (to a minimum of 1), and a -1
penalty on attack rolls and AC due to its increased size.

A humanoid creature whose size increases to Large has a space of 10 feet and a natural reach of 10
feet. This spell does not change the target's speed.

If insufficient room is available for the desired growth, the creature attains the maximum possible
size and may make a Strength check (using its increased Strength) to burst any enclosures in the
process. If it fails, it is constrained without harm by the materials enclosing it - the spell
cannot be used to crush a creature by increasing its size.

All equipment worn or carried by a creature is similarly enlarged by the spell. Melee weapons
affected by this spell deal more damage (see
[Table: Tiny and Large Weapon Damage](ref/rule/weapon-descriptions)). Other magical properties are
not affected by this spell. Any enlarged item that leaves an enlarged creature's possession
(including a projectile or thrown weapon) instantly returns to its normal size. This means that
thrown and projectile weapons deal their normal damage. Magical properties of enlarged items are not
increased by this spell.

Multiple magical effects that increase size do not stack.

Enlarge person counters and dispels [reduce person](ref/spell/reduce-person).

Enlarge person can be made permanent with a [permanency](ref/spell/permanency) spell.

### Mythic Enlarge Person

**Sources:** Mythic Adventures pg 93

You can increase the target's size by up to two size categories, to a maximum of Huge. If the target
grows two sizes, its weight increases by a factor of 25, it gains a +4 size bonus to Strength, and
takes a -4 size penalty to Dexterity and a -2 penalty on attack rolls and to AC because of its
increased size. A Medium humanoid creature whose size increases to Huge has a space of 15 feet and a
natural reach of 10 feet. Mythic enlarge person counters and dispels mythic
_[reduce person](ref/spell/reduce-person)._

### Mass Enlarge Person

**Sources:** PRPG Core Rulebook pg 278

This spell functions like [enlarge person](ref/spell/enlarge-person), except that it affects
multiple creatures.
