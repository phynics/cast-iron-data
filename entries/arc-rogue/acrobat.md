+++
id = "ref/arc-rogue/acrobat"
kind = "archetype"
title = "Acrobat"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Acrobat"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "acrobat", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-players-guide"
page = "132"

[fields]
kind = "archetype"
features = [
  { anchor = "expert-acrobat", level = 1 },
  { anchor = "second-chance", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["expert-acrobat"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["second-chance"] },
]
+++

Agility and daring are both excellent rogue traits, and their confluence can create spectacular
feats of acrobatics. Whether they are daring thieves, infiltrating assassins, or intrepid spies,
proper training in acrobatics is a valuable boon for rogues.

## Expert Acrobat (Ex) {#expert-acrobat}

At 1st level, an acrobat does not suffer any armor check penalties on Acrobatics, Climb, Fly,
Sleight of Hand, or Stealth skill checks while wearing light armor. When she is not wearing armor,
she gains a +2 competency bonus on Acrobatics and Fly skill checks. This ability replaces
trapfinding.

## Second Chance (Ex) {#second-chance}

At 3rd level, an acrobat can reroll any Acrobatics, Climb, or Fly skill check she has just made.
This reroll is made at a -5 penalty. She must take the second result, even if it is worse. An
acrobat can use this ability only once on any given skill check. She can use this ability once per
day at 3rd level, plus one additional time per day for every 3 levels beyond 3rd. This ability
replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the acrobat archetype: expert leaper, fast getaway, ledge
walker, nimble climber, peerless maneuver, rogue crawl, and stand up.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the acrobat archetype: defensive roll, fast tumble,
and improved evasion.
