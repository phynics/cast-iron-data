+++
id = "ref/spell/compulsive-liar"
kind = "spell"
title = "Compulsive Liar"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "compulsive_liar", path = "json/spells12.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "206"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Mesmerist, Skald\
2: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

The target becomes unable to speak the truth. Lies the target speaks don't need to be convincing,
nor do they even need to be consistent, but they can't be true as far as the target is aware. This
extends to non-verbal communication, such as hand signs or written notes. The spell allows talking
in metaphors and talking about fictional figures.

The spell doesn't affect the target's ability to say things that are neither true nor false, such as
questions, commands, or verbal spell components. If the target of this spell is simultaneously
compelled to tell the truth (for instance, by being within a zone of truth), the target is only able
to say things that are neither true nor false.
