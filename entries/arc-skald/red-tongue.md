+++
id = "ref/arc-skald/red-tongue"
kind = "archetype"
title = "Red Tongue"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Red%20Tongue"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "red_tongue", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "great-orator", level = 1 },
  { anchor = "seed-of-discord" },
  { anchor = "rile", level = 1 },
  { anchor = "rogue-talents", level = 7 },
  { anchor = "duplicitous-rhetoric", level = 7 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["rile"] },
  { replaces = "Versatile performance selections normally gained at 7th, 12th, and 17th levels", feature = "versatile-performance", levels = [7, 12, 17], by = ["rogue-talents"] },
  { alters = "Raging song", feature = "raging-song", by = ["great-orator"] },
  { alters = "versatile performance", feature = "versatile-performance", by = ["great-orator"] },
]
+++

In the young tengu nation of Kwanlai, politicos argue endlessly over how best to rule and guide a
people who have been parasites and vassals to other nations for millennia. The tengu tendency toward
dramatic flourishes and rhetoric only complicates this debate, creating an environment in which
political clubs led by hot-blooded firebrands—referred to as red tongues in polite company—dominate
the political scene by swaying emotions in the moment and wielding magic in the shadows. Many
political debates in Hisuikarasu end in violent brawls or daring duels.

## Great Orator {#great-orator}

A red tongue can activate his raging song performances only by using the Perform (oratory) skill. He
must select Perform (oratory) as his versatile performance choice at 2nd level.

This ability modifies the raging song and versatile performance abilities.

## Seed of Discord (Su) {#seed-of-discord}

The fiery outlook of the red tongue imparts instinctual knowledge to invest arcane energy into his
proclamations and denouncements. The red tongue gains the following bonus spells known as he reaches
the appropriate level to cast each spell: _doom_ (1st), _castigate_ (2nd), _charm monster_ (3rd),
_denounce_ (4th), _greater command_ (5th), _mass eagle's splendor_ (6th).

## Rile (Ex) {#rile}

The red tongue is particularly skilled at provoking others to action, even when ignorant on a
subject. He adds 1/2 his skald level on Bluff checks to deceive or conceal his motives and on
Intimidate checks to improve a creature's attitude.

This ability replaces bardic knowledge.

## Rogue Talents (Ex) {#rogue-talents}

At 7th level, the red tongue learns a rogue talent of his choice, treating his skald level as his
rogue level. He cannot select a talent that requires or modifies a class feature he does not have
(such as sneak attack), and he must meet all other prerequisites. For every 5 skald levels beyond
7th, he gains a new rogue talent.

This ability replaces the versatile performance selections normally gained at 7th, 12th, and 17th
levels.

## Duplicitous Rhetoric (Su) {#duplicitous-rhetoric}

At 7th level, when a red tongue begins a raging song, he can select a single rogue talent he knows
and grant it to all creatures under the influence of his inspired rage. If a rogue talent is limited
to a certain number of uses per day, each creature affected is limited to a single use and cannot
gain additional uses from a raging song for 24 hours, even if the red tongue ends his raging song
and starts again.
