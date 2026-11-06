+++
id = "ref/spell/substitute-trail"
kind = "spell"
title = "Substitute Trail"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "substitute_trail", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Ranger", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "unlimited"
effects = [
  { label = "Target", value = "1 creature/level; see text" },
]
duration = "1 day/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Druid, Hunter, Ranger
Casting time: 1 standard action
Components: V, S
Range: unlimited
Duration: 1 day/level (D)
Saving throw: none
Spell resistance: no
Target: 1 creature/level; see text
:::

**Sources:** Inner Sea Intrigue pg 62

This spell can affect any creatures with which you interacted in the last 24 hours. You alter the
trails left by the chosen creatures, making it appear that another creature with which you are
familiar left the trail instead (you must have met the creature with which you are familiar). If a
tracker exceeds the DC of the skill check to follow the trail by an amount equal to your caster
level, the tracker recognizes that the trail has been manipulated by this spell, although it cannot
see the trail's true nature unless it uses magical means, such as true seeing.
