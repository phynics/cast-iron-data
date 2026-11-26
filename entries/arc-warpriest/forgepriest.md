+++
id = "ref/arc-warpriest/forgepriest"
kind = "archetype"
title = "Forgepriest"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Forgepriest"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forgepriest", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "advanced-class-guide"
page = "130"

[fields]
kind = "archetype"
features = [
  { anchor = "blessings", level = 1 },
  { anchor = "smith-s-spells" },
  { anchor = "forge-mastery", level = 2 },
  { anchor = "craft-magic-arms-and-armor", level = 3 },
  { anchor = "creator-s-bond", level = 4 },
  { anchor = "heat-of-the-forge", level = 6 },
]
trades = [
  { replaces = "2nd blessing normally gained by a warpriest", feature = "blessings", by = ["forge-mastery"] },
  { replaces = "Bonus feat gained at 3rd level", feature = "bonus-feats", levels = [3], by = ["craft-magic-arms-and-armor"] },
  { replaces = "Channel energy", feature = "channel-energy", by = ["creator-s-bond"] },
  { replaces = "Bonus feat gained at 6th level", feature = "bonus-feats", levels = [6], by = ["heat-of-the-forge"] },
  { alters = "Blessings", feature = "blessings", by = ["blessings"] },
  { alters = "Bonus feats", feature = "bonus-feats" },
]
+++

Armorers of exquisite skill, forgepriests take inspiration from their deity to produce the most
perfect weapons and armor they can, the better to equip the armies of the faithful.

## Blessings {#blessings}

A forgepriest selects only one blessing. This alters the blessings class feature.

## Smith's Spells {#smith-s-spells}

A forgepriest adds the following spells to his spell list: 1st—_jury rig_, _shield_; 2nd—_heat
metal_, _shatter_; 3rd—_keen edge_, _quench_, _versatile weapon_; 4th—_wreath of blades_;
5th—_fabricate_, _major creation_; 6th—_mage's sword_.

## Forge Mastery (Ex) {#forge-mastery}

At 2nd level, the forgepriest adds a bonus equal to half his level to all Craft checks to make metal
items, armor, and weapons. (This benefit is gained from the altered version of blessings, above.)

## Bonus Feats {#bonus-feats}

A forgepriest can select item creation feats in addition to combat feats when he gains a bonus feat.
This ability alters bonus feats.

## Craft Magic Arms and Armor {#craft-magic-arms-and-armor}

At 3rd level, a forgepriest gains [Craft Magic Arms and Armor](ref/feat/craft-magic-arms-and-armor)
as a bonus feat. This ability replaces the bonus feat gained at 3rd level.

## Creator's Bond (Su) {#creator-s-bond}

At 4th level, when a forgepriest uses his sacred weapon ability with an item he created personally,
he can expend two uses of his fervor ability to increase the bonus granted by 1. Once the
forgepriest has the sacred armor ability, he can also use this ability in conjunction with that.
This ability replaces channel energy.

## Heat of the Forge (Su) {#heat-of-the-forge}

At 6th level, a forgepriest gains fire resistance 5. At 13th level, this resistance increases to 10.
This ability replaces the bonus feat gained at 6th level.
