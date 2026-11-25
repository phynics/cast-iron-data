+++
id = "ref/arc-bard/wit"
kind = "archetype"
title = "Wit"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Wit"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wit", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "way-with-words", level = 1 },
  { anchor = "counterargument" },
  { anchor = "bardic-performance" },
  { anchor = "cutting-remark", level = 3 },
  { anchor = "quick-witted", level = 2 },
  { anchor = "on-the-ball", level = 5 },
  { anchor = "duel-master", level = 10 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["way-with-words"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["cutting-remark"] },
  { replaces = "dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["cutting-remark"] },
  { replaces = "frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["cutting-remark"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["quick-witted"] },
  { replaces = "Lore master", feature = "lore-master", by = ["on-the-ball"] },
  { replaces = "Jack-of-all-trades", feature = "jack-of-all-trades", by = ["duel-master"] },
  { alters = "Countersong", feature = "bardic-performance", power = "countersong", by = ["counterargument"] },
]
+++

The wit is a master of clever repartee and verbal dueling, moving through noble courts like a fish
through water.

## Way with Words (Ex) {#way-with-words}

A wit gains a +1 bonus on Bluff, Diplomacy, Intimidate, Linguistics, and Sense Motive checks. At 4th
level, and every 4 bard levels thereafter, this bonus increases by 1, to a maximum of +6 at 20th
level. He also gains a number of edges at the beginning of any [verbal duel](ref/rule/verbal-duels)
(see pages 176–181) equal to this bonus.

This ability replaces bardic knowledge.

## Counterargument {#counterargument}

A wit can use only Perform (act, comedy, or oratory) to perform a countersong.

This ability alters countersong.

## Bardic Performance {#bardic-performance}

A wit gains the following bardic performance.

## Cutting Remark (Su) {#cutting-remark}

At 3rd level, a wit can wound with his words. The wit can spend 1 round of bardic performance as a
standard action to deal 1d4 points of nonlethal damage + the wit's bard level to a creature within
30 feet. [Damage reduction](ref/rule/damage-reduction) applies to this damage.

At 8th level, a target who takes damage from cutting remark is also [sickened](ref/misc/sickened)
for as long as it remains within 30 feet of the wit and for 1 round thereafter. Additionally, the
nonlethal damage counts as magic for purposes such as overcoming
[damage reduction](ref/rule/damage-reduction).

At 14th level, a target who takes damage from cutting remark must also succeed at a Will save (DC =
10 + 1/2 the wit's bard level + his Charisma modifier) or be [dazed](ref/misc/dazed) for 1 round. A
creature that makes a successful save is immune to the dazing effect of the wit's cutting remark for
24 hours.

Cutting remark is a mind-affecting, language-dependent effect, and relies on audible components.

This ability replaces inspire competence, dirge of doom, and frightening tune.

## Quick Witted (Ex) {#quick-witted}

At 2nd level, a wit can always act in a surprise round (though he remains
[flat-footed](ref/rule/flat-footed) until he acts). In addition, the wit adds half his bard level on
initiative checks.

This ability replaces versatile performance.

## On the Ball (Ex) {#on-the-ball}

At 5th level, rather than roll for initiative, the wit can treat his roll as if it was a 10 (adding
any modifiers as usual). The wit can use this ability once per day at 5th level, and an additional
time per day for every 6 bard levels thereafter. At 20th level, when the wit uses this ability, he
can instead treat his roll as if it was a 20.

This ability replaces lore master.

## Duel Master (Ex) {#duel-master}

At 10th level, the wit does not lose any edges for being at an extreme disadvantage in a verbal duel
(see pages 176–181) and can either ask about one additional bias when successfully using Sense
Motive to determine an audience's biases or automatically seed one of the biases that he discovered.
Once during a verbal duel, he can reassign an appropriate skill from one tactic to another tactic in
which he didn't assign any skills. The original tactic is treated as being unprepared for the rest
of the duel.

This ability replaces jack-of-all-trades.
