+++
id = "ref/arc-alchemist/gun-chemist"
kind = "archetype"
title = "Gun Chemist"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gun_chemist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "archetype"
replaces = ["Weapon and armor proficiencies", "Bombs", "Brew Potion", "Throw Anything", "Poison resistance", "Swift poisoning"]
+++

**Sources:** People of the Wastes pg 11\
Simple alchemists may dabble in explosives, but for the rare gun chemist, a firearm's barrel is his
crucible.

**Weapon and Armor Proficiency**

**Gained:** At 1st Level

**Passive:** Gun chemists are proficient with all simple weapons, firearms, and light armor.

**Replaces:** Weapon and armor proficiencies

**Alchemical Ordnance (Su)**

**Flavor:** A gun chemist is adept at using his know-how to infuse his ammunition with volatile
chemicals and his own magical reserves.

**Free:** When loading a firearm, he can infuse the ammunition. The compounds are unstable, and if
not fired within a number of rounds equal to the gun chemist's Intelligence modifier (though no
sooner than the end of his next turn), the alchemical ordnance becomes inert and loses its
additional effects; he can still fire the firearm as normal.

**Gained:** At 1st Level

**Replaces:** Bombs

**Special:** The DCs of saving throws associated with alchemical ordnance are equal to 10 +
[half](ref/misc/fractions-and-rounding) the gun chemist's alchemist level + the gun chemist's
Intelligence modifier.

**Usage:** Each day, the gun chemist can infuse a number of pieces of alchemical ordnance equal to
his class level + his Intelligence modifier, and he can fire no more than one piece per round.

**Usage:** Each day, the gun chemist can infuse a number of pieces of alchemical ordnance equal to
his class level + his Intelligence modifier, and he can fire no more than one piece per round.

**Alchemical ordnance** deals damage as normal, plus an amount of fire damage equal to 1d6 + the gun
chemist's Intelligence modifier. The damage of the gun chemist's alchemical ordnance increases by
1d6 points at every odd-numbered class level (this bonus damage is not multiplied on a critical hit
or by using feats such as [Vital Strike](ref/feat/vital-strike)). The explosive nature of alchemical
ordnance causes the attack - both the firearm's base damage and the alchemical ordnance's additional
damage - to deal full damage to [swarms](ref/subtype/swarm) of any size. If the gun chemist uses
alchemical ordnance to make a scattering shot with a weapon with the [scatter](ref/misc/scatter)
quality, each creature in the area instead takes additional fire damage equal to the alchemical
ordnance's minimum damage (so if the alchemical ordnance would deal 2d6+4 points of fire damage
normally, it deals only 6 points of fire damage with a scattering shot).

The gun chemist's alchemical ordnance functions safely only in weapons he wields. If anyone but a
gun chemist attempts to fire a firearm loaded with alchemical ordnance that is not yet inert, the
firearm's misfire value increases by 4. If the firearm would explode as the result of such a
misfire, the explosion deals additional fire damage equal to that of the alchemical ordnance.

Alchemical ordnance is treated like an alchemist's bomb for the purpose of **discoveries**, though
such discoveries ignore any effects associated with a bomb's splash damage or radius unless the gun
chemist also applies the _exploding bullet_ discovery. A scattering shot modified by a discovery
applies additional effects as though affected creatures were caught in the splash damage of a bomb
rather than subject to a direct hit.

**Gunsmith**

**Gained:** At 1st Level

**Passive:** A gun chemist gains a battered gun identical to the one gained by a 1st level
[gunslinger](ref/class/gunslinger), as well as the [Gunsmithing](ref/feat/gunsmithing) feat
(including the ability to restore his battered gun as if he were a gunslinger).

**Replaces:** Brew Potion, Throw Anything

**Standard:** The gun chemist can expend one use of his alchemical ordnance to remove the broken
condition from a single firearm he is currently wielding, as long as that condition was gained from
a misfire.

**Discoveries**

**Gained:** At 1st Level

**Passive:** A gun chemist selects alchemist discoveries as normal. He can also select from the
three discoveries below, which are unique to the gun chemist.

**Chemical Stability**

**Passive:** When firing an alchemical ordnance, the gun chemist reduces the misfire value of the
firearm by 1 (minimum 0) and ignores any increased misfire value from using an alchemical cartridge.

**Exploding Bullet**

**Passive:** The gun chemist's alchemical ordnance splashes adjacent targets as though it were a
splash weapon, dealing the alchemical ordnance's minimum additional damage to other creatures caught
in the splash (Reflex half). This discovery does not stack with other bomb-altering alchemist
discoveries that have a one-per-bomb limit (Primary Bomb Discoveries).

**Prereq:** 4th-level alchemist

**Fast Ordnance**

**Ability:** A gun chemist with this discovery can fire more than one piece of alchemical ordnance
as part of a [full attack](ref/rule/full-attack).

**Prereq:** 8th-level alchemist

**Cartridge Savant (Ex)**

**Ability:** At 2nd level, a gun chemist can make optimal and highly efficient use of
[alchemical cartridges](ref/eq-weapon/alchemical-cartridge-flare), such as
_[flare](ref/spell/flare)_ cartridges. If the gun chemist fires such an alchemical cartridge and it
allows a saving throw to negate or reduce the cartridge's effect, the saving throw's DC increases by
1 (to a maximum DC of 22). When a gun chemist fires an alchemical cartridge that deals a type of
damage in place of a firearm's normal damage (such as a
_[dragon's breath](ref/spell/dragons-breath)_ cartridge), he can increase the damage dealt by an
amount equal to his Intelligence modifier.

**At 11th Level:** The DC now increases by 4.

**At 14th Level:** The DC now increases by 5.

**At 17th Level:** The DC now increases by 6.

**At 20th Level:** The DC now increases by 7.

**At 5th Level:** The DC now increases by 2.

**At 8th Level:** The DC now increases by 3.

**Gained:** At 2nd Level

**Replaces:** Poison resistance

**Repeat Fire (Ex)**

**Gained:** At 6th Level

**Passive:** A gun chemist gains [Rapid Reload](ref/feat/rapid-reload) as a bonus feat and must
select a type of firearm. If he already has this feat, he can instead gain one combat feat for which
he qualifies.

**Replaces:** Swift poisoning
