+++
id = "ref/feat/psychic-maestro"
kind = "feat"
title = "Psychic Maestro"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychic_maestro", path = "json/feat12.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/psychic-sensitivity", label = "or" },
]
[[sources]]
publication = "occult-adventures"
page = "138"

[fields]
kind = "feat"
prerequisites = "Psychic Sensitivity or the ability to cast psychic spells."
prerequisite_feats = ["ref/feat/psychic-sensitivity"]
benefit = "Choose two occult skill unlocks. You can use each of those one additional time per day (or per week, in the case of automatic writing). You must have at least 1 rank in the skills associated with the chosen occult skill unlocks."
+++

You can use two occult skill unlocks more often.\
**Prerequisites:** [Psychic Sensitivity](ref/feat/psychic-sensitivity) or the ability to cast
psychic spells.\
**Benefit:** Choose two [occult skill unlocks](ref/rule/occult-skill-unlocks). You can use each of
those one additional time per day (or per week, in the case of automatic writing). You must have at
least 1 rank in the skills associated with the chosen occult skill unlocks.
