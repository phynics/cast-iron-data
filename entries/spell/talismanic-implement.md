+++
id = "ref/spell/talismanic-implement"
kind = "spell"
title = "Talismanic Implement"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "talismanic_implement", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Occultist", level = 3 },
]
casting_time = "10 minutes"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level (d) or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Occultist
Casting time: 10 minutes
Components: V
Range: personal
Duration: 1 hour/level (d) or until discharged
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Occult Adventures pg 188

This spell functions as [contingency](ref/spell/contingency), but you invest a spell whose level
doesn't exceed one-quarter of your level (rounded down, maximum spell level 3rd) into one of your
implements that holds 2 or more points of mental focus. The spell's school must match that of the
implement, and the spell must be one that affects only your person. Casting talismanic implement
reduces the selected implement's mental focus by 2, including for the purposes of determining the
effects of resonant powers. When you refresh your mental focus, talismanic implement ends
automatically, even if the duration hasn't elapsed. Unlike contingency, you may have multiple
talismanic implements simultaneously, though a single implement can hold only one talismanic
implement spell, and if you have any talismanic implements, you can't have any other kind of
contingency in effect.
