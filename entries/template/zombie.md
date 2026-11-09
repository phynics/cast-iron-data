+++
id = "ref/template/zombie"
kind = "rule"
title = "Zombie"
source_ids = ["bestiary", "horror-realms", "classic-horrors-revisited"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "zombie", path = "json/monster_template4.json" },
]
[[sources]]
publication = "bestiary"
page = "288"

[fields]
kind = "none"
+++

**Zombie**

**Acquired:** present

**Challenge rating:** Varies

Zombies are the animated corpses of dead creatures, forced into foul unlife via necromantic magic
like [animate dead](ref/spell/animate-dead). While the most commonly encountered zombies are slow
and tough, others possess a variety of traits, allowing them to spread disease or move with
increased speed.

Zombies are unthinking automatons, and can do little more than follow orders. When left unattended,
zombies tend to mill about in search of living creatures to slaughter and devour. Zombies attack
until destroyed, having no regard for their own safety.

Although capable of following orders, zombies are more often unleashed into an area with no command
other than to kill living creatures. As a result, zombies are often encountered in packs, wandering
around places the living frequent, looking for victims. Most zombies are created using
_[animate dead](ref/spell/animate-dead)._ Such zombies are always of the standard type, unless the
creator also casts [haste](ref/spell/haste) or [remove paralysis](ref/spell/remove-paralysis) to
create fast zombies, or [contagion](ref/spell/contagion) to create plague zombies.

"Zombie" is an acquired template that can be added to any corporeal creature (other than an undead),
referred to hereafter as the base creature.

**CR:** This depends on the creature's new total number of Hit Dice, as follows:

|HD|CR|XP|
| --- | --- | --- |
|1/2|1/8|50|
|1|1/4|100|
|2|1/2|200|
|3-4|1|400|
|5-6|2|600|
|7-8|3|800|
|9-10|4|1,200|
|11-12|5|1,600|
|13-16|6|2,400|
|17-20|7|3,200|
|21-24|8|4,800|
|25-28|9|6,400|

**Alignment:** Always neutral evil.

**Type:** The creature's type changes to [undead](ref/type/undead). It retains any subtype except
for alignment subtypes (such as good) and subtypes that indicate kind. It does not gain the
augmented subtype. It uses all the base creature's statistics and special abilities except as noted
here.

**AC:** Natural armor is based on the zombie's size:

|Zombie Size|Natural Armor Bonus|
| --- | --- |
|Tiny or smaller|+0|
|Small|+1|
|Medium|+2|
|Large|+3|
|Huge|+4|
|Gargantuan|+7|
|Colossal|+11|

**Hit Dice:** Drop HD gained from class levels (minimum of 1) and change racial HD to d8s. Zombies
gain a number of additional HD as noted on the following table.

|Zombie Size|Bonus Hit Dice|
| --- | --- |
|Tiny or smaller|-|
|Small or Medium|+1 HD|
|Large|+2 HD|
|Huge|+4 HD|
|Gargantuan|+6 HD|
|Colossal|+10 HD|

Zombies use their Charisma modifiers to determine bonus hit points (instead of Constitution).

**Saves:** Base save bonuses are Fort +1/3 HD, Ref +1/3 HD, and Will +1/2 HD + 2.

**Defensive Abilities:** Zombies lose their defensive abilities and gain all of the qualities and
immunities granted by the undead type. Zombies gain DR 5/slashing.

**Speed:** Winged zombies can still fly, but maneuverability drops to clumsy. If the base creature
flew magically, so can the zombie. Retain all other movement types.

**Attacks:** A zombie retains all the natural weapons, manufactured weapon attacks, and weapon
proficiencies of the base creature. It also gains a [slam attack](ref/umr/natural-attacks) that
deals damage based on the zombie's size, but as if it were one size category larger than its actual
size.

**Special Attacks:** A zombie retains none of the base creature's special attacks.

**Abilities:** Str +2, Dex -2. A zombie has no Con or Int score, and its Wis and Cha become 10.

**BAB:** A zombie's base attack is equal to 3/4 its Hit Dice.

**Skills:** A zombie has no skill ranks.

**Feats:** A zombie loses all feats possessed by the base creature, and does not gain feats as its
Hit Dice increase, but it does gain [Toughness](ref/feat/toughness) as a bonus feat.

**Special Qualities:** A zombie loses most special qualities of the base creature. It retains any
extraordinary special qualities that improve its melee or ranged attacks. A zombie gains the
following special quality.

