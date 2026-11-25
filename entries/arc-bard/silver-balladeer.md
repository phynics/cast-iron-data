+++
id = "ref/arc-bard/silver-balladeer"
kind = "archetype"
title = "Silver Balladeer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Silver%20Balladeer"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "silver_balladeer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "occult-adventures"
page = "115"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "break-curse", level = 6 },
  { anchor = "holy-vibration", level = 9 },
  { anchor = "mass-break-curse", level = 18 },
  { anchor = "pure-heart", level = 2 },
  { anchor = "silver-mastery", level = 2 },
  { anchor = "order-of-the-eastern-star-cavalier-order" },
  { anchor = "edicts" },
  { anchor = "challenge" },
  { anchor = "feats" },
  { anchor = "order-abilities" },
  { anchor = "order-of-the-shroud-cavalier-order" },
  { anchor = "order-of-the-shroud-cavalier-order-edicts" },
  { anchor = "order-of-the-shroud-cavalier-order-challenge" },
  { anchor = "order-of-the-shroud-cavalier-order-order-abilities" },
]
trades = [
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["break-curse"] },
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["holy-vibration"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["mass-break-curse"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["pure-heart"] },
  { replaces = "The 2nd-level versatile performance", feature = "versatile-performance", levels = [2], by = ["silver-mastery"] },
  { alters = "Alignment" },
]
+++

The bright purity of silver makes beautiful music, and its vibrations are also anathema to unnatural
creatures. Some bards use a mixture of silver-stringed instruments and esoteric knowledge to battle
the dark forces of the world.

## Alignment {#alignment}

A silver balladeer must have a good alignment. This ability alters alignment.

## Bardic Performance {#bardic-performance}

A silver balladeer gains the bardic performances listed below. These bardic performances all require
the use of a silver or silver-stringed instrument, which costs twice as much as a normal
[masterwork instrument](ref/eq-misc/musical-instrument-masterwork).

## Break Curse (Su) {#break-curse}

At 6th level, a silver balladeer can suppress a single curse affecting an ally within 30 feet that
is able to see and hear her. Each round the silver balladeer uses break curse, she attempts a
Perform check against the original DC of the curse. If successful, she suppresses the curse for 1
round. After she has suppressed the curse for 4 consecutive rounds, she can attempt a caster level
check to remove the curse as if she had cast _[remove curse](ref/spell/remove-curse)_. This ability
replaces suggestion.

## Holy Vibration (Su) {#holy-vibration}

At 9th level, a silver balladeer can spend a round of bardic performance to make a single door or a
window within 30 feet resonate with a holy vibration. Undead and creatures with the evil subtype are
unable to open a door or window affected in this way (as _[arcane lock](ref/spell/arcane-lock)_) for
10 minutes per bard level. If such a creature has the incorporeal subtype, it is unable to move
through the affected door or window, or through any walls, floors, or ceilings within 20 feet of it.
Incorporeal creatures can attempt Charisma checks to break through areas warded by holy vibration,
using the same break DC as for the object the creature is trying to move through. This ability
replaces inspire greatness.

## Mass Break Curse (Su) {#mass-break-curse}

At 18th level, a silver balladeer can suppress all curses among any number of allies within 30 feet
when using break curse. Every 4 consecutive rounds of using this performance, the silver balladeer
can attempt a caster level check to remove a single curse on a single ally affected by this
performance, as if she had cast _[remove curse](ref/spell/remove-curse)_. This ability replaces mass
suggestion.

## Pure Heart (Ex) {#pure-heart}

At 2nd level, a silver balladeer gains a +4 bonus on saving throws against curses, hexes, and charm
effects. This ability replaces well-versed.

## Silver Mastery (Su) {#silver-mastery}

At 2nd level, a silver balladeer treats silver weapons as if they were also
[cold iron](ref/eq-material/cold-iron) for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). Also,
[alchemical silver](ref/eq-material/alchemical-silver) weapons do not impose a penalty on damage
rolls when wielded by a silver balladeer, and a silver balladeer gains a +1 bonus on attack rolls
made with [mithral](ref/eq-material/mithral) weapons. This ability replaces the 2nd-level versatile
performance.

## ORDER OF THE EASTERN STAR (CAVALIER ORDER) {#order-of-the-eastern-star-cavalier-order}

This cavalier order exists to keep dangerous secrets hidden from the world and secretly protect the
world against unimaginable threats from beyond the mortal realms. These cavaliers scout and observe,
concerning themselves not with the trivial pursuit of morality, but rather with ensuring the
survival of society itself.

## Edicts {#edicts}

The cavalier must preserve the secrets of his order while acting to protect civilization against
occult threats. He must thwart the schemes of otherworldly horrors and must give his order a full
accounting of any potential threats.

