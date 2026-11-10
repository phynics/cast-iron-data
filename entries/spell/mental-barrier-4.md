+++
id = "ref/spell/mental-barrier-4"
kind = "spell"
title = "Mental Barrier IV"
aon = "SpellDisplay.aspx?ItemName=Mental%20Barrier%20IV"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mental_barrier_4", path = "json/spells14.json" },
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

### Mental Barrier IV

This spell functions as [mental barrier III](ref/spell/mental-barrier-3), but if you are struck by a
critical hit or sneak attack, there is a 25% chance that the additional damage is negated (as light
fortification). This does not stack with similar effects that negate the additional damage from a
critical hit or sneak attack. In addition, you are immune to mind thrust I and II, and you take half
damage from mind thrust III, IV, and V (reduced to one-quarter on a successful Will save). This
spell can be undercast.
