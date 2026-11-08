+++
id = "ref/monster/basidirond"
kind = "creature"
title = "Basidirond"
source_ids = ["bestiary"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "basidirond", path = "json/monsters03.json" },
]

[fields]
kind = "creature"
cr = "5"
creature_type = "plant"
size = "medium"
alignment = "neutral"
ac = "18/11/17"
hp = "52~7d8+21"
fortitude = "+8"
reflex = "+3"
will = "+2"
melee = "slam +10 (1d8+7 plus spores)"
special_attacks = "hallucination cloud~spores"
abilities = ["20", "13", "16", "-", "11", "1"]
+++

_This strange plant consists of four spidery stalks, long green tendrils, and an inverted
bell-shaped cap filled with spores._

**Basidirond**

**Challenge rating:** 5

**Initiative:** +1

**Size:** medium

**Alignment:** Neutral

**Perception:** +0

**Senses:** Low-light vision

**Type:** plant

**Sources:** Pathfinder RPG Bestiary pg 28\
**Tremorsense:** present

**Experience points:** 1,600

**Armor class:** 18/11/17

**Fort:** +8

**Hit points:** 52 (7d8+21)

**Immune:** cold, [plant traits](ref/umr/plant-traits)

**Mod:** +1 Dex, +7 natural

**Ref:** +3

**Weaknesses:** cold lethargy

**Will:** +2

**Offense**

**Speed:** 20 ft.

**Melee:** slam +10 (1d8+7 plus spores)

**Spec Att:** hallucination cloud, spores

**Statistics**

**Ability scores:** Str 20, Dex 13, Con 16, Int -, Wis 11, Cha 1

**Base attack bonus:** +5

**Combat maneuver bonus:** +10

**Combat maneuver defense:** 21 (25 vs. trip)

**Ecology**

**Environment:** any non-cold underground

**Organization:** solitary, pair, or grove (3-8)

**Treasure:** Incidental

### Special Abilities

**Hallucination Cloud (Ex)** As a standard action once per minute, a basidirond can release a cloud
of invisible spores in a 20-foot radius. All creatures within the area must succeed on a DC 16
Fortitude save or be affected by powerful hallucinations as long as they remain in the cloud plus
1d4 rounds after leaving the area. A new save must be made each round a creature remains within the
affected area. A hallucination cloud persists for 5 rounds before dispersing - a strong wind causes
it to disperse immediately. The save DC is Constitution-based. To determine what hallucination is
suffered each round, roll 1d6 and consult the following table.

|d6|Hallucination|
| --- | --- |
|1|You're sinking in quicksand! Fall [prone](ref/rule/prone) and spend 1 round flailing your arms and legs as if trying to swim.|
|2|Attacked by a swarm of spiders! Spend a full round action to attack the floor near you with your weapon.|
|3|An item you hold has turned into a viper! Drop it and flee from the item at top speed for 1 round.|
|4|You're suffocating! Stand in place, hold your breath, and clutch at your throat for 1 round.|
|5|You've shrunk to 1/10th your normal size! Take no actions for 1 round and monsters won't see you.|
|6|You're melting! Grasp hold of yourself in an attempt to hold yourself together, and take no actions for 1 round.|

**Spores (Ex)** Any creature struck by a basidirond's slam attack is coated with spores. The
creature struck must make a DC 16 Fortitude save or these spores take root in his flesh, and
particularly in his lungs. The save DC is Constitution-based.

- [Affliction: Basidirond Spores](ref/affliction/basidirond/basidirond-spores)

**Cold Lethargy (Ex)** Although a basidirond is immune to cold damage, any cold effect it is exposed
to [slows](ref/spell/slow) it for 1d4 rounds. During this time, the basidirond cannot use its
hallucination cloud or spores.

### Description

The strange fungal basidirond is a deadly plant monster that feeds on mineral-rich moisture, be it
runoff from cave walls or fresh blood. By ensuring a constant flow of nutritious moisture, canny
cave dwellers can use basidironds as guardians for their lairs, although they must take care to
avoid the plant's hunting routes lest they become its latest victims.
