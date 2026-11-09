+++
id = "ref/template/skeleton"
kind = "rule"
title = "Skeleton"
source_ids = ["bestiary", "classic-horrors-revisited"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "skeleton", path = "json/monster_template4.json" },
]
[[sources]]
publication = "bestiary"
page = "250"

[fields]
kind = "none"
+++

**Skeleton**

**Acquired:** present

**Challenge rating:** Varies

Skeletons are the animated bones of the dead, brought to unlife through foul magic. While most
skeletons are mindless automatons, they still possess an evil cunning imparted to them by their
animating force - a cunning that allows them to wield weapons and wear armor.

"Skeleton" is an acquired template that can be added to any corporeal creature (other than an
undead) that has a skeletal system (referred to hereafter as the base creature).

**CR:** Depends on Hit Dice, as follows:

|HD|CR|XP|
| --- | --- | --- |
|1/2|1/6|65|
|1|1/3|135|
|2-3|1|400|
|4-5|2|600|
|6-7|3|800|
|8-9|4|1,200|
|10-11|5|1,600|
|12-14|6|2,400|
|15-17|7|3,200|
|18-20|8|4,800|

**Alignment:** Always neutral evil.

**Type:** The creature's type changes to [undead](ref/type/undead). It retains any subtype except
for alignment subtypes (such as good) and subtypes that indicate kind (such as giant). It does not
gain the augmented subtype. It uses all the base creature's statistics and special abilities except
as noted here.

**AC:** Natural armor bonus changes as follows:

|Skeleton Size|Natural Armor Bonus|
| --- | --- |
|Tiny or smaller|+0|
|Small|+1|
|Medium or Large|+2|
|Huge|+3|
|Gargantuan|+6|
|Colossal|+10|

**Hit Dice:** A skeleton drops any HD gained from class levels and changes racial HD to d8s.
Creatures without racial HD are treated as if they have 1 racial HD. If the creature has more than
20 Hit Dice, it can't be made into a skeleton by the [animate dead](ref/spell/animate-dead) spell. A
skeleton uses its Cha modifier (instead of its Con modifier) to determine bonus hit points.

**Saves:** Base save bonuses are Fort +1/3 HD, Ref +1/3 HD, and Will +1/2 HD + 2.

**Defensive Abilities:** A skeleton loses the base creature's defensive abilities and gains DR
5/bludgeoning and [immunity](ref/umr/immunity) to cold. It also gains all of the standard immunities
and traits possessed by undead creatures.

**Speed:** A winged skeleton can't use its wings to fly. If the base creature flew magically, so can
the skeleton. All other movement types are retained.

**Attacks:** A skeleton retains all the natural weapons, manufactured weapon attacks, and weapon
proficiencies of the base creature, except for attacks that can't work without flesh. A creature
with hands gains one [claw attack](ref/umr/natural-attacks) per hand; the skeleton can strike with
each of its claw attacks at its full attack bonus. A claw attack deals damage depending on the
skeleton's size. If the base creature already had claw attacks with its hands, use the skeleton claw
damage only if it's better.

**Special Attacks:** A skeleton retains none of the base creature's special attacks.

**Abilities:** A skeleton's Dexterity increases by +2. It has no Constitution or Intelligence score,
and its Wisdom and Charisma scores change to 10.

**BAB:** A skeleton's base attack bonus is equal to 3/4 of its Hit Dice.

**Skills:** A skeleton loses all skill ranks possessed by the base creature and gains none of its
own.

**Feats:** A skeleton loses all feats possessed by the base creature and gains
[Improved Initiative](ref/feat/improved-initiative) as a bonus feat.

**Special Qualities:** A skeleton loses most special qualities of the base creature. It retains any
extraordinary special qualities that improve its melee or ranged attacks.

**Environment:** Any, usually the same as base creature.

**Organization:** Any.

**Treasure:** Generally none, although sometimes a skeleton's creator arms it with magical armor or
weapons.

### Variant Skeletons

Numerous variant skeletons exist, such as those whose bones burn with an unending fire and those who
drip with gore and reassemble themselves over time. Both of these variant skeletons can be created
using _[animate dead](ref/spell/animate-dead),_ but they count as twice their normal number of Hit
Dice per casting. Once controlled, they count normally against the controller's limit.

Perhaps the most dangerous variant skeleton, though, is the skeletal champion. This skeleton retains
its intellect, and often any class levels it possessed in life. A skeletal champion cannot be
created with _[animate dead](ref/spell/animate-dead)_ - these potent undead only arise under rare
conditions similar to those that cause the manifestation of ghosts or via rare and highly evil
rituals.

Each of the following skeleton types modifies the base skeleton in a few key ways. Except as noted,
these variations can be stacked with one another - it's possible to have a bloody burning skeletal
champion.

### Bloody Skeleton

A bloody skeleton is coated in a slick layer of blood and gore infused with negative energy. This
gore allows the skeleton to reform and heal itself. In addition to the changes for the skeleton
template, make the following adjustments to the base creature.

**CR:** As a normal skeleton + 1.

**Fast Healing:** A bloody skeleton has [fast healing](ref/umr/fast-healing) equal to 1 per 2 Hit
Dice it possesses (minimum 1).

**Saves:** A bloody skeleton gains [channel resistance](ref/umr/channel-resistance) +4.

**Abilities:** A bloody skeleton's Charisma is 14.

**Special Qualities:** A bloody skeleton gains the deathless special quality.

