+++
id = "ref/spell/determine-depth"
kind = "spell"
title = "Determine Depth"
aon = "SpellDisplay.aspx?ItemName=Determine%20Depth"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "determine_depth", path = "json/spells3.json" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "30"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "solid surface touched" },
]
duration = "concentration, up to 1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Arcanist, Bard, Druid, Hunter, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: concentration, up to 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: solid surface touched
:::

With a touch, you can determine the exact thickness of a wall, ceiling, or other solid barrier,
measuring from the point you are touching to the direct opposite side of the barrier in a straight
line. You can only detect depths or widths of up to 10 feet per caster level (maximum 200 feet at
20th level); amounts in excess of this limit are detected as being the maximum you are able to
detect. So, for example, a 5th-level wizard using this spell on a 60-foot-thick wall would detect
that the wall is 50 feet thick.

Determine depth can be used on earthen, plaster, stone, or wooden surfaces, but not on walls made of
metal or other, harder materials. This spell is useful to casters who want to get an idea of their
surroundings, and as a preliminary measure to casting spells such as passwall or dimension door.
