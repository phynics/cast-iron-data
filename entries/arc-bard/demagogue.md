+++
id = "ref/arc-bard/demagogue"
kind = "archetype"
title = "Demagogue"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Demagogue"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "demagogue", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-magic"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "famous", level = 1 },
  { anchor = "bardic-performance" },
  { anchor = "gather-crowd", level = 5 },
  { anchor = "incite-violence", level = 6 },
  { anchor = "righteous-cause", level = 18 },
]
trades = [
  { replaces = "Inspire courage +1", feature = "bardic-performance", levels = [1], power = "inspire courage", by = ["famous"] },
  { replaces = "Lore master", feature = "lore-master", by = ["gather-crowd"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["incite-violence"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["righteous-cause"] },
]
+++

Not content with providing amusing and occasionally instructive performances, the demagogue seeks to
inflame and ignite his audience, driving them toward a specific purpose with carefully chosen words
and tones that may spark momentous change.

## Famous {#famous}

At 1st level, a demagogue is famous in a particular region. This works like the famous ability of
the celebrity bard archetype, except the demagogue's skill bonuses apply to Bluff and Intimidate
instead of Diplomacy and Intimidate. This ability replaces inspire courage +1.

## Bardic Performance {#bardic-performance}

A demagogue gains the following type of bardic performance.

## Gather Crowd (Ex) {#gather-crowd}

At 5th level, the demagogue gains the ability to quickly gather a crowd. This is identical to the
gather crowd ability of the celebrity bard archetype. This ability replaces lore master.

## Incite Violence (Ex) {#incite-violence}

At 6th level, the demagogue can use his performance to fan the fury of a crowd of people he has
fascinated. Using this ability does not disrupt the fascinate effect, but does require a standard
action to activate (in addition to the free action to continue the fascinate effect). The bard
selects a number of targets equal to his level, who must make Will saves (DC 10 + 1/2 the bard's
level + the bard's Charisma modifier) or be affected by _[rage](ref/spell/rage)_ for a number of
rounds equal to the bard's level. The bard indicates who is the intended target of violence (either
after using this ability or as part of the performance leading to it) and the enraged members of the
crowd immediately attack the target if possible. The target does not need to be present ("kill the
king" is a suitable choice) and can be an object instead of a person ("destroy the prison!" is
likewise appropriate). Other members of the crowd may follow suit, though they do not gain the
benefits of _rage_. This is a sound-based effect and is affected by countersong. If two or more
bards are attempting to direct the crowd against different targets, they must make opposed Charisma
checks, with the crowd following the directions of the winner. This ability replaces suggestion.

## Righteous Cause (Ex) {#righteous-cause}

At 18th level, the demagogue can lift a crowd's emotions and turn them toward a common purpose.
First, he must fascinate the crowd, and then use incite violence without designating a target, at
which point he can use righteous cause. Instead of driving the crowd with anger, he fills them with
purpose. Fascinated creatures must make Will saves (DC 10 + 1/2 the bard's level + the bard's
Charisma modifier) to resist. Those who fail are affected by
_[mass suggestion](ref/spell/suggestion-mass)_ of a plausible idea that lingers with them for one
day. Typical uses of this ability are to spark rebellion, overthrow a king, build a beneficial
structure such as an orphanage, or donate money to a cause. This ability replaces mass suggestion.
