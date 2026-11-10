+++
id = "ref/spell/hoodwink"
kind = "spell"
title = "Hoodwink"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hoodwink", path = "json/spells5.json" },
]
[[sources]]
publication = "villain-codex"
page = "212"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (small piece of black cloth)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "up to one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bard, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (small piece of black cloth)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: up to one creature/level, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

You befuddle the targets' senses, preventing the targets from clearly perceiving their surroundings.
Instead, hoodwinked creatures see only the roughest shapes and details and hear only muffled noises.
However, targets can clearly hear verbal communication from the spell's caster. This spell does not
impart understanding of the caster's language if the creature can't already understand it. Other
than to hear the caster speak, targets automatically fail Perception checks with DCs greater than 5,
and they are too disoriented by the spell to accurately remember the path they took while under its
effects.

While under the effects of this spell, targets without the help of a guide move at half speed, and
any attacks they make are treated as though the creature they are attacking had
[concealment](ref/rule/concealment).

Moving faster than half speed requires targets to succeed at a DC 10 Acrobatics check. Those that
fail this check fall prone. If the target is attacked or physically harmed by any creature other
than another target of hoodwink, the spell's effect ends immediately for that target only.
