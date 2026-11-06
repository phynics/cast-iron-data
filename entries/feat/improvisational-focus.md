+++
id = "ref/feat/improvisational-focus"
kind = "feat"
title = "Improvisational Focus"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "improvisational_focus", path = "json/feat09.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/catch-off-guard", label = "or" },
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Catch Off-Guard or Throw Anything, base attack bonus +1."
prerequisite_feats = ["ref/feat/catch-off-guard", "ref/feat/throw-anything"]
benefit = "You gain a +1 bonus on attack rolls you make using an improvised weapon. You are considered proficient with the improvised weapon and are considered to have Weapon Focus with improvised weapons for the purpose of meeting the prerequisites of feats that specifically select a weapon, such as Weapon Specialization."
special = "Thrown splash weapons are not considered improvised weapons for the purposes of this feat."
+++

## Improvisational Focus (Combat)

**Sources:** Martial Arts Handbook pg 8

A makeshift weapon in your hands is as dangerous as any other instrument of violence.\
**Prerequisites:** [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything), base attack bonus +1.\
**Benefit:** You gain a +1 bonus on attack rolls you make using an
[improvised weapon](ref/misc/improvised-weapons). You are considered proficient with the improvised
weapon and are considered to have [Weapon Focus](ref/feat/weapon-focus) with improvised weapons for
the purpose of meeting the prerequisites of feats that specifically select a weapon, such as
[Weapon Specialization](ref/feat/weapon-specialization).\
**Special:** [Thrown splash weapons](ref/rule/throw-splash-weapon) are not considered improvised
weapons for the purposes of this feat.
