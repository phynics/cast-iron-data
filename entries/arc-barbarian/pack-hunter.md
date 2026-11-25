+++
id = "ref/arc-barbarian/pack-hunter"
kind = "archetype"
title = "Pack Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Pack%20Hunter"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pack_hunter", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "in-and-out", level = 3 },
  { anchor = "sympathetic-rage", level = 6 },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["in-and-out"] },
  { replaces = "Rage power normally gained at 6th level", feature = "rage-powers", levels = [6], by = ["sympathetic-rage"] },
  { alters = "Rage power", feature = "rage-powers" },
]
+++

Pack hunter barbarians team up to hunt dangerous prey to feed, to protect their camps, and as a rite
of passage. Often, a tribe of pack hunters looks to a specific species of animal (such as wolves)
who themselves hunt in packs, and view these animals as sacred manifestations of their people's
traditions and values.

## Bonus Feats {#bonus-feats}

Whenever a pack hunter would gain a new rage power, she can instead select a teamwork feat. She must
still meet the prerequisites for the teamwork feat.

This alters rage power.

## In and Out (Ex) {#in-and-out}

At 3rd level, a pack hunter gains a +1 dodge bonus to AC against attacks of opportunity. This bonus
increases by 1 for every 3 barbarian levels after 3rd (to a maximum bonus of +6 at 18th level).

This replaces trap sense.

## Sympathetic Rage (Ex) {#sympathetic-rage}

At 6th level, if an ally within 30 feet is bloodraging or raging, a pack hunter counts as raging
even if knocked unconscious. She has to have been raging when incapacitated to maintain her rage,
and she ceases raging normally if she depletes her maximum number of rounds of rage in a day.

This replaces the rage power normally gained at 6th level.

## Rage Powers {#rage-powers}

The following rage powers complement the pack hunter archetype:
[contagious rage](ref/ragepower/contagious-rage),
[increased damage reduction](ref/ragepower/increased-damage-reduction),
[no escape](ref/ragepower/no-escape), [pack rage](ref/ragepower/pack-rage),
[quick reflexes](ref/ragepower/quick-reflexes), and
[unexpected strike](ref/ragepower/unexpected-strike).
