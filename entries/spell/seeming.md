+++
id = "ref/spell/seeming"
kind = "spell"
title = "Seeming"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seeming", path = "json/spells15.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/disguise-self" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature per two levels, no two of which can be more than 30 ft. apart" },
]
duration = "12 hours (D)"
saving_throw = "Will negates or Will disbelief (if interacted with)"
spell_resistance = "yes or no; see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Medium\
5: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 12 hours (D)
Saving throw: Will negates or Will disbelief (if interacted with)
Spell resistance: yes or no; see text
Targets: one creature per two levels, no two of which can be more than 30 ft. apart
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** PRPG Core Rulebook pg 339

This spell functions like [disguise self](ref/spell/disguise-self), except that you can change the
appearance of other people as well. Affected creatures resume their normal appearances if slain.
Unwilling targets can negate the spell's effect on them by making Will saves or with
[spell resistance](ref/rule/spell-resistance).
