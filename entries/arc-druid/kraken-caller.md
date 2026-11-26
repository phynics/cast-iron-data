+++
id = "ref/arc-druid/kraken-caller"
kind = "archetype"
title = "Kraken Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Kraken%20Caller"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kraken_caller", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "call-of-the-waves" },
  { anchor = "bonus-languages" },
  { anchor = "dauntless-swimmer", level = 2 },
  { anchor = "hold-breath", level = 3 },
  { anchor = "resist-the-waves-lure", level = 4 },
  { anchor = "wild-shape", level = 4 },
  { anchor = "beast-of-the-depths", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["dauntless-swimmer"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["hold-breath"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-the-waves-lure"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["beast-of-the-depths"] },
  { alters = "Bonus languages", feature = "bonus-languages", by = ["bonus-languages"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

Some druids draw upon power irreverently stolen from one of the most dangerous creatures of the
depths: the kraken.

## Call of the Waves (Ex) {#call-of-the-waves}

A kraken caller must choose [Besmara](ref/faith/besmara) as her deity. If she ever changes her
deity, she loses this archetype and becomes a normal druid.

## Bonus Languages {#bonus-languages}

A kraken caller's bonus language options include Aquan instead of Sylvan. This ability alters the
druid's bonus languages class feature.

## Dauntless Swimmer (Ex) {#dauntless-swimmer}

At 2nd level, a kraken caller can always take 10 on Swim checks, even if she is rushed or
threatened. This ability replaces woodland stride.

## Hold Breath (Ex) {#hold-breath}

At 3rd level, a kraken caller can [hold her breath](ref/misc/hold-your-breath) for a number of
minutes equal to her Constitution score before she risks drowning. This ability replaces trackless
step.

## Resist the Waves' Lure (Ex) {#resist-the-waves-lure}

At 4th level, a kraken caller gains a +4 bonus on saving throws against the spell-like and
supernatural abilities of creatures with the aquatic subtype. This ability replaces resist nature's
lure.

## Wild Shape (Su) {#wild-shape}

A kraken caller's options for wild shape are limited to animals with the aquatic or water subtype or
that have the amphibious special quality. The kraken caller can alternatively expend a daily use of
wild shape to grow tentacles out of her body while otherwise retaining her own form. This effect
lasts for 10 minutes per level, or until the kraken caller changes back.

At 4th level, the kraken caller grows two tentacles while in this form. The tentacles have a reach
of 5 feet regardless of the kraken caller's size, and the kraken caller can use them as secondary
[natural attacks](ref/umr/natural-attacks) that deal 1d4 points of damage (1d3 for a Small kraken
caller). She also gains a racial bonus on Climb, Swim, and [dirty trick](ref/rule/dirty-trick)
combat maneuver checks equal to the number of tentacles grown.

At each of 6th, 8th, 10th, and 12th levels, a kraken caller can grow an additional tentacle. As a
move action, she can retract or regrow any number of the additional tentacles, redistributing the
mass of any retracted tentacles. For every 2 retracted tentacles, she can increase the reach of the
remaining tentacles by 5 feet (to a maximum of 15 feet), or increase the damage dealt by her
tentacles as if she were [one size category larger](ref/misc/damage-die-adjustments).

While in this form, a kraken caller can expel a 10-foot-radius cloud of ink once per minute as a
standard action. This cloud provides [total concealment](ref/rule/concealment) in water and persists
for 1 round per level. The ink has no effect out of water. This ability alters wild shape.

## Beast of the Depths (Su) {#beast-of-the-depths}

At 13th level, a kraken caller gains a swim speed equal to her base land speed and can breathe water
as though affected by the spell _[water breathing](ref/spell/water-breathing)_. This ability
replaces a thousand faces.
