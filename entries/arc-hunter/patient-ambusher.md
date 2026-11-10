+++
id = "ref/arc-hunter/patient-ambusher"
kind = "archetype"
title = "Patient Ambusher"
source_ids = ["ultimate-wilderness", "magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "patient_ambusher", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "53"
[[sources]]
publication = "magic-tactics-toolbox"
page = "14"

[fields]
kind = "archetype"
replaces = ["Nature training", "wild empathy", "Hunter tactics", "Teamwork feats", "Raise animal companion"]
+++

Wandering the wilds, some hunters eschew the bond of innate teamwork with their animal companions.
Instead, these hunters master the creation and deployment of intricate ranger traps, often using
themselves or their animal companions to lure foes into their snares.

**Gained class skills:** dd

**Trapfinding (Ex)**

**Ability:** A patient ambusher can use Disable Device to disarm magic traps.

**Passive:** A patient ambusher adds half her hunter level (minimum +1) on Perception checks to
locate traps and on Disable Device skill checks.

**Replaces:** Nature training, wild empathy

**Snare Trap (Ex or Su)**

**Ability:** A patient ambusher learns how to create a snare trap. The patient ambusher can use this
and other learned traps a total number of times per day equal to half her hunter level + her Wisdom
modifier. This snare trap otherwise functions the same as the
[ranger snare trap](ref/trap/spring-snare).

**Replaces:** Hunter tactics

**Additional Traps (Ex or Su)**

**Ability:** A patient ambusher can learn a new type of trap, selected from the list of ranger
traps. Once a trap is learned, it can't be unlearned and replaced with a different type of trap.

**Gained:** At 3rd Level

**Replaces:** Teamwork feats

**Special:** The patient ambusher cannot learn an individual trap more than once.

At 6th level: She gains a 2nd ranger trap.

At 9th level: She learns a 3rd ranger trap.

At 12th level: She gains a 4th ranger trap.

At 15th level: She learns a 5th ranger trap.

At 18th level: She gains a 6th ranger trap.

**Launch Trap (Su)**

**Ability:** A patient ambusher can affix a magical ranger trap to an arrow, a crossbow bolt, or a
thrown weapon, allowing her to set the trap remotely or use it as a direct attack. Attaching the
trap to the projectile is part of the **full-round action** to create a new trap. The trapped
projectile is fired or thrown in the normal manner.

**Info:** If fired at a square, the trap is treated as if the hunter had set the trap in that
square, except the DC is 5 lower than normal. If the trap is fired at a creature, the target takes
damage from the ranged weapon and is treated as if it had triggered the trap (attempting a saving
throw, if any).

**Gained:** At 10th Level

**Replaces:** Raise animal companion

**Special:** The attack has a maximum range of 60 feet, and penalties from range increments apply on
the attack roll. The duration of the trap starts when it is created, not when it is triggered.
