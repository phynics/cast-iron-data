+++
id = "ref/spell/instant-enemy"
kind = "spell"
title = "Instant Enemy"
aon = "SpellDisplay.aspx?ItemName=Instant%20Enemy"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instant_enemy", path = "json/spells14.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "229"

[fields]
kind = "spell"
school = "enchantment"
levels = [
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
]
casting_time = "1 swift action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature that is not your favored enemy." },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Hunter, Ranger
Casting time: 1 swift action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: one creature that is not your favored enemy.
:::

With this spell you designate the target as your [favored enemy](ref/ability/favored-enemy) for the
remainder of its duration. Select one of your favored enemy types. For the duration of the spell,
you treat the target as if it were that type of favored enemy for all purposes.
