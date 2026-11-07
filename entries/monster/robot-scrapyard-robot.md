+++
id = "ref/monster/robot-scrapyard-robot"
kind = "creature"
title = "Scrapyard Robot"
source_ids = ["numeria-land-of-fallen-stars"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "robot_scrapyard_robot", path = "json/monsters20.json" },
]

[fields]
kind = "creature"
cr = "3"
creature_type = "construct"
subtypes = ["robot"]
size = "medium"
alignment = "neutral"
ac = "14/9/14"
hp = "42~4d10+20"
fortitude = "+1"
reflex = "+0"
will = "+1"
melee = "slam +7 (1d4+4) or rotary saw +8 (2d4+4/&times&3)"
special_qualities = "repair, staggered"
abilities = ["17", "8", "-", "5", "10", "1"]
+++

_Frayed wires and broken-off protrusions sprout from mechanical construct, and one of its salvaged
arms ends in a spinning blade._

**Scrapyard Robot**

**Challenge rating:** 3

**Type:** construct

**dv:** 60

**Initiative:** -1

**Size:** medium

**Alignment:** Neutral

**Perception:** +5

**Senses:** Low-light vision

**Sources:** Numeria, Land of Fallen Stars pg 58\
**Subtype:** Robot

**Experience points:** 800

**Armor class:** 14/9/14

**Defensive abilities:** [hardness](ref/umr/hardness) 5

**Fort:** +1

**Hit points:** 42 (4d10+20)

**Immune:** [construct traits](ref/umr/construct-traits)

**Mod:** -1 Dex, +5 natural

**Ref:** +0

**Vulner:** electricity

**Weaknesses:** fall to pieces, vulnerable to critical hits

**Will:** +1

**Offense**

**Speed:** 30 ft.

**Melee:** slam +7 (1d4+4) or rotary saw +8 (2d4+4/&times&3)

**Statistics**

**Ability scores:** Str 17, Dex 8, Con -, Int 5, Wis 10, Cha 1

**Base attack bonus:** +4

**Combat maneuver bonus:** +7

**Combat maneuver defense:** 16 (20 vs. trip)

**Feats:** Power Attack, Weapon Focus (rotary saw)

**Skills:** Knowledge (engineering) +2, Perception +5

**Languages:** Common, Hallit

**Special qualities:** repair, staggered

**Ecology**

**Environment:** any ruin (Numeria)

**Organization:** solitary

**Treasure:** None

### Special Abilities

**Fall to Pieces (Ex)** Attacks and effects that deal more than 25% of a scrapyard robot's maximum
hit points in damage (10 hit points for a standard scrapyard robot) impair one of the robot's
components. Determine which subsystem randomly by rolling 1d6. If the subsystem has already been
impaired, there is no further effect.

|1d6|Effect|
| --- | --- |
|1|CPU: The robot is confused|
|2|Fractured Plating: Reduce the robot's natural armor bonus by 3.|
|3|Power Core: Attacks against the robot with natural weapons, unarmed strikes, or metal weapons deal 1d6 points of electricity damage to the attacker, and the robot's slam attack deals an additional 1d6 points of electricity damage. The robot shuts down from power loss in 1d4+1 rounds.|
|4|Rotary Saw: The robot loses its rotary saw attack.|
|5|Servos: The robot's speed is reduced to 15 feet and its CMD against trip combat maneuvers is reduced by 8.|
|6|Sensors: The robot is blinded.|

**Repair (Ex)** A scrapyard robot can use the inactive bodies of other robots to repair damage to
itself. Doing so restores 10 hit points and removes one condition imparted by its fall to pieces
ability per 8-hour period of uninterrupted work. Eight hours of repair expends all salvageable parts
from 1 Medium robot. For each size category a scrapped robot is above Medium, the scrapyard robot
can perform another 8 hours of repairs using that robot's parts. For each size category smaller than
Medium scrapped robots are, the scrapyard robot requires twice as many robots to complete 8 hours of
work.

**Staggered (Ex)** The poor construction of a scrapyard robot allows it to take only a single move
or standard action each round. In effect, it always has the staggered condition. A scrapyard robot
can move up to its speed and attack in the same round as a charge action.

### Description

Pieced together from broken technology, these constructs lack the balance to stand upright, the
motor control to use their hands (if they have any), and the intelligence possessed by advanced
robots, but they still retain a halting consciousness and the ability to obey simple commands.

**Family:** [Robot](ref/family/robot)
