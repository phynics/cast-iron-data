+++
id = "ref/arc-bard/luring-piper"
kind = "archetype"
title = "Luring Piper"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Luring%20Piper"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "luring_piper", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "fey-secrets", level = 1 },
  { anchor = "luring-presentation" },
  { anchor = "bardic-performance", level = 1 },
  { anchor = "charming-melody", level = 1 },
  { anchor = "deadly-lure", level = 8 },
  { anchor = "fey-wounding-song", level = 12 },
  { anchor = "piper-s-attention", level = 2 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["fey-secrets"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["deadly-lure"] },
  { replaces = "Soothing performance", feature = "bardic-performance", power = "soothing performance", by = ["fey-wounding-song"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["piper-s-attention"] },
  { alters = "Bardic performance", feature = "bardic-performance", by = ["bardic-performance"] },
  { alters = "Fascinate", feature = "bardic-performance", power = "fascinate", by = ["charming-melody"] },
  { alters = "Class skills" },
]
+++

Some bards have an exceptional ability to use their musical performances to entrance the world's
wilder creatures. These performers are so focused that they create melodies capable of leading
animals and fey to their unwilling death.

## Class Skills {#class-skills}

A luring piper gains Survival as a class skill.

This alters the bard's class skills.

## Fey Secrets {#fey-secrets}

A luring piper adds [half](ref/misc/fractions-and-rounding) his class level (minimum 1) on Bluff,
Knowledge (nature), Perception, Sense Motive, and Survival checks when interacting with fey.

This ability replaces bardic knowledge.

## Luring Presentation (Ex) {#luring-presentation}

Creatures that have the animal or fey type take a -2 penalty on saving throws imposed by a luring
piper's bardic performances. Creatures with any other type gain a +2 bonus on saving throws against
a luring piper's bardic performances.

This ability modifies bardic performance.

## Bardic Performance {#bardic-performance}

The luring piper gains the following types of bardic performances that can only be made when using
Perform (wind instruments) and when employing a wind instrument.

## Charming Melody (Su) {#charming-melody}

While using the [fascinate](ref/performance/fascinate) bardic performance, the luring piper can play
a song that compels animals and fey to follow him wherever he goes. Instead of sitting peacefully
and merely observing the luring piper, creatures with the animal or fey type instead quietly and
calmly walk toward the luring piper, stopping once they are adjacent to the luring piper and
following him if he moves.

This performance modifies fascinate.

## Deadly Lure (Sp) {#deadly-lure}

At 8th level, the luring piper can use his [suggestion](ref/performance/suggestion) bardic
performance on targeted animals and fey to make them take actions that result in their own injury or
death, such as leaping off a cliff or into a river. The targeted creature is allowed a second saving
throw to shake off the effect before completing any self-harming actions.

This performance replaces the bard's dirge of doom.

## Fey-Wounding Song (Sp) {#fey-wounding-song}

At 12th level as a full-round action, the luring piper can expend 3 rounds of bardic performance to
play a song that causes fey tremendous pain. Treat this as equivalent to
_[mass inflict serious wounds](ref/spell/inflict-serious-wounds-mass)_, but affecting only fey
targets and using the lurid piper's bard level as his caster level.

This performance replaces soothing performance.

## Piper's Attention (Ex) {#piper-s-attention}

Starting at 2nd level, whenever a luring piper is actively using Perform (wind instruments) as part
of a bardic performance, he gains a +4 bonus on saving throws against language-dependent,
mind-affecting, and sonic effects. If this effect is caused by a fey creature, the luring piper can
also roll the saving throw twice and take the better result.

This ability replaces well-versed.
