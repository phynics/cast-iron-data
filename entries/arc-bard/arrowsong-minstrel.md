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
replaces = ["Bardic knowledge", "dirge of doom", "distraction", "fascinate", "inspire competence", "lore master", "soothing performance", "The versatile performance gained at 2nd level", "well-versed", "Suggestion", "mass suggestion"]
alters = ["Weapon proficiencies", "Spellcasting"]
+++

Originating from the wooded wilds of Hymbria, Arrowsong minstrels combine the elven traditions of
archery, song, and spellcasting into a seamless harmony of dazzling magical effects.

**Weapon Proficiency**

**Alters:** Weapon proficiencies

**Info:** An Arrowsong minstrel is proficient with [longbows](ref/eq-weapon/longbow), but not the
longsword, rapier, or whip.

**Diminished Spellcasting**

**Alters:** Spellcasting

**Info:** An Arrowsong minstrel casts one fewer spell of each level than normal. If this reduces the
number to 0, she can cast spells of that level only if her Charisma score allows
[bonus spells](ref/rule/determine-bonuses) of that level.

**Arcane Archery**

**Flavor:** An Arrowsong minstrel's skill at ranged martial arts allows her to learn to cast a
number of powerful, offensive spells that would otherwise be unavailable to her.

**At 1st Level:** She selects a number of spells from the sorcerer/wizard spell list (see _special_
below) equal to her Charisma modifier (minimum 1) and adds them to her bard spell list as bard
spells of the same level. The spells selected must not already be on the bard spell list, and must
be 6th level or lower.

**At 12th Level:** She adds an additional spell to her bard spell list.

**At 16th Level:** She adds an additional spell to her bard spell list.

**At 20th Level:** She adds an additional spell to her bard spell list.

**At 4th Level:** She adds an additional sorcerer/wizard spell to her bard spell list.

**At 8th Level:** She adds an additional spell to her bard spell list.

**Passive:** For the purpose of meeting the requirements of combat feats and prestige classes, an
Arrowsong minstrel treats her bard level as her base attack bonus (in addition to base attack
bonuses gained from other classes and Hit Dice). Her skilled blending of archery and arcane magic
also allows an Arrowsong minstrel to fulfill a spell's somatic components even when using a bow in
both hands (though not other ranged weapons).

**Replaces:** Bardic knowledge, dirge of doom, distraction, fascinate, inspire competence, lore
master, soothing performance

**Special:** An Arrowsong minstrel is limited to the following spells when adding spells to her
spell list in this manner: [acid arrow](ref/spell/acid-arrow),
[arrow eruption](ref/spell/arrow-eruption), [flame arrow](ref/spell/flame-arrow),
[gravity bow](ref/spell/gravity-bow), [greater magic weapon](ref/spell/magic-weapon-greater),
[longshot](ref/spell/longshot), [magic weapon](ref/spell/magic-weapon),
[protection from arrows](ref/spell/protection-from-arrows),
[spectral hand](ref/spell/spectral-hand), [true strike](ref/spell/true-strike), and sorcerer/wizard
spells of the evocation school. An Arrowsong minstrel must still select these spells as spells known
before she can cast them.

**Precise Minstrel (Ex)**

**Ability:** An Arrowsong minstrel gains [Precise Shot](ref/feat/precise-shot) as a bonus feat.

**Gained:** At 2nd Level

**Passive:** In addition, any creature that is affected by any of the Arrowsong minstrel's bardic
performance does not provide soft [cover](ref/rule/cover) to enemies against her ranged attacks with
a bow.

**Replaces:** The versatile performance gained at 2nd level, well-versed

**Arrowsong Strike (Su)**

**At 18th Level:** An Arrowsong minstrel using a multiple-target spell with this ability can deliver
one ray or line of effect with each attack when using a [full-attack](ref/rule/full-attack) action,
up to the maximum allowed by the spell (in the case of ray effects). Any effects not used in the
round the spell is cast are lost.

**At 6th Level:** An Arrowsong minstrel can use spellstrike (as per the [magus](ref/class/magus)
class feature) to cast a single-target ranged touch attack spell and deliver it through a ranged
weapon attack. Even if the spell can normally affect multiple targets, only a single missile, ray,
or effect accompanies the attack. She cannot use spellstrike with normal touch attacks or melee
attacks.

**Replaces:** Suggestion, mass suggestion
