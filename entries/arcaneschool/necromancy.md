+++
id = "ref/arcaneschool/necromancy"
kind = "rule"
title = "Necromancy"
source_ids = ["core-rulebook", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "necromancy", path = "json/class_ability_arcane_schools.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 81\
The dread and feared necromancer commands undead and uses the foul power of unlife against his
enemies.

**Power over Undead (Su)**

**At 20th Level:** Undead cannot add their [channel resistance](ref/rule/channel-resistance) to the
save against this ability.

**Gained:** At 1st Level

**Standard:** You receive [Command Undead](ref/feat/command-undead) or
[Turn Undead](ref/feat/turn-undead) as a bonus feat, and you can
[channel energy](ref/ability/channel-energy), but only to use the selected feat. You can take other
feats to add to this ability, such as [Extra Channel](ref/feat/extra-channel) and
[Improved Channel](ref/feat/improved-channel), but not feats that alter this ability, such as
[Elemental Channel](ref/feat/elemental-channel) and [Alignment Channel](ref/feat/alignment-channel).
The DC to save against these feats is equal to 10 + 1/2 your wizard level + your Charisma modifier.

**Usage:** Int3 modifier times/day

**Grave Touch (Sp)**

**Gained:** At 1st Level

**Standard:** You can make a melee touch attack that causes a living creature to become
[shaken](ref/misc/shaken) for a number of rounds equal to 1/2 your wizard level (minimum 1). If you
touch a shaken creature with this ability, it becomes [frightened](ref/misc/frightened) for 1 round
if it has fewer Hit Dice than your wizard level.

**Usage:** Int3 modifier times/day

**Life Sight (Su)**

**At 12th Level:** The range increases to 20 feet.

**At 16th Level:** The range increases to 30 feet.

**At 20th Level:** The range increases to 40 feet.

**Gained:** At 8th Level

**Passive:** You gain [blindsight](ref/umr/blindsight) to a range of 10 feet for a number of rounds
per day equal to your wizard level. This ability only allows you to detect living creatures and
undead creatures. This sight also tells you whether a creature is living or undead. Constructs and
other creatures that are neither living nor undead cannot be seen with this ability.

**Usage:** 1 time/day per wizard level

### Life School

**Sources:** Advanced Player's Guide pg 146\
**Associated School:** Necromancy.

**Replacement Powers:** The following school powers replace the _power over undead_ and _grave
touch_ powers of the necromancy school.

**Healing Grace (Su)**

**Ability:** Whenever you cast a spell that has targets, affects creatures in an area, or requires
an attack roll, you may heal creatures affected by the spell a total of 1 point of damage per level
of the spell. This healing may be spread out between the targets of the spell in any way you choose.
This healing occurs when the spell is cast and has no effect on creatures that enter its area after
the spell is in place. If you assign any of the healing to an undead creature, it instead takes 1
point of damage for each point assigned.

**At 11th Level:** The amount of damage cured increases to 2 points of damage per level of the
spell.

**At 20th Level:** The amount of damage cured increases to 3 points of damage per level of the
spell.

**Gained:** At 1st Level

**Share Essence (Sp)**

**Gained:** At 1st Level

**Standard:** You can share your vital energy with a living creature that you touch. You take an
amount of nonlethal damage equal to 1d6 + [half](ref/misc/fractions-and-rounding) of your wizard
level. You cannot take an amount of nonlethal damage equal to or greater than your current hit point
total; any excess is prevented. The recipient gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to the amount of damage you received
(prevented damage is not counted). These temporary hit points disappear 1 hour later. You may not
use this ability to grant yourself temporary hit points.

**Usage:** Int3 modifier times/day

### Undead School

**Sources:** Advanced Player's Guide pg 147\
**Associated School:** Necromancy.

**Replacement Powers:** The following school power replaces the _grave touch_ power of the
necromancy school.

**Bolster (Sp)**

**Gained:** At 1st Level

**Standard:** You can touch an undead creature and infuse it with negative energy. It gains 1
temporary hit point per Hit Die and a +2 bonus to its
[channel resistance](ref/umr/channel-resistance), as well as a profane bonus on all attack rolls and
saving throws; the profane bonus is equal to 1 + [one-fifth](ref/misc/fractions-and-rounding) of
your wizard level. These bonuses last for a number of rounds equal to 1/2 your wizard level (minimum
1 round). The bonuses and temporary hit points are immediately dispelled if the creature is within
the area of a [consecrate](ref/spell/consecrate) spell.

**Usage:** Int3 modifier times/day
