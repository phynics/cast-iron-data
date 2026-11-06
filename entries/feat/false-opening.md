+++
id = "ref/feat/false-opening"
kind = "feat"
title = "False Opening"
source_ids = ["ultimate-combat", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_opening", path = "json/feat06.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/close-quarters-thrower", label = "or" },
  { kind = "prerequisite", target = "ref/feat/point-blank-master", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Dex 13, Dodge, Close Quarters Thrower or Point-Blank Master, Weapon Focus with selected ranged weapon."
prerequisite_feats = ["ref/feat/close-quarters-thrower", "ref/feat/dodge", "ref/feat/point-blank-master", "ref/feat/weapon-focus"]
benefit = "Choose a ranged weapon or a thrown weapon. When you make a ranged attack using that weapon, you can choose to provoke an attack of opportunity from one or more opponents who threaten you. You gain a +4 dodge bonus against such attacks. An opponent that makes such an attack and misses you loses his Dexterity bonus to AC against you until the end of your turn."
+++

## False Opening (Combat)

**Sources:** Ultimate Combat pg 100

When you make a ranged attack while threatened, you can fool your opponent into thinking he has an
opening.\
**Prerequisites:** Dex 13, [Dodge](ref/feat/dodge),
[Close Quarters Thrower](ref/feat/close-quarters-thrower) or
[Point-Blank Master](ref/feat/point-blank-master), [Weapon Focus](ref/feat/weapon-focus) with
selected ranged weapon.\
**Benefit:** Choose a ranged weapon or a thrown weapon. When you make a ranged attack using that
weapon, you can choose to provoke an attack of opportunity from one or more opponents who threaten
you. You gain a +4 dodge bonus against such attacks. An opponent that makes such an attack and
misses you loses his Dexterity bonus to AC against you until the end of your turn.

### Stamina

**Sources:** Pathfinder Unchained pg 119\
When you use this feat, you can spend 5 stamina points to make an attack of opportunity against an
opponent who misses you with the provoked attack (after it loses its Dexterity bonus to AC against
you).
