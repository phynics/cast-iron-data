+++
id = "ref/arc-bard/fey-courtier"
kind = "archetype"
title = "Fey Courtier"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Fey%20Courtier"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fey_courtier", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "scorn-of-the-wilds", level = 8 },
  { anchor = "stone-dance", level = 15 },
  { anchor = "fey-contacts", level = 2 },
  { anchor = "summon-fey-allies", level = 3 },
]
trades = [
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["scorn-of-the-wilds"] },
  { replaces = "frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["scorn-of-the-wilds"] },
  { replaces = "Inspire heroics", feature = "bardic-performance", power = "inspire heroics", by = ["stone-dance"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["fey-contacts"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["summon-fey-allies"] },
]
+++

Fey who associate with courts often become bards skilled at navigating the inhuman societies of the
trackless wilds.

## Bardic Performance {#bardic-performance}

The fey courtier has access to the following bardic performances.

## Scorn of the Wilds (Sp) {#scorn-of-the-wilds}

At 8th level, the fey courtier can use bardic performance to permanently mark a creature with
nature's displeasure by spending 2 rounds performing while the target remains within 30 feet. The
performance includes a litany of the target's misdeeds against fey and nature. Unless the target
succeeds at a Will saving throw (DC = 10 + [half](ref/misc/fractions-and-rounding) the bard's
level + his Charisma modifier), it is cursed as per _[nature's exile](ref/spell/natures-exile)_ or
_[bestow curse](ref/spell/bestow-curse)._ At 14th level, the fey courtier's options expand to
include _[baleful polymorph](ref/spell/baleful-polymorph)_ and
_[green caress](ref/spell/green-caress)_. As part of the performance, the fey courtier must define a
condition under which the curse will be lifted, which must relate to making amends for the crime
against fey or nature and cannot be suicidal to carry out. A creature that succeeds at its saving
throw is immune to the fey courtier's scorn of the wild for 24 hours. This is a curse effect.

This replaces dirge of doom and frightening tune.

## Stone Dance (Sp) {#stone-dance}

At 15th level, the bard's performance can move even the features of the natural world. This
performance functions as _[animate plants](ref/spell/animate-plants)_ (DC = 10 + half the bard's
level + his Charisma modifier) except it can also animate unworked stone and water from natural
bodies of water (with statistics equivalent to an appropriate plant).

This replaces inspire heroics.

## Fey Contacts {#fey-contacts}

At 2nd level, thanks to his fey contacts and knowledge of the byzantine trade customs of the fey
courts, a fey courtier can treat any wilderness area with fey residents as a settlement with a
certain base value and purchase limit based on his bard level for the purpose of buying and selling
magic items. See page 205 of the _Pathfinder RPG GameMastery Guide_ for rules on settlement base
values and purchase limits. The fey courtier can also use these contacts to gather information about
the residents, geography, and nearby areas with Diplomacy.

This replaces versatile performance.

|Bard Level|Base Value|Purchase Limit|
| --- | --- | --- |
|2nd|50 gp|500 gp|
|6th|500 gp|2,500 gp|
|10th|2,000 gp|10,000 gp|
|14th|8,000 gp|50,000 gp|
|18th|32,000 gp|200,000 gp|

## Summon Fey Allies {#summon-fey-allies}

At 3rd level, the fey courtier gains [Augment Summoning](ref/feat/augment-summoning) as a bonus feat
and can call upon natural allies who owe him favors. He adds
_[summon nature's ally I](ref/spell/summon-natures-ally-1)_ to his list of 1st-level bard spells
known. Whenever he gains access to another spell level, he adds the next-higher
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell to his list of bard spells known. The
fey courtier adds the following creatures to the
[summon nature's ally](ref/spell/summon-natures-ally) list:
1st—[grimple (gremlin)](ref/monster/gremlin-grimple), [mite](ref/monster/mite),
[sprite](ref/monster/sprite); 2nd—[atomie](ref/monster/atomie),
[fuath (gremlin)](ref/monster/gremlin-fuath), [nixie](ref/monster/nixie);
3rd—[leprechaun](ref/monster/leprechaun), [nuglub (gremlin)](ref/monster/gremlin-nuglub),
[pooka](ref/monster/pooka); 4th—[kelpie](ref/monster/kelpie), [korred](ref/monster/korred),
[twigjack](ref/monster/twigjack); 5th—[lampad](ref/monster/lampad),
[lurker in light](ref/monster/lurker-in-light), [swan maiden](ref/monster/swan-maiden);
6th—[cold rider](ref/monster/cold-rider), [oceanid](ref/monster/oceanid),
[sangoi](ref/monster/sangoi).

This replaces inspire competence.
