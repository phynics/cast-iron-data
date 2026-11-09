+++
id = "ref/spell/thought-shield-5"
kind = "spell"
title = "Thought Shield V"
aon = "SpellDisplay.aspx?ItemName=Thought%20Shield%20V"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_shield_5", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/thought-shield-4" },
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

### Thought Shield V

This functions as [thought shield IV](ref/spell/thought-shield-4), except as noted above. This spell
immediately ends if you fail a Will saving throw against a mind-affecting effect. This spell can be
undercast.
