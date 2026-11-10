+++
id = "ref/arc-bard/luring-piper"
kind = "archetype"
title = "Luring Piper"
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
replaces = ["Bardic knowledge", "Dirge of doom", "Soothing performance", "Well-versed"]
alters = ["Bardic performance", "Fascinate"]
replaces_features = ["bardic-knowledge", "well-versed"]
alters_features = ["bardic-performance"]
+++

Some bards have an exceptional ability to use their musical performances to entrance the world's
wilder creatures. These performers are so focused that they create melodies capable of leading
animals and fey to their unwilling death.

**Gained class skills:** sur

**Fey Secrets**

**Passive:** A luring piper adds [half](ref/misc/fractions-and-rounding) his class level (minimum 1)
on Bluff, Knowledge (nature), Perception, Sense Motive, and Survival checks when interacting with
fey.

**Replaces:** Bardic knowledge

**Luring Presentation (Ex)**

**Alters:** Bardic performance

**Passive:** Creatures that have the animal or fey type take a -2 penalty on saving throws imposed
by a luring piper's bardic performances. Creatures with any other type gain a +2 bonus on saving
throws against a luring piper's bardic performances.

**Bardic Performance**

**Info:** The luring piper gains the following types of bardic performances that can only be made
when using Perform (wind) and a when employing a wind instrument.

**Charming Melody (Su)**

**Ability:** While using the [fascinate](ref/performance/fascinate) bardic performance, the luring
piper can play a song that compels animals and fey to follow him wherever he goes. Instead of
sitting peacefully and merely observing the luring piper, creatures with the animal or fey type
instead quietly and calmly walk toward the luring piper, stopping once they are adjacent to the
luring piper and following him if he moves.

**Alters:** Fascinate

**Deadly Lure (Sp)**

**Ability:** The luring piper can use his [suggestion](ref/performance/suggestion) bardic
performance on targeted animals and fey to make them take actions that result in their own injury or
death, such as leaping off a cliff or into a river. The targeted creature is allowed a second saving
throw to shake off the effect before completing any self-harming actions.

**Gained:** At 8th Level

**Replaces:** Dirge of doom

**Fey-Wounding Song (Sp)**

**Fullround:** The luring piper can expend 3 rounds of bardic performance to play a song that causes
fey tremendous pain. Treat this as equivalent to
[mass inflict serious wounds](ref/spell/inflict-serious-wounds-mass), but affecting only fey targets
and using the lurid piper's bard level as his caster level.

**Gained:** At 12th Level

**Replaces:** Soothing performance

**Piper's Attention (Ex)**

**Gained:** At 2nd Level

**Passive:** Whenever a luring piper is actively using Perform (wind) as part of a bardic
performance, he gains a +4 bonus on saving throws against language-dependent, mind-affecting, and
sonic effects. If this effect is caused by a fey creature, the luring piper can also roll the saving
throw twice and take the better result.

**Replaces:** Well-versed
