+++
id = "ref/arc-alchemist/grenadier-mc"
kind = "archetype"
title = "Grenadier (MC)"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grenadier_mc", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "monster-codex"
page = "116"

[fields]
kind = "archetype"
replaces = ["Brew Potion", "Poison resistance", "Poison use", "Swift poisoning", "Poison immunity"]
+++

Grenadiers train to exercise their talents in the thick of battle, even when not under the influence
of their mutagens. They learn methods of combining weapon attacks with their alchemical magic, and
sacrifice skill with poisons in order to become more adept at using alchemical bombs or using
alchemical items in conjunction with their martial skills. As an unusual side effect of their skill
at handling bombs and alchemical items with increased speed, grenadiers master the ability to drink
potions, elixirs, and mutagens quickly and without exposing themselves to peril while doing so. A
grenadier has the following class features.

**Martial Weapon Proficiency**

**Ability:** A grenadier picks one martial weapon to become proficient in the use of.

**Gained:** At 1st Level

**Replaces:** Brew Potion

**Alchemical Weapon (Su)**

**At 15th Level:** This ability becomes a **free action**.

**At 6th Level:** A grenadier can use her alchemical weapon ability as a **swift action**.

**Gained:** At 2nd Level

**Move:** A grenadier can infuse a weapon or piece of ammunition with a single harmful alchemical
liquid or powder, such as [alchemist's fire](ref/eq-weapon/alchemists-fire) or
[sneezing powder](ref/eq-weapon/sneezing-powder). This action consumes the alchemical item, but
transfers its effect to the weapon in question. The alchemical item takes full effect on the next
creature struck by the weapon, but does not splash, spread, affect additional targets, or benefit
from any other effects that specifically affect splash weapons. Any extra damage added is not
doubled on a critical hit. The alchemical treatment causes no harm to the weapon treated, and wears
off 1 minute after being applied if no blow is struck. Infusing a new alchemical item also removes
the effect of any alchemical liquid or powder previously applied with this ability.

**Replaces:** Poison resistance

**Precise Bombs (Ex)**

**Ability:** A grenadier gains the [precise bombs](ref/discovery/precise-bombs) alchemist discovery
as a bonus discovery.

**Gained:** At 2nd Level

**Replaces:** Poison use

**Directed Blast (Su)**

**Ability:** A grenadier can detonate a bomb so that it splashes in a 20-foot cone rather than
affecting a radius. The cone starts at the alchemist and extends away from her in the direction she
chooses. The alchemist designates one creature in the squares affected by the cone to be the target
of the bomb and makes her attack roll against that creature; all other squares in the cone take
splash damage. If the alchemist has the [explosive bomb](ref/discovery/explosive-bomb) discovery and
throws an explosive directed blast, the cone of splash damage is 30 feet long instead of 20 feet.

**Gained:** At 6th Level

**Replaces:** Swift poisoning

**Staggering Blast (Su)**

**Ability:** A grenadier's bombs become particularly overwhelming when they explode. Whenever a
grenadier confirms a critical hit with a bomb, the creature directly struck by that bomb is
[staggered](ref/misc/staggered) for 1d4+1 rounds. A successful Fortitude saving throw (DC equals the
bomb's Reflex save DC to avoid splash damage) reduces the duration to 1 round.

**Gained:** At 10th Level

**Replaces:** Poison immunity

**Special:** The effects of this ability stack with a [frost bomb's](ref/discovery/frost-bomb)
staggering effect, but not with the effects of the
[Staggering Critical](ref/feat/staggering-critical) feat. Additional critical hits from a staggering
blast add to the effect's overall duration.
