+++
id = "ref/spell/anonymous-interaction"
kind = "spell"
title = "Anonymous Interaction"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "anonymous_interaction", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "permanent (see text)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Mesmerist, Psychic, Skald, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent (see text)
Saving throw: Will negates
Spell resistance: yes
Target: one creature/level, no two of which can be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Advanced Class Guide pg 174

You cause the targets to forget all but the most general information about you. If they saw you or
interacted with you, they still remember your presence and your general shape (such as humanoid), as
well as the gist of your interactions with them (such as "She was asking about the queen"), but they
don't remember specifically what you said, details of your appearance, or any identifying
information about you. This spell targets any memories of you in the minute preceding its casting,
but is otherwise permanent.
