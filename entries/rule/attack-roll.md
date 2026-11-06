+++
id = "ref/rule/attack-roll"
kind = "rule"
title = "Attack Roll and Attack Bonus"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "attack_roll", path = "json/rules_combat01.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 178

An attack roll represents your attempt to strike your opponent on your turn in a round. When you
make an attack roll, you roll a d20 and add your attack bonus. (Other modifiers may also apply to
this roll.) If your result equals or beats the target's Armor Class, you hit and deal damage.

**Automatic Misses and Hits:** A natural 1 (the d20 comes up 1) on an attack roll is always a miss.
A natural 20 (the d20 comes up 20) is always a hit. A natural 20 is also a threat - a possible
critical hit (see [the attack action](ref/rule/attack)).

Your attack bonus with a melee weapon is the following:

> Base attack bonus + Strength modifier + size modifier

With a ranged weapon, your attack bonus is the following:

> Base attack bonus + Dexterity modifier + size modifier + range penalty
