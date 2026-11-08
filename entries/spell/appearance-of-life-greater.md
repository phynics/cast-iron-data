+++
id = "ref/spell/appearance-of-life-greater"
kind = "spell"
title = "Greater Appearance of Life"
source_ids = ["horror-adventures", "villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "appearance_of_life_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/appearance-of-life" },
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

### Greater Appearance of Life

**Sources:** Villain Codex pg 8

This spell functions as [appearance of life](ref/spell/appearance-of-life), except that you can
disguise a single undead creature regardless of its number of Hit Dice, and the illusion also
creates relevant smells, sounds, textures, and temperatures to match the appearance. If you disguise
the target as a living version of itself, creatures that interact with the target take a -5 penalty
on their Will saving throws to disbelieve the illusion, though if the target attacks a creature, the
attacked creature no longer takes this penalty.
