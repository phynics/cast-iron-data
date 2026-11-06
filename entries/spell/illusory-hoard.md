+++
id = "ref/spell/illusory-hoard"
kind = "spell"
title = "Illusory Hoard"
source_ids = ["dragonslayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "illusory_hoard", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "S, M (an item from the hoard, see below)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates (and see below)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Bard, Skald\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: S, M (an item from the hoard, see below)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level (D)
Saving throw: Will negates (and see below)
Spell resistance: yes
Target: one creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

**Sources:** Dragonslayer's Handbook pg 29

The spell forces the target to believe that nothing in its hoard is missing or has been disturbed.
This spell fools all the senses, convincing the target that its hoard feels and behaves as it
should. Only if the target tries to use an item from this illusory hoard for some other purpose does
it receive another saving throw to disbelieve the effects of the spell (a wizard trying to use an
illusory wand or a dragon trying to unlock a door with an illusory key). For the purposes of this
spell, a hoard is any amount of treasure that is too big to be carried by the treasure's owner
without magical tools such as bags of holding or portable holes, such as a dragon's hoard, a king's
treasury, a merchant's strongbox, or a thief's hidden cache.

The material component is any item worth 10 gp or more taken from the original hoard. This item is
consumed by the spell.
