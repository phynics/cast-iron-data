+++
id = "ref/feat/shikigami-manipulation"
kind = "feat"
title = "Shikigami Manipulation"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shikigami_manipulation", path = "json/feat14.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/catch-off-guard", label = "or" },
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "9"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Catch Off-Guard or Throw Anything, Shikigami Mimicry, Shikigami Style, Use Magic Device 5 ranks."
prerequisite_feats = ["ref/feat/catch-off-guard", "ref/feat/shikigami-mimicry", "ref/feat/shikigami-style", "ref/feat/throw-anything"]
benefit = "While using Shikigami Style, you can treat any magical item you're using as an improvised weapon as if it granted an enhancement bonus on attack and damage rolls equal to the item's caster level divided by 4 (minimum +1), to a maximum bonus of +5."
special = "A character with this feat and Equipment Trick who uses magical equipment to perform a trick can add a bonus equal to the item's caster level divided by 4 (minimum +1) on skill or combat maneuver checks attempted as part of the trick."
+++

## Shikigami Manipulation (Combat)

You channel a magic item's power to enhance its improvised attacks, even though it was never meant
to be used as a weapon.\
**Prerequisites:** [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything), [Shikigami Mimicry](ref/feat/shikigami-mimicry),
[Shikigami Style](ref/feat/shikigami-style), Use Magic Device 5 ranks.\
**Benefit:** While using Shikigami Style, you can treat any magical item you're using as an
[improvised weapon](ref/misc/improvised-weapons) as if it granted an enhancement bonus on attack and
damage rolls equal to the item's caster level divided by 4 (minimum +1), to a maximum bonus of +5.\
**Special:** A character with this feat and [Equipment Trick](ref/feat/equipment-trick) who uses
magical equipment to perform a trick can add a bonus equal to the item's caster level divided by 4
(minimum +1) on skill or combat maneuver checks attempted as part of the trick.
