+++
id = "ref/arc-hunter/chameleon-adept"
kind = "archetype"
title = "Chameleon Adept"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Chameleon%20Adept"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chameleon_adept", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "52"

[fields]
kind = "archetype"
features = [
  { anchor = "shifting-companion", level = 3 },
  { anchor = "terrain-chameleon", level = 1 },
  { anchor = "savage-diplomacy", level = 2 },
  { anchor = "animal-shape", level = 5 },
  { anchor = "improved-shifting-companion", level = 10 },
  { anchor = "one-with-the-wild", level = 17 },
]
trades = [
  { replaces = "Teamwork feats", feature = "teamwork-feat", by = ["shifting-companion"] },
  { replaces = "hunter's tactics", feature = "hunter-tactics", by = ["shifting-companion"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["terrain-chameleon"] },
  { replaces = "Precise companion", feature = "precise-companion", by = ["savage-diplomacy"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["animal-shape"] },
  { replaces = "Raise animal companion", feature = "raise-animal-companion", by = ["improved-shifting-companion"] },
  { alters = "One with the wild", feature = "one-with-the-wild", by = ["one-with-the-wild"] },
]
+++

Some hunters are masters of blending into every situation, even making their companions appear
humanoid for brief periods of time.

## Skills {#skills}

A chameleon adept adds Diplomacy to her list of class skills.

This alters the hunter's class skills.

## Shifting Companion (Su) {#shifting-companion}

At 3rd level as a standard action, a chameleon adept can cause her companion to assume a humanoid
form of the same race as herself. This functions as _[alter self](ref/spell/alter-self)_, except it
is used on an adjacent animal companion to have it assume a humanoid form. The companion always
assumes the same form, selected when the hunter reaches 3rd level. The hunter can change this form
when she gains a new level, but the companion loses the old form and can't resume it unless the
chameleon adept chooses that form when she reaches a new level. The companion is no more intelligent
or less savage than normal; the hunter still needs to control it as normal, and it still can't
activate magic items or wield manufactured weapons. The hunter can use this ability for 10 minutes
per day per hunter level. This duration does not need to be consecutive, but it must be spent in
10-minute increments.

This replaces teamwork feats and hunter's tactics.

## Terrain Chameleon (Su) {#terrain-chameleon}

Choose one type of terrain from the ranger's list of
[favored terrains](ref/ability/favored-terrain). When in the specified type of terrain, a chameleon
adept gains a bonus equal to [half](ref/misc/fractions-and-rounding) her hunter level on Stealth
checks.

This replaces wild empathy.

## Savage Diplomacy (Ex) {#savage-diplomacy}

At 2nd level, while in humanoid form, a chameleon adept's animal companion grants its master a +2
circumstance bonus on Diplomacy and Intimidate checks. Savage diplomacy functions only as long as
the creature being influenced can see both the companion and the master. This bonus increases by 1
at 5th level and every 4 levels thereafter, to a maximum of +6 at 17th level.

This replaces precise companion.

## Animal Shape (Su) {#animal-shape}

At 5th level as a standard action, a chameleon adept can assume a form superficially identical to
her animal companion's animal form. She gains no bonuses or natural attacks while in this form, only
forms of movement. Her size category does not change. This is a polymorph effect. She can assume
this form for 1 minute per level per day, in 1-minute increments. She can dismiss this ability at
any point as a standard action.

This replaces woodland stride.

## Improved Shifting Companion (Su) {#improved-shifting-companion}

At 10th level, a chameleon adept's animal companion improves its ability to change shape. It can use
wild shape, as a [druid](ref/class/druid) of half the hunter's level, to gain the effects of
_[beast shape I](ref/spell/beast-shape-1)_. Unlike a druid's wild shape, this ability does not
improve to encompass larger or smaller animals or elementals.

This replaces raise animal companion.

## One with the Wild (Ex) {#one-with-the-wild}

At 17th level, when the companion is using wild shape to appear as a different type of animal, it
counts as being in that animal focus for the purpose of one with the wild.

This alters one with the wild.
