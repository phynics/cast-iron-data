+++
id = "ref/arc-investigator/cryptid-scholar"
kind = "archetype"
title = "Cryptid Scholar"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cryptid_scholar", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "18"

[fields]
kind = "archetype"
replaces = ["Poison lore", "poison resistance", "Studied combat", "Studied strike"]
replaces_features = ["poison-lore", "poison-resistance", "studied-combat", "studied-strike"]
+++

Cryptid scholars research monsters that lurk secretly at the edge of civilization, developing a deep
expertise regarding their anatomy, habits, and ecology. Most cryptid scholars are affiliated with
the University of Lepidstadt, but spend more time away performing field work than they do consorting
with their fellow scholars (many of whom find a cryptid scholar's peculiar specialty suspicious at
best). Although competent as lone monster hunters, cryptid scholars excel when they have associates
with whom to share their insights.

**Intuitive Monster Lore (Ex)**

**At 5th Level:** A cryptid scholar can take 10 on such checks, even when threatened or distracted.

**Passive:** A cryptid scholar adds his Wisdom modifier on Knowledge skill checks in addition to his
Intelligence modifier when attempting skill checks to identify the abilities and weaknesses of
creatures.

**Replaces:** Poison lore, poison resistance

**Opportune Advice (Ex)**

**Info:** The cryptid scholar cannot choose investigator talents that add effects to _studied
combat_ or _studied strike._

**Gained:** At 4th Level

**Move:** When the cryptid scholar succeeds at a Knowledge check to identify a monster's special
powers or vulnerabilities, he can share his insights with his allies. Allies within 30 feet who can
hear the cryptid scholar gain an insight bonus to their ACs and on saving throws against
extraordinary, supernatural, and [spell-like abilities](ref/umr/spell-like-abilities) used by
creatures of the same type and all the same subtypes as the monster identified. This bonus is equal
to one-fourth of his investigator level, and it lasts for a number of rounds equal to the cryptid
scholar's Intelligence modifier (minimum 1) or until he uses _knowledgeable strike_ (see below),
whichever comes first. A creature cannot benefit from opportune advice regarding more than one
specific kind of monster at a time.

**Replaces:** Studied combat

**Special:** Once the cryptid scholar has used this ability to provide a bonus against a specific
kind of monster, he can't grant a bonus against that same kind of monster again for 24 hours, unless
he expends one use of _inspiration_ when taking a move action to use this ability.

**Knowledgeable Strike (Ex)**

**Ability:** If the cryptid scholar ends his _opportune advice_ early as a **move action**, each
ally within 30 feet who can hear the cryptid scholar deals +1d6 additional damage on its next
successful unarmed, natural, or weapon attack against that specific kind of monster within 1 round.

**Flavor:** The cryptid scholar can direct allies to exploit a monster's weaknesses.

**Gained:** At 4th Level

**Replaces:** Studied strike

**Special:** The damage of _knowledgeable strike_ is precision damage and is not multiplied on a
critical hit; creatures that are immune to sneak attacks are also immune to _knowledgeable strike._
Ranged attacks gain this additional damage only against a target within 30 feet. The ally must be
able to see the target well enough to pick out a vital spot and must be able to reach such a spot.
_Knowledgeable strike_ cannot be used against a creature with [concealment](ref/rule/concealment).

At 8th level: The damage +2d6.

At 12th level: The damage +3d6.

At 16th level: The damage +4d6.

At 20th level: The damage +5d6.
