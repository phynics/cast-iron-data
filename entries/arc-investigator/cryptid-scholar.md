+++
id = "ref/arc-investigator/cryptid-scholar"
kind = "archetype"
title = "Cryptid Scholar"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Cryptid%20Scholar"
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
features = [
  { anchor = "intuitive-monster-lore" },
  { anchor = "opportune-advice", level = 4 },
  { anchor = "knowledgeable-strike", level = 4 },
]
trades = [
  { replaces = "Poison lore", feature = "poison-lore", by = ["intuitive-monster-lore"] },
  { replaces = "poison resistance", feature = "poison-resistance", by = ["intuitive-monster-lore"] },
  { replaces = "Studied combat", feature = "studied-combat", by = ["opportune-advice"] },
  { replaces = "Studied strike", feature = "studied-strike", by = ["opportune-advice", "knowledgeable-strike"] },
]
+++

Cryptid scholars research monsters that lurk secretly at the edge of civilization, developing a deep
expertise regarding their anatomy, habits, and ecology. Most cryptid scholars are affiliated with
the University of Lepidstadt, but spend more time away performing field work than they do consorting
with their fellow scholars (many of whom find a cryptid scholar's peculiar specialty suspicious at
best). Although competent as lone monster hunters, cryptid scholars excel when they have associates
with whom to share their insights.

## Intuitive Monster Lore (Ex) {#intuitive-monster-lore}

A cryptid scholar adds his Wisdom modifier on Knowledge skill checks in addition to his Intelligence
modifier when attempting skill checks to identify the abilities and weaknesses of creatures. At 5th
level, a cryptid scholar can take 10 on such checks, even when threatened or distracted.

This ability replaces poison lore and poison resistance.

## Opportune Advice (Ex) {#opportune-advice}

At 4th level, when the cryptid scholar succeeds at a Knowledge check to identify a monster's special
powers or vulnerabilities, he can take a move action to share his insights with his allies. Allies
within 30 feet who can hear the cryptid scholar gain a +1 insight bonus to their ACs and on saving
throws against extraordinary, supernatural, and [spell-like abilities](ref/umr/spell-like-abilities)
used by creatures of the same type and all the same subtypes as the monster identified. This bonus
lasts for a number of rounds equal to the cryptid scholar's Intelligence modifier (minimum 1) or
until he uses knowledgeable strike (see below), whichever comes first. This bonus increases by 1 at
8th level and every 4 investigator levels thereafter (to a maximum of +5 at 20th level). A creature
cannot benefit from opportune advice regarding more than one specific kind of monster at a time.

Once the cryptid scholar has used this ability to provide a bonus against a specific kind of
monster, he can't grant a bonus against that same kind of monster again for 24 hours, unless he
expends one use of inspiration when taking a move action to use this ability.

This ability replaces studied combat, and the cryptid scholar cannot choose investigator talents
that add effects to studied combat or studied strike.

## Knowledgeable Strike (Ex) {#knowledgeable-strike}

At 4th level, the cryptid scholar can direct allies to exploit a monster's weaknesses. If the
cryptid scholar ends his opportune advice early as a move action, each ally within 30 feet who can
hear the cryptid scholar deals additional damage on its next successful unarmed, natural, or weapon
attack against that specific kind of monster within 1 round. The additional damage is 1d6 at 4th
level and increases by 1d6 for every 4 investigator levels thereafter (to a maximum of 5d6 at 20th
level). The damage of knowledgeable strike is precision damage and is not multiplied on a critical
hit; creatures that are immune to sneak attacks are also immune to knowledgeable strike. Ranged
attacks gain this additional damage only against a target within 30 feet. The ally must be able to
see the target well enough to pick out a vital spot and must be able to reach such a spot.
Knowledgeable strike cannot be used against a creature with [concealment](ref/rule/concealment).

This ability replaces studied strike.
