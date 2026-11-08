+++
id = "ref/arc-barbarian/giant-stalker"
kind = "archetype"
title = "Giant Stalker"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "giant_stalker", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]

[fields]
kind = "archetype"
replaces = ["Uncanny dodge", "Trap sense"]
alters = ["Rage"]
+++

**Sources:** Adventurer's Guide pg 130\
Of the dangerous creatures that roam grim peaks and icy steppes, giants are among the most feared.
They are cunning and capricious, and their ability to craft weapons and coordinate attacks makes
them a constant threat to the nomadic tribes in the region. In the wilds where giants hunt,
cleverness isn't the only thing the people need to survive - they require the fearlessness to
confront a challenge, no matter the size.

Elders select the children of the tribe's fiercest barbarians for the honor of becoming giant
stalkers. Through intense training, these children learn to spot and track giants using telltale
signs along with more subtle clues (such as giants' unique scents). They learn the giants' speech
and culture; they study their traditions and brutality; and most importantly, they foster their
hatred of these oversized foes.

When [Mammoth Lord](ref/rule/aff-beast-riders) followings travel, giant stalkers scout ahead,
securing safe passage through giant-infested territories. They clear giant hunting parties and
ambushes, using gruesome trophies to mark the trails. Sometimes giant hunters send their own raiding
parties into the mountains to capture young giants, as most followings keep giant thralls as symbols
of status.

**Harangue Giant (Ex)**

**Alters:** Rage

**Passive:** While _raging,_ a giant stalker can speak Giant. If the giant stalker already knows
Giant, she gains a +2 bonus on Intimidate checks when speaking Giant while _raging._

**Smell Giants (Ex)**

**Ability:** A giant stalker gains the [scent](ref/umr/scent) special ability, but with regard only
to humanoids with the giant subtype.

**Gained:** At 2nd Level

**Replaces:** Uncanny dodge

**Giant Baiter (Su)**

**At 12th Level:** She can bait up to three giants at once.

**At 15th Level:** Baiting giants becomes a **free action**.

**At 18th Level:** A giant stalker can bait a number of giants equal to 3 + her Constitution
modifier.

**At 6th Level:** A giant stalker can bait two giants at once.

**At 9th Level:** Baiting giants becomes a **swift action**.

**Gained:** At 3rd Level

**Move:** A _raging_ giant stalker can erupt into a violent or vulgar display directed at a single
giant within 60 feet. This display is infused with secret magical traditions that draw upon the
Mammoth Lords' ancestral enmities toward giants. A targeted giant must succeed at a Will save (DC =
10 + [half](ref/misc/fractions-and-rounding) the giant stalker's barbarian level + the giant
stalker's Constitution modifier) or be compelled to focus its attacks on the giant stalker; this
ability can also affect non-giant creatures that are Large or larger, though such creatures gain a
+4 bonus on the Will save to resist the effect. This compulsion ends if the giant stalker is out of
sight or inaccessible to the giant's attacks. While baited, a giant is distracted and enraged by the
insults - a giant stalker gains a dodge bonus to her AC against any giant she has successfully
baited. This dodge bonus is equal to one-third of her barbarian level. Once baited, a giant remains
baited for a number of rounds equal to the giant stalker's Constitution modifier, or until the giant
stalker's _rage_ ends (whichever comes first). If the giant stalker baits a different giant, any
previously baited giant is no longer baited.

**Replaces:** Trap sense

**Special:** A giant that successfully saves against baiting is immune to that giant stalker's giant
baiter ability for 24 hours. This is a language-dependent mind affecting effect.

**Giant Stalker Rage Powers**

**Info:** A giant stalker gains access to the following rage powers.

**Giant Stalker Defense (Ex)**

**Passive:** When _raging,_ a giant stalker does not take a penalty to Armor Class against attacks
from giants.

**Topple Giant (Ex)**

**Ability:** When _raging,_ the giant stalker does not provoke attacks of opportunity when she
attempts to [trip](ref/rule/trip) a giant, and can attempt to trip a giant that is up to two size
categories larger than she is.

**Underfoot (Ex)**

**Move:** When _raging,_ the giant stalker can attempt to enter a giant's space, provided she is at
least one size category smaller than the giant. Doing so requires a successful combat maneuver check
against the giant's CMD. If she succeeds, she enters a square in the giant's space. If she makes an
attack against the giant while sharing its space, the giant is treated as being
[flat-footed](ref/rule/flat-footed) against her. At the end of her turn, she exits the giant's space
into any square adjacent to the giant's space.

**Provokes attack of opportunity:** No
