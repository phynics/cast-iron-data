+++
id = "ref/spell/appearance-of-life-greater"
kind = "spell"
title = "Greater Appearance of Life"
source_ids = ["horror-adventures", "villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "appearance_of_life_greater", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["evil", "glamer"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S, M (one Tiny or larger living creature)"
range = "touch"
effects = [
  { label = "Target", value = "one willing undead creature touched" },
]
duration = "1 hour/level"
saving_throw = "Will disbelief or Will negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Medium, Spiritualist\
5: Arcanist, Cleric, Mesmerist, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, M (one Tiny or larger living creature)
Range: touch
Target: one willing undead creature touched
Duration: 1 hour/level
Saving throw: Will disbelief or Will negates (see text)
Spell resistance: no
Subschool: Glamer
Descriptors: evil, glamer
:::

## Appearance of Life

**Sources:** Horror Adventures pg 108

The illusion makes undead creatures of Medium size or smaller appear as if they were living humanoid
creatures. You can target a number of undead creatures whose total number of Hit Dice is no greater
than twice your caster level. When you create the illusion, you choose the races, genders, and
attire for the undead creatures. Additionally, the illusion makes the undead creatures' movements
appear lifelike (two shuffling zombies could be made to appear as two strolling lovers). The
illusion doesn't create smell, sound, texture, or temperature. Undead with Intelligence scores can
attempt a saving throw to negate the effect of the spell, but mindless undead do not. Any creatures
interacting with the illusion receive a saving throw to disbelieve the illusion.

The illusion interferes with [detect undead](ref/spell/detect-undead), requiring the caster to
succeed at a caster check (DC = 11 + your caster level) for the spell to determine the creatures are
undead.

Appearance of life can be made permanent with a [permanency](ref/spell/permanency) spell by a caster
of 12th level or higher for the cost of 10,000 gp.

### Greater Appearance of Life

**Sources:** Villain Codex pg 8

This spell functions as appearance of life, except that you can disguise a single undead creature
regardless of its number of Hit Dice, and the illusion also creates relevant smells, sounds,
textures, and temperatures to match the appearance. If you disguise the target as a living version
of itself, creatures that interact with the target take a -5 penalty on their Will saving throws to
disbelieve the illusion, though if the target attacks a creature, the attacked creature no longer
takes this penalty.
