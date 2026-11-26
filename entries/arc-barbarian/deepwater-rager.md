+++
id = "ref/arc-barbarian/deepwater-rager"
kind = "archetype"
title = "Deepwater Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Deepwater%20Rager"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deepwater_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "28"

[fields]
kind = "archetype"
features = [
  { anchor = "strong-lungs", level = 1 },
  { anchor = "spiraling-charge", level = 2 },
  { anchor = "disorienting-grapple", level = 5 },
  { anchor = "crushing-grapple", level = 14 },
  { anchor = "full-lungs", level = 17 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["strong-lungs"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["spiraling-charge"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["disorienting-grapple"] },
  { replaces = "Indomitable will", feature = "indomitable-will", by = ["crushing-grapple"] },
  { replaces = "Tireless rage", feature = "tireless-rage", by = ["full-lungs"] },
]
+++

Deepwater ragers bellow ferociously as they charge their enemies, tackling them into the raging
seas. This archetype is compatible with both barbarians and unchained barbarians (_Pathfinder RPG
Pathfinder Unchained_).

## Strong Lungs (Ex) {#strong-lungs}

A deepwater rager can [hold her breath](ref/misc/hold-your-breath) for a number of rounds equal to
four times her Constitution score, and she does not reduce the duration of her held breath by taking
a standard action or a full-round action. Additionally, as long as she is able to speak, the
deepwater rager adds her Constitution modifier to Intimidate skill checks in addition to her
Charisma modifier.

This ability replaces fast movement.

## Spiraling Charge (Ex) {#spiraling-charge}

At 2nd level, a deepwater rager is not required to move in a straight line when she charges,
provided that no space she moves into while charging is farther away from her target than the space
that she is leaving. The deepwater rager must be able to see her target at the beginning of her
charge and cannot use this ability while mounted.

This ability replaces uncanny dodge.

## Disorienting Grapple (Ex) {#disorienting-grapple}

At 5th level, a deepwater rager becomes an expert in flipping and spinning opponents as they are
[grappled](ref/rule/grapple). An opponent grappled by the deepwater rager gains the
[sickened](ref/misc/sickened) condition for as long as it has the grappled condition. When the
creature's grappled condition ends, for any reason, it must succeed at an Acrobatics check (with a
DC equal to the deepwater rager's CMD) or fall [prone](ref/rule/prone).

This ability replaces improved uncanny dodge.

## Crushing Grapple (Ex) {#crushing-grapple}

At 14th level, a deepwater rager gains the [constrict](ref/umr/constrict) special attack, which
deals an amount of damage equal to the damage her unarmed strike deals.

This ability replaces indomitable will.

## Full Lungs (Ex) {#full-lungs}

At 17th level, a deepwater rager does not need to breathe while she is raging.

This ability replaces tireless rage.

## Rage Powers {#rage-powers}

The following rage powers complement the deepwater rager archetype:
[battle roar](ref/ragepower/battle-roar), [bestial swimmer](ref/ragepower/bestial-swimmer),
[brawler](ref/ragepower/brawler), [intimidating glare](ref/ragepower/intimidating-glare),
[raging swimmer](ref/ragepower/raging-swimmer), [rolling dodge](ref/ragepower/rolling-dodge), and
[terrifying howl](ref/ragepower/terrifying-howl).
