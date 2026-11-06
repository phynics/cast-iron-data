+++
id = "ref/spell/track-ship"
kind = "spell"
title = "Track Ship"
source_ids = ["pirates-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "track_ship", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (piece of ship)"
range = "see text"
effects = [
  { label = "Effect", value = "magical icon" },
]
duration = "1 hour/level"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Arcanist, Bard, Cleric, Oracle, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, F (piece of ship)
Range: see text
Duration: 1 hour/level
Saving throw: Will negates (object)
Spell resistance: yes (object)
Effect: magical icon
Subschool: Scrying
:::

**Sources:** Pirates of the Inner Sea pg 29

In order to cast this spell, you must have a piece of the ship you wish to track. Merchants often
preserve slivers from their trade ships specifically for this purpose. You also need a nautical
chart.

When you cast this spell, an icon of the targeted ship appears on the nautical chart. The icon moves
as the ship moves for the duration of this spell. If the ship is not within the area delineated by
the chart, the spell fails. If the ship is reduced to 0 or fewer hit points, its icon changes from a
ship to a skull and crossbones.
