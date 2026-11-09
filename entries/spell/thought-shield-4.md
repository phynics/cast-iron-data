+++
id = "ref/spell/thought-shield-4"
kind = "spell"
title = "Thought Shield IV"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_shield_4", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/thought-shield-3" },
]
[[sources]]
publication = "occult-adventures"
page = "190"

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

### Thought Shield IV

This functions as [thought shield III](ref/spell/thought-shield-3), but any creature that tries to
read your thoughts while this spell lasts must succeed at a Will save or be stunned for 1d4 rounds.
Additionally, if you succeed at your save against a psychic crush spell, you take no damage. This
spell can be undercast.
