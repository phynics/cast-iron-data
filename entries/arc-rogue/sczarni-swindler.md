+++
id = "ref/arc-rogue/sczarni-swindler"
kind = "archetype"
title = "Sczarni Swindler"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Sczarni%20Swindler"
source_ids = ["the-harrow-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sczarni_swindler", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "the-harrow-handbook"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "let-fate-decide", level = 1 },
  { anchor = "quicker-than-the-eye", level = 2 },
  { anchor = "poker-face", level = 3 },
  { anchor = "no-fool", level = 4 },
  { anchor = "cheat-fate", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["let-fate-decide"] },
  { replaces = "Evasion", feature = "evasion", by = ["quicker-than-the-eye"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["poker-face"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["no-fool"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["cheat-fate"] },
]
+++

If life is a game, the Sczarni play to win. When skill and luck aren't enough, cheating is often the
best option.

## Let Fate Decide (Ex) {#let-fate-decide}

At 1st level, the Sczarni swindler can declare two different actions that rely on different types of
rolls or checks, such as attacking a creature (an attack roll) or sneaking past the same creature (a
Stealth check). As a standard action, the swindler then uses a random method to choose one of the
declared activities, such as flipping a coin, rolling a die, or drawing a harrow card. The specific
method doesn't matter as long as there is an equal chance of either activity being chosen. If the
swindler then performs the chosen activity within the next round, she gains a luck bonus on the roll
type required for that activity—attack rolls with a specific weapon, a specific skill check, a
specific ability check, or a specific saving throw—equal to half her rogue level (minimum +1) for 1
minute. If the swindler performs any other action (whether declared or not) in the round after using
this ability, she becomes [shaken](ref/misc/shaken) for 1 minute instead. The swindler can use this
ability a number of times per day equal to 3 + her Charisma modifier. This ability replaces
trapfinding.

## Quicker Than the Eye (Ex) {#quicker-than-the-eye}

At 2nd level, when the Sczarni swindler uses [Sleight of Hand](ref/skill/sleight-of-hand), creatures
take a penalty on their Perception checks equal to half the swindler's class level to notice the
attempt. The swindler also reduces the normal -20 penalty by an amount equal to her class level when
attempting a Sleight of Hand check as a move action instead of as a standard action. Lastly, the
swindler can draw hidden weapons or objects from her person as a move action instead of the usual
standard action. This ability replaces evasion.

## Poker Face (Ex) {#poker-face}

At 3rd level, the Sczarni swindler gains a +1 bonus on Bluff, Profession (gambler), and Sense Motive
checks. This bonus increases by 1 for every 3 levels beyond 3rd. The Sczarni swindler can also
attempt to feint against non-humanoid targets without penalty, though she still takes a -8 penalty
on feint attempts against creatures with animal intelligence and she cannot feint against mindless
creatures. This ability replaces trap sense.

## No Fool (Ex) {#no-fool}

At 4th level, the Sczarni swindler gains a +1 bonus on Will saving throws. This bonus increases by 1
for every 4 levels beyond 4th (to a maximum of +5 at 20th level). This ability replaces uncanny
dodge.

## Cheat Fate (Ex) {#cheat-fate}

At 8th level, once per day, the Sczarni swindler can reroll any one d20 roll she has just made
before the GM has revealed the result. She must take the result of the second roll, even if it is
worse. The swindler can use this ability twice per day at 14th level, and three times per day at
20th. This ability replaces improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the Sczarni swindler archetype: canny observer, fast fingers,
hard to fool, honeyed words, major magic, and minor magic.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the Sczarni swindler archetype: master of disguise,
skill mastery, and slippery mind.
