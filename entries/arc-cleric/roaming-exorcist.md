+++
id = "ref/arc-cleric/roaming-exorcist"
kind = "archetype"
title = "Roaming Exorcist"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Roaming%20Exorcist"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "roaming_exorcist", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "18"

[fields]
kind = "archetype"
alters = ["Domains", "channel energy", "armor proficiency"]
+++

The roaming exorcist travels far and wide to root out possessions, hauntings, and hidden evils. The
roaming exorcist extracts unruly spirits from not only victims of possession, but also haunted sites
and accursed items.

**Skill Ranks per Level**

**Info:** 4 + Int modifier.

**Dedicated Wanderer**

**Alters:** Domains, channel energy, armor proficiency

**Flavor:** A roaming exorcist is dedicated to her cause and affords no time to other pursuits
typical of clerics.

**Info:** A roaming exorcist must choose to channel positive energy. She may choose only one domain
from her deity's list of domains, rather than the normal two domains, and she does not gain Medium
Armor Proficiency or Shield Proficiency.

**Unseen Revealed (Ex)**

**Gained:** At 1st Level

**Passive:** A roaming exorcist gains a bonus equal to [half](ref/misc/fractions-and-rounding) her
cleric level (minimum +1) on Perception checks to detect haunts and incorporeal creatures and on
Sense Motive checks to determine whether a creature is possessed, under the effects of an
enchantment or curse, or otherwise magically controlled.

**Spirit Sleuth (Ex)**

**Free:** Upon interacting with a rejuvenating spirit or haunt for the first time (such as by
attacking the spirit or channeling energy to damage the haunt), a roaming exorcist can attempt a
Sense Motive check to determine the specific course of action required to permanently neutralize the
spirit or haunt (DC = 10 + the undead creature's Hit Dice or the haunt's CR).

**Gained:** At 2nd Level

**Curse Seeker (Su)**

**Flavor:** A roaming exorcist can more readily identify cursed items.

**Gained:** At 5th Level

**Passive:** When identifying a magic item, the roaming exorcist needs to exceed the item's DC by
only 5 (instead of by 10) in order to determine whether the item is cursed.

**Dispossession (Su)**

**Ability:** A roaming exorcist can expend one use of her _channel energy_ ability to force a
possessing creature from its host body. The exorcist must make a melee touch attack against the
possessed creature; if successful, the roaming exorcist deals damage to the possessing creature as
if it were targeted by the roaming exorcist's _channel energy_ ability (regardless of the possessing
creature's creature type), and the possession effect ceases as the possessing creature is ejected
from the host body. A successful Will save (DC = the roaming exorcist's _channel energy_ DC) halves
the damage taken, and the possessing creature resists being ejected from its host.

**Gained:** At 8th Level

**Curse Eater (Su)**

**Ability:** A roaming exorcist gains [Improved Disarm](ref/feat/improved-disarm) as a bonus feat,
regardless of whether she meets the feat's prerequisites.

**Gained:** At 11th Level

**Passive:** The roaming exorcist gains a +2 bonus on combat maneuver checks to disarm a creature of
a magic item she knows to be cursed.

**Special:** If the roaming exorcist successfully disarms a creature of a cursed item without using
a weapon, she may automatically pick up the disarmed cursed item without immediately succumbing to
the item's curse. She may wield or hold this cursed item for a number of rounds equal to her
Charisma modifier (minimum 1 round) - during which time she may use the item normally, as if it were
not cursed - before the item's curse manifests again.
