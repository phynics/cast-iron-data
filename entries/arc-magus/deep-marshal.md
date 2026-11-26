+++
id = "ref/arc-magus/deep-marshal"
kind = "archetype"
title = "Deep Marshal"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Deep%20Marshal"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deep_marshal", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "arcane-anthology"
page = "28"

[fields]
kind = "archetype"
features = [
  { anchor = "deep-spellcasting" },
  { anchor = "bound-by-tradition", level = 1 },
  { anchor = "miner-s-focus-su-ex", level = 3 },
]
trades = [
  { replaces = "Magus arcana gained at 3rd level", feature = "magus-arcana", levels = [3], by = ["miner-s-focus-su-ex"] },
  { alters = "Armor proficiencies", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "medium armor", feature = "medium-armor" },
  { alters = "heavy armor", feature = "heavy-armor" },
  { alters = "Spellcasting", feature = "spells", by = ["deep-spellcasting"] },
  { alters = "Arcane pool", feature = "arcane-pool", by = ["bound-by-tradition"] },
  { alters = "spell combat", feature = "spell-combat", by = ["bound-by-tradition"] },
  { alters = "spellstrike", feature = "spellstrike", by = ["bound-by-tradition"] },
]
+++

According to dwarven legend, the first deep marshals were handpicked by King Taargick himself to
create massive tunnels to aid in the dwarven exodus to Golarion's surface during the Quest for Sky.
Largely unseen by visitors, the deep marshals have survived into the modern era as keepers,
protectors, and repairers of the myriad of stony passages that travel around, through, and under the
Five Kings Mountains. Although the vast majority of deep marshals are [dwarves](ref/race/dwarf), a
few non-dwarves have earned enough trust to be trained as deep marshals, or have learned the same
techniques from studying old dwarven spellbooks.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A deep marshal is proficient with light armor, medium armor, and shields (except tower shields). A
deep marshal can cast magus spells while wearing light armor or medium armor without incurring the
normal spell failure chance. In addition, a deep marshal gains the heavy armor magus ability at 9th
level. This ability alters the magus's armor proficiencies, the medium armor class feature, and the
heavy armor class feature.

## Deep Spellcasting {#deep-spellcasting}

A deep marshal learns numerous arcane secrets involving the shaping and warding of earth and stone.
She adds the following sorcerer/wizard spells to her magus spell list as magus spells of the same
level: _[crafter's curse](ref/spell/crafters-curse)_,
_[crafter's fortune](ref/spell/crafters-fortune)_, _[erase](ref/spell/erase)_,
_[expeditious excavation](ref/spell/expeditious-excavation)_, _[fabricate](ref/spell/fabricate)_,
_[greater make whole](ref/spell/make-whole-greater)_ (_Technology Guide_ 10),
_[knock](ref/spell/knock)_, _[major creation](ref/spell/major-creation)_,
_[make whole](ref/spell/make-whole)_, _[mending](ref/spell/mending)_,
_[minor creation](ref/spell/minor-creation)_, _[move earth](ref/spell/move-earth)_,
_[passwall](ref/spell/passwall)_, _[stone shape](ref/spell/stone-shape)_,
_[transmute mud to rock](ref/spell/transmute-mud-to-rock)_,
_[transmute rock to mud](ref/spell/transmute-rock-to-mud)_, and all 0- through 6th-level
sorcerer/wizard spells of the abjuration school. She must still add such spells to her spellbook to
prepare them. If a spell appears on both the magus and sorcerer/wizard spell lists, the magus uses
the lower of the two spell levels listed for the spell. A deep marshal cannot cast spells from the
enchantment, illusion, or necromancy school and she cannot activate spell-completion or
spell-trigger magic items that use spells from those schools (without making a successful
[Use Magic Device](ref/skill/use-magic-device) check). This alters the magus's spellcasting.

## Bound by Tradition {#bound-by-tradition}

A deep marshal is limited in how she can use her arcane powers. Her arcane pool has a number of
points equal to 1/3 her magus level (minimum 1) + her Intelligence modifier. Furthermore, she cannot
use her arcane pool to grant an enhancement bonus or weapon special ability to a weapon she is
holding unless it is a [battleaxe](ref/eq-weapon/battleaxe), [heavy pick](ref/eq-weapon/heavy-pick),
[warhammer](ref/eq-weapon/warhammer), or weapon with the word "dwarven" in its name. She can use her
spell combat or spellstrike abilities only with such weapons. This alters arcane pool, spell combat,
and spellstrike.

## Miner's Focus (Su/Ex) {#miner-s-focus-su-ex}

At 3rd level, a deep marshal can use the magical properties of her weapon in order to augment her
spellcasting. Whenever she casts a magus spell while wielding a magic battleaxe, heavy pick,
warhammer, or weapon with the word "dwarven" in its name, she adds half the weapon's enhancement
bonus to the her caster level (minimum +1). When attempting a caster level check to overcome
[spell resistance](ref/rule/spell-resistance), she instead adds her weapon's full enhancement bonus.

In addition, she is treated as having a number of ranks in Knowledge (dungeoneering) and Profession
(miner) equal to her magus level, and she attempts Profession (miner) checks using her Intelligence
modifier instead of her Wisdom modifier.

This ability replaces the magus arcana gained at 3rd level.
