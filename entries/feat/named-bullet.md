+++
id = "ref/feat/named-bullet"
kind = "feat"
title = "Named Bullet"
aon = "FeatDisplay.aspx?ItemName=Named%20Bullet"
source_ids = ["champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "named_bullet", path = "json/feat11.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]
[[sources]]
publication = "champions-of-balance"
page = "19"

[fields]
kind = "feat"
feat_types = ["Grit"]
prerequisites = "Amateur Gunslinger feat or grit class feature, Gunsmithing, base attack bonus +5."
prerequisite_feats = ["ref/feat/amateur-gunslinger", "ref/feat/gunsmithing"]
benefit = "Whenever you craft ammunition using Gunsmithing, you may inscribe a bullet or alchemical cartridge with the name of its intended target. The ammunition gains the bane weapon special ability against the chosen creature only. If the ammunition is used to attack any other target, the attack roll is instead made with a -2 penalty. Crafting a named bullet costs 1 grit point and reduces your maximum grit points by 1 until the named bullet is fired or destroyed."
+++

## Named Bullet (Grit)

You can craft ammunition intended to kill specific foes.\
**Prerequisites:** [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat or grit class feature,
[Gunsmithing](ref/feat/gunsmithing), base attack bonus +5.\
**Benefit:** Whenever you craft ammunition using Gunsmithing, you may inscribe a bullet or
alchemical cartridge with the name of its intended target. The ammunition gains the
[bane](ref/magic-enh/bane) weapon special ability against the chosen creature only. If the
ammunition is used to attack any other target, the attack roll is instead made with a -2 penalty.
Crafting a named bullet costs 1 grit point and reduces your maximum grit points by 1 until the named
bullet is fired or destroyed.
