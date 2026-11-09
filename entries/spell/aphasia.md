+++
id = "ref/spell/aphasia"
kind = "spell"
title = "Aphasia"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aphasia", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "204"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (see text)
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You render the target unable to understand any language, including spoken language, written
language, sign language, gestures attempting to mimic a crude language, or even truespeech and
telepathy. The affected creature is unable to communicate, use command words, cast spells with
verbal components, or use any other abilities that requires language. At the end of each of its
turns, the subject can attempt a new saving throw to end the effect.

[Tongues](ref/spell/tongues) counters and dispels aphasia, and a creature with the tongues spell
active is immune to aphasia. Oracles with the Tongues curse ignore aphasia in combat.
