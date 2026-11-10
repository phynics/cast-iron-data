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
replaces = ["Dirge of doom", "frightening tune", "Inspire heroics", "Versatile performance", "Inspire competence"]
replaces_features = ["versatile-performance"]
+++

Fey who associate with courts often become bards skilled at navigating the inhuman societies of the
trackless wilds.

**Prerequisites:** Gathlain

**Bardic Performance**

**Info:** The fey courtier has access to the following bardic performances.

**Scorn of the Wilds (Sp)**

**Ability:** The fey courtier can use bardic performance to permanently mark a creature with
nature's displeasure by spending 2 rounds performing while the target remains within 30 feet. The
performance includes a litany of the target's misdeeds against fey and nature. Unless the target
succeeds at a Will saving throw (DC = 10 + [half](ref/misc/fractions-and-rounding) the bard's
level + his Charisma modifier), it is cursed as per [nature's exile](ref/spell/natures-exile) or
[bestow curse](ref/spell/bestow-curse).

**At 14th Level:** The fey courtier's options expand to include
[baleful polymorph](ref/spell/baleful-polymorph) and [green caress](ref/spell/green-caress).

**Gained:** At 8th Level

**Replaces:** Dirge of doom, frightening tune

**Special:** As part of the performance, the fey courtier must define a condition under which the
curse will be lifted, which must relate to making amends for the crime against fey or nature and
cannot be suicidal to carry out. A creature that succeeds at its saving throw is immune to the fey
courtier's scorn of the wild for 24 hours. This is a curse effect.

**Stone Dance (Sp)**

**Ability:** The bard's performance can move even the features of the natural world. This
performance functions as [animate plants](ref/spell/animate-plants) (DC = 10 + half the bard's
level + his Charisma modifier) except it can also animate unworked stone and water from natural
bodies of water (with statistics equivalent to an appropriate plant).

**Gained:** At 15th Level

**Replaces:** Inspire heroics

**Fey Contacts**

**Gained:** At 2nd Level

**Passive:** Thanks to his fey contacts and knowledge of the byzantine trade customs of the fey
courts, a fey courtier can treat any wilderness area with fey residents as a settlement with a
certain base value and purchase limit based on his bard level for the purpose of buying and selling
magic items (see the table below). The fey courtier can also use these contacts to gather
information about the residents, geography, and nearby areas with Diplomacy.

**Replaces:** Versatile performance

These rules come from [The Settlement Stat Block](ref/rule/the-settlement-stat-block):

> _There is a 75% chance that any item of \[the Base Value\] or lower can be found for sale in the
> community with little effort. If an item is not available, a new check to determine if the item
> has become available can be made in 1 week. A settlement's purchase limit is the most money a shop
> in the settlement can spend to purchase any single item from the PCs. If the PCs wish to sell an
> item worth more than a settlement's purchase limit, they'll either need to settle for a lower
> price, travel to a larger city, or (with the GM's permission) search for a specific buyer in the
> city with deeper pockets._

|Bard Level|Base Value|Purchase Limit|
| --- | --- | --- |
|2nd|50 gp|500 gp|
|6th|500 gp|2,500 gp|
|10th|2,000 gp|10,000 gp|
|14th|8,000 gp|50,000 gp|
|18th|32,000 gp|200,000 gp|

**Summon Fey Allies**

**Ability:** The fey courtier gains [Augment Summoning](ref/feat/augment-summoning) as a bonus feat
and can call upon natural allies who owe him favors. He adds
[summon nature's ally I](ref/spell/summon-natures-ally-1) to his list of 1st-level bard spells
known. Whenever he gains access to another spell level, he adds the next-higher
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell to his list of bard spells known.

**Gained:** At 3rd Level

**Replaces:** Inspire competence

**Special:** The fey courtier adds the following creatures to the
_[summon nature's ally](ref/spell/summon-natures-ally)_ list:
1st-[grimple (gremlin)](ref/monster/gremlin-grimple), [mite](ref/monster/mite),
[sprite](ref/monster/sprite); 2nd-[atomie](ref/monster/atomie),
[fuath (gremlin)](ref/monster/gremlin-fuath), [nixie](ref/monster/nixie);
3rd-[leprechaun](ref/monster/leprechaun), [nuglub (gremlin)](ref/monster/gremlin-nuglub),
[pooka](ref/monster/pooka); 4th-[kelpie](ref/monster/kelpie), [korred](ref/monster/korred),
[twigjack](ref/monster/twigjack); 5th-[lampad](ref/monster/lampad),
[lurker in light](ref/monster/lurker-in-light), [swan maiden](ref/monster/swan-maiden);
6th-[cold rider](ref/monster/cold-rider), [oceanid](ref/monster/oceanid),
[sangoi](ref/monster/sangoi).
