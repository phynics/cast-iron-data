+++
id = "ref/arc-ranger/groom"
kind = "archetype"
title = "Groom"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Groom"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "groom", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "hide-the-horses", level = 1 },
  { anchor = "horse-whisperer", level = 3 },
  { anchor = "scout-the-area", level = 3 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["hide-the-horses"] },
  { replaces = "Endurance", feature = "endurance", by = ["horse-whisperer"] },
  { replaces = "1st favored terrain", feature = "favored-terrain", levels = [3], by = ["scout-the-area"] },
]
+++

The groom attends to the needs of the party's mounts and beasts of burden during their adventures,
and guards these animals while the party goes underground.

## Hide the Horses (Ex) {#hide-the-horses}

A groom finds the best place to stable and conceal a party's mounts while the group explores a
dungeon. A groom adds half her level (minimum 1) on Stealth skill checks for both herself and the
mounts she's hiding while she is concealing a party's mounts. This ability replaces track.

## Horse Whisperer (Su) {#horse-whisperer}

At 3rd level, a groom can use _[speak with animals](ref/spell/speak-with-animals)_ at will, but can
use this power only on horses, riding dogs, and other mounts of the animal type. This ability
replaces Endurance.

## Scout the Area (Ex) {#scout-the-area}

At 3rd level, a groom gains a +4 bonus on Knowledge (local) checks. In addition, she always knows
where to find the nearest expert or spellcaster who can provide a particular service, such as the
nearest source of _[raise dead](ref/spell/raise-dead)_. This ability replaces the ranger's 1st
favored terrain.
