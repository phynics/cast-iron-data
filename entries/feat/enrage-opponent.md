+++
id = "ref/feat/enrage-opponent"
kind = "feat"
title = "Enrage Opponent"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enrage_opponent", path = "json/feat05.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-swashbuckler", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat", "Panache"]
prerequisites = "Cha 13, Persuasive, either Amateur Swashbuckler or the panache class feature."
prerequisite_feats = ["ref/feat/amateur-swashbuckler", "ref/feat/persuasive"]
benefit = "As a swift action, you can spend 1 panache point to enrage a creature with an Intelligence of 4 or more within 60 feet that can see or hear you. Attempt an Intimidate check as if to demoralize the creature. If you succeed, the creature takes a -2 penalty to its AC until it has made at least one attack against you (including area effects that include you) or until it can no longer see or hear you. You can have only one opponent enraged at you with this feat at a time, and once you've enraged a creature, you can't enrage it again for 24 hours."
+++

## Enrage Opponent (Combat, Panache)

**Sources:** Ultimate Intrigue pg 82

With a quip or a suggestive gesture, you send your enemy into a tizzy.\
**Prerequisites:** Cha 13, [Persuasive](ref/feat/persuasive), either
[Amateur Swashbuckler](ref/feat/amateur-swashbuckler) or the panache class feature.\
**Benefit:** As a swift action, you can spend 1 panache point to enrage a creature with an
Intelligence of 4 or more within 60 feet that can see or hear you. Attempt an Intimidate check as if
to demoralize the creature. If you succeed, the creature takes a -2 penalty to its AC until it has
made at least one attack against you (including area effects that include you) or until it can no
longer see or hear you. You can have only one opponent enraged at you with this feat at a time, and
once you've enraged a creature, you can't enrage it again for 24 hours.
