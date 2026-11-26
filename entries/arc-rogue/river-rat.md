+++
id = "ref/arc-rogue/river-rat"
kind = "archetype"
title = "River Rat"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20River%20Rat"
source_ids = ["ultimate-wilderness", "people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "river_rat", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "76"
[[sources]]
publication = "people-of-the-river"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "swamper", level = 1 },
  { anchor = "rat-s-resilience" },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["swamper"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["rat-s-resilience"] },
  { alters = "Class skills" },
]
+++

What highway robbers are to roads, river rats are to waterways. Skilled at hiding amid reeds and
roots, these rogues strike the unwary from the shallows as others would from the shadows.

Despite their strong association with banditry, river rats make excellent guides and hunters.

## Class Skills {#class-skills}

A river rat gains Knowledge (nature) as a class skill instead of Knowledge (dungeoneering).

This alters the rogue's class skills.

## Swamper (Ex) {#swamper}

At 1st level, a river rat gains a bonus equal to half her rogue level on Swim checks (minimum +1).

A river rat ignores [difficult terrain](ref/rule/terrain-and-obstacles) caused by light undergrowth
and shallow bogs, and it costs her only 2 squares of movement to enter a square of
[deep bog](ref/rule/marsh-terrain) or [heavy undergrowth](ref/rule/forest-terrain), rather than 4
squares of movement.

She takes no penalty on Acrobatics or Stealth checks for being in bogs and undergrowth. All of these
abilities apply only when she is wearing light or no armor and carrying no more than a light load.

This replaces trapfinding.

## Rat's Resilience (Ex) {#rat-s-resilience}

A river rat is inured to dangers presented by disease-carrying parasites, poisonous fish, and other
toxic river denizens. At 3rd level, a river rat gains a +1 bonus on saving throws against disease
and poison effects. This bonus increases by 1 every 3 levels thereafter, to a maximum bonus of +6 at
18th level.

This replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the river rat archetype: camouflage, hold breath, rogue
crawl, stand up, strong stroke, survivalist.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the river rat archetype: hide in plain sight,
opportunist, skill mastery, stealthy sniper.
