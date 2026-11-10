+++
id = "ref/feat/cranial-adjustment"
kind = "feat"
title = "Cranial Adjustment"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cranial_adjustment", path = "json/feat03.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/deft-hands", label = "or" },
  { kind = "prerequisite", target = "ref/feat/trepanation", label = "or" },
]
[[sources]]
publication = "occult-origins"
page = "24"

[fields]
kind = "feat"
prerequisites = "Deft Hands or Trepanation."
prerequisite_feats = ["ref/feat/deft-hands", "ref/feat/trepanation"]
benefit = "You can perform the hypnotism occult skill unlock even if you can't use psychic magic. If you can cast psychic spells or have the Psychic Sensitivity feat, you can use hypnotism one additional time per day."
+++

You have learned to manually adjust the plates that make up the skull, inducing altered states in
your subjects.\
**Prerequisites:** [Deft Hands](ref/feat/deft-hands) or [Trepanation](ref/feat/trepanation).\
**Benefit:** You can perform the [hypnotism](ref/skill/diplomacy) occult skill unlock even if you
can't use psychic magic. If you can cast psychic spells or have the
[Psychic Sensitivity](ref/feat/psychic-sensitivity) feat, you can use hypnotism one additional time
per day.

You can use the [Sleight of Hand](ref/skill/sleight-of-hand) skill in place of Diplomacy to
hypnotize a subject, but doing so requires 10 minutes of contact with the target's skull. You can
perform an adjustment that takes 1 hour to access the deeper recesses of a target's emotional mind,
either granting the target a +2 bonus or imposing a -2 penalty on the target's saving throws against
mind-affecting emotion effects for 24 hours.