> [Staggered (Ex):](ref/misc/staggered) Zombies have poor reflexes and can only perform a single
> move action or standard action each round. A zombie can move up to its speed and attack in the
> same round as a [charge](ref/rule/charge) action.

### Variant Zombies

The typical zombie is a slow-moving abomination that is tough to destroy. Yet this tough zombie is
not the only type of zombie to plague crypts or stalk graveyards. Each of the following two variant
zombies modifies the base zombie in a few simple ways.

#### Fast Zombie

Unlike the standard, plodding zombie, a fast zombie moves with a supernatural quickness.

**Speed:** Increase the base creature's land speed by 10 feet.

**Defensive Abilities:** A fast zombie does not gain DR 5/slashing.

**Special Attacks:** A fast zombie gains the following special attack.

> **Quick Strikes (Ex):** Whenever a fast zombie takes a full-attack action, it can make one
> additional slam attack at its highest base attack bonus.

**Abilities:** As a standard zombie, except its Dexterity is increased by 2 instead of reduced by 2.

**Special Qualities:** A fast zombie does not gain the _staggered_ special quality.

#### Plague Zombie

These zombies carry a terrible disease that perpetuates their undead lineage - those infected by a
plague zombie's contagion rise as zombies themselves when they perish.

**Defensive Abilities:** A plague zombie does not gain DR 5/slashing.

**Special Attacks:** A plague zombie gains the following special attacks.

> **Death Burst (Ex):** When a plague zombie dies, it explodes in a burst of decay. All creatures
> adjacent to the plague zombie are exposed to its plague as if struck by a slam attack and must
> make a Fortitude save or contract zombie rot.
>
> **Disease (Su):** The slam attack - as well as any other natural attacks - of a plague zombie
> carries the zombie rot disease.
>
> - [Affliction: Zombie Rot](ref/affliction/zombie/zombie-rot)

#### Yellow Musk Zombie

A yellow musk zombie is a rotting creature from which wet green vines have sprouted. Treat a yellow
musk zombie as a standard zombie, but with this special quality.

> **Plant Traits (Ex):** This zombie's animation is provided not by necromancy but by the plant that
> grows throughout its body. Yellow musk zombies lack undead traits, but gain
> [plant](ref/type/plant) traits. They are treated as plants, not undead, for the resolution of
> magical effects and attacks. [Channel energy](ref/ability/channel-energy) cannot harm a yellow
> musk zombie, for example, nor does negative energy heal a yellow musk zombie.

#### Zombies of the Yellow Mire

**Sources:** Horror Realms pg 33

The yellow musk zombies born in Yellow Mire may be familiar to adventurers who have encountered
[yellow musk creepers](ref/monster/yellow-musk-creeper) in the past, but the abominable flora of
Golden Garden are an altogether separate horror. Below are three of the most common varieties of
yellow musk zombies that arise from Golden Garden, which otherwise share statistics with typical
yellow musk zombies.

> ##### Deathspore Zombie (CR +1)
>
> With stark black rashes streaked across their rotting faces and skeletal bodies, these yellow musk
> zombies are more imposing than their typical counterparts; they gain a +4 bonus to their Strength
> score and have a Charisma of 14. A creature struck by a deathspore zombie's natural attack has a
> chance of being afflicted with the following poison.
>
> - [Affliction: Deathspore Toxin](ref/affliction/zombie/deathspore-toxin)
>
> ##### Gold Musk Zombie (CR +2)
>
> These [advanced](ref/template/advanced) yellow musk zombies have DR 5/cold iron as well as acid,
> cold, and electricity resistance 5, and they can be healed by negative energy as if they were
> undead. In addition, any creature slain by gold musk zombies becomes a gold musk zombie in 1d4
> rounds. These new gold musk zombies are weakened for the first 24 hours of their existence, and
> take a -2 penalty on all d20 rolls and checks, receive -2 hit points per Hit Die, and do not
> create additional gold musk zombies from the creatures they kill. After 24 hours, these penalties
> are lifted.
>
> ##### Pale-Puff Musk Zombie (CR +0)
>
> Weaker than their yellow musk counterparts but far more numerous, pale-puff musk zombies do not
> gain a bonus to Strength from becoming a zombie and have a Charisma score of 6. A large puffball
> of stinky yellow pollen grows out of the zombie's head from a sturdy brown stem. The first time a
> pale-puff musk zombie takes any amount of damage but isn't destroyed by the attack, the puffball
> breaks apart and spreads over a 5-foot-radius area, affecting any creatures in the area as a
> yellow musk creeper's pollen spray ability.

