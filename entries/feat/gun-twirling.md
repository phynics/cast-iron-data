+++
id = "ref/feat/gun-twirling"
kind = "feat"
title = "Gun Twirling"
source_ids = ["champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gun_twirling", path = "json/feat08.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Grit"]
prerequisites = "Amateur Gunslinger feat or grit class feature, Dazzling Display, Weapon Focus."
prerequisite_feats = ["ref/feat/amateur-gunslinger", "ref/feat/dazzling-display", "ref/feat/weapon-focus"]
benefit = "You can spend 1 grit point to make a feint attempt using a one-handed firearm for which you have Weapon Focus (instead of a melee weapon). The target of this feint must be within 30 feet of you and be able to see you."
+++

## Gun Twirling (Grit)

**Sources:** Champions of Balance pg 19

You can spin and juggle a small firearm, making it difficult to predict where you will shoot.\
**Prerequisites:** [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat or grit class feature,
[Dazzling Display](ref/feat/dazzling-display), [Weapon Focus](ref/feat/weapon-focus).\
**Benefit:** You can spend 1 grit point to make a [feint](ref/rule/feint) attempt using a one-handed
firearm for which you have Weapon Focus (instead of a melee weapon). The target of this feint must
be within 30 feet of you and be able to see you.

If you have the [Quick Draw](ref/feat/quick-draw) feat, you can holster a one-handed firearm as a
free action as long as you have at least 1 grit point.
