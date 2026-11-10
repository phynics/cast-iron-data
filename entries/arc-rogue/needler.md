+++
id = "ref/arc-rogue/needler"
kind = "archetype"
title = "Needler"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Needler"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "needler", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "potions-and-poisons"
page = "12"

[fields]
kind = "archetype"
replaces = ["Evasion", "Uncanny dodge", "Rogue talent gained at 6th level", "Improved uncanny dodge"]
replaces_features = ["evasion", "uncanny-dodge", "improved-uncanny-dodge"]
+++

While some assassins and killers prefer to be up front with their poison use, others favor a covert
approach. Needlers use subtlety and misdirection to deliver deadly poisons to unsuspecting victims
in creative and unorthodox ways. This archetype is appropriate for rogues built using the rules from
the Pathfinder RPG Core Rulebook as well as for unchained rogues.

**Adroit Poisoner (Ex)**

**At 2nd Level:** A needler gains a +2 bonus on Sleight of Hand checks. This bonus increases to +4
when the needler uses Sleight of Hand to draw a hidden weapon that is coated in poison.

**At 8th Level:** These bonuses increase to +4 and +6, respectively.

**Replaces:** Evasion

**Subtle Poisoning (Ex)**

**Ability:** A needler can apply a contact or ingested poison to her weapon and deliver it as if it
were an injury poison. The poison must be delivered within 1 minute of this application, or it is
wasted. The DC of the saving throw to resist the poison decreases by 1 when the needler uses this
ability to deliver a contact or ingested poison via injury.

**Gained:** At 4th Level

**Replaces:** Uncanny dodge

**Needle Poisoner (Ex)**

**Gained:** At 6th Level

**Replaces:** Rogue talent gained at 6th level

**Special:** This ability counts as _swift poisoning_ for the purpose of meeting prerequisites.^1^

**Swift:** A needler can apply a dose of poison to a weapon.

**Concealed Delivery (Ex)**

**Flavor:** A needler learns how to deliver all types of poisons with subtlety.

**Gained:** At 8th Level

**Replaces:** Improved uncanny dodge

**Standard:** She can deliver an ingested or inhaled poison to a creature within reach by placing a
dose of poison on the target's lips, on the target's neck, or through other similar contact with the
target's skin as if the poison were a contact poison. Delivering poison in this way requires a
successful Sleight of Hand check opposed by the target's Perception check. The poison is not lost on
a failed check, but it must be successfully delivered within 1 minute of the first attempt, or it is
wasted.

^The only ability named "swift poisoning" is the \[alchemist^(class/alchemist) class feature. There
is also a [swift poison](ref/talent/swift-poison) rogue talent and a
[swift poisoner](ref/ninjatrick/swift-poisoner) ninja trick that this could be referring to. Consult
your GM.\]\{from=1\}
