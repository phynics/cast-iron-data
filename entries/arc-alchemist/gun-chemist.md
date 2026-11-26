+++
id = "ref/arc-alchemist/gun-chemist"
kind = "archetype"
title = "Gun Chemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Gun%20Chemist"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gun_chemist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "alchemical-ordnance", level = 1 },
  { anchor = "gunsmith", level = 1 },
  { anchor = "discoveries" },
  { anchor = "cartridge-savant", level = 2 },
  { anchor = "repeat-fire", level = 6 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Bombs", feature = "bomb", by = ["alchemical-ordnance"] },
  { replaces = "Brew Potion", feature = "brew-potion", by = ["gunsmith"] },
  { replaces = "Throw Anything", feature = "throw-anything", by = ["gunsmith"] },
  { replaces = "Poison resistance", feature = "poison-resistance", by = ["cartridge-savant"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["repeat-fire"] },
]
+++

Simple alchemists may dabble in explosives, but for the rare gun chemist, a firearm's barrel is his
crucible.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Gun chemists are proficient with all simple weapons, firearms, and light armor.

This replaces the gun chemist's weapon and armor proficiencies.

## Alchemical Ordnance (Su) {#alchemical-ordnance}

A gun chemist is adept at using his know-how to infuse his ammunition with volatile chemicals and
his own magical reserves. When loading a firearm, he can infuse the ammunition as a free action. The
compounds are unstable, and if not fired within a number of rounds equal to the gun chemist's
Intelligence modifier (though no sooner than the end of his next turn), the alchemical ordnance
becomes inert and loses its additional effects; he can still fire the firearm as normal. Each day,
the gun chemist can infuse a number of pieces of alchemical ordnance equal to his class level + his
Intelligence modifier, and he can fire no more than one piece per round.

Alchemical ordnance deals damage as normal, plus an amount of fire damage equal to 1d6 + the gun
chemist's Intelligence modifier. The damage of the gun chemist's alchemical ordnance increases by
1d6 points at every odd-numbered class level (this bonus damage is not multiplied on a critical hit
or by using feats such as [Vital Strike](ref/feat/vital-strike)). The explosive nature of alchemical
ordnance causes the attack—both the firearm's base damage and the alchemical ordnance's additional
damage—to deal full damage to [swarms](ref/subtype/swarm) of any size. If the gun chemist uses
alchemical ordnance to make a scattering shot with a weapon with the [scatter](ref/misc/scatter)
quality, each creature in the area instead takes additional fire damage equal to the alchemical
ordnance's minimum damage (so if the alchemical ordnance would deal 2d6+4 points of fire damage
normally, it deals only 6 points of fire damage with a scattering shot).

The gun chemist's alchemical ordnance functions safely only in weapons he wields. If anyone but a
gun chemist attempts to fire a firearm loaded with alchemical ordnance that is not yet inert, the
firearm's misfire value increases by 4. If the firearm would explode as the result of such a
misfire, the explosion deals additional fire damage equal to that of the alchemical ordnance.

Alchemical ordnance is treated like an alchemist's bomb for the purpose of discoveries, though such
discoveries ignore any effects associated with a bomb's splash damage or radius unless the gun
chemist also applies the exploding bullet discovery (see below). A scattering shot modified by a
discovery applies additional effects as though affected creatures were caught in the splash damage
of a bomb rather than subject to a direct hit. The DCs of saving throws associated with alchemical
ordnance are equal to 10 + [half](ref/misc/fractions-and-rounding) the gun chemist's alchemist
level + the gun chemist's Intelligence modifier.

This replaces bombs.

## Gunsmith {#gunsmith}

A gun chemist gains a battered gun identical to the one gained by a 1st level
[gunslinger](ref/class/gunslinger), as well as the [Gunsmithing](ref/feat/gunsmithing) feat
(including the ability to restore his battered gun as if he were a gunslinger). As a standard
action, the gun chemist can expend one use of his alchemical ordnance to remove the broken condition
from a single firearm he is currently wielding, as long as that condition was gained from a misfire.

This replaces Brew Potion and Throw Anything.

## Discoveries {#discoveries}

A gun chemist selects alchemist discoveries as normal. He can also select from the discoveries
below, which are unique to the gun chemist. Discoveries marked with an asterisk (\*) do not stack,
including with other alchemist discoveries marked by an asterisk that modify bombs. Only one such
discovery can be applied to an individual alchemical ordnance.

### Chemical Stability {#chemical-stability}

When firing an alchemical ordnance, the gun chemist reduces the misfire value of the firearm by 1
(minimum 0) and ignores any increased misfire value from using an alchemical cartridge.

### Exploding Bullet\* {#exploding-bullet}

The gun chemist's alchemical ordnance splashes adjacent targets as though it were a splash weapon,
dealing the alchemical ordnance's minimum additional damage to other creatures caught in the splash
(Reflex half). A gun chemist must be at least 4th level before selecting this discovery.

### Fast Ordnance {#fast-ordnance}

A gun chemist with this discovery can fire more than one piece of alchemical ordnance as part of a
[full attack](ref/rule/full-attack). A gun chemist must be at least 8th level before selecting this
discovery.

## Cartridge Savant (Ex) {#cartridge-savant}

At 2nd level, a gun chemist can make optimal and highly efficient use of
[alchemical cartridges](ref/eq-weapon/alchemical-cartridge-flare), such as [flare](ref/spell/flare)
cartridges. If the gun chemist fires such an alchemical cartridge and it allows a saving throw to
negate or reduce the cartridge's effect, the saving throw's DC increases by 1 (to a maximum DC of
22). The DC increases by an additional 1 at 5th level and every 3 levels thereafter (to a maximum of
7 higher at 20th level). When a gun chemist fires an alchemical cartridge that deals a type of
damage in place of a firearm's normal damage (such as a [dragon's breath](ref/spell/dragons-breath)
cartridge), he can increase the damage dealt by an amount equal to his Intelligence modifier.

This replaces poison resistance.

## Repeat Fire (Ex) {#repeat-fire}

At 6th level, a gun chemist gains [Rapid Reload](ref/feat/rapid-reload) as a bonus feat and must
select a type of firearm. If he already has this feat, he can instead gain one combat feat for which
he qualifies.

This replaces swift poisoning.
