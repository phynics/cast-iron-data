+++
id = "ref/invtalent/empathy"
kind = "rule"
title = "Empathy"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "empathy", path = "json/class_ability_investigator_talents.json" },
]

[fields]
kind = "none"
+++

**Empathy (Ex, Su)**

**Ability:** When attempting a [Sense Motive](ref/rule/sense-motive) check, the investigator makes
two d20 rolls and takes the higher result.

If an investigator uses _inspiration_ on a Sense Motive check, he rolls the _inspiration_ dice twice
and takes the higher result.

**Ability2:** Once per day, the investigator can expend one use of _inspiration_ to target a single
creature that he can see and hear within 30 feet. Upon doing so, the investigator detects the
surface thoughts of the target's mind, as if he concentrated for 3 rounds while using the
[detect thoughts](ref/spell/detect-thoughts) spell, unless the creature succeeds a Will saving
throw. The DC of this save is 10 + 1/2 the investigator's level + his Intelligence modifier.

If the target fails, the investigator can continue to detect the surface thoughts of the target
creature for a number of rounds equal to 1/2 his investigator level.

**Prereq:** 5th-level investigator
