+++
id = "ref/spell/appearance-of-life"
kind = "spell"
title = "Appearance of Life"
aon = "SpellDisplay.aspx?ItemName=Appearance%20of%20Life"
source_ids = ["horror-adventures", "villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "appearance_of_life", path = "json/spells.json" },
]
[[sources]]
publication = "horror-adventures"
page = "108"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["evil", "glamer"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, M (one Tiny or larger living creature)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one or more undead creatures" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will disbelief or Will negates (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Medium\
3: Arcanist, Cleric, Mesmerist, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, M (one Tiny or larger living creature)
Range: long (400 ft. + 40 ft./level)
Duration: 10 minutes/level (D)
Saving throw: Will disbelief or Will negates (see text)
Spell resistance: no
Target: one or more undead creatures
Subschool: Glamer
Descriptors: evil, glamer
:::

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
