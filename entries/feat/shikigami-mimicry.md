+++
id = "ref/feat/shikigami-mimicry"
kind = "feat"
title = "Shikigami Mimicry"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shikigami_mimicry", path = "json/feat14.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/catch-off-guard", label = "or" },
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Catch Off-Guard or Throw Anything, Shikigami Style."
prerequisite_feats = ["ref/feat/catch-off-guard", "ref/feat/shikigami-style", "ref/feat/throw-anything"]
benefit = "While in Shikigami Style, you can take a -2 penalty on attack rolls to treat an improvised weapon as if it had one of the following weapon special qualities until the start of your next turn: blocking, brace, disarm, distracting, nonlethal, performance, or trip. If the weapon has the fragile special quality or broken condition, you can treat it as if it had the [jagged](rule/improvised_weapon_special_features) special quality."
+++

## Shikigami Mimicry (Combat)

**Sources:** Martial Arts Handbook pg 9

Your unique understanding of improvised tools enables you to turn the intrinsic form of all manner
of objects to your advantage in combat.\
**Prerequisites:** [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything), [Shikigami Style](ref/feat/shikigami-style).\
**Benefit:** While in Shikigami Style, you can take a -2 penalty on attack rolls to treat an
[improvised weapon](ref/misc/improvised-weapons) as if it had one of the following weapon special
qualities until the start of your next turn: [blocking](ref/misc/blocking), [brace](ref/misc/brace),
[disarm](ref/misc/disarm), [distracting](ref/misc/distracting), [nonlethal](ref/misc/nonlethal),
[performance](ref/misc/performance), or [trip](ref/misc/trip). If the weapon has the
[fragile](ref/misc/fragile) special quality or [broken](ref/misc/broken) condition, you can treat it
as if it had the [jagged](ref/rule/improvised-weapon-special-features) special quality.
