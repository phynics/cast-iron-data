+++
id = "ref/arc-summoner/storm-caller"
kind = "archetype"
title = "Storm Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Storm%20Caller"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "storm_caller", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "stormy-eidolon", level = 1 },
  { anchor = "summon-storm-s-fury" },
  { anchor = "electrical-polarity", level = 4 },
  { anchor = "storm-s-wings", level = 6 },
]
trades = [
  { replaces = "Shield ally", feature = "shield-ally", by = ["electrical-polarity"] },
  { replaces = "greater shield ally", feature = "greater-shield-ally", by = ["electrical-polarity"] },
  { replaces = "Maker's call", feature = "maker-s-call", by = ["storm-s-wings"] },
  { replaces = "transposition", feature = "transposition", by = ["storm-s-wings"] },
  { alters = "Eidolon", feature = "eidolon", by = ["stormy-eidolon"] },
  { alters = "the summoner's summon monster I–IX abilities", feature = "summon-monster-i", by = ["summon-storm-s-fury"] },
]
+++

Many summoners beckon monsters from the Elemental Planes, but few are as specialized as storm
callers, who channel the elemental energies of the Plane of Air. Storm callers are most commonly
encountered in areas where thunderstorms appear frequently, including supernaturally stormy places
like the Sodden Lands. Summoners built using _Pathfinder RPG Pathfinder Unchained_ can also take
this archetype.

## Stormy Eidolon {#stormy-eidolon}

A storm caller must select the [resistance](ref/evolution/resistance) (electricity) or
[immunity](ref/evolution/immunity) (electricity) evolution for his eidolon. If the eidolon has
neither of these evolutions, it becomes [nauseated](ref/misc/nauseated) until it regains one of
them. An unchained summoner with this archetype must select an eidolon subtype that gains resistance
or immunity to electricity at 1st level, such as the elemental eidolon (_Pathfinder Unchained_ 33)
or genie eidolon (see page 27).

This ability alters eidolon.

## Summon Storm's Fury (Sp) {#summon-storm-s-fury}

A storm caller can summon creatures infused with the power of the storm to help him. This functions
as the summoner's summon monster I–IX abilities, except the storm caller can summon only the
following creatures at the indicated spell levels: I—[eagle](ref/monster/eagle);
II—[small air elemental](ref/monster/air-elemental),
[small lightning elemental](ref/monster/lightning-elemental);
III—[dire bat](ref/monster/bat-dire-bat); IV—[medium air elemental](ref/monster/air-elemental),
[medium lightning elemental](ref/monster/lightning-elemental),
[pteranodon](ref/monster/dinosaur-pteranodon); V—[large air elemental](ref/monster/air-elemental),
[large lightning elemental](ref/monster/lightning-elemental);
VI—[huge air elemental](ref/monster/air-elemental),
[huge lightning elemental](ref/monster/lightning-elemental); VII—[roc](ref/monster/roc);
VIII—[elder air elemental](ref/monster/air-elemental),
[elder lightning elemental](ref/monster/lightning-elemental); IX—[advanced](ref/template/advanced)
elder air elemental, advanced elder lightning elemental. Any creatures summoned with this ability
gain immunity to electricity.

Alternatively, whenever his eidolon is not summoned, a storm caller can expend a daily use of this
ability to summon a magical storm as a standard action.

This functions as _call lightning_ with a caster level equal to his summoner level, except as noted
below.

Each bolt of lightning deals 1d6 points of electricity damage. This damage increases by 1d6 at 3rd
level and every 2 levels thereafter, to a maximum of 10d6 at 19th level. The prevailing weather has
no effect on the damage of the lightning bolts. The Reflex save DC is equal to 10 + half the storm
caller's summoner level + his Charisma modifier. If the storm caller uses this ability again before
he has used all of his available bolts of lightning (to summon another magical storm, to summon a
monster, or to use the _[gate](ref/spell/gate)_ spell), any unused bolts are expended with no
effect.

The storm caller adds _call lightning_ to his summoner spell list as a 3rd-level spell and
_[call lightning storm](ref/spell/call-lightning-storm)_ to his summoner spell list as a 5th-level
spell, but he does not automatically add them to his list of spells known.

This alters the summoner's summon monster I–IX abilities.

## Electrical Polarity (Su) {#electrical-polarity}

At 4th level, a storm caller and his eidolon can temporarily form an electrical current between
them. The storm caller can expend a use of his summon storm's fury ability as a standard action to
create an instantaneous line of lightning between him and his eidolon, provided that the eidolon is
within 60 feet of him. The lightning arc deals the same amount of damage to all creatures in the
line and has the same save DC as a bolt of lightning from the summon storm's fury ability (unlike
_[call lightning](ref/spell/call-lightning)_, this damage is dealt only once). The storm caller and
his eidolon are not affected by this lightning.

At 12th level, the storm caller gains the benefit of his eidolon's resistance (electricity) or
immunity (electricity) evolution whenever he is within 30 feet of the eidolon.

This ability replaces shield ally and greater shield ally.

## Storm's Wings (Su) {#storm-s-wings}

At 6th level, a storm caller can borrow some of his eidolon's elemental might. He can gain the
[flight](ref/evolution/flight) evolution as though he were using the summoner's aspect ability,
deducting 2 evolution points from the eidolon's evolution pool. If he does so, his eidolon is unable
to take the flight evolution as long as the storm caller has that evolution.

At 8th level, the storm caller's eidolon can have the flight evolution even if the storm caller has
that evolution.

At 10th level, the storm caller automatically gains the flight evolution without reducing the number
of evolution points available to the eidolon. He can use the aspect ability (and at 18th level, the
greater aspect ability) to gain additional evolutions.

This ability replaces maker's call and transposition.
