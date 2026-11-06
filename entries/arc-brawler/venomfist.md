+++
id = "ref/arc-brawler/venomfist"
kind = "archetype"
title = "Venomfist"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "venomfist", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Wilderness pg 43\
Thanks to alchemical experiments and rigorous study of venomous creatures, a venomfist has toxic
unarmed strikes.

**Venomous Strike (Ex)**

**Ability:** A venomfist's unarmed strikes deal damage as a creature
[one size category smaller](ref/misc/damage-die-adjustments) (1d4 at first level for Medium
venomfists). If she hits with her first unarmed strike in a round, the target must succeed at a
Fortitude saving throw (DC = 10 + [half](ref/misc/fractions-and-rounding) the venomfist's brawler
level + her Constitution modifier) or take an additional amount of damage equal to the venomfist's
Constitution modifier. The venomfist is immune to this toxin.

**Alters:** Unarmed strike

**At 10th Level:** When the venomfist chooses the condition her venom imposes, she can also cause
her venom to deal [ability score damage](ref/rule/ability-damage-drain) each round instead of hit
point damage. She chooses Strength, Dexterity, or Constitution, and her venom deals 1d3 points of
ability score damage each round. In addition, she adds [blinded](ref/misc/blinded),
[exhausted](ref/misc/exhausted), and [staggered](ref/misc/staggered) to the list of secondary
effects she can choose for her venom.

**At 16th Level:** The venomfist's venom is particularly potent. If it fails the initial save, the
target must succeed at two consecutive saves before being cured of the venom, though if the first
save is successful, the secondary effect ends and the creature is immune to the secondary effects of
the venomfist's poison for 24 hours. In addition, the venomfist adds [dazed](ref/misc/dazed) and
[stunned](ref/misc/stunned) to the list of secondary effects she can choose for her venom.

**At 4th Level:** A target that fails this save must succeed at a second saving throw 1 round later
or take the same amount of damage again. This effect repeats as long as the target continues to fail
its saving throws, to a maximum number of rounds equal to 1 plus 1 additional round for every 4
brawler levels the venomfist has. Unlike other poisons, multiple doses of a venomfist's poison never
stack; the more recent poison effect replaces the older one.

**At 5th Level:** After the venomfist gets 8 hours of rest, she can choose a secondary effect for
her venom to impose. She can choose [fatigued](ref/misc/fatigued), [shaken](ref/misc/shaken), or
[sickened](ref/misc/sickened). A creature that fails its saving throw against her venom also gains
the chosen condition until it succeeds at a save against the venom or until the venom's duration
ends. Once a creature succeeds at its save against the poison, it becomes immune to the secondary
condition for 24 hours, but the attack still deals the extra damage.

**Replaces:** Knockout, close weapon mastery

**Special:** This is a poison effect. The venomfist can't suppress it, but she affects only those
she damages with her unarmed strikes (not those she merely touches).