> **Deathless (Su):** A bloody skeleton is destroyed when reduced to 0 hit points, but it returns to
> unlife 1 hour later at 1 hit point, allowing its [fast healing](ref/umr/fast-healing) thereafter
> to resume healing it. A bloody skeleton can be permanently destroyed if it is destroyed by
> positive energy, if it is reduced to 0 hit points in the area of a [bless](ref/spell/bless) or
> [hallow](ref/spell/hallow) spell, or if its remains are sprinkled with a vial of
> [holy water](ref/eq-weapon/holy-water).

### Burning Skeleton

A burning skeleton is surrounded by an aura of flames that deals fire damage to those it strikes. In
addition to the changes for the skeleton template, make the following adjustments to the base
creature.

**CR:** As a normal skeleton + 1.

**Aura:** Burning skeletons possess a fiery aura.

> **Fiery Aura (Ex):** Creatures adjacent to a burning skeleton take 1d6 points of fire damage at
> the start of their turn. Anyone striking a burning skeleton with an unarmed strike or natural
> attack takes 1d6 points of fire damage.

**Defensive Abilities:** Burning skeletons lose their immunity to cold but gain immunity to fire. A
burning skeleton gains [vulnerability](ref/umr/vulnerabilities) to cold damage.

**Melee Attacks:** A burning skeleton's melee attacks (including both those made with a natural
weapon and those made with a manufactured weapon) deal an additional 1d6 points of fire damage.

**Abilities:** A burning skeleton's Charisma is 12.

**Special Qualities:** A burning skeleton gains fiery death.

> **Fiery Death (Su):** A burning skeleton explodes into a burst of flame when it dies. Anyone
> adjacent to the skeleton when it is destroyed takes 1d6 points of fire damage per 2 Hit Dice the
> skeleton possessed (minimum 1d6). A Reflex save (DC = 10 + 1/2 the skeleton's Hit Dice + the
> skeleton's Cha bonus) halves this damage.

### Faces of Death

**Sources:** Classic Horrors Revisited pg 54\
The simple, tottering skeleton and mindless, shambling [zombie](ref/template/zombie) are the
stereotypical image of the walking dead, but these undead horrors come in highly variable forms.
Bloody skeletons, burning skeletons, fast zombies, plague zombies, and deadly intelligent
[skeletal champions](ref/template/skeletal-champion) are the best-known variants, but the walking
dead are a diverse lot, and many more varieties might stalk moonlit graveyards and haunted crypts,
each possessing its own strange and unique abilities. Although some common forms are listed below,
in many cases these variant abilities may be applied to either skeletons or
[zombies](ref/template/zombie), unless common sense dictates otherwise (such as a gasburst
skeleton). Likewise, except as noted, the following variations can be stacked with one another -
it's possible to have an exploding acid skeleton, for example.

**Acid Skeleton:** The bones of an acid skeleton constantly ooze caustic acid. An acid skeleton's
melee attacks deal an additional 1d6 points of acid damage, and anyone striking an acid skeleton
with an unarmed strike or natural attack takes 1d6 points of acid damage. Acid skeletons lose their
immunity to cold but gain immunity to acid. An acid skeleton's Charisma is 12. Other energy types,
such as electric skeletons or frost skeletons, can be applied in a similar fashion. (CR +1)

**Exploding Skeleton:** Also called "bone bombs," an exploding skeleton detonates in a burst of
razor-sharp bone fragments when it dies. Anyone within 10 feet of the skeleton when it is destroyed
takes 1d6 points of damage per hit die of the skeleton (minimum 1d6). A Reflex save (DC 10 + 1/2 the
skeleton's Hit Dice + the skeleton's Cha modifier) halves this damage. Bloody, burning, and
multiplying skeletons cannot be exploding skeletons. (CR +0)

**Host Corpse:** This skeleton or zombie has been infested with a swarm of vermin or Tiny undead
creatures that it releases from its body. Skeletal hosts often hold
[carrionstorms](ref/monster/carrionstorm) or [bat swarms](ref/monster/bat-bat-swarm) in their rib
cages, while zombie hosts frequently carry [locusts](ref/monster/locust-locust-swarm) or
[flesh-eating cockroach swarms](ref/monster/cockroach-cockroach-swarm) inside their rotting husks.
Acid, bloody, and burning skeletons cannot be host corpses. (CR +0, with the swarm's CR counting as
a separate creature)

**Mudra Skeleton:** Sometimes known as "whirlwind skeletons," mudra skeletons are created with four
or more arms, each capable of wielding a weapon. A mudra skeleton's Dexterity increases by +4
(instead of +2), and it gains [Multiweapon Fighting](ref/feat/multiweapon-fighting) and
[Weapon Finesse](ref/feat/weapon-finesse) as bonus feats. (CR +1)

**Multiplying Skeleton:** This fearsome skeleton variant grows into more skeletons if destroyed.
When a multiplying skeleton is destroyed, its bones reform 1d4 rounds later into two smaller
multiplying skeletons with half the Hit Dice of the original. Each resulting multiplying skeleton
continues to reform into smaller and smaller sizes. A Colossal multiplying skeleton splits into two
Huge skeletons, a Gargantuan skeleton becomes two Large skeletons, a Huge skeleton reforms as two
Medium skeletons, and so on, until the skeleton's Hit Dice can no longer be halved or the resulting
skeletons would be Diminutive or smaller, at which point the skeletons are finally destroyed.
Bloody, burning, and exploding skeletons cannot be multiplying skeletons. (CR +1)

**Skeletal Archer:** While not as intelligent or skilled as skeletal champions, skeletal archers are
nevertheless a welcome addition to any undead army. Skeletal archers gain
[Point-Blank Shot](ref/feat/point-blank-shot) and [Precise Shot](ref/feat/precise-shot) as bonus
feats. (CR +0)
