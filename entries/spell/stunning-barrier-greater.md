+++
id = "ref/spell/stunning-barrier-greater"
kind = "spell"
title = "Greater Stunning Barrier"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stunning_barrier_greater", path = "json/spells16.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/stunning-barrier" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level or until discharged"
saving_throw = "none and Will negates (see text)"
spell_resistance = "no and yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Arcanist, Cleric, Inquisitor, Oracle, Paladin, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 1 round/level or until discharged
Saving throw: none and Will negates (see text)
Spell resistance: no and yes (see text)
:::

## Stunning Barrier

**Sources:** Advanced Class Guide pg 194

You are closely surrounded by a barely visible magical field. The field provides a +1 deflection
bonus to AC and a +1 resistance bonus on saves. Any creature that strikes you with a melee attack is
stunned for 1 round (Will negates). Once the field has stunned an opponent, the spell is discharged.

### Greater Stunning Barrier

**Sources:** Advanced Class Guide pg 195

This spell functions as [stunning barrier](ref/spell/stunning-barrier), except as noted above, and
it provides a +2 bonus to AC and on saving throws. It is not discharged until it has stunned a
number of creatures equal to your caster level.
