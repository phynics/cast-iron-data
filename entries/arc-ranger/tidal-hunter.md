+++
id = "ref/arc-ranger/tidal-hunter"
kind = "archetype"
title = "Tidal Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Tidal%20Hunter"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tidal_hunter", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "73"

[fields]
kind = "archetype"
features = [
  { anchor = "waterborn", level = 1 },
  { anchor = "keen-scent", level = 1 },
  { anchor = "aquatic-mastery", level = 3 },
  { anchor = "wave-rush", level = 7 },
  { anchor = "tidal-surge", level = 16 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["waterborn"] },
  { replaces = "6th-level combat style feat", feature = "combat-style-feat", levels = [6], by = ["waterborn"] },
  { replaces = "Track", feature = "track", by = ["keen-scent"] },
  { replaces = "camouflage", feature = "camouflage", by = ["keen-scent"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["wave-rush"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["tidal-surge"] },
  { alters = "Favored terrain", feature = "favored-terrain", by = ["aquatic-mastery"] },
]
+++

The tidal hunter draws strength from the fish and other wildlife of the deep.

## Waterborn (Su) {#waterborn}

A tidal hunter can breathe water for up to 10 minutes per ranger level each day. At 6th level, he
can breathe underwater indefinitely.

This replaces wild empathy and the 6th-level combat style feat.

## Keen Scent (Ex) {#keen-scent}

A tidal hunter gains [scent](ref/umr/scent), as per the universal monster rule. At 12th level, while
in water, the tidal hunter can detect particularly strong or distinct odors (such as blood) up to 1
mile away.

This replaces track and camouflage.

## Aquatic Mastery (Ex) {#aquatic-mastery}

At 3rd level, a tidal hunter must select water as his favored terrain, and he doesn't gain
additional favored terrains. At 8th level and every 5 levels thereafter, the bonus from this favored
terrain increases by 2.

This alters favored terrain.

## Wave Rush (Ex) {#wave-rush}

At 7th level, a tidal hunter gains a swim speed equal to his base speed. If he already has a swim
speed, it increases by 10 feet.

This replaces woodland stride.

## Tidal Surge (Sp) {#tidal-surge}

At 16th level, a tidal hunter gains control over water, and he can use the tides to attack his foes.
Once per day, he can cast _[tidal surge](ref/spell/tidal-surge)_ (see page 237) as a
[spell-like ability](ref/umr/spell-like-abilities).

This replaces improved evasion.
