+++
id = "ref/spell/ego-whip-3"
kind = "spell"
title = "Ego Whip III"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ego_whip_3", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ego-whip-1" },
]
[[sources]]
publication = "occult-adventures"
page = "169"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Psychic", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

### Ego Whip III

This functions as [ego whip I](ref/spell/ego-whip-1), but the target takes a -6 penalty to the
chosen ability score and is staggered for 1d6 rounds on a failed Will save. This spell can be
undercast.
