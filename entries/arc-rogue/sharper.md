+++
id = "ref/arc-rogue/sharper"
kind = "archetype"
title = "Sharper"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Sharper"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sharper", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "scam-artist", level = 1 },
  { anchor = "sticky-fingers", level = 2 },
  { anchor = "lucky-save", level = 3 },
  { anchor = "audacious-overconfidence", level = 4 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["scam-artist"] },
  { replaces = "Rogue talents gained at 2nd, 6th, and 8th levels", feature = "rogue-talents", levels = [2, 6, 8], by = ["sticky-fingers"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["lucky-save"] },
  { replaces = "Rogue talents gained at 4th, 10th, and 16th levels", feature = "rogue-talents", levels = [4, 10, 16], by = ["audacious-overconfidence"] },
]
+++

Sharpers use trickery and deception to part an owner from his valuables. Pathological risk-takers,
they distinguish themselves from con artists and burglars by virtue of the simplicity and boldness
of their schemes, which are usually impromptu, rather than carefully orchestrated. Many sharpers
consider themselves romantic figures and foster the image of a resourceful, dashing rogue living by
wits and luck while subverting authority at every turn.

## Scam Artist (Ex) {#scam-artist}

A sharper gains a bonus equal to half her rogue level (minimum +1) on all Bluff and Sleight of Hand
checks.

This ability replaces trapfinding.

## Sticky Fingers (Ex) {#sticky-fingers}

At 2nd level, a sharper receives [Improved Steal](ref/feat/improved-steal) as a bonus feat. At 6th
level, she receives [Greater Steal](ref/feat/greater-steal) as a bonus feat, and at 8th level, she
receives [Quick Steal](ref/feat/quick-steal) as a bonus feat. The sharper gains these feats even if
she doesn't meet the prerequisites.

This ability replaces the rogue talents gained at 2nd, 6th, and 8th levels.

## Lucky Save (Su) {#lucky-save}

At 3rd level, when a sharper's wits aren't enough to pull her out of a bad situation, her luck still
just might save her. She gains a +1 luck bonus on all saving throws. This bonus increases to +2 at
9th level and to +3 at 15th level.

This ability replaces trap sense.

## Audacious Overconfidence (Ex) {#audacious-overconfidence}

At 4th level, after failing an attack roll, skill check, or saving throw, a sharper can reduce her
saving throw bonus from lucky save by 1 for 24 hours in order to reroll the failed roll. She can use
this ability once per day at 4th level, plus an additional time per day at 10th level and again at
16th level. The decreases to her bonus from lucky save stack with each other.

This ability replaces the rogue talents gained at 4th, 10th, and 16th levels.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the sharper archetype: charmer, convincing lie, deft palm,
false friend, fast fingers, follow along, honeyed words, obfuscate story, shades of gray, and steal
the story (as well as certainty for an unchained rogue).

## Advanced Talents {#advanced-talents}

The following advanced talents complement the sharper archetype: another day, defensive roll, hidden
mind, improved evasion, redirect attack, and skill mastery (as well as cutting edge for an unchained
rogue).
