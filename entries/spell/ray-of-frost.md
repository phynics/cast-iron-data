+++
id = "ref/spell/ray-of-frost"
kind = "spell"
title = "Ray of Frost"
aon = "SpellDisplay.aspx?ItemName=Ray%20of%20Frost"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ray_of_frost", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "330"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 0 },
  { class = "Magus", level = 0 },
  { class = "Sorcerer", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 0: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Effect: ray
Descriptors: cold
:::

A ray of freezing air and ice projects from your pointing finger. You must succeed on a ranged touch
attack with the ray to deal damage to a target. The ray deals 1d3 points of cold damage.
