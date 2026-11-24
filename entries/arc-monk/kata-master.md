+++
id = "ref/arc-monk/kata-master"
kind = "archetype"
title = "Kata Master"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Kata%20Master"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kata_master", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-class-guide"
page = "105"

[fields]
kind = "archetype"
features = [
  { anchor = "panache", level = 1 },
  { anchor = "menacing-swordplay", level = 3 },
  { anchor = "ki-pool", level = 4 },
  { anchor = "targeted-strike", level = 7 },
  { anchor = "dizzying-defense", level = 15 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["panache"] },
  { replaces = "Still mind", feature = "still-mind", by = ["menacing-swordplay"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["targeted-strike"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["dizzying-defense"] },
  { alters = "Ki pool", feature = "ki-pool", by = ["ki-pool"] },
]
+++

The kata master takes the visual aspect of his martial art to its logical extreme, harnessing her
flowing movements and skilled maneuvers as a psychological weapon against her enemies. A kata master
forsakes the mental discipline of her more contemplative brethren in favor of these flamboyant
exhibitions. She often performs in staged fights and tournaments, utilizing stylized forms to amaze
the audience and shock and dismay her opponents.

## Panache {#panache}

At 1st level, a kata master gains the [swashbuckler's](ref/class/swashbuckler) panache class
ability. At the start of each day, a kata master gains a number of panache points equal to her
Charisma bonus (minimum 1). Her panache goes up or down throughout the day, but usually cannot go
higher than his Charisma bonus (minimum 1). A kata master gains the swashbuckler's
[derring-do](ref/swashdeed/derring-do) and [dodging panache](ref/swashdeed/dodging-panache) deeds. A
kata master can use an unarmed strike or monk special weapon in place of a light or one-handed
piercing melee weapon for granted swashbuckler class features and deeds. This ability replaces
stunning fist.

## Menacing Swordplay (Ex) {#menacing-swordplay}

At 3rd level, a kata master gains the swashbuckler's
[menacing swordplay](ref/swashdeed/menacing-swordplay) deed. This ability replaces still mind.

## Ki Pool (Su) {#ki-pool}

At 4th level, a kata master can treat ki points as panache points for any swashbuckler deed gained
through this archetype. This ability modifies ki pool.

## Targeted Strike (Ex) {#targeted-strike}

At 7th level, a kata master gains the swashbuckler's targeted strike deed. This ability replaces
wholeness of body.

## Dizzying Defense (Ex) {#dizzying-defense}

At 15th level, a kata master gains the [dizzying defense](ref/swashdeed/dizzying-defense)
swashbuckler deed. This ability replaces quivering palm.
