+++
id = "ref/arc-witch/seducer"
kind = "archetype"
title = "Seducer"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Seducer"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "seducer", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "patron" },
  { anchor = "otherworldly-allure" },
  { anchor = "fey-charm", level = 1 },
  { anchor = "seducer-s-kiss", level = 6 },
  { anchor = "garden-of-delight", level = 8 },
]
trades = [
  { replaces = "Hex gained at 6th level", feature = "hex", levels = [6], by = ["seducer-s-kiss"] },
  { replaces = "Hex gained at 8th level", feature = "hex", levels = [8], by = ["garden-of-delight"] },
  { alters = "Hex gained at 1st level", feature = "hex", levels = [1], by = ["fey-charm"] },
]
+++

These charismatic witches, often devotees of the Green Mother, rely on their otherworldly charms to
achieve their aims. A seducer focuses on enchantments, turning enemies into friends and friends into
toys for her amusement.

## Patron {#patron}

A seducer must select [deception](ref/patron/deception), [enchantment](ref/patron/enchantment),
[plant](ref/patron/plant), [thorns](ref/patron/thorns), or [trickery](ref/patron/trickery) as her
patron.

## Otherworldly Allure {#otherworldly-allure}

A seducer's power comes from her allure. She uses her Charisma rather than her Intelligence score
for the purpose of all class features and effects related to her witch class, such as
[bonus spells](ref/rule/determine-bonuses) per day, the maximum spell level she can cast, and save
DCs of her spells and hexes.

## Fey Charm (Su) {#fey-charm}

A seducer gains the [charm](ref/hex/charm) hex at 1st level. The save DC of this hex is increased
by 1. If the target is (or could be) sexually attracted to the seducer, the save DC is instead
increased by 2. If she and the target have had willing sexual relations in the past 24 hours, the
save DC is instead increased by 3.

This ability alters the hex gained at 1st level.

## Seducer's Kiss (Su) {#seducer-s-kiss}

At 6th level, a seducer can kiss another creature as a melee touch attack. The target must succeed
at a Will save (DC 10 + half the seducer's level + her Charisma modifier) or be
[staggered](ref/misc/staggered) for 1 round. If the target is (or could be) sexually attracted to
the seducer, the save DC is increased by 2. If the seducer and the target have had willing sexual
relations in the past 24 hours, the save DC is instead increased by 4. Whether or not the creature
succeeds at this save, it cannot be the target of this ability again for 1 day. At 10th level, this
ability causes the target to become [stunned](ref/misc/stunned) for 1 round, then staggered for an
additional round. This is a mind-affecting charm effect.

This ability replaces the hex gained at 6th level.

## Garden of Delight (Su) {#garden-of-delight}

At 8th level, the seducer can create a magical bower once per day. This functions as
_[tiny hut](ref/spell/tiny-hut)_ with a caster level equal to the seducer's witch level, but the
interior is a lush garden. Those who rest for 8 hours within the garden heal at twice the usual
rate. In addition, any creature engaging in willing sexual relations with the seducer in this garden
gains a +2 morale bonus on saving throws for the next 24 hours. This bonus does not apply on saving
throws against the seducer's spells or abilities.

This replaces the hex gained at 8th level.
