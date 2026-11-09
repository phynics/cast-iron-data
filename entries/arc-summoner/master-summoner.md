+++
id = "ref/arc-summoner/master-summoner"
kind = "archetype"
title = "Master Summoner"
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
replaces = ["Eidolon", "Summon monster I", "shield ally", "Bond senses"]
+++

Most summoners forge a bond with a single, powerful eidolon, but some summoners seek to control a
variety of creatures. The master summoner sacrifices the power of his eidolon in favor of summoning
a plethora of otherworldly creatures to aid him.

**Lesser Eidolon**

**Info:** A master summoner's class level is halved (minimum 1) for the purposes of determining his
[eidolon's](ref/sidekick/eidolon) abilities, Hit Dice, evolution pool, and so on. The eidolon
otherwise functions as normal.

**Replaces:** Eidolon

**Summoning Mastery (Sp)**

**Ability:** A master summoner can cast [summon monster I](ref/spell/summon-monster-1) as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 5 + his
Charisma modifier. The summoner can use this ability when his eidolon is summoned.

**Gained:** At 1st Level

**Replaces:** Summon monster I, shield ally

**Special:** Only one _[summon monster](ref/spell/summon-monster)_ spell may be in effect while the
eidolon is summoned. If the summoner's eidolon is not summoned, the number of creatures that can be
summoned with this ability is only limited by its uses per day. This ability otherwise functions as
the summoner's normal _[summon monster I](ref/spell/summon-monster-1)_ ability. Other than these
restrictions, there is no limit to how many _[summon monster](ref/spell/summon-monster)_ or
[gate](ref/spell/gate) spells the summoner can have active at one time.

**Augment Summoning**

**Ability:** A master summoner gains [Augment Summoning](ref/feat/augment-summoning) as a bonus
feat. He does not have to meet any requirements for this feat.

**Gained:** At 2nd Level

**Replaces:** Bond senses

### Hordes of Summoned Monsters

The [broodmaster](ref/arc-summoner/broodmaster) and master summoner archetypes can potentially have
5, 10, or even more summoned creatures in play. This is a deliberate feature of these archetypes,
and means that the summoner can potentially be a strong candidate for "solo" adventuring by one
player. However, in the hands of an inexperienced or moderately experienced player, dealing with all
of those creatures in combat can take a long time, forcing other players to wait extended periods
between their turns in the initiative. It is strongly recommended that GMs only allow these
archetypes for experienced players, or decide on a way to speed up the summoner's turn (such as by
allowing other players to control some of the summoned monsters).
