+++
id = "ref/spell/mighty-strength"
kind = "spell"
title = "Mighty Strength"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mighty_strength", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/bulls-strength" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Dwarves of Golarion pg 22

> _In order to prepare this spell, the caster must spend an hour performing a ritual in which he
> beseeches [Torag](ref/faith/torag) (or a member of his family) for the aid of
> [Trudd](ref/faith/trudd). For 24 hours after the ritual, the caster may prepare spells of the
> requested deity. The caster may only attune himself to one additional deity at a time._

As [bull's strength](ref/spell/bulls-strength), except it grants a +8 enhancement bonus to Strength.
