+++
id = "ref/arc-inquisitor/abolisher"
kind = "archetype"
title = "Abolisher"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "abolisher", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]

[fields]
kind = "archetype"
replaces = ["Stern gaze", "Detect alignment", "Discern lies"]
alters = ["Domains", "Bane"]
+++

**Sources:** Monster Hunter's Handbook pg 7\
Abolishers are incorruptible inquisitors who weed out creatures of alien, unnatural origins, finding
and exposing aberrations for what they are.

**Sworn to Purity (Ex)**

**Alters:** Domains

**Choice:** An abolisher must select one of the following domains: [Air](ref/domain/air),
[Animal](ref/domain/animal), [Earth](ref/domain/earth), [Fire](ref/domain/fire),
[Plant](ref/domain/plant), [Water](ref/domain/water), or [Weather](ref/domain/weather). If she ever
changes her deity to one that has none of the listed domains, she loses this archetype and becomes a
normal inquisitor or ex-inquisitor.

**Revealing Gaze (Ex)**

**Passive:** An abolisher receives a morale bonus on opposed Perception checks against other
creatures' Disguise and Stealth checks equal to [half](ref/misc/fractions-and-rounding) her
inquisitor level (minimum +1). She grants this bonus to all adjacent allies.

**Replaces:** Stern gaze

**Expose Aberration (Sp)**

**Ability:** An abolisher can use [detect aberration](ref/spell/detect-aberration) at will. When she
hits a creature with a weapon attack, she automatically knows if the creature is an aberration or
not.

**Alters:** Bane

**At 5th Level:** She can activate her _[bane](ref/spell/bane)_ ability as an **immediate action**
after she hits an aberration but before damage is rolled.

**Gained:** At 2nd Level

**Replaces:** Detect alignment

**Escape Corruption's Grasp (Sp)**

**Flavor:** An abolisher is divinely protected against the grasping tentacles and paralyzing
secretions of aberrations.

**Immediate:** She can ignore impediments to movement, as per
[freedom of movement](ref/spell/freedom-of-movement).

**Gained:** At 5th Level

**Replaces:** Discern lies

**Usage:** 1 time/day per inquisitor level
