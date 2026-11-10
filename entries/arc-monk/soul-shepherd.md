+++
id = "ref/arc-monk/soul-shepherd"
kind = "archetype"
title = "Soul Shepherd"
source_ids = ["pathfinder-139-the-dead-road"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_shepherd", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "pathfinder-139-the-dead-road"
page = "65"

[fields]
kind = "archetype"
replaces = ["Stunning fist", "Evasion", "improved evasion", "Abundant step", "Quivering palm"]
replaces_features = ["stunning-fist", "evasion", "improved-evasion", "abundant-step", "quivering-palm"]
+++

Whether studying at the feet of psychopomps or merely imitating the creatures' philosophy and
methods, soul shepherds believe in safeguarding the Cycle of Souls.

**Calming Strike (Su)**

**Ability:** The soul shepherd can use this ability against a haunt by making a touch attack against
an AC of 10 + the haunt's CR. A haunt does not receive a saving throw against this ability, but the
ability's duration changes to concentration + 1 round, up to 1 round per level.

**Immediate:** After hitting an incorporeal undead creature with an unarmed strike, a soul shepherd
can attempt to calm the creature, encouraging it to move peacefully to the next stage of its
metaphysical journey. The target must succeed at a Will save (DC = 10 + half soul shepherd's level +
the soul shepherd's Wisdom modifier) or be calmed, as [calm spirit](ref/spell/calm-spirit), for 1
minute.

**Replaces:** Stunning fist

**Usage:** 1 time/day per monk level

**Otherworldly Resilience (Ex)**

**At 9th Level:** This improves to DR 5/adamantine, cold resistance 10, and electricity
resistance 10.

**Gained:** At 2nd Level

**Passive:** A soul shepherd gains [DR](ref/rule/damage-reduction) 2/adamantine, cold resistance 5,
and electricity resistance 5.

**Replaces:** Evasion, improved evasion

**Spirit Sense (Su)**

**Gained:** At 12th Level

**Replaces:** Abundant step

**Swift:** A soul shepherd can spend 1 point from his _ki pool_ to grant himself the ability to
notice, locate, and distinguish between living and undead creatures within 30 feet, just as if he
had a [psychopomp's](ref/subtype/psychopomp) _spiritsense_ ability, for a number of rounds equal to
his Wisdom modifier (minimum 1).

**Yamaraj's Judgment (Sp)**

**Gained:** At 15th Level

**Replaces:** Quivering palm

**Standard:** A soul shepherd can spend 1 point from his _ki pool_ to attempt to free an enslaved
soul from an effect that is imprisoning it, such as [soul bind](ref/spell/soul-bind) or
[trap the soul](ref/spell/trap-the-soul). This functions as a targeted
[dispel magic](ref/spell/dispel-magic) spell with a caster level equal to the soul shepherd's level.
He can spend an additional ki point when he activates this ability to gain a +4 bonus on the caster
level check. If the soul is held prisoner by a creature or a non-spell effect, the soul shepherd
frees it if his caster level check result is at least 11 + the creature or effect's CR.
