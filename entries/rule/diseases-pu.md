+++
id = "ref/rule/diseases-pu"
kind = "rule"
title = "Diseases"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "diseases_pu", path = "json/rules_adv_gm01.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "138"

[fields]
kind = "none"
+++

The disease track simulates the progression of a disease, starting with incubation. Ignore any onset
entry for a disease; the victim attempts saving throws at a rate based on the disease's frequency.
At the GM's discretion, if the disease's Cure entry does not allow a cure, the disease's progression
may be irreversible without the use of a [heal](ref/spell/heal) spell, and even a successful
[remove disease](ref/spell/remove-disease) only prevents further deterioration. There are two
different tracks: one for diseases that affect physical ability scores (such as bubonic plague or
slimy doom) and one for those that affect mental ability scores (such as cackle, fever or mindfire).
