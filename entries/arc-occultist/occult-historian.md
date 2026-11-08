+++
id = "ref/arc-occultist/occult-historian"
kind = "archetype"
title = "Occult Historian"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "occult_historian", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]

[fields]
kind = "archetype"
replaces = ["Object reading", "aura sight", "3rd-level focus power", "Outside contact 2, 3, and 4"]
+++

**Sources:** Ultimate Wilderness pg 67\
Many wilderness areas contain the remnants of ancient civilizations, with some waiting to be
discovered and some held by fierce monsters or devious cults. An occult historian seeks these ruins
not only for their esoteric artifacts but also to learn the structures' secrets.

**Ruin Reading (Su)**

**Ability:** An occult historian can glean secrets from ruined structures. She must spend 1 minute
examining and touching part of the structure (such as a wall or a doorframe). At the end of the
minute, the occult historian attempts a Knowledge (history) check. If the ruin has been claimed as a
lair for a creature, the DC of this check is equal to 10 + the CR of the most powerful creature in
the ruin. If the ruin holds a magic item (or multiple magic items), the DC of this check is equal to
11 + the highest caster level of all the magic items in the ruin. If the occult historian succeeds
at the check, she learns the layout of the area of the ruin within 30 feet of her (including any
secret doors), as well as a piece of information about the structure's history (as determined by the
GM).

**At 5th Level:** The occult historian can see into a ruin's past. This reveals the same information
that can be gathered with the spell [retrocognition](ref/spell/retrocognition), except the occult
historian can use it only in ruins. If the occult historian succeeds at the check outlined above,
she sees the events that occurred in the ruin over the past hour; for each minute she concentrates,
she can see 1 additional hour into the ruin's past. If the result of her check exceeds the DC by 5
or more, she can see the events that occurred over the past week, plus for 1 additional week per
minute she concentrates. If the result of her check exceeds the DC by 10 or more, she can see the
events of the past year, plus for 1 additional year per minute she concentrates. If the result of
her check exceeds the DC by 20 or more, she can see the events of the past century, plus for 1
additional century per minute she concentrates.

**Gained:** At 2nd Level

**Replaces:** Object reading, aura sight

**Usage:** 1 time/day + 1 per 4 occultist levels beyond 2nd

**Trap Sense (Ex)**

**Gained:** At 3rd Level

**Passive:** An occult historian gains [trap sense](ref/ability/trap-sense), as per the rogue class
feature of the same name, giving her a bonus on Reflex saves made to avoid traps and a dodge bonus
to AC against attacks made by traps. This bonus is equal to one-third of her occultist level.

**Replaces:** 3rd-level focus power

**Crumbling Strike (Su)**

**Ability:** The occult historian can make a melee attack against a single target at her highest
base attack bonus. If she hits, she deals 2d6 points of damage per occultist level she has (maximum
40d6). If the target succeeds at a Fortitude save (the save DC is equal to 10 + half the occult
historian's occultist level + her Intelligence modifier), it takes only 5d6 points of damage. A
creature slain by this attack crumbles to dust.

**Flavor:** An occult historian can channel the erosion of countless ages into a single melee
strike.

**Gained:** At 12th Level

**Replaces:** Outside contact 2, 3, and 4

**Usage:** 1 time/day + 1 per 4 occultist levels beyond 12th
