+++
id = "ref/arc-druid/naga-aspirant"
kind = "archetype"
title = "Naga Aspirant"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Naga%20Aspirant"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "naga_aspirant", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-race-guide"
page = "196"

[fields]
kind = "archetype"
features = [
  { anchor = "aspirant-s-bond" },
  { anchor = "aspirant-s-enlightenment", level = 4 },
  { anchor = "naga-shape", level = 6 },
  { anchor = "augmented-form", level = 9 },
  { anchor = "charming-gaze" },
  { anchor = "darkvision" },
  { anchor = "detect-thoughts" },
  { anchor = "guarded-thoughts" },
  { anchor = "poison-immunity" },
  { anchor = "poisonous-sting" },
  { anchor = "spit-venom" },
  { anchor = "sting" },
  { anchor = "swim" },
  { anchor = "tough-scales" },
  { anchor = "venomous-bite" },
  { anchor = "true-naga", level = 20 },
]
trades = [
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["aspirant-s-bond"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["aspirant-s-enlightenment"] },
  { replaces = "Wild Shape", feature = "wild-shape", by = ["naga-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["augmented-form"] },
  { replaces = "a thousand faces", feature = "a-thousand-faces", by = ["augmented-form"] },
  { replaces = "timeless body", feature = "timeless-body", by = ["augmented-form"] },
  { replaces = "Wildshape (at will)", by = ["true-naga"] },
]
+++

The naga aspirant follows the ancient beliefs and engages in the rituals of a druidic sect dedicated
to the transcendence of her nagaji form through absolute devotion to nagas and naga gods. Through
acting as a herald to the naga deities, the aspirant is rewarded with the ability to unlock her
ultimate spirit form and become a true naga. A naga aspirant has the following class features.

## Aspirant's Bond (Ex) {#aspirant-s-bond}

A naga aspirant gains a spiritual connection to the serpentine deities worshiped by the nagas. At
1st level, and each time she gains a druid level, she may add one of the following spells to her
druid spell list.

0—_acid splash_, _bleed_, _daze_, _mage hand_, _open/close_, _ray of frost_; 1st—_charm person_,
_divine favor_, _expeditious retreat_, _mage armor_, _magic missile, ray of enfeeblement, shield,
shield of faith, silent image, true strike_; 2nd—_acid arrow_, _detect thoughts_, _invisibility_,
_mirror image_, _scorching ray_, _see invisibility_; 3rd— _dispel magic, displacement, fireball,
lightning bolt, suggestion_; 4th—_divine power_, _greater invisibility_.

This ability replaces spontaneous casting.

## Aspirant's Enlightenment (Ex) {#aspirant-s-enlightenment}

At 4th level, a naga aspirant gains a +4 bonus on saving throws against the
[spell-like abilities](ref/umr/spell-like-abilities), supernatural abilities, and poison of nagas.
This ability replaces resist nature's lure.

## Naga Shape (Su) {#naga-shape}

At 6th level, the naga aspirant can use her wild shape ability (gained at 4th level, as normal) to
assume the form of a true naga. This effect functions in a similar manner to a
_[shapechange](ref/spell/shapechange)_ spell with the following exception. The druid's true naga
form is unique, representing her personal evolution. When taking naga form, the nagaji's body
transforms into that of a large serpent, though she keeps her own head. The naga aspirant loses her
limbs and her size increases by one category, granting her a +4 size bonus to Strength and
Constitution, a -2 penalty to Dexterity, and a +2 enhancement bonus to her natural armor bonus. She
gains a +10 enhancement bonus to land speed and a [bite attack](ref/umr/natural-attacks) that deals
1d6 points of damage. She can cast verbal spells in this form, but cannot cast spells with other
components without metamagic or feats such as [Natural Spell](ref/feat/natural-spell). This
otherwise works like and replaces wild shape.

## Augmented Form (Su) {#augmented-form}

At 9th level and every four levels thereafter, a naga aspirant can choose one of the following
abilities to enhance her naga form. Once chosen, this augmentation cannot be changed and always
applies to her naga form. The caster level for these abilities is equal to her druid level, and
unless otherwise stated, the DC is equal to 10 + 1/2 the druid's class level + the druid's Charisma
bonus. This ability replaces venom immunity, a thousand faces, and timeless body.

## Charming Gaze (Sp) {#charming-gaze}

The druid gains a [gaze](ref/umr/gaze) attack that affects creatures within 30 feet as a
_[charm person](ref/spell/charm-person)_ spell.

## Darkvision (Su) {#darkvision}

The druid gains [darkvision](ref/rule/darkvision) with a range of 60 feet.

## Detect Thoughts (Su) {#detect-thoughts}

The druid can use _[detect thoughts](ref/spell/detect-thoughts)_ at will.

## Guarded Thoughts (Ex) {#guarded-thoughts}

The druid gains a +2 racial bonus on saves against charm effects and immunity to any form of mind
reading (such as _[detect thoughts](ref/spell/detect-thoughts)_).

## Poison Immunity (Ex) {#poison-immunity}

The druid gains immunity to all poisons. The druid's naga form must have at least one poison-based
natural attack in order to select this ability.

## Poisonous Sting (Ex) {#poisonous-sting}

The druid's stinger becomes venomous. The naga form must have a tail stinger to take this ability.
Sting—injury; save Fort DC 10 + 1/2 the druid's class level + the druid's Constitution modifier;
_frequency_ 1 round; _effect_ sleep for 2d4 minutes; _cure_ 1 save.

## Spit Venom (Ex) {#spit-venom}

The naga form can spit her venom up to 30 feet as a standard action. This is a ranged touch attack
with no range increment. Any opponent hit by this attack must make a successful save (see above) to
avoid the effect. The naga form must have a [venomous bite](ref/spell/venomous-bite) to take this
ability.

## Sting (Ex) {#sting}

The naga form grows a stinger on the end of her tail, granting her a sting natural attack that deals
1d6 points of piercing damage.

## Swim (Ex) {#swim}

The naga form gains a swim speed equal to her base speed.

## Tough Scales (Ex) {#tough-scales}

The druid's enhancement bonus to her natural armor increases by +2. The druid may select this
ability more than once. Its effects stack.

## Venomous Bite (Ex) {#venomous-bite}

The naga form's bite attack becomes poisonous. Bite—injury; _save_ Fortitude DC 10 + 1/2 the druid's
class level + the druid's Constitution modifier; _frequency_ 1/ round for 6 rounds; _effect_ 1
Constitution damage, _cure_ 1 save.

## True Naga (Su) {#true-naga}

At 20th level, a naga aspirant metamorphoses into a unique naga. Her wild shape form becomes her
natural form, though she can transform into her original nagaji shape at will. Her creature type
permanently changes to aberration. This ability replaces wildshape (at will).
