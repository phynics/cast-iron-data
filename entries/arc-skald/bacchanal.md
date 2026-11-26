+++
id = "ref/arc-skald/bacchanal"
kind = "archetype"
title = "Bacchanal"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Bacchanal"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bacchanal", path = "json/archetypes_skald.json" },
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
  { anchor = "fermented-fruit", level = 1 },
  { anchor = "drunken-dancer", level = 2 },
  { anchor = "raging-song" },
  { anchor = "song-of-urging", level = 3 },
  { anchor = "maddening-dance", level = 10 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["fermented-fruit"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["drunken-dancer"] },
  { replaces = "Song of marching", feature = "song-of-marching", by = ["song-of-urging"] },
  { replaces = "Dirge of doom", feature = "dirge-of-doom", by = ["maddening-dance"] },
]
+++

Bacchanals are skalds who use ecstatic dancing and ribald songs to influence the primal instincts of
listeners. To these skalds, the passionate frenzy of a celebration or feast shares many features
with the violence of combat, and several of their talents blur the line between festival and battle
in dramatic ways.

## Fermented Fruit (Sp) {#fermented-fruit}

A bacchanal adds _[goodberry](ref/spell/goodberry)_ to his list of 1st-level skald spells known. In
addition, he can cast it as a [spell-like ability](ref/umr/spell-like-abilities) once per day. When
he casts _[goodberry](ref/spell/goodberry)_ as a spell or spell-like ability, the targeted berries
ferment; this causes each berry to act as a serving of an alcoholic beverage. A creature that eats a
fermented berry does not gain a meal's nourishment, but it is cured of 1 point of damage and becomes
slightly foolhardy as if tipsy, gaining a +1 bonus on saves against fear effects for 1 minute after
eating the berry.

This replaces Scribe Scroll.

## Drunken Dancer (Su) {#drunken-dancer}

At 2nd level, while maintaining a raging song, a bacchanal can consume a berry affected by
_[goodberry](ref/spell/goodberry)_, a potion, or a serving of alcohol as a move action that does not
provoke attacks of opportunity. A berry affected by _[goodberry](ref/spell/goodberry)_ or a potion
has its normal effect, while an alcoholic drink or a berry affected by
_[goodberry](ref/spell/goodberry)_ via fermented fruit (see above) allows the skald to maintain his
raging song that round without expending a round of raging song for the day (instead of the normal
effects of the alcohol or fermented berry). For each alcoholic drink or fermented berry consumed
while raging, the skald is [nauseated](ref/misc/nauseated) for 1 round after his raging song ends.
The internal fortitude rage power prevents this nauseated condition from occurring.

At 7th level, when the bacchanal consumes an alcoholic drink or fermented berry while maintaining
his rage song, he can gain the benefits of _[cure light wounds](ref/spell/cure-light-wounds)_ or
_[remove fear](ref/spell/remove-fear)_ (for the duration of the raging song) at his caster level by
spending 2 rounds of raging song. At 12th level, the bacchanal can gain the benefits of
_[heroism](ref/spell/heroism)_ (for the duration of the raging song) in this manner. At 17th level,
he can gain the benefits of _[persistent vigor](ref/spell/persistent-vigor)_ (for the duration of
the raging song) in this manner.

This replaces versatile performance.

## Raging Song (Su) {#raging-song}

A bacchanal gains access to the following raging songs.

## Song of Urging (Su) {#song-of-urging}

At 3rd level, the bacchanal's raging song can wordlessly influence creatures of the wild. This
raging song functions just like a [Diplomacy](ref/skill/diplomacy) check to make a simple request or
an Intimidate check but can influence only animals. The bacchanal rolls 1d20 and adds his skald
level and his Charisma modifier to determine the urging check's result. Bonuses and penalties that
apply to wild empathy checks apply to these urging checks. The typical domestic animal has a
starting attitude of indifferent, while wild animals are usually unfriendly. The song can influence
plants or magical beasts with Intelligence scores of 1 or 2 as well as drunken creatures of any
Intelligence (even without sharing a language), but against these nonanimals, the bacchanal takes a
-4 penalty on this check. The bacchanal must continue to perform the song for the entire time
required for the check; otherwise, its effect is wasted, but only 1 round of raging song is expended
regardless of how long the check takes.

This raging song replaces song of marching.

## Maddening Dance (Su) {#maddening-dance}

At 10th level, the bacchanal's raging song can compel a creature within 30 feet to perform an
ecstatic dance. Unless it succeeds at its Will save, the victim becomes
[confused](ref/misc/confused), takes a -2 penalty to its AC and on Reflex saving throws, and loses
the benefit of any shield it holds. The effect ends when the target can no longer hear the bacchanal
from within 30 feet. As an immediate action, an ally of the bacchanal within 30 feet can dance along
as a full-round action (taking all penalties except the confused condition for that round) to allow
the bacchanal to target an additional creature. A creature that succeeds at the Will saving throw
against this raging song is immune to this effect for 24 hours. This is a compulsion, emotion,
enchantment, and mind-affecting effect.

This raging song replaces dirge of doom.

## Rage Powers {#rage-powers}

The following rage powers complement the bacchanal archetype: animal fury, boasting taunt, fearless
rage, fierce fortitude, increased [damage reduction](ref/rule/damage-reduction), internal fortitude,
liquid courage, night vision, roaring drunk, and staggering drunk.
