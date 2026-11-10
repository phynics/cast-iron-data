+++
id = "ref/arc-unchained-summoner/storm-caller"
kind = "archetype"
title = "Storm Caller"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "storm_caller", path = "json/archetypes_summoner_UC.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/unchained-summoner" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "16"

[fields]
kind = "archetype"
replaces = ["Shield ally", "greater shield ally", "Maker's call", "transposition"]
alters = ["Eidolon"]
+++

Many summoners beckon monsters from the Elemental Planes, but few are as specialized as storm
callers, who channel the elemental energies of the Plane of Air. Storm callers are most commonly
encountered in areas where thunderstorms appear frequently, including supernaturally stormy places
like the Sodden Lands.

**Stormy Eidolon**

**Alters:** Eidolon

**Info:** A storm caller must select an eidolon subtype that gains
[resistance](ref/unchevolution/resistance) or [immunity](ref/unchevolution/immunity) to electricity
at 1st level, such as the [elemental](ref/eidolon/elemental) eidolon or [genie](ref/eidolon/genie)
eidolon. If the eidolon has neither of these evolutions, it becomes [nauseated](ref/misc/nauseated)
until it regains one of them.

;;;ab\{title="Summon Storm's Fury (Sp)" action=Ability icon=down-magic-learn alter="Summon monster
I-IX"\}

A storm caller can summon creatures infused with the power of the storm to help him. This functions
as the summoner's _summon monster I-IX_ abilities, except the storm caller can summon only the
following creatures at the indicated spell levels:

**I**

**Details:** [eagle](ref/monster/eagle)

**II**

**Details:** [small air elemental](ref/monster/air-elemental),
[small lightning elemental](ref/monster/lightning-elemental)

**III**

**Details:** [dire bat](ref/monster/bat-dire-bat)

**IV**

**Details:** [medium air elemental](ref/monster/air-elemental),
[medium lightning elemental](ref/monster/lightning-elemental),
[pteranodon](ref/monster/dinosaur-pteranodon)

**V**

**Details:** [large air elemental](ref/monster/air-elemental),
[large lightning elemental](ref/monster/lightning-elemental)

**VI**

**Details:** [huge air elemental](ref/monster/air-elemental),
[huge lightning elemental](ref/monster/lightning-elemental)

**VII**

**Details:** [roc](ref/monster/roc)

**VIII**

**Details:** [elder air elemental](ref/monster/air-elemental),
[elder lightning elemental](ref/monster/lightning-elemental)

**IX**

**Details:** [advanced](ref/template/advanced) elder air elemental, advanced elder lightning
elemental

Any creatures summoned with this ability gain immunity to electricity.

Alternatively, whenever his eidolon is not summoned, a storm caller can expend a daily use of this
ability to summon a magical storm as a **standard action**. This functions as
[call lightning](ref/spell/call-lightning) with a caster level equal to his summoner level, except
as noted below.

Each bolt of lightning deals 1d6 points of electricity damage. As the summoner gains levels, this
damage increases as indicated on the table below. The prevailing weather has no effect on the damage
of the lightning bolts. The Reflex save DC is equal to 10 + half the storm caller's summoner level +
his Charisma modifier. If the storm caller uses this ability again before he has used all of his
available bolts of lightning (to summon another magical storm, to summon a monster, or to use the
[gate](ref/spell/gate) spell), any unused bolts are expended with no effect.

|Level|Damage|
| --- | --- |
|1|1d6|
|3|2d6|
|5|3d6|
|7|4d6|
|8|5d6|
|11|6d6|
|13|7d6|
|15|8d6|
|17|9d6|
|19|10d6|

The storm caller adds _[call lightning](ref/spell/call-lightning)_ to his summoner spell list as a
3rd-level spell and [call lightning storm](ref/spell/call-lightning-storm) to his summoner spell
list as a 5th-level spell, but he does not automatically add them to his list of spells known.

;;;

**Electrical Polarity (Su)**

**Ability:** A storm caller and his eidolon can temporarily form an electrical current between them.
The storm caller can expend a use of his _summon storm's fury_ ability as a **standard action** to
create an instantaneous line of lightning between him and his eidolon, provided that the eidolon is
within 60 feet of him. The lightning arc deals the same amount of damage to all creatures in the
line and has the same save DC as a bolt of lightning from the _summon storm's fury_ ability (unlike
_[call lightning](ref/spell/call-lightning),_ this damage is dealt only once). The storm caller and
his eidolon are not affected by this lightning.

**At 12th Level:** The storm caller gains the benefit of his eidolon's resistance (electricity) or
immunity (electricity) evolution whenever he is within 30 feet of the eidolon.

**Gained:** At 4th Level

**Replaces:** Shield ally, greater shield ally

**Storm's Wings (Su)**

**Ability:** A storm caller can borrow some of his eidolon's elemental might. He can gain the
[flight](ref/unchevolution/flight) evolution as though he were using the summoner's _aspect_
ability, deducting 2 evolution points from the eidolon's evolution pool. If he does so, his eidolon
is unable to take the flight evolution as long as the storm caller has that evolution.

**At 10th Level:** The storm caller automatically gains the flight evolution without reducing the
number of evolution points available to the eidolon. He can use the _aspect_ ability (and at 18th
level, the _greater aspect_ ability) to gain additional evolutions.

**At 8th Level:** The storm caller's eidolon can have the flight evolution even if the storm caller
has that evolution.

**Gained:** At 6th Level

**Replaces:** Maker's call, transposition
