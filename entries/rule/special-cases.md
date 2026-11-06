+++
id = "ref/rule/special-cases"
kind = "rule"
title = "Special Cases"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "special_cases", path = "json/rules_opt_combat01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 111

Dealing with spells and abilities that grant additional attacks, rerolls, or high bonuses can be
tricky under this system. So many rules are based around iterative attacks that it's not possible to
cover every type of effect that needs to be adjusted. GMs should use the following rules as
guidelines when interpreting how to implement similar spells and abilities.

### Extra Attacks

Effects such as haste that grant additional attacks instead raise your maximum number of hits by
one. This includes secondary natural attacks made at the end of a manufactured weapon full attack.

### Rerolls

Since the full attack roll simulates a series of rolls, effects that grant or force single rerolls
instead grant either a +2 bonus (if the attacker keeps the better roll, or the character causing the
reroll intends to aid the attacker) or -2 penalty (if the attacker keeps the lower roll, or the
character causing the reroll intends to hinder the attacker). Effects that would grant rerolls for
all attack rolls made as part of the full attack allow the attacker to reroll the attack roll
instead of imposing a bonus or penalty.

### True Strike

When using [true strike](ref/spell/true-strike) with a full attack, first see how many hits you
would have scored without _[true strike](ref/spell/true-strike)._ A single casting of
_[true strike](ref/spell/true-strike)_ adds at most one more hit.
