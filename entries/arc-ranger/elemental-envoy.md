+++
id = "ref/arc-ranger/elemental-envoy"
kind = "archetype"
title = "Elemental Envoy"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Elemental%20Envoy"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_envoy", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "disciples-doctrine"
page = "5"

[fields]
kind = "archetype"
features = [
  { anchor = "planar-combatant", level = 2 },
  { anchor = "elemental-explorer", level = 3 },
]
trades = [
  { alters = "Combat style feats", feature = "combat-style-feat", by = ["planar-combatant"] },
  { alters = "Favored terrain", feature = "favored-terrain", by = ["elemental-explorer"] },
]
+++

An elemental envoy travels the Elemental Planes. He has learned to protect himself from their many
dangers, and he models his fighting style after their teachings.

## Planar Combatant (Ex) {#planar-combatant}

At 2nd level, an elemental envoy must choose the elemental combat style on this page, choosing his
combat style feats from that list.

This alters the ranger's combat style feats.

## Elemental Explorer (Ex) {#elemental-explorer}

At 3rd level, instead of selecting a favored terrain, an elemental envoy gains the typical favored
terrain bonuses when traveling on the Plane of Air, Plane of Earth, Plane of Fire, and Plane of
Water, except the elemental envoy gains a bonus on Knowledge (planes) checks instead of Knowledge
(geography) checks. At 8th level and every 5 levels thereafter, he does not select an additional
favored terrain, but his favored terrain bonuses increase by 2.

This alters favored terrain.
