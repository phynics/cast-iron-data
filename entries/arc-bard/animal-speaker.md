+++
id = "ref/arc-bard/animal-speaker"
kind = "archetype"
title = "Animal Speaker"
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
replaces = ["Fascinate", "Well-versed", "Inspire competence", "Suggestion", "Mass suggestion"]
+++

An animal speaker focuses not on the ears and minds of humans, but on the creatures of the wild and
those in the underbellies of cities.

**Animal Friend**

**Choice:** An animal speaker selects a particular kind of animal, such as apes, badgers, bears,
boars, cats, snakes, and so on.

**Passive:** The bard gains a +4 bonus on Handle Animal checks to influence animals of his chosen
kind. Animals of this kind have a starting attitude of at least &quot&indifferent&quot& toward the
bard and never attack him unless he attacks them first.

**Replaces:** Fascinate

**Special:** Animal companions and magically controlled animals of the bard's chosen kind can be
directed to attack the bard if the controlling creature wins an opposed Charisma check against the
bard (this check can be made once per round until it succeeds, after which no further checks are
needed). Supernatural versions of animals (such as animals with the
[fiendish](ref/template/fiendish) template) can attempt an opposed Charisma check against the bard
with a +4 bonus on its roll to overcome this hesitation. This ability has no effect on creatures
other than animals.

**Nature's Speaker**

**At 11th Level:** The animal speaker selects a third kind of _animal friend._

**At 17th Level:** The animal speaker selects a fourth kind of _animal friend._

**At 5th Level:** The animal speaker selects a second kind of _animal friend._

**Replaces:** Well-versed

**Special:** The bard can use [speak with animals](ref/spell/speak-with-animals) at will on animals
of his selected kinds.

**Bardic Performance**

**Ability:** An animal speaker gains the following types of bardic performance.

**Soothing Performance**

**Ability:** An animal speaker can use bardic performance to influence animals. This works like the
druid ability [wild empathy](ref/ability/wild-empathy), except he expends 1 round of bardic
performance and makes a Perform check. If the bard already has wild empathy from another class, he
adds the class levels that provide wild empathy to the result of his Perform check to influence an
animal.

**Gained:** At 3rd Level

**Replaces:** Inspire competence

**Attract Rats**

**Ability:** The animal speaker can use bardic performance to summon 1d3
[rat swarms](ref/monster/rat-rat-swarm); they remain as long as he continues performing.

**At 11th Level:** He summons 2d3 swarms instead of 1d3 and the swarms have the
[advanced](ref/template/advanced) creature simple template.

**At 17th Level:** The number of swarms he summons increases to 3d3.

**Gained:** At 6th Level

**Replaces:** Suggestion

**Summon Nature's Ally**

**Ability:** At 1st level, the animal speaker adds
[summon nature's ally I](ref/spell/summon-natures-ally-1) to his bard spell list and bard spells
known as a 1st-level spell. At 4th level, he adds
[summon nature's ally II](ref/spell/summon-natures-ally-2) to his spell list and spells known as a
2nd-level spell, and so on every 3 levels thereafter, until 16th level when he adds
[summon nature's ally VI](ref/spell/summon-natures-ally-6) to his 6th-level spell list and spells
known.

**Replaces:** Mass suggestion
