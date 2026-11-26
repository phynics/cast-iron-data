+++
id = "ref/arc-rogue/tidal-trickster"
kind = "archetype"
title = "Tidal Trickster"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Tidal%20Trickster"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tidal_trickster", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "aquatic-adventures"
page = "55"

[fields]
kind = "archetype"
features = [
  { anchor = "wisdom-of-the-waves", level = 1 },
  { anchor = "liquid-disruption", level = 4 },
  { anchor = "tidal-distortion", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["wisdom-of-the-waves"] },
  { replaces = "trap sense", feature = "trap-sense", by = ["wisdom-of-the-waves"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["liquid-disruption"] },
  { replaces = "4th-level rogue talent", feature = "rogue-talents", levels = [4], by = ["liquid-disruption"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["tidal-distortion"] },
  { replaces = "8th-level rogue talent", feature = "rogue-talents", levels = [8], by = ["tidal-distortion"] },
  { alters = "Sneak attack", feature = "sneak-attack", by = ["liquid-disruption"] },
]
+++

Tidal tricksters roam the seas, using their skillful mastery of the currents to move across aquatic
battlefields and throw their enemies off-balance.

## Wisdom of the Waves (Ex) {#wisdom-of-the-waves}

A tidal trickster gains a swim speed equal to her unmodified base land speed (or increases her swim
speed by 10 feet, if she has a racial swim speed). Instead of the +8 bonus granted by a swim speed,
she gains a racial bonus on Swim checks equal to 4 + half her rogue level (if she has a racial swim
speed, she uses the better bonus). She gains a bonus on Bluff checks equal to half her rogue level.
At 3rd level, she gains a +1 bonus on Will saves whenever she is underwater; this bonus increases by
1 at 6th level and every 3 levels thereafter.

This ability replaces trapfinding and trap sense.

## Liquid Disruption (Ex) {#liquid-disruption}

At 4th level, a tidal trickster can use her knowledge of the cohesion of liquids to disrupt certain
foes. She can deal sneak attack damage to [oozes](ref/type/ooze) and creatures with the
[water](ref/subtype/water) subtype that are normally immune to precision damage (such as
[water elementals](ref/monster/water-elemental)), and she ignores a
[hydrokineticist's](ref/class/kineticist) chance to negate precision damage from elemental overflow.

This ability alters sneak attack and replaces uncanny dodge and the 4th-level rogue talent.

## Tidal Distortion (Ex) {#tidal-distortion}

At 8th level, while making a full attack underwater, a tidal trickster can give up one attack to
create a tidal distortion. When she creates a tidal distortion, the tidal trickster moves up to 10
feet. If any part of her movement includes a square adjacent to one or more foes, she can choose one
of those foes and attempt a Bluff check with a DC of 11 + either the enemy's Sense Motive or Swim
modifier, whichever is higher. Her Bluff check is subject to any penalties the attack roll she
sacrificed would have taken, and if she trades an iterative attack gained from having a high base
attack bonus, she also takes a penalty based on that attack's lower base attack bonus (a -5 penalty
for the second iterative attack, a -10 penalty for the third iterative attack, and a -15 penalty for
the fourth iterative attack, if she manages to gain one). If she succeeds at the Bluff check, the
movement doesn't provoke an attack of opportunity from that foe and the foe becomes
[off-balance](ref/rule/off-balance-and-prone-underwater) (see page 45) until its next turn. A tidal
trickster can give up any number of her attacks in a given full attack to create tidal distortions,
but she can't give up two consecutive attacks.

This ability replaces improved uncanny dodge and the 8th-level rogue talent.
