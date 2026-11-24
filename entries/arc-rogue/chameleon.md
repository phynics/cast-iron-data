+++
id = "ref/arc-rogue/chameleon"
kind = "archetype"
title = "Chameleon"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Chameleon"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chameleon", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-combat"
page = "71"

[fields]
kind = "archetype"
features = [
  { anchor = "misdirection", level = 1 },
  { anchor = "effortless-sneak", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["misdirection"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["effortless-sneak"] },
]
+++

An absolute master of disguise, a chameleon effortlessly blends into any environment. Whether
disappearing into crowded city streets, vanishing into desert sands, or slipping into the darkness
of subterranean tunnels, the chameleon relies upon her ability to become part of her surroundings.

## Misdirection (Ex) {#misdirection}

At 1st level, a chameleon begins her career knowing that the secret to disappearing lies in
deceiving the senses of her observers. Every day she gains a pool of stealth points equal to her
ranks in Bluff. These points refresh at the start of each day. Before making a Stealth check, she
can choose to put stealth points into the roll, gaining a bonus on Stealth checks equal to the
number of stealth points she puts into the roll. If she gains a bonus on Bluff checks because of a
feat (such as [Skill Focus](ref/feat/skill-focus) \[Bluff\]), she adds a number of points to her
stealth pool equal to the bonus the feat grants. This ability replaces trapfinding.

## Effortless Sneak (Sp) {#effortless-sneak}

At 3rd level, the chameleon chooses a single terrain from the ranger's
[favored terrain](ref/ability/favored-terrain) class feature. While she is within that terrain, she
can take 10 on any Stealth check she can make within that terrain. When the chameleon reaches 6th
level, and every three levels thereafter, she chooses a new type of terrain from the ranger's
favored terrain list. She gains this ability with the newly picked terrain. This ability replaces
trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the chameleon archetype: camouflage, fast stealth, quick
disguise, and terrain mastery.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the chameleon archetype: hide in plain sight and
master of disguise.
