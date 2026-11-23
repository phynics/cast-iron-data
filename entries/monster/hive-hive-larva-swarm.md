+++
id = "ref/monster/hive-hive-larva-swarm"
kind = "creature"
title = "Hive Larva Swarm"
aon = "MonsterDisplay.aspx?ItemName=Hive%20Larva%20Swarm"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hive_hive_larva_swarm", path = "json/monsters13.json" },
]
[[sources]]
publication = "horror-adventures"
page = "236"

[fields]
kind = "creature"
cr = "5"
creature_type = "aberration"
subtypes = ["hive", "swarm"]
size = "fine"
alignment = "neutral"
ac = "20/20/18"
hp = "52~7d8+21"
fortitude = "+5"
reflex = "+4"
will = "+5"
melee = "swarm (2d6 plus distraction and poison)"
special_attacks = "death throes (7d6, DC 16)~infest~poison"
special_qualities = "blind"
abilities = ["1", "15", "16", "-", "10", "1"]
+++

_This mass of writhing, maggot-like creatures secretes a caustic odor._

::: statblock
Challenge rating: 5
Type: aberration
blindsense: 60
blindsight: 10
Size: fine
Initiative: +2
Alignment: Neutral
Perception: +0
Senses: Hive mind
Subtype: Hive, Swarm
Experience points: 1,600
:::

### Defense

::: statblock
Armor class: 20
Touch: 20
Flat-footed: 18
AC modifiers: +2 Dex, +8 Size
Hit points: 52 (7d8+21)
Fort: +5
Ref: +4
Will: +5
Defensive abilities: corrosive blood (1d4), heat adaptability, swarm traits
Immune: acid, mind-affecting effects, weapon damage
:::

### Offense

::: statblock
Speed: 10 ft., climb 10 ft.
Melee: swarm (2d6 plus distraction and poison)
Reach: 10
Space: 10
Spec Att: death throes (7d6, DC 16), infest, poison
:::

### Statistics

::: statblock
Ability scores: Str 1, Dex 15, Con 16, Int -, Wis 10, Cha 1
Base attack bonus: +5
Combat maneuver bonus: -
Combat maneuver defense: -
Special qualities: blind
:::

### Ecology

::: statblock
Environment: any
Organization: solitary or hive (1-20 plus 1-50 hive workers and [warriors](ref/monster/hive-hive-warrior) and 1 [queen](ref/monster/hive-hive-queen))
Treasure: Incidental
:::

### Special Abilities

**Infest (Ex)** A hive larva swarm can enter the body of a single Small or larger helpless living
creature. When it does so, a portion of the swarm enters a creature's mouth and gestates for 1d4
minutes. The gestated larvae ravage the host for 24 hours, during which time the infested creature
falls unconscious and can't be woken by any means. During this period the larvae are vulnerable to
expulsion by remove disease (same DC as death throes, typically DC 16). If successful, the hive
larvae die inside of the host, dealing another 1d6 points of acid damage. In some cases, metabolized
hive larvae corpses can infect the creature with the [hive corruption](ref/rule/hive).

After 24 hours, the hive larvae achieve symbiosis. The host awakens feeling healthy but hungry.
Spells such as diagnose disease and Heal checks used to detect disease no longer detect the hive
infestation, and the host creature is now treated as both its original creature type and an
aberration for purposes of spells and effects (whichever is worse). A successful DC 25 Knowledge
(dungeoneering) check can identify the symbiosis. If the host dies at this point, the larval
infestation dies as well. However, if the host is then returned from the dead, the larvae are
returned to life as well.

The swarm fully matures 2d12 hours after symbiosis. By this point, there is no way to save the host
short of a miracle or wish spell. Each round for 2d12 rounds, the host suffers agonizing pain and
must succeed at a Fortitude save (DC 16) or be nauseated for 1 round. On each failed save, the host
takes 4d6 points of damage as the mature hive creature forcibly separates itself. At the end of the
2d12 rounds, or after the host is slain by the damage, a fully formed hive creature (usually a hive
warrior) explodes from within, destroying the host's body.

**Poison (Ex)**

**Type:** Poison (Swarm-injury)

**Save:** Fortitude DC 16

**Frequency:** 1/round for 6 rounds

**Effect:** Strength damage 1d4

**Cure:** 2 consecutive saves

### Description

Hive larvae are the first stage of the hive life cycle. These tenacious creatures render suitable
hosts incapacitated and infest their bodies, transforming them into new hive creatures.

**Family:** [Hive](ref/family/hive)
