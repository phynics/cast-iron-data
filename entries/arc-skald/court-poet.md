+++
id = "ref/arc-skald/court-poet"
kind = "archetype"
title = "Court Poet"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Court%20Poet"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "court_poet", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "insightful-contemplation", level = 1 },
  { anchor = "song-of-inspiration", level = 6 },
  { anchor = "handling-the-crowd", level = 2 },
]
trades = [
  { replaces = "Inspired rage", feature = "inspired-rage", by = ["insightful-contemplation"] },
  { replaces = "Song of strength", feature = "song-of-strength", by = ["song-of-inspiration"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["handling-the-crowd"] },
]
+++

Many courts are places of artistic refinement, attracting those performers who wish to revel in an
aristocratic art scene. Such artists may aim to become a darling of the court, focusing on the
aesthetic requirements of a particular tradition as well as learning details about that court's
history and culture. Court poets elevate the skald's love of history and poetry to an aristocratic
ideal, captivating courts with complicated poetic traditions and inspiring others with their craft.
Some court poets go on to create their own works, weaving their magic and force of personality into
their unique performances.

## Raging Song (Su) {#raging-song}

A court poet gains the following raging songs, allowing her to use oratory, music, and other
performances to elevate the aesthetic sensibilities of her allies.

## Insightful Contemplation (Su) {#insightful-contemplation}

At 1st level, affected allies gain a +2 morale bonus to Intelligence and Charisma and a +1 morale
bonus on Will saving throws, but they also take a -1 penalty to AC. While under the effects of
insightful contemplation, allies other than the court poet can't use any Strength-based skills or
make any physical effort that requires a Constitution check. At 4th level and every 4 skald levels
thereafter, the song's bonus on Will saves increases by 1; the penalty to AC doesn't change. At 8th
and 16th levels, the song's bonuses to Intelligence and Charisma increase by 2. (Unlike the
barbarian's rage ability, those affected are not fatigued after the song ends.)

This ability replaces inspired rage.

## Song of Inspiration (Su) {#song-of-inspiration}

At 6th level, a court poet can use raging song to inspire her allies to greater mental clarity. Once
each round while the court poet uses this performance, allies within 60 feet who can hear her can
add 1/2 the court poet's skald level to a single Wisdom check or Wisdom-based skill check.

This ability replaces song of strength.

## Handling the Crowd (Ex) {#handling-the-crowd}

At 2nd level, a court poet gains a +1 bonus to AC and on Perform checks when adjacent to two or more
creatures. In addition, her movement is not impeded by crowds and she gains a bonus equal to 1/2 her
skald level on Diplomacy checks to influence crowds.

This ability replaces well-versed.
