+++
id = "ref/feat/redirected-shot"
kind = "feat"
title = "Redirected Shot"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "redirected_shot", path = "json/feat13.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat", "Grit"]
prerequisites = "Amateur Gunslinger or the grit class feature, Deadly Aim, Precise Shot."
prerequisite_feats = ["ref/feat/amateur-gunslinger", "ref/feat/deadly-aim", "ref/feat/precise-shot"]
benefit = "As long as you have at least 1 grit point, after an ally has made a ranged attack roll but before the results of the roll have been revealed, you can fire a loaded firearm at the volley as it moves toward its target, redirecting its path. Make an attack roll using your highest attack bonus, and use your result in place of your ally's original attack roll. On a successful hit, your ally's attack deals damage as normal. You may perform this action a number of times per round up to your Wisdom bonus (minimum 1)."
+++

## Redirected Shot (Combat, Grit)

**Sources:** Inner Sea Combat pg 17

You can redirect your allies' poorly aimed ranged attacks with incredible accuracy.\
**Prerequisites:** [Amateur Gunslinger](ref/feat/amateur-gunslinger) or the grit class feature,
[Deadly Aim](ref/feat/deadly-aim), [Precise Shot](ref/feat/precise-shot).\
**Benefit:** As long as you have at least 1 grit point, after an ally has made a ranged attack roll
but before the results of the roll have been revealed, you can fire a loaded firearm at the volley
as it moves toward its target, redirecting its path. Make an attack roll using your highest attack
bonus, and use your result in place of your ally's original attack roll. On a successful hit, your
ally's attack deals damage as normal. You may perform this action a number of times per round up to
your Wisdom bonus (minimum 1).
