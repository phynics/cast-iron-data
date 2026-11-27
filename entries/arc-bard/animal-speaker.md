+++
id = "ref/arc-bard/animal-speaker"
kind = "archetype"
title = "Animal Speaker"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Animal%20Speaker"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animal_speaker", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-magic"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "animal-friend", level = 1 },
  { anchor = "nature-s-speaker", level = 5 },
  { anchor = "soothing-performance", level = 3 },
  { anchor = "attract-rats", level = 6 },
  { anchor = "summon-nature-s-ally", level = 1 },
]
trades = [
  { replaces = "Fascinate", feature = "bardic-performance", power = "fascinate", by = ["animal-friend"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["nature-s-speaker"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["soothing-performance"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["attract-rats"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["summon-nature-s-ally"] },
]
+++

An animal speaker focuses not on the ears and minds of humans, but on the creatures of the wild and
those in the underbellies of cities.

## Animal Friend {#animal-friend}

An animal speaker selects a particular kind of animal, such as apes, badgers, bears, boars, cats,
snakes, and so on. The bard gains a +4 bonus on Handle Animal checks to influence animals of his
chosen kind. Animals of this kind have a starting attitude of at least "indifferent" toward the bard
and never attack him unless he attacks them first.

Animal companions and magically controlled animals of the bard's chosen kind can be directed to
attack the bard if the controlling creature wins an opposed Charisma check against the bard (this
check can be made once per round until it succeeds, after which no further checks are needed).
Supernatural versions of animals (such as animals with the [fiendish](ref/template/fiendish)
template) can attempt an opposed Charisma check against the bard with a +4 bonus on its roll to
overcome this hesitation. This ability has no effect on creatures other than animals. This ability
replaces fascinate.

## Nature's Speaker {#nature-s-speaker}

At 5th, 11th, and 17th level, the animal speaker selects another kind of animal friend. The bard can
use _[speak with animals](ref/spell/speak-with-animals)_ at will on animals of his selected kinds.
This ability replaces well-versed.

## Bardic Performance {#bardic-performance}

An animal speaker gains the following types of bardic performance.

## Soothing Performance {#soothing-performance}

At 3rd level, an animal speaker can use bardic performance to influence animals. This works like the
druid ability [wild empathy](ref/ability/wild-empathy), except he expends 1 round of bardic
performance and makes a Perform check. If the bard already has wild empathy from another class, he
adds the class levels that provide wild empathy to the result of his Perform check to influence an
animal. This ability replaces inspire competence.

## Attract Rats {#attract-rats}

At 6th level, the animal speaker can use bardic performance to summon 1d3
[rat swarms](ref/monster/rat-rat-swarm); they remain as long as he continues performing. At 11th
level, he summons 2d3 swarms instead of 1d3 and the swarms have the
[advanced](ref/template/advanced) creature simple template. At 17th level, the number of swarms he
summons increases to 3d3. This ability replaces _suggestion_.

## Summon Nature's Ally {#summon-nature-s-ally}

At 1st level, the animal speaker adds _[summon nature's ally I](ref/spell/summon-natures-ally-1)_ to
his bard spell list and bard spells known as a 1st-level spell. At 4th level (when he gains access
to 2nd-level spells) he adds _[summon nature's ally II](ref/spell/summon-natures-ally-2)_ to his
spell list and spells known as a 2nd-level spell, and so on every 3 levels thereafter, until 16th
level when he adds _[summon nature's ally VI](ref/spell/summon-natures-ally-6)_ to his 6th-level
spell list and spells known. This replaces mass suggestion.
