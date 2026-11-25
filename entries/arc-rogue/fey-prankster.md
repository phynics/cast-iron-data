+++
id = "ref/arc-rogue/fey-prankster"
kind = "archetype"
title = "Fey Prankster"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Fey%20Prankster"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fey_prankster", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "treacherous-plants", level = 1 },
  { anchor = "improved-dirty-trick", level = 2 },
  { anchor = "steal-appearance", level = 4 },
  { anchor = "greater-dirty-trick", level = 6 },
  { anchor = "plant-traps", level = 8 },
  { anchor = "unseen-trickster", level = 12 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["treacherous-plants"] },
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["improved-dirty-trick"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["steal-appearance"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["steal-appearance"] },
  { replaces = "Rogue talent gained at 6th level", feature = "rogue-talents", levels = [6], by = ["greater-dirty-trick"] },
  { replaces = "Rogue talent gained at 8th level", feature = "rogue-talents", levels = [8], by = ["plant-traps"] },
  { replaces = "Rogue talent gained at 12th level", feature = "rogue-talents", levels = [12], by = ["unseen-trickster"] },
]
+++

Fey pranksters specialize in tricking others to teach a lesson or for their own entertainment.

## Treacherous Plants (Sp) {#treacherous-plants}

The fey prankster can cause plants to distract nearby creatures. To use this ability, the fey
prankster attempts a Bluff check to create a distraction to hide as a swift action or to
[feint](ref/rule/feint) against an adjacent opponent as a move action, so long as the target is
adjacent to plants. He gains a bonus on this check equal to half his rogue level (minimum +1).

This replaces trapfinding.

## Improved Dirty Trick {#improved-dirty-trick}

At 2nd level, the fey prankster gains [Improved Dirty Trick](ref/feat/improved-dirty-trick) as a
bonus feat. He need not meet the prerequisites.

This replaces the rogue talent gained at 2nd level.

## Steal Appearance (Sp) {#steal-appearance}

At 4th level, the fey prankster can exchange the appearance of two adjacent items of the same size.
He can also exchange the appearance of two creatures if at least one is willing and both are
adjacent. Affecting an unwilling creature or an item it wears or carries requires a successful
[dirty trick](ref/rule/dirty-trick) combat maneuver against that creature. If he succeeds, the
objects or creatures are each disguised as the other as if with _[veil](ref/spell/veil)_ cast at his
rogue level. The Will save DC to resist or disbelieve the illusion is equal to 10 + half the rogue's
level + his Intelligence modifier.

At 8th level, the fey prankster can also exchange the locations of the two targets by succeeding at
a DC 20 Sleight of Hand check. If he succeeds, observers can't tell which is the original based on
movement without succeeding at a Perception check against his Sleight of Hand result.

This replaces uncanny dodge and improved uncanny dodge.

## Greater Dirty Trick {#greater-dirty-trick}

At 6th level, the fey prankster gains [Greater Dirty Trick](ref/feat/greater-dirty-trick) as a bonus
feat. He does not need to meet the prerequisites.

This replaces the rogue talent gained at 6th level.

## Plant Traps (Su) {#plant-traps}

At 8th level, the fey trickster can modify a plant (but not plant creatures) into a trap as a
full-round action up to three times per day. The Perception and Disable Device DCs for the trap are
each equal to 15 + his rogue level. A Tiny or larger plant can be used to perform a
[trip](ref/rule/trip) or dirty trick combat maneuver using the fey trickster's CMB and the plant's
size. A Large or larger plant can be used to create a _[snare](ref/spell/snare)_ as per the spell.
The save DC is equal to 12 + the rogue's Intelligence modifier. The fey trickster can trigger any
plant trap he created as a standard action as long as he is within 60 feet of it.

This replaces the rogue talent gained at 8th level.

## Unseen Trickster {#unseen-trickster}

At 12th level, the fey trickster can attempt Stealth checks in areas with plants even if he does not
have [cover](ref/rule/cover) or [concealment](ref/rule/concealment).

This replaces the rogue talent gained at 12th level.
