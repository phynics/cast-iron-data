+++
id = "ref/feat/thuvian-grenadier"
kind = "feat"
title = "Thuvian Grenadier"
source_ids = ["people-of-the-sands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thuvian_grenadier", path = "json/feat16.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/precise-shot", label = "or" },
  { kind = "prerequisite", target = "ref/feat/throw-anything", label = "or" },
]
[[sources]]
publication = "people-of-the-sands"
page = "9"

[fields]
kind = "feat"
feat_types = ["Teamwork"]
prerequisites = "Precise Shot or Throw Anything."
prerequisite_feats = ["ref/feat/precise-shot", "ref/feat/throw-anything"]
benefit = "Whenever you hit a creature with a splash weapon, you may choose to exclude one creature within the weapon's splash area from taking splash damage. If a creature within the splash area also has this feat, it automatically ignores splash damage from your splash weapons on a successful hit."
+++

## Thuvian Grenadier (Teamwork)

Training with alchemically inclined allies helps you avoid friendly fire.\
**Prerequisites:** [Precise Shot](ref/feat/precise-shot) or
[Throw Anything](ref/feat/throw-anything).\
**Benefit:** Whenever you hit a creature with a [splash weapon](ref/rule/throw-splash-weapon), you
may choose to exclude one creature within the weapon's splash area from taking splash damage. If a
creature within the splash area also has this feat, it automatically ignores splash damage from your
splash weapons on a successful hit.

In addition, if you miss with a splash weapon and the errant weapon lands in a square occupied or
adjacent to an ally with this feat, your ally can attempt a DC 20 Reflex save. If the ally succeeds,
he is able to catch the weapon. If your ally also has the [Snatch Arrows](ref/feat/snatch-arrows)
feat, he can toss the splash weapon back to you as an immediate action.
