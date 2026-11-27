+++
id = "ref/arc-spiritualist/priest-of-the-fallen"
kind = "archetype"
title = "Priest of the Fallen"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Priest%20of%20the%20Fallen"
source_ids = ["heroes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "priest_of_the_fallen", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "heroes-of-golarion"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "mythmaker", level = 1 },
  { anchor = "channel-energy", level = 3 },
  { anchor = "phantom-call", level = 6 },
  { anchor = "fused-consciousness", level = 10 },
  { anchor = "masterful-faith", level = 17 },
  { anchor = "true-legend", level = 20 },
]
trades = [
  { replaces = "Shared consciousness", feature = "shared-consciousness", by = ["mythmaker"] },
  { replaces = "Bonded manifestation", feature = "bonded-manifestation", by = ["channel-energy"] },
  { replaces = "Phantom recall", feature = "phantom-recall", by = ["phantom-call"] },
  { replaces = "Dual bond", feature = "dual-bond", by = ["masterful-faith"] },
  { alters = "Phantom", feature = "phantom", by = ["mythmaker"] },
  { alters = "Fused consciousness", feature = "fused-consciousness", by = ["fused-consciousness"] },
  { alters = "Empowered consciousness", feature = "empowered-consciousness", by = ["true-legend"] },
]
+++

Countless hero-gods have risen and fallen through Iblydos's long history, leaving behind mighty
spirits. Those attuned to these fallen hero-gods can become conduits for their restless souls and
agents acting out their divine will. The result is a priest of the fallen, a spiritualist who
channels her land's legends and provides a vessel for mighty heroes to perform heroic acts once
more.

## Mythmaker (Su) {#mythmaker}

A priest of the fallen can channel many different hero-god phantoms, though only one at a time.
These spirits will not suffer being confined in a mortal's consciousness and must be manifested in
ectoplasmic or incorporeal form or they return to the Ethereal Plane. They each have an emotional
focus depending on their personality and retain some of their hero-god powers, determined by their
mythic archetype. A priest of the fallen can channel a hero-god phantom with a ritual that takes 1
minute to perform. A priest of the fallen can channel only one hero-god phantom per 24 hours, but
once channeled, a hero-god phantom remains until a new one is channeled.

### Archmage {#archmage}

The phantom gains _[magic missile](ref/spell/magic-missile)_ and _[sleep](ref/spell/sleep)_ as
[spell-like abilities](ref/umr/spell-like-abilities). It can use each spell-like ability a number of
times per day equal to its Hit Dice, which it uses in place of a caster level. At 12th level, it can
also cast _[fireball](ref/spell/fireball)_ and _[hold person](ref/spell/hold-person)_ each once per
day.

### Champion {#champion}

The phantom gains [Weapon Focus](ref/feat/weapon-focus) (slam) as a bonus feat. At 12th level, it
gains [Greater Weapon Focus](ref/feat/greater-weapon-focus) (slam) and
[Weapon Specialization](ref/feat/weapon-specialization) (slam) as bonus feats.

### Guardian {#guardian}

The phantom gains a +2 natural armor bonus when it manifests in its ectoplasmic form, and a +2
deflection bonus to AC when it manifests in its incorporeal form. At 12th level, the phantom
increases its maximum hit points by twice its number of Hit Dice.

### Hierophant {#hierophant}

The phantom gains _[bane](ref/spell/bane)_ and _[bless](ref/spell/bless)_ as
[spell-like abilities](ref/umr/spell-like-abilities). It can use each spell-like ability a number of
times per day equal to its Hit Dice, which it uses in place of a caster level. At 12th level, it can
also cast _[prayer](ref/spell/prayer)_ and _[searing light](ref/spell/searing-light)_ each once per
day.

### Marshal {#marshal}

The phantom can fill its allies with its triumphant spirit as a standard action, granting them a +1
morale bonus on saving throws against charm and fear effects and a +1 competence bonus on attack and
weapon damage rolls for a number of rounds per day equal to 2 + its Charisma modifier. These rounds
need not be consecutive. At 12th level, if the phantom is hit by an attack of opportunity, it can
use an immediate action to allow an ally to make an attack of opportunity against the creature that
attacked the phantom if it's within the ally's melee reach.

### Trickster {#trickster}

The phantom gains the [sneak attack](ref/ability/sneak-attack) rogue class feature as a rogue of a
level equal to the phantom's Hit Dice. It can use the sneak attack ability a number of times per day
equal to its Dexterity modifier (minimum 1). At 12th level, whenever the phantom is in darkness or
[dim light](ref/rule/vision-and-light), it can move at full speed without taking a penalty on
Stealth checks.

This alters phantom and replaces shared consciousness.

## Channel Energy (Su) {#channel-energy}

At 3rd level, a priest of the fallen can channel her phantom's divine energy. This functions as the
cleric's [channel energy](ref/ability/channel-energy) class feature, except that the amount of
damage dealt or hit points restored is equal to 1d6 points plus an additional 1d6 points for every 2
spiritualist levels beyond 3rd. The priest of the fallen decides to channel positive or negative
energy based on her alignment. A neutral priest of the fallen can channel either positive or
negative energy, but once this choice is made, it cannot be changed. She can use this ability a
number of times per day equal to her Charisma modifier (minimum 1).

This replaces bonded manifestation.

## Phantom Call (Su) {#phantom-call}

At 6th level, once per day, a priest of the fallen can summon a fully manifested hero-god phantom
from the Ethereal Plane as a standard action. If she already has a hero-god phantom manifested, that
phantom vanishes back to the Ethereal Plane.

This replaces phantom recall.

## Fused Consciousness (Su) {#fused-consciousness}

At 10th level, this ability functions as usual, except the phantom retreats to the Ethereal Plane
rather than the priest's consciousness.

This alters fused consciousness.

## Masterful Faith (Su) {#masterful-faith}

At 17th level, a priest of the fallen chooses any two [cleric domains](ref/ability/domains) and
receives their full benefits, treating her spiritualist level as her cleric level. She adds the
domain spells to her spells known.

This replaces dual bond.

## True Legend (Su) {#true-legend}

At 20th level, a priest of the fallen is strong enough to confine a phantom in her consciousness as
a standard action. On the start of her following turn, she gains access to all standard spiritualist
abilities involving a confined phantom. She can confine her phantom for a number of rounds per day
equal to 4 + her Wisdom modifier.

This alters empowered consciousness.
