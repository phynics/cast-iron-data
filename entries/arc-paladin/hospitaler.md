+++
id = "ref/arc-paladin/hospitaler"
kind = "archetype"
title = "Hospitaler"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hospitaler", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-players-guide"
page = "116"

[fields]
kind = "archetype"
replaces = ["Channel positive energy", "Aura of justice"]
alters = ["Smite evil"]
+++

Paladins are known for their charity and for tending to the sick. The hospitaler takes to this
calling above all others, spending much of her time healing the poor, and giving aid and succor to
those in need. The hospitaler has the following class features.

**Smite Evil (Su)**

**Alters:** Smite evil

**Info:** This functions as the paladin ability, with the adjusted advancement stated below.

**Usage:** 1 time/day + 1 per 6 paladin levels beyond 1st

**Channel Positive Energy (Su)**

**At 4th Level:** A hospitaler gains the ability to channel positive energy as a
[cleric](ref/class/cleric) equal to her paladin level - 3.

**Replaces:** Channel positive energy

**Special:** Using this ability does not expend uses of _lay on hands,_ as it does with other
paladins.

**Usage:** Charisma3 modifier times/day

**Aura of Healing (Su)**

**Ability:** A hospitaler can expend one use of her _channel positive energy_ ability to emit a
30-foot aura of healing for a number of rounds equal to her paladin level. Allies in this aura
(including the hospitaler) automatically [stabilize](ref/misc/stable) if below 0 hit points and are
immune to [bleed](ref/umr/bleed) damage.

**Gained:** At 11th Level

**Passive:** Allies (including the paladin) that spend at least 1 full round inside the aura are
healed an amount of damage equal to their total number of Hit Dice and may make a saving throw
against any afflictions they are suffering from, such as a curse, disease, or poison. This saving
throw only counts toward curing the affliction and does not impose any penalty on a failed save.

**Replaces:** Aura of justice

**Special:** Allies can only be healed once by a use of this ability and they can only attempt
additional saving throws once per day, even if they are exposed to this aura multiple times.
