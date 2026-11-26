+++
id = "ref/arc-inquisitor/sworn-of-the-eldest"
kind = "archetype"
title = "Sworn of the Eldest"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Sworn%20of%20the%20Eldest"
source_ids = ["wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sworn_of_the_eldest", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "wilderness-origins"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "whimsical-worship" },
  { anchor = "deity" },
  { anchor = "disarming-discernment", level = 1 },
  { anchor = "feytongue", level = 1 },
  { anchor = "feywatcher" },
  { anchor = "magic-of-the-eldest", level = 3 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["disarming-discernment"] },
  { replaces = "Stern gaze", feature = "stern-gaze", by = ["feytongue"] },
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["feywatcher"] },
  { replaces = "All teamwork feats", feature = "teamwork-feat", by = ["magic-of-the-eldest"] },
  { alters = "Domain", feature = "domain", by = ["deity"] },
]
+++

Sworn of the Eldest are gathlains who have pledged their loyalty to one of
[Eldest of the First World](ref/rule/the-eldest). Although the Eldest rarely have adherents as other
deities do, they still occasionally require mortal agents to advance their aims. Sworn of the Eldest
consider their chosen Eldest to be akin to powerful patrons or fey royalty and serve them
faithfully.

## Whimsical Worship (Ex) {#whimsical-worship}

A sworn of the Eldest uses her Charisma modifier, rather than her Wisdom modifier, to determine all
class features and effects relating to her inquisitor class, including her spells, cunning
initiative, and true judgment abilities.

## Deity {#deity}

A sworn of the Eldest must select one of the Eldest (_Ultimate Wilderness_ 130) as a deity and must
select a domain or subdomain of that Eldest for her domain ability; she cannot be devoted to an
ideal or philosophy.

This alters domain.

## Disarming Discernment (Ex) {#disarming-discernment}

A sworn of the Eldest adds her Charisma modifier on Sense Motive skill checks, in addition to her
Wisdom modifier.

This replaces monster lore.

## Feytongue (Ex) {#feytongue}

A sworn of the Eldest receives a morale bonus equal to half her inquisitor level (minimum +1) on
Bluff and Diplomacy checks.

This replaces stern gaze.

## Feywatcher (Ex) {#feywatcher}

Resistant to the tricky ways of other fey, a sworn of the Eldest gains the
[resist nature's lure](ref/ability/resist-natures-lure) druid class feature.

This replaces solo tactics.

## Magic of the Eldest {#magic-of-the-eldest}

At 3rd level and every 3 levels thereafter, a sworn of the Eldest gains a bonus spell slot of the
highest spell level she can cast, and she learns the corresponding spell listed for her domain as a
bonus spell known. She can use this bonus spell slot only to cast the domain spell of that level.

This replaces all teamwork feats.