### Faces of Death

**Sources:** Classic Horrors Revisited pg 25\
The simple, tottering skeleton and mindless, shambling zombie are the stereotypical image of the
walking dead, but these undead horrors come in highly variable forms. Bloody skeletons, burning
skeletons, fast zombies, plague zombies, and deadly intelligent skeletal champions are the
best-known variants, but the walking dead are a diverse lot, and many more varieties might stalk
moonlit graveyards and haunted crypts, each possessing its own strange and unique abilities.
Although some common forms are listed below, in many cases these variant abilities may be applied to
either [skeletons](ref/template/skeleton) or zombies, unless common sense dictates otherwise (such
as a gasburst skeleton). Likewise, except as noted, the following variations can be stacked with one
another - it's possible to have an exploding acid skeleton, for example.

**Alchemical Zombie:** This zombie has been created through alchemical processes rather than
necromantic magic. As such, positive energy has less effect on it, giving it
[channel resistance](ref/umr/channel-resistance) +2. Its alchemically treated flesh is also more
resistant to damage, granting it an additional +2 bonus to its natural Armor Class above that which
it gains based on its size. (CR +1)

**Brain-eating Zombie:** These terrifying zombie variants feed on humanoid brains. They gain a
[bite attack](ref/umr/natural-attacks) that deals damage based on the zombie's size, and the
[grab](ref/umr/grab) special attack, usable against opponents of the zombie's own size or smaller.
When an opponent dies, the zombie uses its next turn to feast upon its victim's brain, making spells
that require a complete corpse (such as [raise dead](ref/spell/raise-dead)) useless. Anyone killed
after being bitten by a brain-eating zombie rises as a brain-eating zombie in 2d6 hours unless the
corpse is blessed or similar preventative measures are taken. (CR +0)

**Cursed Zombie:** Created as the result of a powerful curse rather than through necromantic spells,
cursed zombies can bestow a curse upon their victims. A cursed zombie gains the curse special
attack, delivered with its slam attack. (CR +1)

- [Affliction: Zombie Curse (Su)](ref/affliction/zombie/zombie-curse-su)

**Gasburst Zombie:** These bloated zombies are filled with toxic gas. When a gasburst zombie dies,
it explodes in a cloud of noxious vapors which fill a 10-foot cube surrounding the zombie. Gasburst
zombies are commonly filled with [burnt othur fumes](ref/eq-poison/burnt-othur-fumes) or
[ungol dust](ref/eq-poison/ungol-dust), but any poisonous gas may be used. Gas burst zombies have DR
5/piercing instead of DR 5/slashing. (CR depends on poison used, usually +1)

**Host Corpse:** This skeleton or zombie has been infested with a swarm of vermin or Tiny undead
creatures that it releases from its body. Skeletal hosts often hold
[carrionstorms](ref/monster/carrionstorm) or [bat swarms](ref/monster/bat-bat-swarm) in their rib
cages, while zombie hosts frequently carry [locusts](ref/monster/locust-locust-swarm) or
[flesh-eating cockroach swarms](ref/monster/cockroach-cockroach-swarm) inside their rotting husks.
Acid, bloody, and burning skeletons cannot be host corpses. (CR +0, with the swarm's CR counting as
a separate creature)

**Relentless Zombie:** These have all the powers of fast zombies, and also gain a climb speed equal
to half the base creature's land speed, the [scent](ref/umr/scent) special ability, a +4 racial
bonus to [Survival](ref/skill/survival) checks to track by smell, and two additional Hit Dice. (CR
+1)

**Zombie Lord:** [Zombie lords](ref/template/zombie-lord) are the fleshy counterparts to skeletal
champions, rare zombies who have somehow managed to retain their intelligence. Use the normal zombie
template for the zombie lord's Armor Class, base save bonuses, speed, melee attacks, base attack
bonus, and [damage reduction](ref/rule/damage-reduction). Use the
[skeletal champion](ref/template/skeletal-champion) template for the zombie lord's Hit Dice, skills,
and ability scores. Zombie lords gain [channel resistance](ref/umr/channel-resistance) +4 and
[Toughness](ref/feat/toughness) as a bonus feat. A zombie lord does not gain the staggered special
quality. (CR as a zombie of the same Hit Dice +1.)
