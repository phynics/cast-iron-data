+++
id = "ref/spell/veil"
kind = "spell"
title = "Veil"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "veil", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Targets", value = "one or more creatures, no two of which can be more than 30 ft. apart" },
]
duration = "concentration+ 1 hour/level (D)"
saving_throw = "Will negates; see text"
spell_resistance = "yes; see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: concentration+ 1 hour/level (D)
Saving throw: Will negates; see text
Spell resistance: yes; see text
Targets: one or more creatures, no two of which can be more than 30 ft. apart
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** PRPG Core Rulebook pg 364

You instantly change the appearance of the subjects and then maintain that appearance for the
spell's duration. You can make the subjects appear to be anything you wish. The subjects look, feel,
and smell just like the creatures the spell makes them resemble. Affected creatures resume their
normal appearances if slain. You must succeed on a Disguise check to duplicate the appearance of a
specific individual. This spell gives you a +10 bonus on the check.

Unwilling targets can negate the spell's effect on them by making Will saves or with
[spell resistance](ref/rule/spell-resistance). Those who interact with the subjects can attempt Will
disbelief saves to see through the glamer, but spell resistance doesn't help.
