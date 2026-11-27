+++
id = "ref/arc-skald/boaster"
kind = "archetype"
title = "Boaster"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Boaster"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "boaster", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "84"

[fields]
kind = "archetype"
features = [
  { anchor = "endurance", level = 1 },
  { anchor = "song-of-endurance", level = 3 },
  { anchor = "song-of-surmounting", level = 7 },
  { anchor = "frightful-boast", level = 14 },
  { anchor = "rage-power", level = 4 },
  { anchor = "greater-endurance", level = 6 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["endurance"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["song-of-endurance"] },
  { replaces = "Lore master", feature = "lore-master", by = ["song-of-surmounting"] },
  { replaces = "Song of the fallen", feature = "song-of-the-fallen", by = ["frightful-boast"] },
  { replaces = "Rage power gained at 6th level", feature = "rage-powers", levels = [6], by = ["greater-endurance"] },
  { alters = "Song of marching", feature = "song-of-marching", by = ["song-of-endurance"] },
  { alters = "Rage powers", feature = "rage-powers", by = ["rage-power"] },
]
+++

Boasters use incredible tales and claims to challenge themselves and their allies to accomplish
remarkable feats. With a properly delivered boast, a boaster can inspire listeners to attempt, and
more often than not, succeed at stunts or tasks they may not have realized they were capable of
doing.

## Endurance {#endurance}

The boaster gains [Endurance](ref/feat/endurance) as a bonus feat.

This replaces Scribe Scroll.

## Raging Song (Su) {#raging-song}

A boaster gains access to the following raging songs.

## Song of Endurance (Su) {#song-of-endurance}

At 3rd level, the boaster's raging song can inspire his allies to great feats of endurance. This
raging song functions as song of marching except affected allies also gain the benefits of the
Endurance feat in addition to the benefits of any of the following feats the boaster has (even if
they don't meet the prerequisites): [Deathless Initiate](ref/feat/deathless-initiate),
[Deathless Master](ref/feat/deathless-master), [Deathless Zealot](ref/feat/deathless-zealot),
[Diehard](ref/feat/diehard), [Fast Healer](ref/feat/fast-healer),
[Heroic Defiance](ref/feat/heroic-defiance), and [Heroic Recovery](ref/feat/heroic-recovery).

This raging song replaces uncanny dodge and alters song of marching.

## Song of Surmounting (Su) {#song-of-surmounting}

At 7th level, the boaster's raging song can inspire allies to move quickly and easily. By spending 1
round of raging song, the boaster can affect all allies within 90 feet for 1 hour. Affected allies
gain a benefit according to the surrounding terrain (the benefits don't stack): a climb speed equal
to half their base speed (forest, jungle, mountain, underground), a swim speed equal to their base
speed (swamp, water), or a +10 foot enhancement bonus to their base speed (cold, desert, hill,
plains, or urban). The skald must continue to perform the song for the remainder of the hour;
otherwise, its effects end, but only 1 round of raging song is expended for that hour. At 13th
level, the speed or bonus granted by this ability doubles. At 19th level, this ability grants triple
the listed speed or bonus.

This raging song replaces lore master.

## Frightful Boast (Su) {#frightful-boast}

At 14th level, the boaster's raging song can frighten foes, as per the
[frightening tune](ref/performance/frightening-tune) bardic performance.

This replaces song of the fallen.

## Rage Power (Ex) {#rage-power}

The boaster does not gain this ability until 4th level.

This alters the skald's rage powers.

## Greater Endurance {#greater-endurance}

At 6th level, the boaster gains a bonus feat that he qualifies for. The feat must have Endurance as
a prerequisite (such as Diehard or Fast Healer).

This replaces the rage power gained at 6th level.

## Rage Powers {#rage-powers}

The following rage powers complement the boaster archetype: boasting taunt, come and get me,
fearless rage, fierce fortitude, intimidating glare, raging climber, raging flier, raging leaper,
raging swimmer, sprint, strength surge, and swift foot.
