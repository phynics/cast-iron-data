+++
id = "ref/arc-inquisitor/cold-iron-warden"
kind = "archetype"
title = "Cold Iron Warden"
source_ids = ["demon-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cold_iron_warden", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "demon-hunters-handbook"
page = "15"

[fields]
kind = "archetype"
replaces = ["Track", "teamwork feats gained at 12th and 18th level", "Solo tactics", "teamwork feats gained at 6th and 15th level", "Teamwork feats gained at 3rd and 9th level", "Discern lies"]
alters = ["Bane"]
replaces_features = ["track", "solo-tactics", "discern-lies"]
alters_features = ["bane"]
+++

The natural enemies of [demoniacs](ref/pclass/demoniac) and other cultists of fiendish forces, cold
iron wardens are inquisitors who dedicate their lives to eradicating the taint of
[demonkind](ref/family/demon) from Golarion.

**Track Teleportation (Su)**

**Flavor:** A cold iron warden may acquire clues about a teleporting creature's destination by
closely examining the place it once stood.

**Fullround:** While standing in a square that a creature occupied when it cast a conjuration
(teleportation) spell or [spell-like ability](ref/umr/spell-like-abilities), the cold iron warden
may attempt a Survival check (DC 10 + the teleportation spell's caster level) to sense the direction
of the creature's destination as well as whether the destination lies within 25 feet, 100 feet,
1,000 feet, or more than 1,000 feet of her. She must use this ability within a number of rounds
after the creature's teleportation equal to 1/2 her inquisitor level, after which the trail goes
cold.

**At 12th Level:** If the cold iron warden exceeds the Survival check DC by 5 or more, she can also
sense the creature's location as if using the [locate creature](ref/spell/locate-creature) spell,
using her inquisitor level as the caster level.

**At 18th Level:** If the cold iron warden exceeds the Survival check DC by 10 or more, she can also
sense the creature's location as if she had cast [discern location](ref/spell/discern-location).

**Gained:** At 2nd Level

**Replaces:** Track, teamwork feats gained at 12th and 18th level

**Usage:** 1 time/day + 1 per 4 inquisitor levels beyond 2nd

**Abyssal Scourge (Su)**

**Ability:** She can [channel energy](ref/ability/channel-energy) as a cleric of her inquisitor
level - 2, but only to use Alignment Channel to damage outsiders. The DC of the Will save to halve
the damage is equal to 10 + 1/2 the inquisitor's level + the inquisitor's Charisma modifier.

**Choice:** A cold iron warden gains [Alignment Channel](ref/feat/alignment-channel) as a bonus feat
and must choose either chaotic or evil outsiders.

**At 15th Level:** Any chaotic or evil creature that casts a conjuration (teleportation) spell or
[spell-like ability](ref/umr/spell-like-abilities) while in the mist must succeed at a concentration
check (same DC as above) or lose the spell.

**At 6th Level:** The energy lingers in the affected area for 1 round as a shimmering, barely
perceptible, mist that disrupts Abyssal magic. A creature in the mist that casts a conjuration
(summoning) spell or [spell-like ability](ref/umr/spell-like-abilities) with the selected alignment
subtype must succeed at a [concentration](ref/rule/concentration) check (DC 15 + double the level of
the conjuration spell) or lose the spell.

**Gained:** At 3rd Level

**Replaces:** Solo tactics, teamwork feats gained at 6th and 15th level

**Special:** A cold iron warden can take other feats to add to this ability such as
[Improved Channel](ref/feat/improved-channel), but not feats that alter this ability, such as
[Command Undead](ref/feat/command-undead).

**Usage:** Charisma3 modifier times/day

**Favored Judgment**

**At 3rd Level:** The inquisitor gains [Favored Judgment](ref/feat/favored-judgment) as a bonus feat
but must choose either outsider (chaotic) or outsider (evil).

**At 9th Level:** She gains Favored Judgment as a bonus feat a second time and must choose either
outsider (chaotic) or outsider (evil).

**Replaces:** Teamwork feats gained at 3rd and 9th level

**Bane (Su)**

**Alters:** Bane

**Passive:** A cold iron warden reduces the amount of bonus damage dealt when using her bane ability
against creatures that are not outsiders with the chaotic or evil subtype by 1d6. She increases the
amount of bonus damage by 1d6 when she selects outsiders with the chaotic or evil subtype.

**Translate Telepathy (Su)**

**Ability:** An inquisitor can sense when a creature within 5 feet of her receives or sends a
telepathic message.

**Immediate:** By making a Perception check (DC 15 + the highest CR of the creatures using
telepathy), she may listen to all telepathic messages sent to and by creatures in this area for a
number of rounds per day equal to her inquisitor level. These rounds do not need to be consecutive.

**Gained:** At 5th Level

**Replaces:** Discern lies

At 10th level: The distance at which she can detect telepathic messages 10 feet.

At 15th level: The distance at which she can detect telepathic messages 15 feet.

At 20th level: The distance at which she can detect telepathic messages 20 feet.
