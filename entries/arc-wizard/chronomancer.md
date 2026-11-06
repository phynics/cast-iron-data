+++
id = "ref/arc-wizard/chronomancer"
kind = "archetype"
title = "Chronomancer"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chronomancer", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]

[fields]
kind = "none"
+++

**Sources:** Legacy of the First World pg 30\
Time is not an immutable force but an inscrutable phenomenon. Rare arcane scholars known as
chronomancers demonstrate the ability to shift themselves in short bursts between the past, future,
and alternate presents.

**Temporal Pool (Su)**

**Ability:** A chronomancer gains a reservoir of temporal energy to manipulate the time stream in a
variety of ways listed below. This temporal pool has a number of points equal to half his class
level + his Intelligence modifier (minimum 1). This pool refreshes once per day when the
chronomancer prepares his spells.

**Forewarned**

**Ability:** The chronomancer can expend 1 point from his temporal pool when he rolls initiative to
allow himself or an ally within 30 feet to roll 1d4 and add it to that character's initiative
result.

**At 10th Level:** The die size increases to 1d6.

**At 5th Level:** The chronomancer can expend 2 points from his temporal pool as an **immediate
action** to apply this benefit to a saving throw he has just rolled (but before the result is
revealed).

**Rewind**

**Immediate:** After losing a spell due to a failed [concentration](ref/rule/concentration) check or
after casting a spell that had no effect (such as due to successful saving throws, a failed caster
level check to overcome [spell resistance](ref/rule/spell-resistance), or other immunities), the
chronomancer can expend a number of points from his temporal pool equal to half the spell's level
(minimum 1) to immediately prepare the spell again, as if it had not been cast. Any material
components expended in the original casting remain expended, as are actions used to cast the
original spell.

**Accelerate**

**Ability:** When casting a spell, the chronomancer can expend 2 points from his temporal pool to
apply the effects of [haste](ref/spell/haste) to one creature affected by the spell until the end of
the chronomancer's next turn.

**Gained:** At 10th Level

**Complex Contingency**

**Ability:** The chronomancer can specify two trigger conditions when casting
[contingency](ref/spell/contingency).

**Immediate:** In addition, when the chronomancer's _[contingency](ref/spell/contingency)_ would
trigger, the chronomancer can expend 1 point from his temporal pool to prevent the
_[contingency](ref/spell/contingency)_ from triggering, saving the stored effect for later.

**Gained:** At 15th Level

**Parallel Self**

**Ability:** If the chronomancer is killed, he can immediately expend 10 points from his temporal
pool to summon an alternate version of himself from a parallel existence, appearing up to 30 feet
away. This alternate version is identical to the chronomancer except he is a member of a random
race, determined using the table that accompanies [reincarnate](ref/spell/reincarnate). The
alternate version has half the chronomancer's total hit points (but not any
[temporary hit points](ref/rule/temporary-hit-points)) and those spells the chronomancer had
prepared when he died. The alternate version has the same equipment as the chronomancer but does not
bear any artifacts the chronomancer was carrying. Any expendable items, charges, or expensive
material components the alternate version uses are also expended for the chronomancer. This
alternate version remains for 1 minute before the duplicate and its equipment are ripped back to
their reality.

**Gained:** At 20th Level

**Replaces:** Arcane bond, 10th-, 15th-, and 20th-level bonus feats
