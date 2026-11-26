+++
id = "ref/arc-swashbuckler/veiled-blade"
kind = "archetype"
title = "Veiled Blade"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Veiled%20Blade"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "veiled_blade", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "53"

[fields]
kind = "archetype"
features = [
  { anchor = "deeds" },
  { anchor = "quick-draw", level = 1 },
  { anchor = "hidden-blade", level = 3 },
  { anchor = "instant-unveil", level = 7 },
  { anchor = "soul-veil", level = 15 },
]
trades = [
  { replaces = "Opportune parry and riposte deed", feature = "deeds", power = "opportune parry and riposte", by = ["quick-draw"] },
  { replaces = "Menacing swordplay deed", feature = "deeds", power = "menacing swordplay", by = ["hidden-blade"] },
  { replaces = "Swashbuckler's grace deed", feature = "deeds", power = "swashbuckler's grace", by = ["instant-unveil"] },
  { replaces = "Swashbuckler's edge deed", feature = "deeds", power = "swashbuckler's edge", by = ["soul-veil"] },
  { alters = "Class skills" },
]
+++

Veiled blades specialize in subtlety, not through clandestine sneaking but simply by appearing to be
someone harmless and unarmed. When a fight breaks out, a veiled blade doffs that facade and pulls
out her hidden trump cards. Those who have mastered the art of the veiled blade can even hide their
weapons on their own bodies as brands.

## Class Skills {#class-skills}

A veiled blade adds Disguise to her list of class skills, instead of Intimidate.

This alters the swashbuckler's class skills.

## Deeds {#deeds}

A veiled blade gains the following deeds.

## Quick Draw (Ex) {#quick-draw}

At 1st level, whenever she has at least 1 panache point, a veiled blade gains the benefits of the
[Quick Draw](ref/feat/quick-draw) feat.

This deed replaces the swashbuckler's opportune parry and riposte deed.

## Hidden Blade (Ex) {#hidden-blade}

At 3rd level, whenever she has at least 1 panache point, a veiled blade can hide any light or
one-handed piercing melee weapon using Sleight of Hand, and she receives a +4 insight bonus on her
check to hide the weapon.

This deed replaces the menacing swordplay deed.

## Instant Unveil (Ex) {#instant-unveil}

At 7th level, when she uses her swashbuckler's initiative deed to draw a light or one-handed
piercing weapon as part of an initiative check, she can draw that weapon even if it is hidden.

This deed replaces the swashbuckler's grace deed.

## Soul Veil (Sp) {#soul-veil}

At 15th level, a veiled blade can merge a light or one-handed piercing melee weapon with herself, as
if using the spell _[ghost brand](ref/spell/ghost-brand)_ (see page 215), except that it takes only
a swift action to manifest or store the weapon. This ability lasts until it is dispelled or until
the veiled blade merges with a different light or one-handed piercing melee weapon.

This deed replaces the swashbuckler's edge deed.
