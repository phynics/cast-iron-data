+++
id = "ref/arc-bard/dragon-yapper"
kind = "archetype"
title = "Dragon Yapper"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Dragon%20Yapper"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragon_yapper", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "monster-codex"
page = "128"

[fields]
kind = "archetype"
features = [
  { anchor = "yapping-song", level = 1 },
  { anchor = "frightful-song", level = 8 },
  { anchor = "versatile-performance", level = 2 },
]
trades = [
  { replaces = "Fascinate", feature = "bardic-performance", power = "fascinate", by = ["yapping-song"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["frightful-song"] },
]
+++

Kobolds' yammering songs distract opponents in combat, hindering their ability to attack.

## Bardic Performance {#bardic-performance}

A dragon yapper gains the following types of bardic performance.

## Yapping Song (Su) {#yapping-song}

A dragon yapper can use performance to annoy those that hear it, causing them to take a -1 penalty
on attack and damage rolls (minimum 1) and a -1 penalty on saves against fear effects and charm
effects as long as the dragon yapper continues performing. This penalty increases by 1 at 5th level
and every 6 levels thereafter. Yapping song is a mind-affecting ability that uses audible
components, but is not language-dependent. This performance replaces fascinate.

## Frightful Song (Su) {#frightful-song}

A dragon yapper of 8th level or higher can amplify his voice to sound like an actual dragon. Enemies
within 30 feet become [shaken](ref/misc/shaken) unless they succeed at a Will save (DC 10 +1/2 the
dragon yapper's level + the dragon yapper's Charisma modifier). A successful save renders targets
immune to this ability for 24 hours. Frightful song is a mind-affecting ability, and a fear effect
that uses audible components. This performance replaces dirge of doom.

## Versatile Performance (Ex) {#versatile-performance}

A dragon yapper must choose sing at 2nd level.
