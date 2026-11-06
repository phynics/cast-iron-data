+++
id = "ref/rule/base-attack-bonus"
kind = "rule"
title = "Base Attack Bonus"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "base_attack_bonus", path = "json/rules_opt_pc_adv01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 40

There are three base attack bonus progressions. For classes with a d6 Hit Die, their BAB increases
by 1/2 per level. For classes with a d8 Hit Die, their BAB increases by 3/4 per level. For classes
with a d10 or d12 Hit Die, their BAB increases by 1 per level (so it's not necessary to round the
BAB for these classes). A multiclass character's base attack bonus will only ever improve using this
variant.

For example, a character who's a 2nd-level rogue and a 9th-level wizard would have a BAB of +5 in
the core rules: +1 from her rogue levels and +4 from her wizard levels. Using the fractional system,
that character's BAB would be +6, with +1-1/2 from her rogue levels and +4-1/2 from her wizard
levels - enough for her to gain a second attack at a +1 bonus.
