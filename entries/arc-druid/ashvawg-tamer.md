+++
id = "ref/arc-druid/ashvawg-tamer"
kind = "archetype"
title = "Ashvawg Tamer"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Ashvawg%20Tamer"
source_ids = ["pathfinder-5-sins-of-the-saviors"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ashvawg_tamer", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "pathfinder-5-sins-of-the-saviors"
page = "71"

[fields]
kind = "archetype"
features = [
  { anchor = "bestial-bond", level = 4 },
  { anchor = "variant-companion", level = 4 },
  { anchor = "undying-bond", level = 6 },
  { anchor = "exotic-companion", level = 9 },
]
trades = [
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure" },
  { replaces = "Second daily use of wild shape at level 6", feature = "wild-shape", levels = [6] },
  { replaces = "venom immunity", feature = "venom-immunity" },
]
+++

The ashvawg tamer is a variant class that allows a druid to bond with strange and monstrous
creatures. Given the unusual nature of these companions, the tamer also learns ways to strengthen
his valuable ally. Most tamers worship [Lamashtu](ref/faith/lamashtu), the Demon Queen, though a few
have discovered these practices independently. Tamers develop a stronger bond with their companion
than some of the most powerful druids or rangers, and often travel to exotic locations to find
strange specimens to tame, with bragging rights going to those with the most unusual creature.

## Class Skills {#class-skills}

Eliminate Diplomacy and Heal from the druid's class skill list.

Add Intimidate and Knowledge (arcana).

## Class Features {#class-features}

All of the following are features of the ashvawg tamer druid variant class.

## Bestial Bond (Sp) {#bestial-bond}

At 4th level, the druid can call out to savage powers of the wilds, entreating them to aid her and
her companion. Doing so allows her to cast _[cure serious wounds](ref/spell/cure-serious-wounds)_,
_[neutralize poison](ref/spell/neutralize-poison)_, or _[remove disease](ref/spell/remove-disease)_
on her animal companion as a [spell-like ability](ref/umr/spell-like-abilities) by channeling the
power of nature. The druid does not need to have these spells prepared as they come directly from
the goddess. Using this ability, however, causes the druid to take 1d4 points of
[Wisdom damage](ref/rule/ability-damage-drain). Any effect that prevents this Wisdom damage from
occurring also prevents the use of this ability.

## Variant Companion (Ex) {#variant-companion}

At 4th level the druid adds additional non-animals to her alternate list of animal companions. If
she chooses one of these creatures as an animal companion, she may use her wild empathy ability to
influence the creature (even though it is not an animal and its intelligence may be above 2), though
she takes a -4 penalty on this check. If the druid and the companion share a common language these
checks are not needed. If the companion's intelligence is 3 or higher, the number of "tricks" the
druid can teach it refers to the number of commands the creature understands regardless of language.

- 1st Level or Higher: [darkmantle](ref/monster/darkmantle), [krenshar](ref/monster/krenshar),
  [shocker lizard](ref/monster/shocker-lizard)

- 4th Level or Higher (Level -3): [hippogriff](ref/monster/hippogriff)

- 10th Level or Higher (Level -9): [girallon](ref/monster/girallon), [griffon](ref/monster/griffon),
  [owlbear](ref/monster/owlbear), [sea cat](ref/monster/sea-cat)

- 13th Level or Higher (Level -12): [bulette](ref/monster/bulette), [chimera](ref/monster/chimera)

## Undying Bond (Sp) {#undying-bond}

At 6th level the druid can use her bestial bond ability to cast
_[resurrection](ref/spell/resurrection)_ on her animal companion.

## Exotic Companion (Ex) {#exotic-companion}

At 9th level the druid adds additional non-animals to her alternate list of animal companions, all
of them with higher intelligence and strange shapes. It otherwise functions as the variant companion
ability.

- 7th Level or Higher (Level -6): [worg](ref/monster/worg)

- 10th Level or Higher (Level -9): [ettercap](ref/monster/ettercap),
  [manticore](ref/monster/manticore), [minotaur](ref/monster/minotaur),
  [winter wolf](ref/monster/worg-winter-wolf)

- 13th Level or Higher (Level -12): [behir](ref/monster/behir), [dragonne](ref/monster/dragonne),
  [hieracosphinx](ref/monster/sphinx-hieracosphinx)

## Resist Nature's Lure {#resist-nature-s-lure}

The druid does not gain this ability.

## Wild Shape (Su) {#wild-shape}

The druid does not gain her second daily use of her wild shape ability at level 6. Hereafter she has
one fewer daily use of the ability than a standard druid of her level.

## Venom Immunity (Ex) {#venom-immunity}

The druid does not gain this ability.
