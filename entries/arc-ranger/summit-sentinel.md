+++
id = "ref/arc-ranger/summit-sentinel"
kind = "archetype"
title = "Summit Sentinel"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Summit%20Sentinel"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summit_sentinel", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "72"

[fields]
kind = "archetype"
replaces = ["Combat style feats", "Swift tracker", "Hide in plain sight"]
alters = ["Favored terrain", "Spells"]
+++

Some rangers eschew the path of the swift skirmisher and embrace the implacable strength of the
mountain.

**Roots of the Mountain (Su)**

**Ability:** A summit sentinel gains [Toughness](ref/feat/toughness) as a bonus feat.

**Gained:** At 2nd Level

**Move:** She can enter a defensive stance for 1 minute. While in this stance, the summit sentinel's
speed is reduced to 5 feet, she gains a +2 enhancement bonus to her natural armor, and she gains a
+2 bonus to her CMD against maneuvers that would move her or knock her prone. If the ranger loses
contact with the ground or other solid surface, the stance ends immediately.

**Replaces:** Combat style feats

**Usage:** Constitution3 modifier times/day

**Mountain Mastery (Ex)**

**Alters:** Favored terrain

**At 18th Level:** The bonus on attack and damage rolls increases to +2.

**At 8th Level:** A summit sentinel draws strength from the earth. When she and her target are both
in contact with the ground or an earthen floor, the summit sentinel gains a +1 bonus on attack and
damage rolls against the target.

**Info:** A summit sentinel must select mountains as her _favored terrain,_ and she does not gain
additional _favored terrains_ at higher levels.

**Gained:** At 3rd Level

At 10th level: The bonus from this _favored terrain_ +4.

At 15th level: The bonus from this _favored terrain_ +6.

At 20th level: The bonus from this _favored terrain_ +8.

**Spells**

**Ability:** A summit sentinel adds [stoneskin](ref/spell/stoneskin) to the ranger spell list as a
4th-level spell.

**Alters:** Spells

**Rockslide (Su)**

**Gained:** At 8th Level

**Replaces:** Swift tracker

**Standard:** Once per day, a summit sentinel can create a rushing wave of earth and stone. The
summit sentinel chooses a point on the ground or floor within 30 feet. Rippling waves of earth and
stone emanate from the chosen point in a 25-foot cone in a direction of the summit sentinel's
choice. Each creature in the area takes 4d6 points of bludgeoning damage and is pushed to the end of
the cone. A target that succeeds at a Reflex save (DC = 10 + half the ranger's level + the ranger's
Wisdom modifier) takes half damage and is not pushed.

**Invincible (Su)**

**Flavor:** A summit sentinel takes on the unyielding [hardness](ref/umr/hardness) of the mountains.

**Gained:** At 17th Level

**Passive:** While in her _roots of the mountain_ defensive stance, she is immune to critical hits
and precision damage.

**Replaces:** Hide in plain sight
