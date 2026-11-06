+++
id = "ref/rule/monster-skill-bonuses"
kind = "rule"
title = "Monster Skill Bonuses"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monster_skill_bonuses", path = "json/rules_opt_skills01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 68

When running a prebuilt monster, the GM can convert core skills to consolidated skills on the fly.
The GM can choose one of two paths: either use the monster's highest printed bonus as its bonus with
the relevant consolidated skill, or treat each bonus as though it applies only to a sub-function of
a consolidated skill. For example, an ice devil has a +22 bonus on Acrobatics checks and a +13 bonus
on Fly checks. The GM could either give the devil a +22 bonus on all Acrobatics checks, or use the
+22 bonus if the monster is moving through a threatened area and the +13 bonus if it's flying.
Either approach can work, but the GM should be consistent with which she uses.

A GM using the highest-bonus approach still might want to consider separating out the bonuses in the
case of large racial modifiers. A monster with a climb speed should probably not get its +8 racial
bonus on Athletics checks to jump or swim.
