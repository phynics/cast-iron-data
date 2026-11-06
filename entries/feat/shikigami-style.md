+++
id = "ref/feat/shikigami-style"
kind = "feat"
title = "Shikigami Style"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shikigami_style", path = "json/feat14.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/catch-off-guard", label = "or" },
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat", "Style"]
prerequisites = "Catch Off-Guard or Throw Anything."
prerequisite_feats = ["ref/feat/catch-off-guard", "ref/feat/throw-anything"]
benefit = "While in this style, you deal damage with improvised weapons as if they were one size category larger. For every style feat you have that lists Shikigami Style as a prerequisite, treat the improvised weapon as an additional size category larger, to a maximum of three sizes larger than its actual size."
+++

## Shikigami Style (Combat, Style)

**Sources:** Martial Arts Handbook pg 9

Your skill with improvised weapons makes them more dangerous than they would otherwise be.\
**Prerequisites:** [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything).\
**Benefit:** While in this style, you deal damage with
[improvised weapons](ref/misc/improvised-weapons) as if they were
[one size category larger](ref/misc/damage-die-adjustments). For every style feat you have that
lists Shikigami Style as a prerequisite, treat the improvised weapon as an additional size category
larger, to a maximum of three sizes larger than its actual size.
