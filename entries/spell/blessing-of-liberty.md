+++
id = "ref/spell/blessing-of-liberty"
kind = "spell"
title = "Blessing of Liberty"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blessing_of_liberty", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Bard", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a feather or small object that symbolizes good fortune)"
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
School: abjuration
Level: 2: Bard, Shaman, Skald
Casting time: 1 standard action
Components: V, S, M (a feather or small object that symbolizes good fortune)
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Heroes of the Streets pg 22

You imbue yourself with the blessings of liberty. You gain a +1 luck bonus per 6 caster levels
(minimum +1, maximum +3) to your CMD and on saving throws against spells and traps that would move
you or impede your movement. You can end the spell's effects as a swift action to gain a +20 foot
enhancement bonus to your base speed for 1 round per whole minute of duration remaining.
