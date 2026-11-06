+++
id = "ref/feat/dastardly-trick"
kind = "feat"
title = "Dastardly Trick"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dastardly_trick", path = "json/feat04.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-swashbuckler", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat", "Panache"]
prerequisites = "Int 13; Amateur Swashbuckler or panache class feature; Combat Expertise; Improved Dirty Trick."
prerequisite_feats = ["ref/feat/amateur-swashbuckler", "ref/feat/combat-expertise", "ref/feat/improved-dirty-trick"]
benefit = "When you attempt a dirty trick combat maneuver check and expend 1 point of panache, if the maneuver is successful, your opponent must succeed at a Will save (DC = 10 + 1/2 your character level + your Charisma modifier) to remove its dirty trick condition."
+++

## Dastardly Trick (Combat, Panache)

**Sources:** Dirty Tactics Toolbox pg 14

Your confident attacks leave your foes wavering and unable to regain their composure.\
**Prerequisites:** Int 13; [Amateur Swashbuckler](ref/feat/amateur-swashbuckler) or panache class
feature; [Combat Expertise](ref/feat/combat-expertise);
[Improved Dirty Trick](ref/feat/improved-dirty-trick).\
**Benefit:** When you attempt a [dirty trick](ref/rule/dirty-trick) combat maneuver check and expend
1 point of panache, if the maneuver is successful, your opponent must succeed at a Will save (DC =
10 + 1/2 your character level + your Charisma modifier) to remove its dirty trick condition.
