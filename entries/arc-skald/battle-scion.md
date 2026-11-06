+++
id = "ref/arc-skald/battle-scion"
kind = "archetype"
title = "Battle Scion"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "battle_scion", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Intrigue pg 48\
The battle scion possesses a unique mixture of courtly grace alongside martial and magical prowess.
She is a warrior-poet, as skilled with her words as she is with blades. Battle scions sometimes rule
as queens over courts of brave knights who scour the world championing bold quests.

**Courtly Presence (Ex)**

**Ability:** The battle scion adds 1/2 her character level to [Intimidate](ref/skill/intimidate)
checks, and she starts any [verbal duel](ref/rule/verbal-duels) with an extra edge that she can use
for the presence tactic so long as she is not at a significant or extreme disadvantage in the duel.
However, her bardic knowledge ability applies to only Knowledge (geography), Knowledge (history),
Knowledge (local), and Knowledge (nobility).

**Flavor:** A battle scion's bearing radiates command and presence, allowing her to tower over her
opponents in social situations.

**Gained:** At 1st Level

**Replaces:** Bardic knowledge

**Battle Prowess (Ex)**

**Ability:** Whenever a battle scion would gain a rage power from the skald's _rage power_ ability
(at 3rd level and every 3 skald levels thereafter), she can instead choose to gain a combat feat or
teamwork feat for which she meets the prerequisites. Like rage powers she selects in this way, the
battle scion can grant this feat to allies under the effect of _inspired rage,_ as long as those
allies also meet the prerequisites, but she must expend 2 rounds of _raging song_ for each round in
which she grants a combat feat or teamwork feat.

**Replaces:** Rage power

**Special:** If the battle scion gains multiple feats from _battle prowess,_ allies can use these
feats to meet the prerequisites for other feats while they're affected by _battle prowess_ (for
example, a battle scion with [Power Attack](ref/feat/power-attack) and [Cleave](ref/feat/cleave)
from _battle prowess_ could grant both, allowing allies with a +1 base attack bonus and a Strength
score of 13 to gain both, since they can use Power Attack to qualify for Cleave).

**Raging Song (Su)**

**Info:** A battle scion gains the following _raging song._

**Song of Questing (Su)**

**Ability:** The battle scion can spend 4 rounds of _raging song_ to draw upon a target's honor,
ambition, and sense of self in order to bind the target to an agreed-upon task, often a noble quest.
This works like [geas/quest](ref/spell/geas-quest), except it applies only if the target is truly
willing (not magically compelled or tricked), and the target automatically understands the full
terms of the agreement before deciding whether he is willing.

**At 14th Level:** She can offer the same quest to up to one willing creature per skald level. If
she does so, the effect ends for all creatures as soon as anyone completes the quest, though only
the creature who completes it earns any offered reward.

**Info:** The battle scion can offer a reward for the completion of the noble quest, but if she does
so and fails to live up to her agreement, she becomes an ex-battle scion and loses all benefits
gained from the archetype (she does not gain the abilities they replaced, either).

**Gained:** At 10th Level

**Replaces:** Dirge of doom, song of the fallen

**Once and Future Scion (Su)**

**Flavor:** A battle scion becomes extremely difficult to kill.

**Gained:** At 20th Level

**Passive:** Whenever she is slain, as long as her body isn't destroyed, she enters a deathlike
sleep for 3 days, after which she returns to life as per [raise dead](ref/spell/raise-dead), except
that it can restore her even if she was slain by a death effect. Spells that would restore her to
life function as if she were dead during this time, allowing her to recover sooner.

**Replaces:** Master skald
