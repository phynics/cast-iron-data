+++
id = "ref/arc-magus/kensai"
kind = "archetype"
title = "Kensai"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Kensai"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kensai", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-combat"
page = "55"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting" },
  { anchor = "canny-defense", level = 1 },
  { anchor = "weapon-focus", level = 1 },
  { anchor = "perfect-strike", level = 4 },
  { anchor = "fighter-training", level = 7 },
  { anchor = "iaijutsu", level = 7 },
  { anchor = "critical-perfection", level = 9 },
  { anchor = "superior-reflexes", level = 11 },
  { anchor = "iaijutsu-focus", level = 13 },
  { anchor = "iaijutsu-master", level = 19 },
  { anchor = "weapon-mastery", level = 20 },
]
trades = [
  { replaces = "Spell recall", feature = "spell-recall", by = ["perfect-strike"] },
  { replaces = "Knowledge pool", feature = "knowledge-pool", by = ["fighter-training"] },
  { replaces = "Medium armor", feature = "medium-armor", by = ["iaijutsu"] },
  { replaces = "Magus arcana gained at 9th level", feature = "magus-arcana", levels = [9], by = ["critical-perfection"] },
  { replaces = "Improved spell recall", feature = "improved-spell-recall", by = ["superior-reflexes"] },
  { replaces = "Heavy armor", feature = "heavy-armor", by = ["iaijutsu-focus"] },
  { replaces = "Greater spell access", feature = "greater-spell-access", by = ["iaijutsu-master"] },
  { replaces = "True magus", feature = "true-magus", by = ["weapon-mastery"] },
]
+++

A kensai spends his life focusing his training and meditation into a rapturous perfection of the use
of a single weapon, which is usually but not always a sword, channeling his arcane might through it
in a dizzying and deadly dance beyond the abilities of even the greatest of mundane warriors.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A kensai is proficient in simple weapons and in a single martial or exotic melee weapon of his
choice. A kensai is not proficient with armor or shields and suffers normal arcane spell failure
chance when casting magus spells while armored.

## Diminished Spellcasting {#diminished-spellcasting}

A kensai may cast one fewer spell of each level than normal. If this reduces the number to 0, he may
cast spells of that level only if his Intelligence allows [bonus spells](ref/rule/determine-bonuses)
of that level.

## Canny Defense (Ex) {#canny-defense}

At 1st level, when a kensai is wielding his chosen weapon, he gains the canny defense ability. This
is identical to the [duelist prestige class](ref/pclass/duelist) ability of the same name (_Core
Rulebook_ 382), save that his chosen weapon may be of any type.

## Weapon Focus (Ex) {#weapon-focus}

At 1st level, a kensai gains [Weapon Focus](ref/feat/weapon-focus) with his chosen weapon as a bonus
feat.

## Perfect Strike (Ex) {#perfect-strike}

At 4th level, when a kensai hits with his chosen weapon, he can spend 1 point from his arcane pool
in order to maximize his weapon damage. Don't roll for damage—the weapon deals maximum damage. This
affects only the weapon's base damage dice, not additional damage from
[sneak attack](ref/ability/sneak-attack), magical weapon properties, spellstrike, or critical hits.

If the kensai confirms a critical hit, he can instead spend 2 points from his arcane pool to
increase his weapon's critical multiplier by 1. This ability replaces spell recall.

## Fighter Training (Ex) {#fighter-training}

Starting at 7th level, a kensai counts his magus level -3 as his fighter level for the purpose of
qualifying for feats (if he has levels in fighter, these levels stack), but forfeits the benefit of
such feats with weapons other than his favored weapon. This ability replaces knowledge pool.

## Iaijutsu (Ex) {#iaijutsu}

At 7th level, a kensai applies his Intelligence modifier as well as his Dexterity modifier on
initiative rolls (minimum 0). A kensai may make attacks of opportunity when
[flat-footed](ref/rule/flat-footed), and may draw his favored weapon as a free action as part of
taking an attack of opportunity. This ability replaces the medium armor ability.

## Critical Perfection (Ex) {#critical-perfection}

At 9th level, a kensai adds his Intelligence bonus (minimum 0) on critical hit confirmation rolls
with his favored weapon. In addition, the kensai may use his magus levels in place of his base
attack bonuses to qualify for [Critical Focus](ref/feat/critical-focus) and any feat for which it is
a prerequisite; these feats apply only with a kensai's favored weapon. This ability replaces the
magus arcana normally gained at 9th level.

## Superior Reflexes (Ex) {#superior-reflexes}

At 11th level, kensai can make a number of attacks of opportunity in a round equal to his
Intelligence modifier (minimum 1). This effect stacks with the
[Combat Reflexes](ref/feat/combat-reflexes) feat. This ability replaces improved spell recall.

## Iaijutsu Focus (Ex) {#iaijutsu-focus}

At 13th level, a kensai may always act and may draw his weapon as a swift action during a surprise
round, though he is considered flat-footed until he acts. During a surprise round or when attacking
a flat-footed opponent, he adds his Intelligence modifier on damage with his chosen weapon (minimum
0). This ability replaces heavy armor.

## Iaijutsu Master (Ex) {#iaijutsu-master}

At 19th level, a kensai's initiative roll is automatically a natural 20 and he is never surprised.
This ability replaces greater spell access.

## Weapon Mastery (Ex) {#weapon-mastery}

At 20th level, a kensai gains weapon mastery with his favored weapon, as the
[fighter](ref/class/fighter) class ability. This ability replaces true magus.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the kensai archetype: [concentrate](ref/arcana/concentrate),
[critical strike](ref/arcana/critical-strike), [prescient attack](ref/arcana/prescient-attack),
[prescient defense](ref/arcana/prescient-defense), [spell shield](ref/arcana/spell-shield).
