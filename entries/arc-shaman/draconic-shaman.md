+++
id = "ref/arc-shaman/draconic-shaman"
kind = "archetype"
title = "Draconic Shaman"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Draconic%20Shaman"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "draconic_shaman", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "24"

[fields]
kind = "archetype"
replaces = ["Spirit", "spirit animal", "hexes gained at 4th and 10th levels"]
alters = ["Spirit magic"]
replaces_features = ["spirit", "spirit-animal"]
alters_features = ["spirit-magic"]
+++

In some regions of Tian Xia, shamans are unusually common, and may have strong ties to dragon gods
and imperial dragons who act as mentors. Some of these shamans draw their powers from the might of
dragons, rather than from spirits. These shamans each gain a powerful drake as an ally, and view
caring for that drake as a sacred duty.

**Drake Companion**

**Alters:** Spirit magic

**Info:** A draconic shaman gains a [drake companion](ref/sidekick/drake) instead of a spirit
animal, and she communes with the drake to prepare her spells just as other shamans commune with
their spirit animals. She doesn't gain a primary spirit, but she still gains _wandering spirit_ at
4th level. She must select all her hexes (other than her wandering hexes) from the list of shaman
hexes, and she can't select the _witch hex_ shaman hex. She doesn't gain _spirit magic_ slots until
4th level when she gains her _wandering spirit._ Any ability granted by a _wandering spirit_ that
would normally affect a spirit animal (such as [nature's](ref/shamanspirit/nature) _true spirit
ability_) has no effect for a draconic shaman.

**Replaces:** Spirit, spirit animal, hexes gained at 4th and 10th levels
