+++
id = "ref/arc-hunter/patient-ambusher"
kind = "archetype"
title = "Patient Ambusher"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Patient%20Ambusher"
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
features = [
  { anchor = "trapfinding", level = 1 },
  { anchor = "snare-trap", level = 3 },
  { anchor = "additional-traps", level = 3 },
  { anchor = "launch-trap", level = 10 },
]
trades = [
  { replaces = "Nature training", feature = "nature-training", by = ["trapfinding"] },
  { replaces = "wild empathy", feature = "wild-empathy", by = ["trapfinding"] },
  { replaces = "Hunter tactics", feature = "hunter-tactics", by = ["snare-trap"] },
  { replaces = "Teamwork feats", feature = "teamwork-feat", by = ["additional-traps"] },
  { replaces = "Raise animal companion", feature = "raise-animal-companion", by = ["launch-trap"] },
  { alters = "Class skills" },
]
+++

Wandering the wilds, some hunters eschew the bond of innate teamwork with their animal companions.
Instead, these hunters master the creation and deployment of intricate ranger traps, often using
themselves or their animal companions to lure foes into their snares.

## Class Skills {#class-skills}

A patient ambusher adds Disable Device to her list of class skills.

This alters the hunter's class skills.

## Trapfinding (Ex) {#trapfinding}

A patient ambusher adds half her hunter level (minimum +1) on Perception checks to locate traps and
on Disable Device skill checks. A patient ambusher can use Disable Device to disarm magic traps.

This replaces nature training and wild empathy.

## Snare Trap (Ex or Su) {#snare-trap}

At 3rd level, a patient ambusher learns how to create a snare trap. The patient ambusher can use
this and other learned traps a total number of times per day equal to half her hunter level + her
Wisdom modifier. This snare trap otherwise functions the same as the
[ranger snare trap](ref/trap/spring-snare) detailed in _Pathfinder RPG Ultimate Magic_.

This replaces the hunter tactics class feature.

## Additional Traps (Ex or Su) {#additional-traps}

At 3rd level and every 3 hunter levels thereafter, a patient ambusher can learn a new type of trap,
selected from the list of ranger traps presented on pages 64–65 of _Ultimate Magic_. Once a trap is
learned, it can't be unlearned and replaced with a different type of trap. The patient ambusher
cannot learn an individual trap more than once.

This replaces teamwork feats.

## Launch Trap (Su) {#launch-trap}

At 10th level, a patient ambusher can affix a magical ranger trap to an arrow, a crossbow bolt, or a
thrown weapon, allowing her to set the trap remotely or use it as a direct attack. Attaching the
trap to the projectile is part of the full-round action to create a new trap. The trapped projectile
is fired or thrown in the normal manner. If fired at a square, the trap is treated as if the hunter
had set the trap in that square, except the DC is 5 lower than normal. If the trap is fired at a
creature, the target takes damage from the ranged weapon and is treated as if it had triggered the
trap (attempting a saving throw, if any). The attack has a maximum range of 60 feet, and penalties
from range increments apply on the attack roll. The duration of the trap starts when it is created,
not when it is triggered.

This replaces raise animal companion.
