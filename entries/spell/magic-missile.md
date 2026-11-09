+++
id = "ref/spell/magic-missile"
kind = "spell"
title = "Magic Missile"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_missile", path = "json/spells6.json" },
]
[[sources]]
publication = "core-rulebook"
page = "309"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "up to five creatures, no two of which can be more than 15 ft. apart" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Arcanist, Bloodrager, Magus, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Targets: up to five creatures, no two of which can be more than 15 ft. apart
Descriptors: force
:::

A missile of magical energy darts forth from your fingertip and strikes its target, dealing 1d4+1
points of force damage.

The missile strikes unerringly, even if the target is in melee combat, so long as it has less than
total cover or total concealment. Specific parts of a creature can't be singled out. Objects are not
damaged by the spell.

For every two caster levels beyond 1st, you gain an additional missile-two at 3rd level, three at
5th, four at 7th, and the maximum of five missiles at 9th level or higher. If you shoot multiple
missiles, you can have them strike a single creature or several creatures. A single missile can
strike only one creature. You must designate targets before you check for
[spell resistance](ref/rule/spell-resistance) or roll damage.
