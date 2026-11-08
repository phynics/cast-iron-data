+++
id = "ref/spell/etherealness"
kind = "spell"
title = "Etherealness"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "etherealness", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ethereal-jaunt" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 8 },
  { class = "Shaman", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch; see text"
effects = [
  { label = "Targets", value = "you and one other touched creature per three levels" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Psychic\
9: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch; see text
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Targets: you and one other touched creature per three levels
:::

**Sources:** PRPG Core Rulebook pg 279

This spell functions like [ethereal jaunt](ref/spell/ethereal-jaunt), except that you and other
willing creatures joined by linked hands (along with their equipment) become ethereal. Besides
yourself, you can bring one creature per three caster levels to the Ethereal Plane. Once ethereal,
the subjects need not stay together.

When the spell expires, all affected creatures on the Ethereal Plane return to material existence.
