+++
id = "ref/rule/calculating-skill-bonuses"
kind = "rule"
title = "Calculating Skill Bonuses"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calculating_skill_bonuses", path = "json/rules_opt_skills01.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "70"

[fields]
kind = "none"
+++

If a character has a specialty in a skill and that skill is also in a skill group she's trained in,
her bonus on checks using the skill is equal to her relevant ability modifier + her character level.
If only one applies - she only has a specialty in the skill or she is trained in that skill's group
but doesn't have a specialty in the skill - her bonus is equal to her relevant ability modifier +
1/2 her character level (minimum 1).

If a skill is on her class skill list, she gains the +3 bonus if she's trained in its skill group or
has a specialty in it; she doesn't have to both be trained and have a specialty. Class skill bonuses
look only at specific skills, not groups. If Diplomacy is on a character's class skill list but
Bluff isn't, having training in the Social skill group doesn't allow that character to gain the
class skill bonus on Bluff checks. Any circumstance that modifies skill checks, such as the
[Skill Focus](ref/feat/skill-focus) feat or certain spells, still grants the same bonus or penalty
as it would if the campaign weren't using grouped skills.
