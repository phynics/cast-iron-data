+++
id = "ref/arc-monk/maneuver-master"
kind = "archetype"
title = "Maneuver Master"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Maneuver%20Master"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "maneuver_master", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-combat"
page = "58"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-feat" },
  { anchor = "flurry-of-maneuvers", level = 1 },
  { anchor = "maneuver-defense", level = 3 },
  { anchor = "reliable-maneuver", level = 4 },
  { anchor = "meditative-maneuver", level = 5 },
  { anchor = "sweeping-maneuver", level = 11 },
  { anchor = "whirlwind-maneuver", level = 15 },
]
trades = [
  { replaces = "Flurry of blows", feature = "flurry-of-blows", by = ["flurry-of-maneuvers"] },
  { replaces = "Still mind", feature = "still-mind", by = ["maneuver-defense"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["reliable-maneuver"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["meditative-maneuver"] },
  { replaces = "Diamond body", feature = "diamond-body", by = ["sweeping-maneuver"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["whirlwind-maneuver"] },
]
+++

The maneuver master specializes in more complicated moves than simple damage-dealing strikes.

## Bonus Feat {#bonus-feat}

In addition to normal monk bonus feats, a maneuver master may select any Improved combat maneuver
feat (such as [Improved Overrun](ref/feat/improved-overrun)) as a bonus feat. At 6th level and
above, he may select any Greater combat maneuver feat (such as
[Greater Grapple](ref/feat/greater-grapple)) as a bonus feat. At 10th level and above, he may select
any maneuver Strike feat (such as [Tripping Strike](ref/feat/tripping-strike)) as a bonus feat.

## Flurry of Maneuvers (Ex) {#flurry-of-maneuvers}

At 1st level, as part of a full-attack action, a maneuver master can make one additional combat
maneuver, regardless of whether the maneuver normally replaces a melee attack or requires a standard
action. The maneuver master uses his monk level in place of his base attack bonus to determine his
CMB for the bonus maneuvers, though all combat maneuver checks suffer a -2 penalty when using a
flurry. At 8th level, a maneuver master may attempt a second additional combat maneuver, with an
additional -3 penalty on combat maneuver checks. A maneuver master loses this ability when wearing
armor, using a shield, or carrying a medium or heavy load. At 15th level, a maneuver master may
attempt a third additional combat maneuver, with an additional -7 penalty on combat maneuver checks.
This ability replaces flurry of blows.

## Maneuver Defense (Ex) {#maneuver-defense}

At 3rd level, if a maneuver master has an Improved combat maneuver feat, any creature attempting
that maneuver against the maneuver master provokes an attack of opportunity, even if it would not
normally do so. This ability replaces still mind.

## Reliable Maneuver (Ex) {#reliable-maneuver}

At 4th level, as a swift action, a maneuver master may spend 1 point from his ki pool before
attempting a combat maneuver. He can roll his combat maneuver check for that maneuver twice and use
the better result. This ability replaces slow fall.

## Meditative Maneuver (Ex) {#meditative-maneuver}

At 5th level, as a swift action, a maneuver master can add his Wisdom modifier on any combat
maneuver check he makes before the beginning of his next turn. He must choose which combat maneuver
check to grant the bonus to before making the combat maneuver check. This ability replaces purity of
body.

## Sweeping Maneuver (Ex) {#sweeping-maneuver}

At 11th level, a maneuver master can make two combat maneuvers as a standard action, as long as
neither maneuver requires the maneuver master to move. He may perform two identical maneuvers
against two adjacent enemies, or he may perform two different combat maneuvers against the same
target. This ability replaces diamond body.

## Whirlwind Maneuver (Ex) {#whirlwind-maneuver}

At 15th level, once per day as a full-round action, a maneuver master can attempt a single combat
maneuver against every opponent he threatens, as long as the combat maneuver does not require
movement. He makes a single combat maneuver check, and it applies to all targets. This ability
replaces quivering palm.
