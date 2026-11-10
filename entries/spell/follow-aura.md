+++
id = "ref/spell/follow-aura"
kind = "spell"
title = "Follow Aura"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "follow_aura", path = "json/spells13.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "224"

[fields]
kind = "spell"
school = "divination [chaotic, evil, good, or lawful]"
levels = [
  { class = "Inquisitor", level = 2 },
  { class = "Occultist", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination \[chaotic, evil, good, or lawful\]
Level: 2: Inquisitor\
3: Occultist
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

_Choose one alignment type:_ chaotic, evil, good, or lawful. You gain the ability to follow the
trail of a strong or overwhelming aura of that alignment (see [detect evil](ref/spell/detect-evil)).
This is treated as tracking using the scent special quality, except you are following the traces of
their aura upon the ground rather than their scent, and you receive no bonus on Perception checks.
At 10th level, you can track the trail of creatures with a moderate alignment aura as well.

When you use this spell to track a given alignment, it gains the descriptor of the opposite
alignment. For example, when follow aura is used to track evil, it gains the good descriptor.
