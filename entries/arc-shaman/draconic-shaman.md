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
features = [
  { anchor = "drake-companion", level = 1 },
]
trades = [
  { replaces = "Spirit", feature = "spirit", by = ["drake-companion"] },
  { replaces = "spirit animal", feature = "spirit-animal", by = ["drake-companion"] },
  { replaces = "hexes gained at 4th and 10th levels", feature = "hex", levels = [4, 10], by = ["drake-companion"] },
  { alters = "Spirit magic", feature = "spirit-magic", by = ["drake-companion"] },
]
+++

In some regions of Tian Xia, shamans are unusually common, and may have strong ties to dragon gods
and imperial dragons who act as mentors. Some of these shamans draw their powers from the might of
dragons, rather than from spirits. These shamans each gain a powerful drake as an ally, and view
caring for that drake as a sacred duty.

## Drake Companion {#drake-companion}

A draconic shaman gains a [drake companion](ref/sidekick/drake) instead of a spirit animal, and she
communes with the drake to prepare her spells just as other shamans commune with their spirit
animals. She doesn't gain a primary spirit, but she still gains wandering spirit at 4th level. She
must select all her hexes (other than her wandering hexes) from the list of shaman hexes, and she
can't select the witch hex shaman hex. She doesn't gain spirit magic slots until 4th level when she
gains her wandering spirit. Any ability granted by a wandering spirit that would normally affect a
spirit animal (such as [nature's](ref/shamanspirit/nature) true spirit ability) has no effect for a
draconic shaman.

This ability replaces spirit, spirit animal, and the hexes gained at 4th and 10th levels and alters
spirit magic.
