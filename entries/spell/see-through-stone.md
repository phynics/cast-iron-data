+++
id = "ref/spell/see-through-stone"
kind = "spell"
title = "See Through Stone"
aon = "SpellDisplay.aspx?ItemName=See%20Through%20Stone"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "see_through_stone", path = "json/spells15.json" },
]
[[sources]]
publication = "dwarves-of-golarion"
page = "25"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "concentration, up to 1 round/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Hunter, Ranger\
4: Druid
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: concentration, up to 1 round/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You gain the ability to see through solid rock as if it were transparent glass. You may see through
1 foot of stone per caster level. You see within the stone as if you were looking at the area in
normal light, even if there is no illumination, though [low-light vision](ref/rule/low-light-vision)
and [darkvision](ref/rule/darkvision) have no effect on your ability to see through stone. Metal at
least 1 inch thick or wood or dirt at least 3 feet thick blocks your vision.

The spell does not negate [concealment](ref/rule/concealment) for those creatures hiding behind
stone objects (the stone is still an obstacle to your attacks).
