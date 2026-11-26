+++
id = "ref/arc-spiritualist/phantom-blade"
kind = "archetype"
title = "Phantom Blade"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Phantom%20Blade"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantom_blade", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "psychic-anthology"
page = "4"

[fields]
kind = "archetype"
features = [
  { anchor = "phantom-weapon", level = 1 },
  { anchor = "spell-combat", level = 1 },
  { anchor = "spellstrike", level = 2 },
  { anchor = "spirit-of-war", level = 3 },
  { anchor = "etheric-focus", level = 4 },
]
trades = [
  { replaces = "Phantom", feature = "phantom", by = ["phantom-weapon"] },
  { replaces = "phantom recall", feature = "phantom-recall", by = ["phantom-weapon"] },
  { replaces = "spiritual bond", feature = "spiritual-bond", by = ["phantom-weapon"] },
  { replaces = "dual bond", feature = "dual-bond", by = ["phantom-weapon"] },
  { replaces = "Etheric tether", feature = "etheric-tether", by = ["spell-combat"] },
  { replaces = "shared consciousness", feature = "shared-consciousness", by = ["spell-combat"] },
  { replaces = "fused consciousness", feature = "fused-consciousness", by = ["spell-combat"] },
  { replaces = "empowered consciousness", feature = "empowered-consciousness", by = ["spell-combat"] },
  { replaces = "Bonded senses", feature = "bonded-senses", by = ["spellstrike"] },
  { replaces = "Bonded manifestation", feature = "bonded-manifestation", by = ["spirit-of-war"] },
  { replaces = "Spiritual interference", feature = "spiritual-interference", by = ["etheric-focus"] },
  { replaces = "greater spiritual interference", feature = "greater-spiritual-interference", by = ["etheric-focus"] },
  { alters = "Weapon", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { alters = "armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
]
+++

A small selection of spiritualists are connected to spirits of combat and warfare, and manifest a
weapon instead of a phantom. These spiritualists are known as phantom blades and fight with
ectoplasmic weapons. Phantom blades are often found in Mendev and the Worldwound, where
spiritualists are baptized in the blood of comrades; the last survivor of an unfortunate squad might
return bearing one of these ghostly blades.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A phantom blade is proficient with all simple and martial weapons. She is also proficient with light
and medium armor.

This ability alters the spiritualist's weapon and armor proficiency.

## Phantom Weapon {#phantom-weapon}

A phantom blade begins play with an ectoplasmic sentient weapon known as a _phantom weapon_ whose
weapon type is chosen by the phantom blade. The weapon type must be one with which the phantom blade
is proficient. A _phantom weapon_ functions similarly to the _black blade_ of the
[bladebound](ref/arc-magus/bladebound) magus archetype except as noted on the Phantom Weapon
Progression table on page 6 and in the descriptions below. A phantom blade with this class feature
can't have a phantom of any kind, even from another class.

This replaces phantom, phantom recall, spiritual bond, and dual bond.

## Spell Combat (Ex) {#spell-combat}

A phantom blade can cast spells and wield her _phantom weapon_ at the same time. This functions as
the [magus's](ref/class/magus) spell combat class ability (_Ultimate Magic_ 10).

This replaces etheric tether, shared consciousness, fused consciousness, and empowered
consciousness.

## Spellstrike (Su) {#spellstrike}

At 2nd level, a phantom blade can deliver spells through her _phantom weapon_. This functions like
the magus's spellstrike class ability (_Ultimate Magic_ 10) except the only weapon the spiritualist
can use to deliver spells is her _phantom weapon_.

This replaces bonded senses.

## Spirit of War (Ex) {#spirit-of-war}

At 3rd level and every 5 spiritualist levels thereafter, a phantom blade gains a bonus combat feat.
The spiritualist must meet the prerequisites for these feats, but she treats her spiritualist level
as her base attack bonus (in addition to base attack bonuses gained from other classes and racial
Hit Dice) for the purpose of qualifying for these feats. The phantom blade also treats her
spiritualist level as her fighter level for the purpose of selecting feats with a minimum number of
fighter levels as a prerequisite.

This replaces bonded manifestation.

## Etheric Focus (Ex) {#etheric-focus}

At 4th level, the phantom blade can use her _phantom weapon_ to aid her in casting spells with
[thought components](ref/rule/components-oa). She can center herself (_Pathfinder RPG Occult
Adventures_ 144) as a swift action. At 12th level, the spiritualist can center herself as a free
action.

This ability replaces spiritual interference and greater spiritual interference.

## Phantom Weapon Ability Descriptions {#phantom-weapon-ability-descriptions}

A _phantom weapon_ has special abilities (or imparts abilities to its wielder) depending on the
wielder's spiritualist level. These abilities are cumulative. A _phantom weapon_ normally refuses to
use any of its abilities when wielded by anyone other than its phantom blade, and acts as an
incorporeal masterwork weapon of its type.

**Phantom Weapon Progression**

|Spiritualist Class Level|Enhancement Bonus|Cha|Int/Wis|Ego|Special|
| --- | --- | --- | --- | --- | --- |
|1st–2nd|+0|10|6|5|Alertness, phantom touch, telepathy, weapon of the mind|
|3rd–4th|+1|11|7|5|Quick manifest|
|5th–6th|+2|12|8|8|Ectoplasmic pool|
|7th–8th|+2|13|9|10|Reshape|
|9th–10th|+3|14|10|12|Phantom tether|
|11th–12th|+3|15|11|14|—|
|13th–14th|+4|16|12|16|Quick reshape|
|15th–16th|+4|17|13|18|—|
|17th–18th|+5|18|14|22|Etheric strikes|
|19th–20th|+5|19|15|24|Soul eater|

### Alertness (Ex) {#alertness}

While the phantom blade is wielding or harboring her _phantom weapon_, she gains the
[Alertness](ref/feat/alertness) feat.

### Phantom Touch (Ex) {#phantom-touch}

A _phantom weapon_ is always treated as a _[ghost touch](ref/magic-enh/ghost-touch-weapon)_ weapon,
regardless of weapon type or any other abilities modifying the weapon. If the _phantom weapon_ would
ever be destroyed, it is instead harbored in the spiritualist's consciousness for 24 hours.

### Telepathy (Su) {#telepathy}

While the phantom blade is wielding or carrying her _phantom weapon_, she can communicate
telepathically with the weapon.

### Weapon of the Mind (Ex) {#weapon-of-the-mind}

The phantom blade can harbor her _phantom weapon_ in her consciousness or manifest it in its
ectoplasmic form. The phantom blade can manifest the weapon through a ritual that takes 1 minute to
perform. Harboring the _phantom weapon_ requires a full-round action.

While the weapon is harbored, the phantom blade gains
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat and treats her unarmed
strike damage as a [monk](ref/class/monk) of her level - 2. If the phantom blade already has this
feat, she instead gains [Weapon Focus](ref/feat/weapon-focus) (unarmed strike). The phantom blade's
unarmed strikes gain the phantom weapon's enhancement bonus and other abilities when the weapon is
harbored. The phantom weapon also recovers a number of hit points equal to its ego score every hour
that it is harbored.

### Quick Manifest (Ex) {#quick-manifest}

At 3rd level, the phantom blade can manifest her _phantom weapon_ as a swift action.

### Ectoplasmic Pool (Ex) {#ectoplasmic-pool}

At 5th level, the phantom blade gains a reservoir of excess ethereal energy and ectoplasm that she
can draw upon to improve her _phantom weapon_. This pool has a number of ectoplasmic points equal to
half her spiritualist level + her Wisdom modifier. The pool refreshes once per day when the
spiritualist refreshes her daily spells.

The phantom blade can spend a number of ectoplasmic points to enhance or modify her _phantom
weapon_. As a free action, she can spend 1 point to manifest or harbor her weapon. The spiritualist
can also spend 2 ectoplasmic points as a free action to allow attacks made with her _phantom weapon_
to resolve against touch AC for 1 round.

As a swift action, she can spend 2 ectoplasmic points to grant the weapon one of the following
weapon special abilities for 1 minute: _[corrosive](ref/magic-enh/corrosive)_,
_[defending](ref/magic-enh/defending)_, _[flaming](ref/magic-enh/flaming)_,
_[frost](ref/magic-enh/frost)_, _[keen](ref/magic-enh/keen)_, _[merciful](ref/magic-enh/merciful)_,
_[shock](ref/magic-enh/shock)_, or _[throwing](ref/magic-enh/throwing)_. At 11th level, she can
spend 3 ectoplasmic points to grant the weapon one of the following weapon special abilities for 1
minute: _[corrosive burst](ref/magic-enh/corrosive-burst)_,
_[disruption](ref/magic-enh/disruption)_, _[flaming burst](ref/magic-enh/flaming-burst)_,
_[holy](ref/magic-enh/holy)_, _[icy burst](ref/magic-enh/icy-burst)_,
_[shocking burst](ref/magic-enh/shocking-burst)_, or _[unholy](ref/magic-enh/unholy)_. At 15th
level, she can spend 5 ectoplasmic points to grant the weapon one of the following weapon special
abilities for 1 minute: _[brilliant energy](ref/magic-enh/brilliant-energy)_,
_[dancing](ref/magic-enh/dancing)_, or _[speed](ref/magic-enh/speed)_. A phantom blade can spend an
appropriate number of points to grant the weapon multiple abilities as one action. A _phantom
weapon_ cannot have a modified bonus higher than +10.

### Reshape (Ex) {#reshape}

At 7th level, a phantom blade can change the weapon type of her _phantom weapon_ when she refreshes
her daily spells.

### Phantom Tether (Su) {#phantom-tether}

At 9th level, a phantom blade can spend 1 ectoplasmic point as a swift action to instantly recall
her _phantom weapon_ to her hand or consciousness from as far as 1 mile away.

### Quick Reshape (Ex) {#quick-reshape}

At 13th level, a phantom blade can spend 1 ectoplasmic point to reshape her _phantom weapon_ as a
full-round action, 2 ectoplasmic points to reshape her weapon as a standard action, 3 ectoplasmic
points to reshape her weapon as a move action, and 4 ectoplasmic points to reshape her weapon as a
swift action.

### Etheric Strikes (Sp) {#etheric-strikes}

At 17th level, a phantom blade can spend 1 ectoplasmic point as a swift action to allow her _phantom
weapon_ to ignore a number of points of [damage reduction](ref/rule/damage-reduction) equal to twice
her Wisdom modifier or twice the weapon's Charisma modifier, whichever is higher.

### Soul Eater (Su) {#soul-eater}

At 19th level, the phantom blade and her weapon can feast on the energy of departing souls. Each
time she kills a living or incorporeal creature with her _phantom weapon_, she can pick one of the
following effects: she gains a +2 bonus on attack and damage rolls for 1 round, she recovers one
1st- or 2nd-level spell slot, or she gains a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to the _phantom weapon's_ ego (these
temporary hit points last until lost or 1 minute, whichever is shorter). The creature killed must
have a number of Hit Dice equal to or greater than half the phantom blade's spiritualist level for
this to occur.
