+++
id = "ref/feat/pinpoint-poisoner"
kind = "feat"
title = "Pinpoint Poisoner"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pinpoint_poisoner", path = "json/feat12.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/two-weapon-fighting", label = "or" },
]
[[sources]]
publication = "ultimate-combat"
page = "113"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Poison use class feature, Craft (alchemy) 6 ranks, Adder Strike, Improved Unarmed Strike, Two-Weapon Fighting or flurry of blows class feature."
prerequisite_feats = ["ref/feat/adder-strike", "ref/feat/improved-unarmed-strike", "ref/feat/two-weapon-fighting"]
benefit = "When you use Adder Strike, you can instead poison up to two blowgun darts that you can then use to strike your opponent in melee. (Drawing such darts is a free action.) While holding these darts, you can spend a standard action to attack with one or a full-attack action to attack with both. Such attacks are considered melee touch attacks that deal 1d2 damage plus any bonuses you gain on your normal unarmed strike damage, and they deliver the poison. You can instead throw such darts as if they were shuriken, making your ranged attack rolls against the target's AC."
normal = "Applying poison to a weapon or single piece of ammunition is a standard action."
+++

## Pinpoint Poisoner (Combat)

You deftly use specially prepared needles to apply poison for maximum effect.\
**Prerequisites:** [Poison use](ref/ability/poison-use) class feature, Craft (alchemy) 6 ranks,
[Adder Strike](ref/feat/adder-strike), [Improved Unarmed Strike](ref/feat/improved-unarmed-strike),
[Two-Weapon Fighting](ref/feat/two-weapon-fighting) or flurry of blows class feature.\
**Benefit:** When you use Adder Strike, you can instead poison up to two
[blowgun darts](ref/eq-weapon/blowgun-darts) that you can then use to strike your opponent in melee.
(Drawing such darts is a free action.) While holding these darts, you can spend a standard action to
attack with one or a full-attack action to attack with both. Such attacks are considered melee touch
attacks that deal 1d2 damage plus any bonuses you gain on your normal unarmed strike damage, and
they deliver the poison. You can instead throw such darts as if they were
[shuriken](ref/eq-weapon/shuriken), making your ranged attack rolls against the target's AC.\
**Normal:** Applying poison to a weapon or single piece of ammunition is a standard action.
