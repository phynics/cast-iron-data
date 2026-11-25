+++
id = "ref/arc-oracle/dual-cursed-oracle"
kind = "archetype"
title = "Dual-Cursed Oracle"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Dual-Cursed%20Oracle"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dual_cursed_oracle", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "ultimate-magic"
page = "58"

[fields]
kind = "archetype"
features = [
  { anchor = "oracle-s-curse" },
  { anchor = "revelations" },
  { anchor = "misfortune", level = 1 },
  { anchor = "fortune", level = 5 },
]
trades = [
  { replaces = "Mystery bonus spells at these levels", feature = "mystery", levels = [2, 4, 6], power = "bonus spells" },
  { alters = "Oracle's curse", feature = "oracle-s-curse", by = ["oracle-s-curse"] },
]
+++

All oracles are cursed to some degree, but some oracles bear an even heavier burden. Though doubly
afflicted with supernatural or physical hindrances, a dual-cursed oracle can manipulate fortune and
gains greater insights into her mystery.

## Recommended Mysteries {#recommended-mysteries}

Any.

## Oracle's Curse {#oracle-s-curse}

A dual-cursed oracle must choose two curses at 1st level. One of these curses (oracle's choice)
never changes its abilities as the oracle gains levels; for example, an oracle with
[clouded vision](ref/oraclecurse/clouded-vision) never gains [darkvision](ref/rule/darkvision) 60
feet, [blindsense](ref/rule/blindsight-and-blindsense), or blindsight. The other curse comes with
its normal benefits.

## Class Skills {#class-skills}

A dual-cursed oracle gains no additional class skills from her mystery.

## Bonus Spells {#bonus-spells}

_ill omen_ (2nd), _oracle's burden_ (4th), _bestow curse_ (6th). These bonus spells replace the
oracle's mystery bonus spells at these levels.

## Revelations {#revelations}

A dual-cursed oracle gains a new revelation at 5th level and 13th level. These are in addition to
the normal revelations she receives at 3rd level, 7th level, and so on. In addition, the cursed
oracle may select the following revelations in place of a mystery revelation.

## Misfortune (Ex) {#misfortune}

At 1st level, as an immediate action, you can force a creature within 30 feet to reroll any one d20
roll that it has just made before the results of the roll are revealed. The creature must take the
result of the reroll, even if it's worse than the original roll. Once a creature has suffered from
your misfortune, it cannot be the target of this revelation again for 1 day.

## Fortune (Ex) {#fortune}

At 5th level, as an immediate action, you can reroll any one d20 roll that you have just made before
the results of the roll are revealed. You must take the result of the reroll, even if it's worse
than the original roll. You can use this ability once per day at 5th level, and one additional time
per day for every six oracle level beyond 5th.
