+++
id = "ref/arc-spiritualist/necrologist"
kind = "archetype"
title = "Necrologist"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Necrologist"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "necrologist", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "horror-adventures"
page = "69"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "shared-consciousness" },
  { anchor = "undead-phantom" },
  { anchor = "cling-of-the-grave" },
  { anchor = "unnatural-aura", level = 5 },
  { anchor = "channel-resistance", level = 6 },
  { anchor = "lifedrinker", level = 13 },
  { anchor = "bonded-manifestation" },
  { anchor = "channel-energy", level = 4 },
  { anchor = "necropsychic-conduit", level = 12 },
]
trades = [
  { replaces = "Slam damage increase gained at 5th level", feature = "phantom", levels = [5], power = "slam damage", by = ["unnatural-aura"] },
  { replaces = "Devotion", by = ["channel-resistance"] },
  { replaces = "Slam damage increase gained at 13th level", feature = "phantom", levels = [13], power = "slam damage", by = ["lifedrinker"] },
  { replaces = "Spiritual interference", feature = "spiritual-interference", by = ["channel-energy"] },
  { replaces = "Greater spiritual interference", feature = "greater-spiritual-interference", by = ["necropsychic-conduit"] },
  { alters = "Alignment" },
  { alters = "Bonded manifestation", feature = "bonded-manifestation", by = ["bonded-manifestation"] },
  { alters = "Shared consciousness", feature = "shared-consciousness", by = ["shared-consciousness"] },
  { alters = "Share spells", by = ["cling-of-the-grave"] },
]
+++

All spiritualists call upon residual phantoms that cling to the living world through force of will
and unresolved passion. The vile spiritualists known as necrologists reach farther toward the
Negative Energy Plane, however, and for whatever evil purpose, they bring back malevolent spirits
whose passions have turned to vengeance and hate for all life.

## Alignment {#alignment}

Only an evil character can contact a malevolent undead phantom and take the necrologist archetype.
If a necrologist becomes nonevil, she can continue to take spiritualist levels, but her phantom
ceases to give her benefits while in her consciousness, she can't use bonded manifestation, and if
she manifests the phantom, it is no longer loyal to her and likely attacks her and her allies.

This alters the spiritualist's alignment.

## Spells {#spells}

A necrologist adds the following spells to her class list: 1st—_hide from undead_; 2nd—_ghostly
disguise_, _haunting mists_; 3rd—_haunting choir_; 4th—_lesser age resistance_; 5th—_age
resistance_; 6th—_greater age resistance , create greater undead_.

## Shared Consciousness {#shared-consciousness}

A necrologist gains a bonus on saving throws against death effects, energy drain, and negative
energy rather than against mind-affecting effects (and can shunt such an effect onto the phantom)
when her undead phantom is contained within her consciousness.

This ability alters shared consciousness.

## Undead Phantom {#undead-phantom}

A necrologist's phantom is [undead](ref/type/undead), rather than an outsider. It has normal undead
immunities and no Constitution score; uses d8 Hit Dice, each of which is modified by the phantom's
Charisma modifier as normal; and gains the abilities below at the levels indicated. An undead
phantom otherwise follows the standard phantom rules (for instance, its base attack bonus and skills
don't change to match undead).

## Cling of the Grave (Su) {#cling-of-the-grave}

An undead phantom can [hold the charge](ref/rule/duration) on a touch spell of the necromancy school
up to a maximum of 1 round per spiritualist level of the necrologist.

This ability alters share spells.

## Unnatural Aura (Su) {#unnatural-aura}

At 5th level, animals do not willingly approach within 30 feet of a fully manifested undead phantom
unless the necrologist succeeds at a Handle Animal, Ride, or wild empathy check (DC = 10 + 1/2 the
necrologist's spiritualist level + the phantom's Charisma modifier).

This replaces the slam damage increase gained at 5th level.

## Channel Resistance (Su) {#channel-resistance}

At 6th level, a necrologist's phantom gains a +4 bonus on saving throws to resist the effects of
channel energy.

This ability replaces devotion.

## Lifedrinker (Su) {#lifedrinker}

At 13th level, when a necrologist's phantom reduces a creature to fewer than 0 hit points with an
attack or spell, the necrologist can expend one use of her channel energy ability as a swift action
to affect the same target with _[death knell](ref/spell/death-knell)_. If the target fails its save,
the necrologist can choose either herself or her phantom to gain the benefit of the spell.

This replaces the necrologist's slam damage increase gained at 13th level.

## Bonded Manifestation {#bonded-manifestation}

A necrologist cannot use ectoplasmic bonded manifestation.

This ability alters bonded manifestation.

## Channel Energy (Su) {#channel-energy}

At 4th level, a necrologist gains the ability to
[channel negative energy](ref/ability/channel-energy), with an effective cleric level equal to her
spiritualist level - 3. She can use this ability a number of times per day equal to 1 + her Charisma
modifier.

This ability replaces spiritual interference.

## Necropsychic Conduit {#necropsychic-conduit}

At 12th level, a necrologist can cast psychic spells as if she had the
[Thanatopic Spell](ref/feat/thanatopic-spell) and [Threnodic Spell](ref/feat/threnodic-spell)
metamagic feats, using her undead phantom as a conduit to pierce the defenses of undead creatures.
If her phantom has been banished or is not within 30 feet of her when she casts the spells, however,
these feats have no effect.

This ability replaces greater spiritual interference.
