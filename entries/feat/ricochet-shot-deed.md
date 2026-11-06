+++
id = "ref/feat/ricochet-shot-deed"
kind = "feat"
title = "Ricochet Shot Deed"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ricochet_shot_deed", path = "json/feat13.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Grit"]
prerequisites = "Grit class feature or Amateur Gunslinger feat, Blind-Fight."
prerequisite_feats = ["ref/feat/amateur-gunslinger", "ref/feat/blind-fight"]
benefit = "You can fire a shot at a wall or piece of solid terrain, and have it ricochet off. When you do, use the square immediately in front of the wall or piece of solid terrain to determine line of sight to a target, and this square is considered the new origin square of the attack. Use that square to determine the effects of cover, and your own square to determine the effects of concealment. You can make this shot as long as you have at least 1 grit point. When making this shot, you can spend 1 grit point to ignore the effects of all cover or concealment. You must choose to spend the grit point before you make the attack roll."
+++

## Ricochet Shot Deed (Grit)

**Sources:** Ultimate Combat pg 116

You can ricochet a firearm shot off the wall and still hit your target.\
**Prerequisites:** Grit class feature or [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat,
[Blind-Fight](ref/feat/blind-fight).\
**Benefit:** You can fire a shot at a wall or piece of solid terrain, and have it ricochet off. When
you do, use the square immediately in front of the wall or piece of solid terrain to determine line
of sight to a target, and this square is considered the new origin square of the attack. Use that
square to determine the effects of [cover](ref/rule/cover), and your own square to determine the
effects of [concealment](ref/rule/concealment). You can make this shot as long as you have at least
1 grit point. When making this shot, you can spend 1 grit point to ignore the effects of all cover
or concealment. You must choose to spend the grit point before you make the attack roll.
