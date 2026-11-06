+++
id = "ref/spell/confess"
kind = "spell"
title = "Confess"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "confess", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round"
saving_throw = "Will partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Inquisitor, Mesmerist, Psychic
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Will partial, see text
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: language-dependant, mind-affecting
:::

**Sources:** Advanced Player's Guide pg 212

You ask the target creature a single question. On the subject's next action, it must answer
truthfully in the same language as the question or take 1d6 points of damage per two caster levels
(maximum 5d6) and be sickened for 2d4 rounds. A successful Will save negates the sickening effect
and halves the damage. A creature that is unable to answer still takes damage.
