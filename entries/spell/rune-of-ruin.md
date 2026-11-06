+++
id = "ref/spell/rune-of-ruin"
kind = "spell"
title = "Rune of Ruin"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rune_of_ruin", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a self-portrait on a thin sheet of paper)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "1 object" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (object)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Bard, Inquisitor, Investigator, Skald\
5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a self-portrait on a thin sheet of paper)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude negates (object)
Spell resistance: no
Target: 1 object
Descriptors: curse
:::

**Sources:** Arcane Anthology pg 22

You curse a magic item, such as magical clothing, a suit of armor, or a weapon. The object is
reduced to 1/4 its normal hit point total, gains the broken condition, and appears damaged and worn.
If it grants a numeric bonus, such as a +2 deflection bonus to AC, that bonus is reduced by 1 for
every 3 caster levels you possess, to a minimum of +0. Other magical qualities fail to work 50% of
the time when called upon, so a resistance bonus on saves or a weapon's flaming special ability
could fail each time the item is used.

If the object is an intelligent magical item, its Ego score remains unchanged despite its reduced
quality. The weapon has only a 50% chance to successfully use any spells or
[spell-like abilities](ref/umr/spell-like-abilities) it has, and has a 25% chance of forgetting its
special purpose (if any). If an intelligent weapon is actively dominating its wielder when it fails
its save against rune of ruin, the wielder gains an immediate saving throw with a +4 bonus to regain
control. Rune of ruin has no affect on magical artifacts.
