+++
id = "ref/arc-magus/spire-defender"
kind = "archetype"
title = "Spire Defender"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Spire%20Defender"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spire_defender", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "inner-sea-magic"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-augmentation", level = 4 },
]
trades = [
  { replaces = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Armor proficiencies", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { replaces = "Spell recall", feature = "spell-recall", by = ["arcane-augmentation"] },
]
+++

Spire defenders are magi who train themselves to accompany sages and archaeologists who venture from
the Mordant Spire, acting as aids and bodyguards. Because they often operate in
[difficult terrain](ref/rule/terrain-and-obstacles)—narrow trenches in dig sites, flooded dungeons,
and tight corridors in ancient ruins—spire defenders place mobility and agility at a premium. As a
result, they eschew armor entirely. Most spire defenders are elves—it's exceptionally rare for a
non-[elf](ref/race/elf) to be granted access to the training required to take this archetype
(non-elves need GM approval to take this archetype). A spire defender has the following class
features.

## Weapon Proficiency {#weapon-proficiency}

A spire defender is proficient with all light and one-handed simple and martial weapons, as well as
one exotic light or one-handed melee weapon that has the [disarm](ref/misc/disarm) or
[trip](ref/misc/trip) special feature. This replaces the magus's normal weapon proficiencies.

## Bonus Feats (Ex) {#bonus-feats}

At 1st level, the spire defender gains [Combat Expertise](ref/feat/combat-expertise) and
[Dodge](ref/feat/dodge) as bonus feats, even if he doesn't meet the prerequisites. The spire
defender is not proficient in any kind of armor or shield. The spire defender does not have the
magus' ability to ignore arcane spell failure from armor; however, if the spire defender becomes
proficient in light armor, he automatically gains the magus's ability to ignore the arcane spell
failure chance of light armor. If he becomes proficient in medium armor, at 7th level he ignores
medium armor's chance of arcane spell failure. If he becomes proficient in heavy armor, at 13th
level he ignores heavy armor's chance of arcane spell failure. This replaces the magus's normal
armor proficiencies.

## Arcane Augmentation (Su) {#arcane-augmentation}

At 4th level, a magus can expend 1 point from his arcane pool as a swift action to grant himself a
+5 competence bonus for 1 minute to one of the following skills: Acrobatics, Climb, Escape Artist,
Perception, Stealth, and Swim. For every three levels beyond 4th, the magus gains another +1
enhancement bonus, to a maximum of +10 at 19th level. This ability replaces the spell recall
ability.
