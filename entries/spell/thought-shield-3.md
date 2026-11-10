+++
id = "ref/spell/thought-shield-3"
kind = "spell"
title = "Thought Shield III"
aon = "SpellDisplay.aspx?ItemName=Thought%20Shield%20III"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_shield_3", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/thought-shield-1" },
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

### Thought Shield III

This functions as [thought shield I](ref/spell/thought-shield-1), but the circumstance bonus on Will
saves to resist mind-affecting effects increases to +8. In addition, any creature that tries to read
your thoughts while this spell lasts must succeed at a Will save or be stunned for 1 round. This
spell can be undercast.
