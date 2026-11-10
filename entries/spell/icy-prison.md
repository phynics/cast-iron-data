+++
id = "ref/spell/icy-prison"
kind = "spell"
title = "Icy Prison"
aon = "SpellDisplay.aspx?ItemName=Icy%20Prison"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "icy_prison", path = "json/spells5.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "224"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level; see text"
saving_throw = "Reflex partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level; see text
Saving throw: Reflex partial
Spell resistance: yes
Target: one creature
Descriptors: cold
:::

You trap the target in solid ice 1 inch thick per caster level. If the creature fails its save, it
is helpless, but can still breathe (the ice blocks line of effect to the target). If the target
makes its save, it gains the entangled condition but can otherwise act normally. Whether or not the
target saves, it takes 1 point of cold damage per caster level each round it is helpless or
entangled in the ice. The ice has [hardness](ref/umr/hardness) 0 and 3 hit points per inch of
thickness; if broken, the creature is freed. A creature can break the ice as a full-round action
with a successful Strength check (DC 15 + your caster level).
