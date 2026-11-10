+++
id = "ref/spell/slick-walls"
kind = "spell"
title = "Slick Walls"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "slick_walls", path = "json/spells9.json" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "31"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (drop of oil)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "30-ft.-radius emanation centered on a point in space" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Bard, Magus, Skald, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (drop of oil)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Area: 30-ft.-radius emanation centered on a point in space
Subschool: Creation
:::

You coat all walls and ceilings within the spell's area with a slick substance. The DC of all Climb
checks for the affected surfaces increases by twice your caster level (maximum +20). Creatures
cannot take 10 on Climb checks while scaling the affected surfaces, even if they have a climb speed
or other ability that would normally allow taking 10. This spell has no effect on magical walls or
surfaces, such as the sides of a hole created with create pit.