## Challenge {#challenge}

Whenever a cavalier of the order of the eastern star issues a challenge, he receives a +1 dodge
bonus to AC and a +1 insight bonus on saves against the attacks and abilities of the target of his
challenge. He must be wearing light armor and carrying no more than a light load to receive these
bonuses. These bonuses increase by 1 for every 4 class levels the cavalier possesses.

## Skills {#skills}

A cavalier belonging to the order of the eastern star adds Knowledge (arcana) and Knowledge (planes)
to his class skills. He can attempt Knowledge (arcana) and Knowledge (planes) checks untrained. If
he has ranks in these skills, as long as a check involves knowledge of the occult or supernatural,
he receives a bonus on the check equal to 1/2 his cavalier level (minimum +1).

## Feats {#feats}

A cavalier of this order gains Psychic Sensitivity as a bonus feat.

## Order Abilities {#order-abilities}

A cavalier belonging to this order gains the following abilities as he increases in level.

_Guarded (Ex)_: At 2nd level, the cavalier gains DR 1/—and a +2 morale bonus on saving throws when
wearing light armor or no armor and fighting defensively or using Combat Expertise. At 6th level and
every 4 levels thereafter, this DR increases by 1. He loses the benefits of this ability if carrying
a medium or heavier load.

_Pierce the Guard (Ex)_: At 8th level, when attacking with a light or one-handed weapon, the
cavalier ignores the penalty for fighting defensively or using Combat Expertise on his first melee
attack roll each round. If fighting with two weapons, he ignores the penalty for the first attack
with each weapon, as long as the off-hand weapon is a light weapon.

The cavalier can't use this ability with double weapons.

_One Purpose (Ex)_: At 15th level, the cavalier's mount shares the benefits of the cavalier's
guarded ability as long as both are wearing light or no armor and carrying no more than a light
load.

The cavalier must fight defensively or use Combat Expertise to grant these benefits, but the mount
need not. In addition, the mount gains all the benefits of the cavalier's challenge, regardless of
what barding it wears.

## ORDER OF THE SHROUD (CAVALIER ORDER) {#order-of-the-shroud-cavalier-order}

Cavaliers of this order seek out and destroy undead and those who harbor or create them. They scour
old crypts, graveyards, and battlefields to bring eternal rest.

## Edicts {#order-of-the-shroud-cavalier-order-edicts}

The cavalier must protect the common folk from the scourge of the undead. He must seek out and
destroy the restless dead and give aid to those haunted by them. He must protect those who cannot
defend themselves, and root out sources that birth the corruption of life and death.

## Challenge {#order-of-the-shroud-cavalier-order-challenge}

Whenever an order of the shroud cavalier issues a challenge to an undead creature, he receives a +1
morale bonus on attack rolls against the target of his challenge for 1 minute. The bonus increases
by 1 for every 4 class levels the cavalier possesses.

## Skills {#order-of-the-shroud-cavalier-order-skills}

An order of the shroud cavalier adds Knowledge (local) (Int) and Knowledge (religion) (Int) to his
list of class skills. An order of the shroud cavalier can attempt Knowledge (religion) checks
untrained. If he has ranks in that skill, as long as a Knowledge (religion) check involves undead or
haunts, he receives a bonus on the check equal to 1/2 his cavalier level (minimum +1).

## Order Abilities {#order-of-the-shroud-cavalier-order-order-abilities}

A cavalier belonging to the order of the shroud gains the following abilities as he increases in
level.

_Spiritual Shield (Su)_: At 2nd level, the cavalier can call upon the spirits of the fallen for
protection. Once per day as an immediate action when attacked by an undead target of his challenge,
the cavalier can gain a deflection bonus equal to his Charisma modifier to his AC against that
attack. The cavalier must decide to use this ability before the attack roll.

_Destroyer of the Undead (Su)_: At 8th level, the cavalier's weapons are treated as having the
cavalier's alignment for the purpose of overcoming the damage reduction of undead creatures. Against
an undead target of his challenge, the cavalier automatically overcomes all damage reduction that
undead possesses.

_Stand Against Darkness (Ex or Su)_: At 15th level, the cavalier can take revenge on undead that
dare strike him or those he seeks to protect. Whenever an undead creature that is the subject of his
challenge hits the cavalier or an adjacent ally with a melee attack, the creature provokes an attack
of opportunity from the cavalier. The cavalier gains a +2 morale bonus on attacks of opportunity
provoked as a result of this ability. If an undead subject of the cavalier's challenge threatens a
critical hit against the cavalier, the cavalier gains a deflection bonus equal to his Charisma
modifier against the confirmation roll. This bonus functions as a supernatural ability.
