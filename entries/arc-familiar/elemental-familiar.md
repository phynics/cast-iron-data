+++
id = "ref/arc-familiar/elemental-familiar"
kind = "archetype"
title = "Elemental Familiar"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_familiar", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "plane-hoppers-handbook"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "elemental-type" },
  { anchor = "elemental-manifestation" },
  { anchor = "elemental-speech" },
]
trades = [
  { replaces = "Improved evasion", by = ["elemental-manifestation"] },
  { replaces = "Speak with animals of its kind", by = ["elemental-speech"] },
]
+++

The raw power of an elemental plane suffuses the body of an elemental familiar.

## Planar Companion Archetypes {#planar-companion-archetypes}

Rare creatures are born with a spark of elemental power. When selecting either of the archetypes
below, choose one of the following elements that define which abilities the archetype grants: air,
earth, fire, or water.

## Elemental Type (Ex) {#elemental-type}

An elemental familiar gains a subtype that matches its element: air, earth, fire, or water.

## Elemental Manifestation (Ex) {#elemental-manifestation}

An elemental familiar gains one or more special abilities based on its element. An air familiar
gains a fly speed of 20 feet (good maneuverability); an air familiar that already has a fly speed
instead improves its maneuverability by one category or increases its fly speed by 10 feet. An air
familiar is considered three size categories larger than its actual size when calculating whether it
can be moved by wind. An earth familiar increases the natural armor bonus it gains from its master's
class level by 50% (minimum +1). A fire familiar can spit a globule of fire as a ranged touch attack
once every 1d4 rounds; this attack has a range of 30 feet and deals 1d4 fire damage for every 3
character levels the master has. A water familiar can breathe underwater and gains a swim speed of
20 feet; a water familiar that already has a swim speed instead increases its swim speed by 10 feet.
A water familiar also gains a bonus to its CMD when resisting bull rush, drag, reposition, and trip
combat maneuvers; this bonus is equal to the natural armor adjustment gained from its master's
level.

This replaces improved evasion.

## Elemental Speech (Ex) {#elemental-speech}

An elemental familiar gains the ability to speak and understand a language based on its element:
Aquan (water), Auran (air), Ignan (fire), or Terran (earth).

This ability replaces speak with animals of its kind.
