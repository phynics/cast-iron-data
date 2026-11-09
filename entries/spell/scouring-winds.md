+++
id = "ref/spell/scouring-winds"
kind = "spell"
title = "Scouring Winds"
aon = "SpellDisplay.aspx?ItemName=Scouring%20Winds"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scouring_winds", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "236"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["air", "earth"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "sandstorm in 20-ft. radius, 20 ft. high" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Arcanist, Druid, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes (see text)
Effect: sandstorm in 20-ft. radius, 20 ft. high
Descriptors: air, earth
:::

This spell brings forth a windstorm of stinging sand that blocks all vision. You can move the storm
up to 30 feet each round as a move action.

Any creature in the area takes 3d6 points of piercing damage each round. The area is considered a
windstorm (see the [wind effects](ref/rule/winds) table).

If a creature with [spell resistance](ref/rule/spell-resistance) successfully resists this spell, it
is unaffected by the winds and sand, but still unable to see within the area of the spell.
