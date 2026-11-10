+++
id = "ref/spell/wandering-trail"
kind = "spell"
title = "Wandering Trail"
aon = "SpellDisplay.aspx?ItemName=Wandering%20Trail"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wandering_trail", path = "json/spells11.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "63"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "1 mile/level"
effects = [
  { label = "Target", value = "up to one creature/level within 180 feet" },
]
duration = "1 day/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Druid, Hunter
Casting time: 1 standard action
Components: V, S
Range: 1 mile/level
Duration: 1 day/level (D)
Saving throw: none
Spell resistance: no
Target: up to one creature/level within 180 feet
:::

You cause the trail left by the targets within range to automatically reroute, potentially taking
any course within the area. Your modification of the trail within the spell's area can result in a
trail at least half the original length or up to twice the original length. If the trail continues
beyond the spell's range, you must leave it connecting at that point on the edge of the spell's
range. If a tracking creature exceeds the DC of the skill check to follow the trail by an amount
equal to your caster level, the tracker recognizes that the trail has been manipulated by this
spell, although it cannot see the trail's true nature unless it uses magical means, such as true
seeing.
