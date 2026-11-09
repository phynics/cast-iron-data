+++
id = "ref/spell/cold-ice-strike"
kind = "spell"
title = "Cold Ice Strike"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cold_ice_strike", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "211"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 swift action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft. line" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Cleric, Occultist, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 swift action
Components: V, S
Range: 30 ft.
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 30-ft. line
Descriptors: cold
:::

You create a shredding flurry of ice slivers, which blast from your hand in a line. The line deals
1d6 points of cold damage per caster level (maximum 15d6).
