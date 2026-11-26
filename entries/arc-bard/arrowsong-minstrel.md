+++
id = "ref/arc-bard/arrowsong-minstrel"
kind = "archetype"
title = "Arrowsong Minstrel"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Arrowsong%20Minstrel"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arrowsong_minstrel", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "arcane-anthology"
page = "30"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting", level = 1 },
  { anchor = "arcane-archery", level = 1 },
  { anchor = "precise-minstrel", level = 2 },
  { anchor = "arrowsong-strike", level = 6 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["arcane-archery"] },
  { replaces = "dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["arcane-archery"] },
  { replaces = "distraction", feature = "bardic-performance", power = "distraction", by = ["arcane-archery"] },
  { replaces = "fascinate", feature = "bardic-performance", power = "fascinate", by = ["arcane-archery"] },
  { replaces = "inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["arcane-archery"] },
  { replaces = "lore master", feature = "lore-master", by = ["arcane-archery"] },
  { replaces = "soothing performance", feature = "bardic-performance", power = "soothing performance", by = ["arcane-archery"] },
  { replaces = "The versatile performance gained at 2nd level", feature = "versatile-performance", levels = [2], by = ["precise-minstrel"] },
  { replaces = "well-versed", feature = "well-versed", by = ["precise-minstrel"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["arrowsong-strike"] },
  { replaces = "mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["arrowsong-strike"] },
  { alters = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { alters = "Spellcasting", feature = "spells", by = ["diminished-spellcasting"] },
]
+++

Originating from the wooded wilds of Hymbria, Arrowsong minstrels combine the elven traditions of
archery, song, and spellcasting into a seamless harmony of dazzling magical effects.

## Weapon Proficiency {#weapon-proficiency}

An Arrowsong minstrel is proficient with [longbows](ref/eq-weapon/longbow), but not the longsword,
rapier, or whip. This alters the bard's weapon proficiencies.

## Diminished Spellcasting {#diminished-spellcasting}

An Arrowsong minstrel casts one fewer spell of each level than normal. If this reduces the number to
0, she can cast spells of that level only if her Charisma score allows
[bonus spells](ref/rule/determine-bonuses) of that level. This alters the bard's spellcasting.

## Arcane Archery {#arcane-archery}

An Arrowsong minstrel's skill at ranged martial arts allows her to learn to cast a number of
powerful, offensive spells that would otherwise be unavailable to her. At 1st level, she selects a
number of spells from the sorcerer/wizard spell list equal to her Charisma modifier (minimum 1) and
adds them to her bard spell list as bard spells of the same level. The spells selected must not
already be on the bard spell list, and must be 6th level or lower. At 4th level and every 4 bard
levels thereafter, she adds an additional sorcerer/wizard spell to her bard spell list. An Arrowsong
minstrel is limited to the following spells when adding spells to her spell list in this manner:
_[acid arrow](ref/spell/acid-arrow)_, _[arrow eruption](ref/spell/arrow-eruption)_,
_[flame arrow](ref/spell/flame-arrow)_, _[gravity bow](ref/spell/gravity-bow)_,
_[greater magic weapon](ref/spell/magic-weapon-greater)_, _[longshot](ref/spell/longshot)_,
_[magic weapon](ref/spell/magic-weapon)_,
_[protection from arrows](ref/spell/protection-from-arrows)_,
_[spectral hand](ref/spell/spectral-hand)_, _[true strike](ref/spell/true-strike)_, and
sorcerer/wizard spells of the evocation school. An Arrowsong minstrel must still select these spells
as spells known before she can cast them.

In addition, for the purpose of meeting the requirements of combat feats and prestige classes, an
Arrowsong minstrel treats her bard level as her base attack bonus (in addition to base attack
bonuses gained from other classes and Hit Dice). Her skilled blending of archery and arcane magic
also allows an Arrowsong minstrel to fulfill a spell's somatic components even when using a bow in
both hands (though not other ranged weapons).

This ability replaces bardic knowledge, dirge of doom, distraction, fascinate, inspire competence,
lore master, and soothing performance.

## Precise Minstrel (Ex) {#precise-minstrel}

At 2nd level, an Arrowsong minstrel gains [Precise Shot](ref/feat/precise-shot) as a bonus feat. In
addition, any creature that is affected by any of the Arrowsong minstrel's bardic performance does
not provide soft [cover](ref/rule/cover) to enemies against her ranged attacks with a bow. This
ability replaces the versatile performance gained at 2nd level and well-versed.

## Arrowsong Strike (Su) {#arrowsong-strike}

At 6th level, an Arrowsong minstrel can use spellstrike (as per the [magus](ref/class/magus) class
feature) to cast a single-target ranged touch attack spell and deliver it through a ranged weapon
attack. Even if the spell can normally affect multiple targets, only a single missile, ray, or
effect accompanies the attack. She cannot use spellstrike with normal touch attacks or melee
attacks.

At 18th level, an Arrowsong minstrel using a multiple-target spell with this ability can deliver one
ray or line of effect with each attack when using a [full-attack](ref/rule/full-attack) action, up
to the maximum allowed by the spell (in the case of ray effects). Any effects not used in the round
the spell is cast are lost.

This ability replaces suggestion and mass suggestion.
