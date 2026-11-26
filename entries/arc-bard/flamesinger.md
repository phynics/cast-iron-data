+++
id = "ref/arc-bard/flamesinger"
kind = "archetype"
title = "Flamesinger"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Flamesinger"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flamesinger", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "fire-music", level = 1 },
  { anchor = "blazing-blades", level = 1 },
  { anchor = "wildfire", level = 2 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["fire-music"] },
  { replaces = "lore master", feature = "lore-master", by = ["fire-music"] },
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["blazing-blades"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["wildfire"] },
]
+++

The flamesinger finds inspiration in the mesmerizing beauty of fire. While the flamesinger's
tradition originated among the varied peoples of the Padishah Empire of Kelesh, it long ago spread
to Qadira and from there throughout the Inner Sea region.

## Fire Music {#fire-music}

A flamesinger gains [Fire Music](ref/feat/fire-music) as a bonus feat at 1st level (without needing
to meet the normal prerequisites). At 4th level (when she gains access to 2nd-level spells), she
adds _[summon monster I](ref/spell/summon-monster-1)_ and
_[summon monster II](ref/spell/summon-monster-2)_ to her bard spells known; every 3 levels
thereafter she gains the next level of _[summon monster](ref/spell/summon-monster)_, until she adds
_[summon monster VI](ref/spell/summon-monster-6)_ to her spells known at 16th level. The flamesinger
must apply the Fire Music feat's effect when casting these spells.

This ability replaces bardic knowledge and lore master.

## Bardic Performance {#bardic-performance}

A flamesinger gains the following bardic performance.

## Blazing Blades (Su) {#blazing-blades}

The flamesinger's song causes allies' weapons to burst into flames. To be affected, an ally must be
able to hear the bard perform and be within 30 feet. An affected creature's successful attacks with
manufactured or natural weapons deal 1d4 additional points of fire damage. These flames do not harm
the weapon or its wielder. This damage stacks with other sources of fire damage, such as the
_[flaming](ref/magic-enh/flaming)_ special weapon ability. At 5th level and every 6 bard levels
thereafter, this bonus fire damage increases by 1d4 (to a maximum of 4d4 at 17th level). This is a
fire effect that relies on audible components.

This ability replaces inspire courage.

## Wildfire (Ex) {#wildfire}

Like a raging wildfire, a flamesinger moves with blistering speed. At 2nd level and every 4 levels
thereafter, the flamesinger gains a +5-foot enhancement bonus to her base speed (to a maximum of +25
feet at 18th level).

This ability replaces versatile performance.
