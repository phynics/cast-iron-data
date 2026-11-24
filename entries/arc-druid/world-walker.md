+++
id = "ref/arc-druid/world-walker"
kind = "archetype"
title = "World Walker"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20World%20Walker"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "world_walker", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-combat"
page = "43"

[fields]
kind = "archetype"
features = [
  { anchor = "favored-terrain", level = 3 },
  { anchor = "path-of-trees", level = 9 },
]
trades = [
  { replaces = "Trackless step", feature = "trackless-step", by = ["favored-terrain"] },
  { replaces = "resist nature's lure", feature = "resist-nature-s-lure", by = ["favored-terrain"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["path-of-trees"] },
  { replaces = "timeless body", feature = "timeless-body", by = ["path-of-trees"] },
]
+++

While all druids traverse the wilderness with ease, the world walkers take it upon themselves to
travel the entire world. Some act as messengers and scouts for druidic circles, while others have a
seemingly unquenchable wanderlust; each new land provides new mysteries to discover and new wisdom
to be gained from mastering those mysteries.

## Favored Terrain (Ex) {#favored-terrain}

At 3rd level, the world walker gains the ranger's [favored terrain](ref/ability/favored-terrain)
ability. She treats her druid level as her ranger level for this ability. If she has levels in both
classes, both class's levels stack for determining the effect of this ability. This ability replaces

trackless step and resist nature's lure.

## Path of Trees (Su) {#path-of-trees}

At 9th level, once a day, a wanderer

can step within a tree and then teleport from that tree to

another one in a manner similar to the _[tree stride](ref/spell/tree-stride)_ spell. She gains an

extra use of this ability each

day at 12th level, and a

third use of this ability at

15th level. Furthermore,

a world walker of 13th level or

higher can use this ability to teleport

to any other tree of its type up to 100

miles away. This ability replaces

both venom immunity

and timeless body.
