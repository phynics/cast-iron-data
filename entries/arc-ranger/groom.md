+++
id = "ref/arc-ranger/groom"
kind = "archetype"
title = "Groom"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "groom", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]

[fields]
kind = "archetype"
replaces = ["Track", "Endurance", "1st favored terrain"]
+++

**Sources:** Dungeoneer's Handbook pg 21\
The groom attends to the needs of the party's mounts and beasts of burden during their adventures,
and guards these animals while the party goes underground.

**Hide the Horses (Ex)**

**Flavor:** A groom finds the best place to stable and conceal a party's mounts while the group
explores a dungeon.

**Passive:** A groom adds half her level (minimum 1) on Stealth skill checks for both herself and
the mounts she's hiding while she is concealing a party's mounts.

**Replaces:** Track

**Horse Whisperer (Su)**

**Ability:** A groom can use [speak with animals](ref/spell/speak-with-animals) at will, but can use
this power only on horses, riding dogs, and other mounts of the animal type.

**Gained:** At 3rd Level

**Replaces:** Endurance

**Scout the Area (Ex)**

**Ability:** She always knows where to find the nearest expert or spellcaster who can provide a
particular service, such as the nearest source of [raise dead](ref/spell/raise-dead).

**Gained:** At 3rd Level

**Passive:** A groom gains a +4 bonus on Knowledge (local) checks.

**Replaces:** 1st favored terrain
