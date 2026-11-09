+++
id = "ref/spell/flame-strike"
kind = "spell"
title = "Flame Strike"
aon = "SpellDisplay.aspx?ItemName=Flame%20Strike"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flame_strike", path = "json/spells4.json" },
]
[[sources]]
publication = "core-rulebook"
page = "283"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "cylinder (10-ft. radius, 40-ft. high)" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Druid, Hunter\
5: Cleric, Inquisitor, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: cylinder (10-ft. radius, 40-ft. high)
Descriptors: fire
:::

A flame strike evokes a vertical column of divine fire. The spell deals 1d6 points of damage per
caster level (maximum 15d6). Half the damage is fire damage, but the other half results directly
from divine power and is therefore not subject to being reduced by resistance to fire-based attacks.
