+++
id = "ref/arc-druid/mooncaller"
kind = "archetype"
title = "Mooncaller"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Mooncaller"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mooncaller", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-magic"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "night-sight", level = 2 },
  { anchor = "resist-call-of-the-wild", level = 4 },
  { anchor = "purity-of-body", level = 9 },
  { anchor = "wolfsbane", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["night-sight"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-call-of-the-wild"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["purity-of-body"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["wolfsbane"] },
]
+++

A mooncaller is bound to the subtle influences of the ever-changing moon and its endless cycles from
light to dark and back again.

## Night Sight (Ex) {#night-sight}

At 2nd level, a mooncaller gains [low-light vision](ref/rule/low-light-vision). If she already has
low-light vision, she gains [darkvision](ref/rule/darkvision) with a range of 30 feet. If she
already has darkvision, the range of her darkvision is increased by 30 feet. This ability replaces
woodland stride.

## Resist Call of the Wild (Ex) {#resist-call-of-the-wild}

At 4th level, a mooncaller gains a +4 bonus on saving throws to avoid confusion, daze, feeblemind,
and insanity effects. She also gains a +4 bonus against the exceptional, spell-like, and
supernatural abilities of creatures with the shapechanger subtype. This ability replaces resist
nature's lure.

## Purity of Body (Ex) {#purity-of-body}

At 9th level, a mooncaller gains immunity to all diseases, including supernatural and magical
diseases. This ability replaces venom immunity.

## Wolfsbane (Su) {#wolfsbane}

At 13th level, a mooncaller gains DR 3/ silver, increasing to DR 4/silver at 16th level and DR
5/silver at 19th level. This ability replaces a thousand faces.
