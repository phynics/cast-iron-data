+++
id = "ref/arc-shifter/wild-effigy"
kind = "archetype"
title = "Wild Effigy"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Wild%20Effigy"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_effigy", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "construct-handbook"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "armor-plating", level = 1 },
  { anchor = "heart-of-earth", level = 4 },
  { anchor = "stoneclaw-strike", level = 6 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["armor-plating"] },
  { replaces = "track", feature = "track", by = ["armor-plating"] },
  { replaces = "woodland stride", feature = "woodland-stride", by = ["armor-plating"] },
  { replaces = "trackless step", feature = "trackless-step", by = ["armor-plating"] },
  { replaces = "Defensive instinct", feature = "defensive-instinct", by = ["heart-of-earth"] },
]
+++

A wild effigy still takes on the shapes of natural animals, but rather than transforming her body
into flesh and muscle, she transforms into constructed effigies of her chosen aspects.

## Armor Plating (Su) {#armor-plating}

A wild effigy's animal aspects are made out of carved, living rock. When a wild effigy is shifted
into one of her minor or major aspects, she gains a +1 enhancement bonus to natural armor and gains
DR adamantine equal to half her shifter level (minimum 1). The enhancement increases by 1 at 4th
level and every 4 levels thereafter, to a maximum of +6 at 20th level. At 6th level, these bonuses
also apply when the wild effigy is transformed into one of her aspects using wild shape.

This replaces wild empathy, track, woodland stride, and trackless step.

## Heart of Earth (Su) {#heart-of-earth}

At 4th level, a wild effigy's stone aspects no longer require even the semblance of flesh and blood
to function. When a wild effigy is shifted into a minor or major aspect, or is transformed into one
of her aspects using wild shape, she adds her shifter level on checks to stabilize at negative hit
points and gains a 25% chance to ignore a critical hit or precision damage. This does not stack with
the _fortification_ armor property or similar effects.

At 9th level, this chance increases to 50% and she becomes immune to petrification.

At 15th level, this chance increases to 75% and she becomes immune to [bleed](ref/umr/bleed) and
[blood drain](ref/umr/blood-drain) effects.

This replaces defensive instinct.

## Stoneclaw Strike (Su) {#stoneclaw-strike}

At 6th level, a wild effigy can sacrifice minutes from her aspects' minor forms to turn her claws
into adamantine. By expending a 1-minute increment of her shifter's minor aspect ability as a swift
action, she can grant her shifter's claws the ability to ignore an amount of DR or
[hardness](ref/umr/hardness) equal to her shifter level for 1 minute. The wild effigy can use this
ability 3 times per day.
