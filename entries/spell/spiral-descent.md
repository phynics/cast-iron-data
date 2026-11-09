+++
id = "ref/spell/spiral-descent"
kind = "spell"
title = "Spiral Descent"
aon = "SpellDisplay.aspx?ItemName=Spiral%20Descent"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spiral_descent", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spiral-ascent" },
]
[[sources]]
publication = "inner-sea-temples"
page = "43"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "you and touched objects" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: you and touched objects
Subschool: Teleportation
:::

### Spiral Descent

This spell functions as [spiral ascent](ref/spell/spiral-ascent), except the destination and
direction of travel is downward from your current location.
