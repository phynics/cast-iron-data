+++
id = "ref/rule/damage-reduction"
kind = "rule"
title = "Damage Reduction"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "damage_reduction", path = "json/rules_combat01.json" },
]
[[sources]]
publication = "core-rulebook"
page = "561"

[fields]
kind = "none"
+++

Some magic creatures have the supernatural ability to instantly heal damage from weapons or ignore
blows altogether as though they were invulnerable.

The numerical part of a creature's damage reduction (or DR) is the amount of damage the creature
ignores from normal attacks. Usually, a certain type of weapon can overcome this reduction (see
Overcoming DR). This information is separated from the damage reduction number by a slash. For
example, DR 5/magic means that a creature takes 5 less points of damage from all weapons that are
not magic. If a dash follows the slash, then the damage reduction is effective against any attack
that does not ignore damage reduction.

Some DR has multiple parts, separated by an "and" or an "or". An attack must have **all** qualities
of an "and" DR in order to bypass it (e.g. a [lich's](ref/template/lich) DR 15/bludgeoning and
magic), but needs only **one** quality of an "or" DR to get through (e.g. a
[dretch's](ref/monster/demon-dretch) DR 5/cold iron or good).

Whenever damage reduction completely negates the damage from an attack, it also negates most special
effects that accompany the attack, such as injury poison, a monk's stunning, and injury-based
disease. Damage reduction does not negate touch attacks, energy damage dealt along with an attack,
or energy drains. Nor does it affect poisons or diseases delivered by inhalation, ingestion, or
contact.

Attacks that deal no damage because of the target's damage reduction do not disrupt spells.

Spells, [spell-like abilities](ref/umr/spell-like-abilities), and energy attacks (even nonmagical
fire) ignore damage reduction.

Sometimes damage reduction represents instant healing. Sometimes it represents the creature's tough
hide or body. In either case, other characters can see that conventional attacks won't work.

If a creature has damage reduction from more than one source, the two forms of damage reduction do
not stack. Instead, the creature gets the benefit of the best damage reduction in a given situation.

**Overcoming DR:** Damage reduction may be overcome by special materials, magic weapons (any weapon
with a +1 or higher enhancement bonus, not counting the enhancement from masterwork quality),
certain types of weapons (such as slashing or bludgeoning), and weapons imbued with an alignment.

Ammunition fired from a projectile weapon with an enhancement bonus of +1 or higher is treated as a
magic weapon for the purpose of overcoming damage reduction. Similarly, ammunition fired from a
projectile weapon with an alignment gains the alignment of that projectile weapon (in addition to
any alignment it may already have).

Weapons with an enhancement bonus of +3 or greater can ignore some types of damage reduction,
regardless of their actual material or alignment. The following table shows what type of enhancement
bonus is needed to overcome some common types of damage reduction.

|DR Type|Weapon Enhancement Bonus Equivalent|
| --- | --- |
|Cold Iron/Silver|+3|
|Adamantine^[1](ref/rule/damage-reduction#footnote-1)^|+4|
|Alignment-based|+5|

[Some weapons](ref/rule/weapon-descriptions) deal damage of multiple types. If a weapon causes two
types of damage, the type it deals is not half one type and half another; all damage caused is of
both types. Therefore, a creature would have to be immune to both types of damage to ignore any of
the damage caused by such a weapon (e.g. a +3 [morningstar](ref/eq-weapon/morningstar) \[B and P
damage\] deals full damage to a lich).

In other cases, a weapon can deal either of two types of damage. In a situation where the damage
type is significant, the wielder can choose which type of damage to deal with such a weapon (e.g. a
+3 [lucerne hammer](ref/eq-weapon/lucerne-hammer) \[B or P damage\] only overcomes a lich's DR when
used to deal bludgeoning damage).

###### ^1^ {#footnote-1}

Note that this does not give the ability to ignore [hardness](ref/umr/hardness), like an actual
[adamantine](ref/eq-material/adamantine) weapon does
