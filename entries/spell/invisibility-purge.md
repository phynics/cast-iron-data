+++
id = "ref/spell/invisibility-purge"
kind = "spell"
title = "Invisibility Purge"
aon = "SpellDisplay.aspx?ItemName=Invisibility%20Purge"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "invisibility_purge", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "302"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Cleric, Inquisitor, Occultist, Oracle, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

You surround yourself with a sphere of power with a radius of 5 feet per caster level that negates
all forms of invisibility.

Anything invisible becomes visible while in the area.
