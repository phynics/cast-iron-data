+++
id = "ref/spell/mental-barrier-5"
kind = "spell"
title = "Mental Barrier V"
aon = "SpellDisplay.aspx?ItemName=Mental%20Barrier%20V"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mental_barrier_5", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mental-barrier-3" },
]
[[sources]]
publication = "occult-adventures"
page = "176"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Psychic", level = 2 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Psychic
Casting time: 1 immediate action
Components: V
Range: personal
Duration: 1 round
Saving throw: none
Spell resistance: no
Target: you
:::

### Mental Barrier V

This functions as [mental barrier III](ref/spell/mental-barrier-3), but if you are struck by a
critical hit or sneak attack, there is a 50% chance that the additional damage is negated (as
moderate fortification). This does not stack with similar effects that negate the additional damage
from a critical hit or sneak attack. In addition, you are immune to mind thrust I, II, and III, and
you take half damage from mind thrust IV, V, and VI (reduced to one-quarter on a successful Will
save). This spell can be undercast.
