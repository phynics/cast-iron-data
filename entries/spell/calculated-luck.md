+++
id = "ref/spell/calculated-luck"
kind = "spell"
title = "Calculated Luck"
source_ids = ["occult-mysteries"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calculated_luck", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Cleric, Oracle, Warpriest\
4: Witch
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Occult Mysteries pg 50

You are able to use the Path of Numbers to substantially boost your combat preparedness, but your
foresight comes at a price. Roll 3d8 and refer to the
[Eight Basic Energies table](ref/rule/mathematical-spellcasting). After rolling, assign each die to
one of the following.

- Energy Type: You gain vulnerability to the energy type that matches the die's result for the
  duration of the spell. You take half again as much damage (+50%) from that energy type, regardless
  of whether you successfully saved against the damaging spell or effect.
- Magic School: For the spell's duration, you cast all spells from the school that matches the die's
  result at +1 caster level.
- d20 Roll Type: You receive a +2 luck bonus on the d20 roll that matches the die's result for the
  duration of the spell.
