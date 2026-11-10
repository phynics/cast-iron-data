+++
id = "ref/feat/casterbane-shot"
kind = "feat"
title = "Casterbane Shot"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "casterbane_shot", path = "json/feat02.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]
[[sources]]
publication = "inner-sea-combat"
page = "17"

[fields]
kind = "feat"
feat_types = ["Combat", "Grit"]
prerequisites = "Amateur Gunslinger or grit class feature, Point-Blank Shot, Precise Shot, base attack bonus +4."
prerequisite_feats = ["ref/feat/amateur-gunslinger", "ref/feat/point-blank-shot", "ref/feat/precise-shot"]
benefit = "If you ready a ranged attack with a firearm to attack a spellcaster when he begins casting a spell and successfully hit your opponent, you can expend 1 grit point to increase the target's concentration check DC for being injured while casting by 5."
+++

## Casterbane Shot (Combat, Grit)

Life in the Mana Wastes, where magic has unpredictable and often fatal effects, has taught you to
disable spellcasters with your firearms.\
**Prerequisites:** [Amateur Gunslinger](ref/feat/amateur-gunslinger) or grit class feature,
[Point-Blank Shot](ref/feat/point-blank-shot), [Precise Shot](ref/feat/precise-shot), base attack
bonus +4.\
**Benefit:** If you ready a ranged attack with a firearm to attack a spellcaster when he begins
casting a spell and successfully hit your opponent, you can expend 1 grit point to increase the
target's [concentration](ref/rule/concentration) check DC for being injured while casting by 5.
