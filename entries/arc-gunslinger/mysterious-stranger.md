+++
id = "ref/arc-gunslinger/mysterious-stranger"
kind = "archetype"
title = "Mysterious Stranger"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Mysterious%20Stranger"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mysterious_stranger", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "ultimate-combat"
page = "51"

[fields]
kind = "archetype"
features = [
  { anchor = "grit" },
  { anchor = "deeds" },
  { anchor = "focused-aim", level = 1 },
  { anchor = "clipping-shot", level = 11 },
  { anchor = "lucky", level = 2 },
  { anchor = "stranger-s-fortune", level = 5 },
]
trades = [
  { replaces = "Quick clear deed", feature = "deeds", power = "quick clear", by = ["focused-aim"] },
  { replaces = "Bleeding wound deed", feature = "deeds", power = "bleeding wound", by = ["clipping-shot"] },
  { replaces = "Nimble", feature = "nimble", by = ["lucky"] },
  { replaces = "Gun training 1", feature = "gun-training", levels = [5], by = ["stranger-s-fortune"] },
  { alters = "Grit", feature = "grit", by = ["grit"] },
]
+++

Gunslingers use a potent mixture of common sense and manual dexterity in order to control the fickle
power of their weapons. But a few rare gunslingers seem to accomplish their chosen tasks purely
through willpower and an unwillingness to ever give up. These mysterious strangers use their force
of personality to keep going when the chips are down, often moving on from a region as soon as they
accomplish their goals—hence the name.

## Grit (Ex) {#grit}

A mysterious stranger is a force to be reckoned with. Instead of using her Wisdom to determine the
number of grit points she gains at the start of each day, she uses Charisma. This ability works in
all other ways like the gunslinger's grit class feature.

## Deeds {#deeds}

A mysterious stranger swaps a pair of deeds for the following.

## Focused Aim (Ex) {#focused-aim}

At 1st level, as a swift action, the mysterious stranger can spend 1 grit point to gain a bonus on
all firearm damage rolls equal to her Charisma modifier (minimum 1) with all firearm attacks she
makes until the end of her turn. At 7th level, when she uses the [dead shot](ref/deed/dead-shot)
deed, she multiplies this bonus by the number of hits she made while rolling the Dead Shot attack.
This deed replaces the quick clear deed.

## Clipping Shot (Ex) {#clipping-shot}

At 11th level, when the mysterious stranger misses with a firearm attack, she can spend 1 grit point
to deal half the damage that attack would have dealt if it were a hit (roll damage normally). She
can decide to use this deed and spend the grit point after making the attack. This deed has no
effect if the attack used the dead shot deed. The cost of using this deed cannot be reduced with the
[Signature Deed](ref/feat/signature-deed) feat, the true grit class feature, or any similar effect.
This replaces the bleeding wound deed.

## Lucky (Ex) {#lucky}

Starting at 2nd level, a mysterious stranger gains a +1 luck bonus on Will saving throws. This bonus
increases by +1 for every four levels beyond 2nd level (to a maximum of +5 at 18th level). This
ability replaces nimble.

## Stranger's Fortune (Ex) {#stranger-s-fortune}

Starting at 5th level, a mysterious stranger can ignore a firearm misfire a number of times per day
equal to her Charisma bonus. She can use this ability as a free action. This ability replaces gun
training 1.
