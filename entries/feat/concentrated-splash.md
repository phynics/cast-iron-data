+++
id = "ref/feat/concentrated-splash"
kind = "feat"
title = "Concentrated Splash"
source_ids = ["ranged-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "concentrated_splash", path = "json/feat03.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/precise-shot", label = "or" },
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]
[[sources]]
publication = "ranged-tactics-toolbox"
page = "6"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Precise Shot or Throw Anything."
prerequisite_feats = ["ref/feat/precise-shot", "ref/feat/throw-anything"]
benefit = "When you deal a direct hit to a creature with a splash weapon that normally also deals splash damage, you can choose to forgo dealing splash damage. If you do, the damage dealt to the target of the direct hit increases by 50%. This damage is multiplied on a critical hit."
+++

## Concentrated Splash (Combat)

You can limit the splatter of your splash weapons to increase damage against your target.\
**Prerequisites:** [Precise Shot](ref/feat/precise-shot) or
[Throw Anything](ref/feat/throw-anything).\
**Benefit:** When you deal a direct hit to a creature with a
[splash weapon](ref/rule/throw-splash-weapon) that normally also deals splash damage, you can choose
to forgo dealing splash damage. If you do, the damage dealt to the target of the direct hit
increases by 50%. This damage is multiplied on a critical hit.

This feat cannot be used with an alchemist's bombs.
