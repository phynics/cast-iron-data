+++
id = "ref/feat/guild-emissary"
kind = "feat"
title = "Guild Emissary"
aon = "FeatDisplay.aspx?ItemName=Guild%20Emissary"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guild_emissary", path = "json/feat08.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/leadership", label = "or" },
  { kind = "prerequisite", target = "ref/feat/underworld-connections", label = "or" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "29"

[fields]
kind = "feat"
prerequisites = "Leadership or Underworld Connections (see below)."
prerequisite_feats = ["ref/feat/leadership", "ref/feat/underworld-connections"]
benefit = "You can attempt a special character level check (1d20 + your Charisma modifier + your character level) in place of a Diplomacy check when attempting to gather information. You can ask local contacts to find information for you. While this still takes the normal amount of time (typically 1d4 hours), you can gather information about multiple topics at once (up to a maximum number of topics equal to 3 + your Charisma bonus)."
+++

Not only are you associated with a powerful thieves' guild or similar shadowy group, you are
well-enough connected to gain benefits when dealing with the underworld in any settlement.\
**Prerequisites:** [Leadership](ref/feat/leadership) or
[Underworld Connections](ref/feat/underworld-connections) (see below).\
**Benefit:** You can attempt a special character level check (1d20 + your Charisma modifier + your
character level) in place of a [Diplomacy](ref/skill/diplomacy) check when attempting to gather
information. You can ask local contacts to find information for you. While this still takes the
normal amount of time (typically 1d4 hours), you can gather information about multiple topics at
once (up to a maximum number of topics equal to 3 + your Charisma bonus).

Additionally, when you are in a [settlement](ref/rule/the-settlement-stat-block) no smaller than a
small city and are seeking a magic item with a value equal to or less than the city's base value and
the item is not available, you can check again after 1 day (rather than 1 week).

If using the [contact rules](ref/rule/contacts) you gain a single reliable contact each time you
enter a settlement no smaller than a small city. This contact is randomly determined to be a fence,
gossip, manipulator, merchant, petty criminal, snitch, or thug. The contact operates only within
that city, and if the contact's [Trust score](ref/rule/trust) goes down, it immediately drops to 1.
