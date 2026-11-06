+++
id = "ref/spell/sympathetic-vibration"
kind = "spell"
title = "Sympathetic Vibration"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sympathetic_vibration", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Skald", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, F (a tuning fork)"
range = "touch"
effects = [
  { label = "Target", value = "one freestanding structure" },
]
duration = "up to 1 round/level"
saving_throw = "none; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Bard, Skald
Casting time: 10 minutes
Components: V, S, F (a tuning fork)
Range: touch
Duration: up to 1 round/level
Saving throw: none; see text
Spell resistance: yes
Target: one freestanding structure
Descriptors: sonic
:::

**Sources:** PRPG Core Rulebook pg 357

By attuning yourself to a freestanding structure, you can create a damaging vibration within it.
Once it begins, the vibration deals 2d10 points of damage per round to the target structure,
bypassing [hardness](ref/umr/hardness). You can choose at the time of casting to limit the duration
of the spell; otherwise it lasts for 1 round per level. If the spell is cast upon a target that is
not freestanding, the surrounding stone dissipates the effect and no damage occurs.

Sympathetic vibration cannot affect creatures (including constructs). Since a structure is an
unattended object, it gets no saving throw to resist the effect.
