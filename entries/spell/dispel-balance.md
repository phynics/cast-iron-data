+++
id = "ref/spell/dispel-balance"
kind = "spell"
title = "Dispel Balance"
source_ids = ["planar-adventures", "champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dispel_balance", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "you and a touched, neutral creature from another plane, or you and an enchantmnet on a touched creature or object" },
]
duration = "1 round/level or until discharged, whichever comes first"
saving_throw = "see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level or until discharged, whichever comes first
Saving throw: see text
Spell resistance: see text
Target: you and a touched, neutral creature from another plane, or you and an enchantmnet on a touched creature or object
:::

**Sources:** Planar Adventures pg 40, Champions of Balance pg 27

Pulsing bronze energy surrounds you, bestowing three effects.

First, you gain a +3 deflection bonus to AC against attacks by chaotic neutral, lawful neutral,
neutral evil, and neutral good creatures. Against attacks by creatures whose alignment is neutral
with no other alignment components, this deflection bonus is instead +5.

Second, upon making a successful melee touch attack against a creature from another plane with a
neutral component to its alignment, you can banish that creature back to its home plane. The
creature's [spell resistance](ref/rule/spell-resistance) applies to this attempt, and the creature
can negate this effect with a successful Will save. If the creature's alignment is neutral with no
other alignment components, the creature takes a -2 penalty on this saving throw. This use
discharges and ends the spell.

Third, with a touch, you can automatically dispel any one enchantment spell cast by a creature with
a neutral component to its alignment. Spells that can't be dispelled by
[dispel magic](ref/spell/dispel-magic) also can't be dispelled by dispel balance. Saving throws and
[spell resistance](ref/rule/spell-resistance) do not apply to this effect. This use discharges and
ends the spell.
