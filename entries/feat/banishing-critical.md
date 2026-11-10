+++
id = "ref/feat/banishing-critical"
kind = "feat"
title = "Banishing Critical"
source_ids = ["monster-summoners-handbook", "blood-of-angels"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "banishing_critical", path = "json/feat01.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/arcane-strike", label = "or" },
  { kind = "prerequisite", target = "ref/feat/disruptive", label = "or" },
]
[[sources]]
publication = "monster-summoners-handbook"
page = "8"
[[sources]]
publication = "blood-of-angels"
page = "24"

[fields]
kind = "feat"
feat_types = ["Critical"]
prerequisites = "Arcane Strike or Disruptive; Spellcraft 8 ranks; arcane pool class feature."
prerequisite_feats = ["ref/feat/arcane-strike", "ref/feat/disruptive"]
benefit = "When you confirm a critical hit against a target while using Arcane Strike or with a weapon enhanced by your arcane pool, if the target was summoned by a spell you identified using a Spellcraft check, it must succeed at a Will save (DC = 10 + 1/2 your character level + your Intelligence modifier) or be sent back to its home plane as per the dismissal spell."
+++

## Banishing Critical (Critical)

Your familiarity with summoning creatures has taught you how to send them away with a well-timed
strike.\
**Prerequisites:** [Arcane Strike](ref/feat/arcane-strike) or [Disruptive](ref/feat/disruptive);
[Spellcraft](ref/skill/spellcraft) 8 ranks; arcane pool class feature.\
**Benefit:** When you confirm a critical hit against a target while using Arcane Strike or with a
weapon enhanced by your arcane pool, if the target was summoned by a spell you identified using a
Spellcraft check, it must succeed at a Will save (DC = 10 + 1/2 your character level + your
Intelligence modifier) or be sent back to its home plane as per the [dismissal](ref/spell/dismissal)
spell.
