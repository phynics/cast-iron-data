+++
id = "ref/arc-monk/nornkith"
kind = "archetype"
title = "Nornkith"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Nornkith"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nornkith", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "conviction-of-fate" },
  { anchor = "forewarned", level = 1 },
  { anchor = "shears", level = 1 },
  { anchor = "resist-death-s-lure", level = 5 },
  { anchor = "fate-weaver", level = 11 },
  { anchor = "snip-thread", level = 15 },
  { anchor = "inscrutable", level = 19 },
  { anchor = "norn-transformation", level = 20 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["forewarned"] },
  { replaces = "Bonus feat gained at 1st level", feature = "bonus-feat", levels = [1], by = ["shears"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["resist-death-s-lure"] },
  { replaces = "bonus feat gained at 10th level", feature = "bonus-feat", levels = [10], by = ["resist-death-s-lure"] },
  { replaces = "Diamond soul", feature = "diamond-soul", by = ["fate-weaver"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["snip-thread"] },
  { replaces = "Empty body", feature = "empty-body", by = ["inscrutable"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["norn-transformation"] },
]
+++

Nornkith hone their bodies and minds to follow the branching threefold paths of fate. Nornkith seek
to emulate the fey masters of fate called [norns](ref/monster/norn) and eventually ascend to become
norns in their own right.

## Conviction of Fate (Ex) {#conviction-of-fate}

A nornkith uses her Charisma, rather than her Wisdom, to determine all class features and effects
relating to his monk class.

## Forewarned (Su) {#forewarned}

A nornkith can always act in the surprise round, even if he does not notice her enemies, though she
remains [flat-footed](ref/rule/flat-footed) until she takes an action. In addition, she gains a
bonus on initiative rolls equal to half her monk level (minimum +1). At 20th level, a nornkith's
initiative roll is automatically a natural 20.

This ability replaces stunning fist.

## Shears (Su) {#shears}

Whenever a nornkith makes an unarmed strike, she can cause shimmering silver shears to manifest
around the blow, causing the unarmed strike to count as silver for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). At 7th level, she gains
[Improved Critical](ref/feat/improved-critical) (unarmed strike) as a bonus feat, even if she does
not meet the prerequisites.

This ability replaces the bonus feat gained at 1st level.

## Resist Death's Lure (Su) {#resist-death-s-lure}

At 5th level, a nornkith gains a +4 morale bonus on saves against death effects,
[energy drain](ref/rule/energy-drain-and-negative-levels), and negative energy. At 10th level, she
gains immunity to energy drain and negative energy.

This ability replaces purity of body and the bonus feat gained at 10th level.

## Fate Weaver (Su) {#fate-weaver}

At 11th level, a nornkith can spend 1 ki point as an immediate action to force a creature within 60
feet to reroll one saving throw before the results of the roll are revealed. The creature must take
the result of the second roll, even if it's worse than the original roll. Whether the new result is
a success or failure, the creature cannot be the target of this ability again for 1 day.

This ability replaces diamond soul.

## Snip Thread (Su) {#snip-thread}

At 15th level, as a standard action, a monk can spend 1 ki point to produce a golden thread linked
to the fate of a creature within 60 feet and mimic snipping through the thread with a pair of
shears. The target takes 1d6 points of damage per nornkith level and can attempt a Fortitude saving
throw (DC = 10 + half the nornkith's monk level + her Charisma modifier) to halve this damage. If
the damage would bring the target's hit points to 0 or below, the nornkith can spend another ki
point to sever the golden thread completely; in this case, the target dies and can only be restored
to life with _[miracle](ref/spell/miracle)_, _[wish](ref/spell/wish)_, or divine intervention. The
nornkith can use this ability once per day. This is a death effect.

This ability replaces quivering palm.

## Inscrutable (Su) {#inscrutable}

At 19th level, the nornkith is protected by a constant _[mind blank](ref/spell/mind-blank)_ effect
with a caster level equal to her monk level. The nornkith can suppress or resume this protection as
a standard action.

This ability replaces empty body.

## Norn Transformation {#norn-transformation}

At 20th level, a nornkith attains her [fey](ref/type/fey) heritage. Her type changes to fey, and she
gains DR 10/cold iron.

This ability replaces perfect self.
