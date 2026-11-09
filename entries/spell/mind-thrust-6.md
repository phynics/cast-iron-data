+++
id = "ref/spell/mind-thrust-6"
kind = "spell"
title = "Mind Thrust VI"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_thrust_6", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/mind-thrust-4" },
]
[[sources]]
publication = "occult-adventures"
page = "177"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Psychic", level = 1 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

### Mind Thrust VI

This functions as [mind thrust IV](ref/spell/mind-thrust-4), but the target takes 1d8 points of
damage per caster level (maximum 20d8) and is exhausted and stunned for 1 round if it fails its
save. This spell can be undercast.
