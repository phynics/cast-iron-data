+++
id = "ref/arc-bard/wit"
kind = "archetype"
title = "Wit"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wit", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]

[fields]
kind = "archetype"
replaces = ["Bardic knowledge", "Inspire competence", "dirge of doom", "frightening tune", "Versatile performance", "Lore master", "Jack-of-all-trades"]
alters = ["Countersong"]
+++

**Sources:** Ultimate Intrigue pg 23\
The wit is a master of clever repartee and verbal dueling, moving through noble courts like a fish
through water.

**Way with Words (Ex)**

**Passive:** A wit gains a bonus on Bluff, Diplomacy, Intimidate, Linguistics, and Sense Motive
checks. This bonus is equal to 1 + one-fourth of his bard level. He also gains a number of edges at
the beginning of any [verbal duel](ref/rule/verbal-duels) equal to this bonus.

**Replaces:** Bardic knowledge

**Counterargument**

**Ability:** A wit can use only Perform (act, comedy, or oratory) to perform a countersong.

**Alters:** Countersong

**Bardic Performance**

**Info:** A wit gains the following bardic performance.

**Cutting Remark (Su)**

**At 14th Level:** A target who takes damage from cutting remark must also succeed at a Will save
(DC = 10 + [half](ref/misc/fractions-and-rounding) the wit's bard level + his Charisma modifier) or
be [dazed](ref/misc/dazed) for 1 round. A creature that makes a successful save is immune to the
dazing effect of the wit's cutting remark for 24 hours.

**At 8th Level:** A target who takes damage from cutting remark is also
[sickened](ref/misc/sickened) for as long as it remains within 30 feet of the wit and for 1 round
thereafter. Additionally, the nonlethal damage counts as magic for purposes such as overcoming
[damage reduction](ref/rule/damage-reduction).

**Gained:** At 3rd Level

**Replaces:** Inspire competence, dirge of doom, frightening tune

**Special:** Cutting remark is a mind-affecting, language-dependent effect, and relies on audible
components.

**Standard:** A wit can wound with his words. The wit can spend 1 round of bardic performance to
deal 1d4 points of nonlethal damage + the wit's bard level to a creature within 30 feet.
[Damage reduction](ref/rule/damage-reduction) applies to this damage.

**Quick Witted (Ex)**

**At 2nd Level:** A wit can always act in a surprise round (though he remains
[flat-footed](ref/rule/flat-footed) until he acts). In addition, the wit adds half his bard level on
initiative checks.

**Replaces:** Versatile performance

**On the Ball (Ex)**

**At 20th Level:** When the wit uses this ability, he can instead treat his roll as if it was a 20.

**At 5th Level:** Rather than roll for initiative, the wit can treat his roll as if it was a 10
(adding any modifiers as usual).

**Replaces:** Lore master

**Usage:** 1 time/day + 1 per 6 bard levels beyond 5th

**Duel Master (Ex)**

**Ability:** Once during a verbal duel, he can reassign an appropriate skill from one tactic to
another tactic in which he didn't assign any skills. The original tactic is treated as being
unprepared for the rest of the duel.

**Gained:** At 10th Level

**Passive:** The wit does not lose any edges for being at an extreme disadvantage in a verbal duel
and can either ask about one additional bias when successfully using Sense Motive to determine an
audience's biases or automatically seed one of the biases that he discovered.

**Replaces:** Jack-of-all-trades
