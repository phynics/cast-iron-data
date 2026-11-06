+++
id = "ref/spell/mages-crawl-space"
kind = "spell"
title = "Mage's Crawl Space"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mages_crawl_space", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of clay)"
range = "personal"
effects = [
  { label = "Effect", value = "5-foot sphere centered on yourself" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bard, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of clay)
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Effect: 5-foot sphere centered on yourself
:::

**Sources:** Heroes of the Darklands pg 9

When you cast this spell, you merge with an adjacent natural stone surface, forming a 5-foot pocket
within. If the stone surface does not have enough volume to safely contain a 5-foot sphere of empty
space, the spell fails. When created, there is sufficient air within the pocket for up to one Medium
creature to survive for the spell's duration, including one additional Tiny or smaller creature,
such as a familiar. At the end of the spell's duration, you are immediately expelled into the
nearest available open space adjacent to the surface you merged with.
