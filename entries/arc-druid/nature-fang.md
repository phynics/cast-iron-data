+++
id = "ref/arc-druid/nature-fang"
kind = "archetype"
title = "Nature Fang"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Nature%20Fang"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nature_fang", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-class-guide"
page = "92"

[fields]
kind = "archetype"
features = [
  { anchor = "studied-target", level = 1 },
  { anchor = "slayer-talent", level = 4 },
  { anchor = "sneak-attack", level = 4 },
  { anchor = "swift-studied-target", level = 9 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["studied-target"] },
  { replaces = "wild empathy", feature = "wild-empathy", by = ["studied-target"] },
  { replaces = "woodland stride", feature = "woodland-stride", by = ["studied-target"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["slayer-talent"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["sneak-attack"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["swift-studied-target"] },
]
+++

A nature fang is a druid who stalks and slays those who despoil nature, kill scarce animals, or
introduce diseases to unprotected habitats. She gives up a close empathic connection with the
natural world to become its deadly champion and avenger.

## Studied Target (Ex) {#studied-target}

At 1st level, a nature fang gains the [slayer's](ref/class/slayer) studied target class feature. At
5th level and every 5 levels thereafter, the nature fang's bonus against her studied target
increases by 1. Unlike a slayer, a nature fang does not gain the ability to maintain more than one
studied target at the same time. This ability replaces nature sense, wild empathy, and
[woodland stride](ref/slayertalent/woodland-stride).

## Slayer Talent {#slayer-talent}

At 4th level and every 2 levels thereafter, a nature fang selects a slayer talent. Starting at 12th
level, she can select an advanced slayer talent in place of a slayer talent. She uses her druid
level as her slayer level to determine what talents she can select. This ability replaces wild
shape.

## Sneak Attack (Ex) {#sneak-attack}

At 4th level, a nature fang gains [sneak attack](ref/ability/sneak-attack) +1d6. This functions as
the [rogue](ref/class/rogue) sneak attack ability. If the nature fang gets a sneak attack bonus from
another source, the bonuses on damage stack. This ability replaces resist nature's lure.

## Swift Studied Target {#swift-studied-target}

At 9th level, a nature fang can study an opponent as a move or swift action. This ability replaces
venom immunity.

## Slayer Talents {#slayer-talents}

The following slayer talents complement the nature fang archetype:
[foil scrutiny](ref/slayertalent/foil-scrutiny), [poison use](ref/slayertalent/poison-use),
[ranger combat style](ref/slayertalent/ranger-combat-style). Additionally, the following rogue
talents, which are also available to slayers, complement the archetype:
[bleeding attack](ref/talent/bleeding-attack), [camouflage](ref/talent/camouflage),
[fast stealth](ref/talent/fast-stealth), [finesse rogue](ref/talent/finesse-rogue),
[lasting poison](ref/talent/lasting-poison), [rogue crawl](ref/talent/rogue-crawl),
[slow reactions](ref/talent/slow-reactions), [surprise attack](ref/talent/surprise-attack),
[swift poison](ref/talent/swift-poison), [terrain mastery](ref/talent/terrain-mastery).

## Advanced Talents {#advanced-talents}

The following advanced talents complement the nature fang archetype:
[assassinate](ref/slayertalent/assassinate),
[slayer camouflage](ref/slayertalent/slayer-camouflage), woodland stride. The rogue advanced talent
[master of disguise](ref/talent/master-of-disguise) also fits the archetype.
