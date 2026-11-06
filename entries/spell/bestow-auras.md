+++
id = "ref/spell/bestow-auras"
kind = "spell"
title = "Bestow Auras"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bestow_auras", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Paladin", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Antipaladin, Paladin
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: one creature
:::

**Sources:** Advanced Class Guide pg 175

You transfer one or more of your paladin or antipaladin auras (such as aura of courage and aura of
resolve) to another creature. You retain the personal effect of that aura, but the target becomes
the center of the aura effect instead of you. For example, if you transfer your aura of courage, you
remain immune to fear, but the target becomes the center of the aura that grants a +4 morale bonus
on saves against fear effects. If an aura functions only when you are conscious, the transferred
aura functions only when the target is conscious. If an aura functions only when you expend uses of
another ability (such as with aura of justice or aura of vengeance), the transferred aura functions
only if the target has that other ability and expends uses of it to activate the aura.

You cannot transfer an aura that affects only you (such as aura of good).
