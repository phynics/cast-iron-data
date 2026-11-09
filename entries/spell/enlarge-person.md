+++
id = "ref/spell/enlarge-person"
kind = "spell"
title = "Enlarge Person"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enlarge_person", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "277"

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
components = "V, S, M (powdered iron)"
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
Components: V, S, M (powdered iron)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one humanoid creature
:::

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
