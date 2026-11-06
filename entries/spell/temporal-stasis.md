+++
id = "ref/spell/temporal-stasis"
kind = "spell"
title = "Temporal Stasis"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "temporal_stasis", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (powdered diamond, emerald, ruby, and sapphire dust worth 5,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (powdered diamond, emerald, ruby, and sapphire dust worth 5,000 gp)
Range: touch
Duration: permanent
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
:::

**Sources:** PRPG Core Rulebook pg 359

You must succeed on a melee touch attack. You place the subject into a state of suspended animation.
For the creature, time ceases to flow, and its condition becomes fixed. The creature does not grow
older. Its body functions virtually cease, and no force or effect can harm it. This state persists
until the magic is removed (such as by a successful [dispel magic](ref/spell/dispel-magic) spell or
a [freedom](ref/spell/freedom) spell).
