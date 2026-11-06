+++
id = "ref/spell/poisoned-egg"
kind = "spell"
title = "Poisoned Egg"
source_ids = ["inner-sea-gods", "gods-and-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poisoned_egg", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "one egg" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bard, Cleric, Inquisitor, Magus, Oracle, Red Mantis Assassin, Shaman, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no (object)
Target: one egg
Descriptors: poison
:::

**Sources:** Inner Sea Gods pg 238, Gods and Magic pg 29

You transform the contents of a normal egg into a single dose of
[small centipede poison](ref/eq-poison/small-centipede-poison). The poison reverts to a normal egg
at the end of the spell's duration (the reverted egg substance is harmless unless the poisoned
creature is vulnerable to eggs). The egg may be raw or cooked but must be whole and not empty when
you cast the spell. When applying the poisoned egg's contents to a weapon, the wielder has no chance
of poisoning herself, as though she had the poison use class feature.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
