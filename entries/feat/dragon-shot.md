+++
id = "ref/feat/dragon-shot"
kind = "feat"
title = "Dragon Shot"
source_ids = ["heroes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragon_shot", path = "json/feat05.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat", "Grit"]
prerequisites = "Amateur Gunslinger feat or grit class feature, Spellcraft 5 ranks."
prerequisite_feats = ["ref/feat/amateur-gunslinger"]
benefit = "As a swift action, you can spend 1 grit point to convert your gun's damage into acid, fire, electricity, or cold damage for 1 round. You can choose a different damage type each time you use this ability. This still counts as a ranged weapon attack for critical hit multipliers and abilities such as Deadly Aim."
+++

## Dragon Shot (Combat, Grit)

**Sources:** Heroes of Golarion pg 4

You instinctively channel your latent magical abilities through your firearm.\
**Prerequisites:** [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat or grit class feature,
Spellcraft 5 ranks.\
**Benefit:** As a swift action, you can spend 1 grit point to convert your gun's damage into acid,
fire, electricity, or cold damage for 1 round. You can choose a different damage type each time you
use this ability. This still counts as a ranged weapon attack for critical hit multipliers and
abilities such as [Deadly Aim](ref/feat/deadly-aim).
