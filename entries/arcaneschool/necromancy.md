+++
id = "ref/arcaneschool/necromancy"
kind = "class_option"
title = "Necromancy"
source_ids = ["core-rulebook", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "necromancy", path = "json/class_ability_arcane_schools.json" },
]
[[sources]]
publication = "core-rulebook"
page = "81"
[[sources]]
publication = "advanced-players-guide"
page = "146-147"

[fields]
kind = "class_option"
group = "arcane-school"
features = [
  { anchor = "power-over-undead" },
  { anchor = "grave-touch" },
  { anchor = "life-sight", level = 8 },
]
+++

The dread and feared necromancer commands undead and uses the foul power of unlife against his
enemies.

## Power over Undead (Su) {#power-over-undead}

You receive [Command Undead](ref/feat/command-undead) or [Turn Undead](ref/feat/turn-undead) as a
bonus feat. You can [channel energy](ref/ability/channel-energy) a number of times per day equal to
3 + your Intelligence modifier, but only to use the selected feat. You can take other feats to add
to this ability, such as [Extra Channel](ref/feat/extra-channel) and
[Improved Channel](ref/feat/improved-channel), but not feats that alter this ability, such as
[Elemental Channel](ref/feat/elemental-channel) and [Alignment Channel](ref/feat/alignment-channel).
The DC to save against these feats is equal to 10 + 1/2 your wizard level + your Charisma modifier.
At 20th level, undead cannot add their [channel resistance](ref/rule/channel-resistance) to the save
against this ability.

## Grave Touch (Sp) {#grave-touch}

As a standard action, you can make a melee touch attack that causes a living creature to become
[shaken](ref/misc/shaken) for a number of rounds equal to 1/2 your wizard level (minimum 1). If you
touch a shaken creature with this ability, it becomes [frightened](ref/misc/frightened) for 1 round
if it has fewer Hit Dice than your wizard level. You can use this ability a number of times per day
equal to 3 + your Intelligence modifier.

## Life Sight (Su) {#life-sight}

At 8th level, you gain [blindsight](ref/umr/blindsight) to a range of 10 feet for a number of rounds
per day equal to your wizard level. This ability only allows you to detect living creatures and
undead creatures. This sight also tells you whether a creature is living or undead. Constructs and
other creatures that are neither living nor undead cannot be seen with this ability. The range of
this ability increases by 10 feet at 12th level, and by an additional 10 feet for every four levels
beyond 12th. These rounds do not need to be consecutive.

## Life School {#sec-life-school}

**Associated School:** Necromancy.

**Replacement Powers:** The following school powers replace the power over undead and grave touch
powers of the necromancy school.

**Healing Grace (Su):** Whenever you cast a spell that has targets, affects creatures in an area, or
requires an attack roll, you may heal creatures affected by the spell a total of 1 point of damage
per level of the spell. This healing may be spread out between the targets of the spell in any way
you choose. If you assign any of the healing to an undead creature, it instead takes 1 point of
damage for each point assigned. At 11th level, the amount of damage cured increases to 2 points of
damage per level of the spell. This healing occurs when the spell is cast and has no effect on
creatures that enter its area after the spell is in place. At 20th level, the amount of damage cured
increases to 3 points of damage per level of the spell.

**Share Essence (Sp):** As a standard action, you can share your vital energy with a living creature
that you touch. You take 1d6 points of nonlethal damage + 1 for every two wizard levels you possess.
You cannot take an amount of nonlethal damage equal to or greater than your current hit point total;
any excess is prevented. The recipient gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to the amount of damage you received
(prevented damage is not counted). These temporary hit points disappear 1 hour later. You may not
use this ability to grant yourself temporary hit points. You can use this ability a number of times
per day equal to 3 + your Intelligence modifier. This ability has no effect if you are immune to
nonlethal damage.

## Undead School {#sec-undead-school}

**Associated School:** Necromancy.

**Replacement Power:** The following school power replaces the grave touch power of the necromancy
school.

**Bolster (Sp):** As a standard action, you can touch an undead creature and infuse it with negative
energy. It gains a +1 profane bonus on all attack rolls and saving throws, as well as 1 temporary
hit point per Hit Die and a +2 bonus to its turn resistance. The bonus on attack rolls and saving
throws increases by +1 for every 5 wizard levels you possess. These bonuses last for a number of
rounds equal to 1/2 your wizard level (minimum 1 round). The bonuses and temporary hit points are
immediately dispelled if the creature is within the area of a _[consecrate](ref/spell/consecrate)_
spell. You can use this ability a number of times per day equal to 3 + your Intelligence modifier.
