+++
id = "ref/carried/bestiary-3/monsters/swarm/parasite/rot-grub"
kind = "creature"
title = "Swarm, Parasite, Rot Grub"
source_ids = ["bestiary-3", "pathfinder-25-the-bastards-of-erebus"]
section = ["Monsters", "Swarm", "Parasite"]
tags = ["vermin", "swarm", "fine"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary 3/Monsters/Swarm/Parasite/Rot Grub", path = "bestiary_3/creature/swarm_parasite_rot_grub.json" },
]

[fields]
kind = "creature"
cr = "7"
creature_type = "vermin"
subtypes = ["swarm"]
size = "Fine"
alignment = "N"
ac = "20, touch 20, flat-footed 18 (+2 Dex, +8 size)"
hp = "85 (10d8+40)"
fortitude = "+11"
reflex = "+5"
will = "+3"
melee = "swarm (2d6 plus distraction and infestation)"
special_attacks = "distraction (DC 19), infestation"
abilities = ["1", "15", "18", "-", "10", "1"]
+++

::: statblock
CR: 7
XP: 3,200
Alignment: N
Size: Fine
Type: Vermin (swarm)
Init: +2
Senses: [blindsense](ref/rule/blindsight-and-blindsense) 30 ft.; Perception +0
AC: 20, touch 20, flat-footed 18 (+2 Dex, +8 size)
hp: 85 (10d8+40)
Fort: +11
Ref: +5
Will: +3
Defensive Abilities: swarm traits
Immune: mind-affecting effects, weapon damage
Speed: 10 ft.
Melee: swarm (2d6 plus distraction and infestation)
Space: 10 ft.
Reach: 0 ft.
Special Attacks: distraction (DC 19), infestation
Ability Scores: Str 1, Dex 15, Con 18, Int -, Wis 10, Cha 1
Base Atk: +7
CMB: -
CMD: —
Environment: any
Organization: solitary
Treasure: none
:::

_This nauseating carpet of wriggling white grubs undulates outward in a pallid wave of hunger._

## Special Abilities {#special-abilities}

### Infestation {#infestation}

::: statblock
Ability Type: Extraordinary
:::

Any living creature that takes damage from a rot grub swarm becomes infested unless it succeeds at a
DC 19 Reflex save. On a failed save, the infested creature takes 1d4 points of Constitution damage
per round as the rot grubs burrow through and consume its flesh—this effect continues as long as the
victim remains in the swarm and continues for 1d6 rounds after it leaves the swarm. Any energy-based
attack (including damage from negative energy) that deals at least 5 points of damage to the victim
automatically destroys all of the rot grubs infesting it, ending the effect prematurely.
Additionally, any effect that removes disease instantly ends a rot grub infestation. Immunity to
disease offers no defense. The save DC is Constitution-based.
