+++
id = "ref/arc-magus/myrmidarch"
kind = "archetype"
title = "Myrmidarch"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Myrmidarch"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "myrmidarch", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-combat"
page = "56"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting", level = 1 },
  { anchor = "ranged-spellstrike", level = 4 },
  { anchor = "weapon-training", level = 6 },
  { anchor = "fighter-training", level = 7 },
  { anchor = "armor-training", level = 8 },
  { anchor = "armor-mastery", level = 20 },
]
trades = [
  { replaces = "Spell recall", feature = "spell-recall", by = ["ranged-spellstrike"] },
  { replaces = "improved spell recall", feature = "improved-spell-recall", by = ["ranged-spellstrike"] },
  { replaces = "Magus arcana gained at 6th, 12th, and 18th levels", feature = "magus-arcana", levels = [6, 12, 18], by = ["weapon-training"] },
  { replaces = "Knowledge pool", feature = "knowledge-pool", by = ["fighter-training"] },
  { replaces = "Fighter training the magus gains at 10th level", feature = "fighter-training", levels = [10], by = ["fighter-training"] },
  { replaces = "Improved spell combat", feature = "improved-spell-combat", by = ["armor-training"] },
  { replaces = "greater spell combat", feature = "greater-spell-combat", by = ["armor-training"] },
  { replaces = "True magus", feature = "true-magus", by = ["armor-mastery"] },
]
+++

The myrmidarch is a skilled specialist, using magic to supplement and augment his martial mastery.

## Diminished Spellcasting {#diminished-spellcasting}

Myrmidarchs cast one fewer spell of each level than normal. If this reduces the number to 0, he may
cast spells of that level only if his Intelligence allows [bonus spells](ref/rule/determine-bonuses)
of that level.

## Ranged Spellstrike (Su) {#ranged-spellstrike}

At 4th level, a myrmidarch can use spellstrike to cast a single-target touch attack ranged spell and
deliver it through a ranged weapon attack. Even if the spell can normally affect multiple targets,
only a single missile, ray, or effect accompanies the attack.

At 11th level, a myrmidarch can spend a full-round action to cast a spell that includes multiple
ranged touch attacks and deliver more than one using ranged attacks. The spell must have a casting
time of 1 full-round action or less. This functions similarly to the base ability of ranged
spellstrike, but the myrmidarch can deliver a number of missiles, rays, or effect up to the number
of attacks he could make with a full attack. Attacks beyond the first take penalties as if the
myrmidarch were making a full attack. Any effects not used in the round the spell is cast are lost,
as are any additional ranged touch attacks the spell would allow beyond the myrmidarch's maximum
number of attacks. This ability replaces spell recall and improved spell recall.

## Weapon Training (Ex) {#weapon-training}

At 6th level, a myrmidarch gains weapon training, as the [fighter](ref/class/fighter) ability,
adding an additional [weapon group](ref/ability/weapon-groups) every six levels after 6th (to a
maximum of three groups at 18th level) and increasing the bonus on attack and damage rolls for
weapon groups already chosen by +1. This ability replaces the magus arcana normally gained at 6th,
12th, and 18th levels.

## Fighter Training (Ex) {#fighter-training}

At 7th level, a myrmidarch counts his magus level -3 as his fighter level for the purpose of
qualifying for feats (if he has levels in fighter, these levels stack). At 10th level, the
myrmidarch treats his magus levels as fighter levels for the purposes of fighter training. This
ability replaces knowledge pool and the fighter training the magus gains at 10th level.

## Armor Training (Ex) {#armor-training}

At 8th level, a myrmidarch gains armor training, as the fighter ability. At 14th level, he gains
armor training 2. This ability replaces improved spell combat and greater spell combat.

## Armor Mastery (Ex) {#armor-mastery}

At 20th level, a myrmidarch gains DR 5/– when wearing armor. This ability replaces true magus.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the myrmidarch archetype:
[accurate strike](ref/arcana/accurate-strike), [arcane edge](ref/arcana/arcane-edge),
[lingering pain](ref/arcana/lingering-pain), [prescient attack](ref/arcana/prescient-attack),
[prescient defense](ref/arcana/prescient-defense), [spell shield](ref/arcana/spell-shield),
[spellbreaker](ref/arcana/spellbreaker).
