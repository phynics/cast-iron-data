+++
id = "ref/spell/invigorating-repose"
kind = "spell"
title = "Invigorating Repose"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invigorating_repose", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 hour or until discharged
Saving throw: none
Spell resistance: no
Target: you
Subschool: Healing
:::

**Sources:** Dwarves of Golarion pg 22

> _In order to prepare this spell, the caster must spend an hour performing a ritual in which he
> beseeches [Torag](ref/faith/torag) (or a member of his family) for the aid of
> [Magrim](ref/faith/magrim). For 24 hours after the ritual, the caster may prepare spells of the
> requested deity. The caster may only attune himself to one additional deity at a time._

This spell enhances your spells that bring the dead back to life. If you cast
[raise dead](ref/spell/raise-dead), the target creature is restored to full hit points. If you cast
breath of life, that spell can revive a dead target as long as you cast it within a number of rounds
equal to half your caster level, and the healing effect is treated as if the spell were empowered
with the [Empower Spell](ref/feat/empower-spell) feat. Casting any of these spells discharges the
invigorating repose spell.
