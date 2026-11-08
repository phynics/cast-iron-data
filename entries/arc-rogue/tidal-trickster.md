+++
id = "ref/arc-rogue/tidal-trickster"
kind = "archetype"
title = "Tidal Trickster"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tidal_trickster", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]

[fields]
kind = "archetype"
replaces = ["Trapfinding", "trap sense", "Uncanny dodge, 4th-level rogue talent", "Improved uncanny dodge, 8th-level rogue talent"]
alters = ["Sneak attack"]
+++

**Sources:** Aquatic Adventures pg 55\
Tidal tricksters roam the seas, using their skillful mastery of the currents to move across aquatic
battlefields and throw their enemies off-balance.

**Wisdom of the Waves (Ex)**

**Ability:** A tidal trickster gains a swim speed equal to her unmodified base land speed (or
increases her swim speed by 10 feet, if she has a racial swim speed). Instead of the +8 bonus
granted by a swim speed, she gains a racial bonus on Swim checks equal to 4 + half her rogue level
(if she has a racial swim speed, she uses the better bonus).

**At 3rd Level:** She gains a bonus on Will saves whenever she is underwater. This bonus is equal to
one-third of her rogue level.

**Passive:** She gains a bonus on Bluff checks equal to half her rogue level.

**Replaces:** Trapfinding, trap sense

**Liquid Disruption (Ex)**

**Ability:** She can deal sneak attack damage to [oozes](ref/type/ooze) and creatures with the
[water](ref/subtype/water) subtype that are normally immune to precision damage (such as
[water elementals](ref/monster/water-elemental)), and she ignores a
[hydrokineticist's](ref/class/kineticist) chance to negate precision damage from _elemental
overflow._

**Alters:** Sneak attack

**Flavor:** A tidal trickster can use her knowledge of the cohesion of liquids to disrupt certain
foes.

**Gained:** At 4th Level

**Replaces:** Uncanny dodge, 4th-level rogue talent

**Tidal Distortion (Ex)**

**Ability:** While making a full attack underwater, a tidal trickster can give up one attack to
create a _tidal distortion._ When she creates a _tidal distortion,_ the tidal trickster moves up to
10 feet. If any part of her movement includes a square adjacent to one or more foes, she can choose
one of those foes and attempt a Bluff check with a DC of 11 + either the enemy's Sense Motive or
Swim modifier, whichever is higher. Her Bluff check is subject to any penalties the attack roll she
sacrificed would have taken, and if she trades an iterative attack gained from having a high base
attack bonus, she also takes a penalty based on that attack's lower base attack bonus (a -5 penalty
for the second iterative attack, a -10 penalty for the third iterative attack, and a -15 penalty for
the fourth iterative attack, if she manages to gain one). If she succeeds at the Bluff check, the
movement doesn't provoke an attack of opportunity from that foe and the foe becomes
[off-balance](ref/rule/off-balance-and-prone-underwater) until its next turn.

**Gained:** At 8th Level

**Replaces:** Improved uncanny dodge, 8th-level rogue talent

**Special:** A tidal trickster can give up any number of her attacks in a given full attack to
create _tidal distortions,_ but she can't give up two consecutive attacks.
