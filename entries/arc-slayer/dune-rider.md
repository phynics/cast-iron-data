+++
id = "ref/arc-slayer/dune-rider"
kind = "archetype"
title = "Dune Rider"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Dune%20Rider"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dune_rider", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "86"

[fields]
kind = "archetype"
replaces = ["Track", "fast tracker", "Studied target", "Stalker", "slayer talent gained at 4th level", "Slayer talent gained at 8th level", "Master slayer"]
replaces_features = ["track", "studied-target", "stalker", "master-slayer"]
+++

Mounted harriers, saboteurs, and skirmishers, dune riders can disrupt even the most organized
opposition.

**Sand Foot (Ex)**

**At 11th Level:** The dune rider and his mount no longer treat sand or rocky ground as
[difficult terrain](ref/rule/terrain-and-obstacles), and they gain a +10-foot enhancement bonus to
their base speed in warm deserts, hills, and mountains.

**Passive:** The dune rider adds half his level as a bonus on Ride checks in warm deserts, hills,
and mountains.

**Replaces:** Track, fast tracker

**Desert Skirmisher (Ex)**

**Passive:** The dune rider excels in combat in warm deserts, hills, and mountains. While in such
terrain, he gains a +2 bonus on initiative, Perception, and Stealth checks, and a +1 bonus on attack
and damage rolls.

**Replaces:** Studied target

**Galloping Fire (Ex)**

**At 7th Level:** These penalties now decrease by 4.

**Gained:** At 4th Level

**Passive:** The penalties for the dune rider's ranged attacks while mounted decrease by 2.

**Replaces:** Stalker, slayer talent gained at 4th level

**Dust Vision (Ex)**

**Flavor:** The dune rider is at home in the desert.

**Gained:** At 8th Level

**Passive:** He exists comfortably in hot conditions up to 140&deg& Fahrenheit without having to
attempt Fortitude saves. His equipment is likewise protected. He takes no penalties on Perception
checks from blowing sand, dust, or heat shimmers, nor do these effects grant
[concealment](ref/rule/concealment) to the dune rider's enemies within 30 feet. Effects that would
grant total concealment work normally.

**Replaces:** Slayer talent gained at 8th level

**Dunes of Death (Su)**

**Flavor:** A dune rider can use the desert's heat to finish off his foes.

**Gained:** At 20th Level

**Replaces:** Master slayer

**Special:** Whether or not the target succeeds, it can't be targeted by this ability again for 24
hours.

**Standard:** He can make a single attack at his full base attack bonus while in warm desert, hills,
or mountains, choosing one of the following effects: kill, knock unconscious for 1d4 hours, or
paralyze for 2d6 rounds. If the attack hits, the target takes damage normally and must succeed at a
Fortitude save or suffer the additional effect. The DC of this save is 20 + the dune rider's
Intelligence modifier.
