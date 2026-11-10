+++
id = "ref/arc-bard/prankster"
kind = "archetype"
title = "Prankster"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Prankster"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prankster", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-race-guide"
page = "35"

[fields]
kind = "archetype"
replaces = ["Fascinate", "Suggestion", "Mass suggestion", "Lore master"]
replaces_features = ["lore-master"]
+++

The prankster sees humor as the highest form or art, and pranks as the highest form of humor. In
addition to setting friends up for light-hearted pranks, the prankster can use his quick wit and
cruel sense of humor to enrage foes before incapacitating them with a clever turn of phrase.

**Prerequisites:** Gnome

**Bardic Performance**

**Info:** A prankster's bardic performance functions like a bard's, but some of its performances are
exchanged for those listed below.

**Mock (Su)**

**At 1st Level:** The prankster can use his performance to cause one creature to become furious with
him. The creature to be mocked must be within 90 feet, able to see, hear, and understand the
prankster, and capable of paying attention to him. The prankster must also be able to see the
creature affected. A creature within range receives a Will save (DC 10 +
[half](ref/misc/fractions-and-rounding) the prankster's level + the prankster's Charisma modifier)
to negate the effect. If a creature's saving throw succeeds, the prankster cannot successfully mock
that creature for 24 hours. If its saving throw fails, the creature is angered by the performance
and seeks to harm the prankster. While the prankster maintains the mocking, the target takes a -2
penalty on all attack rolls and skill checks until it has successfully attacked the prankster with a
melee or ranged attack, or has harmed the creature with a spell that deals damage.

**At 10th Level:** He can mock four at once.

**At 13th Level:** He can mock five creatures at once.

**At 16th Level:** He can mock six at once.

**At 19th Level:** He can mock seven people at once.

**At 4th Level:** He can mock two people at once.

**At 7th Level:** He can mock three creatures at once.

**Replaces:** Fascinate

**Special:** Mock is an enchantment (compulsion) mind-affecting ability. Mock relies on audible and
visual components in order to function.

**Punchline (Sp)**

**Ability:** The prankster can use his performance to tell a punchline to amuse a creature he has
already _mocked_ (see above), goading it into [hideous laughter](ref/spell/hideous-laughter) (as the
spell). Using this ability does not disrupt the _mock_ effect, but it does require a **standard
action** to activate (in addition to the **free action** to continue the _mock_ effect). This
ability affects only a single creature. A prankster can use this ability more than once against an
individual creature during an individual performance.

**Gained:** At 6th Level

**Replaces:** Suggestion

**Special:** Telling a punchline does not count against a prankster's daily use of bardic
performance. A Will saving throw (DC 10 + 1/2 the bard's level + the bard's Charisma modifier)
negates the effect. Punchline is an enchantment (compulsion), mind affecting, language-dependent
ability and relies on audible components.

**Mass Punchline (Sp)**

**Ability:** This ability functions just like _punchline,_ but allows a prankster of 18th level or
higher to use _[hideous laughter](ref/spell/hideous-laughter)_ simultaneously against any number of
creatures that he has mocked.

**Gained:** At 18th Level

**Replaces:** Mass suggestion

**Swap (Ex)**

**Ability:** A prankster can steal an object from a creature and replace it with another object of
the same size or smaller that the prankster has in his hand. This functions as the
[steal](ref/rule/steal) combat maneuver, but the prankster does not provoke an attack of
opportunity, and may use his Sleight of Hand check in place of his combat maneuver check. If the
prankster's check exceeds the target's CMD by 10 or more, the target is unaware the swap has been
made until it tries to use the swapped object or the end of its next turn (whichever happens first).

**Replaces:** Lore master
