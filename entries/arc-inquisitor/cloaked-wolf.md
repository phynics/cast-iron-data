+++
id = "ref/arc-inquisitor/cloaked-wolf"
kind = "archetype"
title = "Cloaked Wolf"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Cloaked%20Wolf"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloaked_wolf", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "28"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "lure-prey", level = 1 },
  { anchor = "always-wary" },
  { anchor = "unleashed-fury", level = 3 },
]
trades = [
  { replaces = "Stern gaze", feature = "stern-gaze", by = ["lure-prey"] },
  { replaces = "Monster lore", feature = "monster-lore", by = ["always-wary"] },
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["unleashed-fury"] },
  { replaces = "teamwork feats", feature = "teamwork-feat", by = ["unleashed-fury"] },
  { alters = "Cunning initiative", feature = "cunning-initiative", by = ["always-wary"] },
]
+++

Some inquisitors are adept at appearing harmless until they throw off their unassuming facades and
take their enemies by surprise.

## Class Skills {#class-skills}

A cloaked wolf adds Sleight of Hand to her list of class skills, instead of Intimidate.

This alters the inquisitor's class skills.

## Lure Prey (Ex) {#lure-prey}

Cloaked wolves are skilled at maintaining a harmless guise even while they silently prepare to
strike against their enemies. Starting at 1st level, a cloaked wolf receives a morale bonus on all
Disguise and Sleight of Hand checks equal to [half](ref/misc/fractions-and-rounding) her inquisitor
level (minimum +1). When a cloaked wolf uses Sleight of Hand to draw a hidden weapon, this bonus
doubles.

This ability replaces stern gaze.

## Always Wary (Ex) {#always-wary}

A cloaked wolf is always ready for betrayal and subterfuge. Whenever she attempts a Sense Motive
check to avoid being surprised by a foe using Bluff to conceal the attack, the cloaked wolf can
always act during the surprise round, regardless of the result of the check. At 2nd level, she adds
her Wisdom modifier (in addition to her Dexterity modifier) to her initiative checks during any such
encounter.

This ability alters cunning initiative and replaces monster lore.

## Unleashed Fury (Ex) {#unleashed-fury}

At 3rd level, a cloaked wolf can transition between parley and combat in the blink of an eye. She
gains [Quick Draw](ref/feat/quick-draw) as a bonus feat.

Additionally, at 6th level and every 3 inquisitor levels thereafter, she gains a bonus feat from the
following list: [Alertness](ref/feat/alertness), [Catch Off-Guard](ref/feat/catch-off-guard),
[Deceitful](ref/feat/deceitful), [Deft Hands](ref/feat/deft-hands), [Dodge](ref/feat/dodge),
[Improved Initiative](ref/feat/improved-initiative),
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike),
[Improvised Weapon Mastery](ref/feat/improvised-weapon-mastery), [Lookout](ref/feat/lookout),
[Mobility](ref/feat/mobility), [Spring Attack](ref/feat/spring-attack),
[Stunning Fist](ref/feat/stunning-fist), and [Throw Anything](ref/feat/throw-anything). She must
meet the prerequisites of the selected bonus feat.

As a standard action, a cloaked wolf can choose to learn a new bonus feat from the above list in
place of the most recent bonus feat she has already learned. In effect, the cloaked wolf loses the
bonus feat in exchange for the new one. She can only change the most recent bonus feat gained.
Whenever she gains a new bonus feat, the previous bonus feat becomes set and cannot be changed
again. A cloaked wolf can change her most recent bonus feat a number of times per day equal to her
Wisdom modifier (minimum 1).

This ability replaces solo tactics and teamwork feats.
