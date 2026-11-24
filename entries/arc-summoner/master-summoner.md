+++
id = "ref/arc-summoner/master-summoner"
kind = "archetype"
title = "Master Summoner"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Master%20Summoner"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "master_summoner", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "ultimate-magic"
page = "80"

[fields]
kind = "archetype"
features = [
  { anchor = "lesser-eidolon", level = 1 },
  { anchor = "summoning-mastery", level = 1 },
  { anchor = "augment-summoning", level = 2 },
]
trades = [
  { replaces = "Eidolon", feature = "eidolon", by = ["lesser-eidolon"] },
  { replaces = "Summon monster I", feature = "summon-monster-i", by = ["summoning-mastery"] },
  { replaces = "shield ally", feature = "shield-ally", by = ["summoning-mastery"] },
  { replaces = "Bond senses", feature = "bond-senses", by = ["augment-summoning"] },
]
+++

Most summoners forge a bond with a single, powerful eidolon, but some summoners seek to control a
variety of creatures. The master summoner sacrifices the power of his eidolon in favor of summoning
a plethora of otherworldly creatures to aid him.

## Lesser Eidolon {#lesser-eidolon}

A master summoner's class level is halved (minimum 1) for the purposes of determining his
[eidolon's](ref/sidekick/eidolon) abilities, Hit Dice, evolution pool, and so on. The eidolon
otherwise functions as normal. This ability replaces the summoner's normal eidolon ability.

## Summoning Mastery (Sp) {#summoning-mastery}

Starting at 1st level, a master summoner can cast _[summon monster I](ref/spell/summon-monster-1)_
as a [spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 5 + his
Charisma modifier. The summoner can use this ability when his eidolon is summoned. Only one
_[summon monster](ref/spell/summon-monster)_ spell may be in effect while the eidolon is summoned.
If the summoner's eidolon is not summoned, the number of creatures that can be summoned with this
ability is only limited by its uses per day. This ability otherwise functions as the summoner's
normal _[summon monster I](ref/spell/summon-monster-1)_ ability. Other than these restrictions,
there is no limit to how many _[summon monster](ref/spell/summon-monster)_ or
_[gate](ref/spell/gate)_ spells the summoner can have active at one time. This ability replaces the
summoner's normal _summon monster I_ ability and shield ally.

## Augment Summoning {#augment-summoning}

At 2nd level, a master summoner gains [Augment Summoning](ref/feat/augment-summoning) as a bonus
feat. He does not have to meet any requirements for this feat. This ability replaces bond senses.
