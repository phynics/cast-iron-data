+++
id = "ref/arc-fighter/relic-master"
kind = "archetype"
title = "Relic Master"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Relic%20Master"
source_ids = ["weapon-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "relic_master", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "weapon-masters-handbook"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "improved-item-mastery", level = 3 },
  { anchor = "relic-channeler", level = 5 },
  { anchor = "improvised-item-mastery", level = 19 },
]
trades = [
  { replaces = "Armor training", feature = "armor-training", by = ["improved-item-mastery"] },
  { replaces = "Weapon training", feature = "weapon-training", by = ["relic-channeler"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["improvised-item-mastery"] },
  { alters = "Class skills" },
]
+++

Commonly trained in the well-funded temples of Osirion or Qadira, the relic master is skilled in
magic item mastery.

## Class Skills {#class-skills}

The relic master receives Knowledge (arcana) and Use Magic Device as class skills, but doesn't
receive Handle Animal or Ride as class skills. This alters the fighter's class skills.

## Improved Item Mastery (Su) {#improved-item-mastery}

At 3rd level, once per day, a relic master can use a item mastery feat she knows with a magic item
that doesn't have an appropriate spell in its construction requirements. The magic item must meet
all other requirements of the item mastery feat. Alternatively, if she is using a magic item with an
appropriate spell in its construction requirements, she can use an item mastery feat without it
counting against the feat's total uses per day. She can use this ability one additional time per day
at 7th, 11th, and 15th levels. This ability replaces armor training.

## Relic Channeler (Su) {#relic-channeler}

At 5th level, a relic master can increase the potency of a magic item she wields by investing it
with a bit of her vitality as a swift action. If the item is armor, a shield, or a weapon, its
enhancement bonus increases by 1 to a maximum of +5. If the magic item creates a spell or has a save
DC, its effective caster level increases by 1. A relic master can use this ability for a number of
minutes per day equal to 1 + her Constitution modifier (minimum 1 minute). This duration doesn't
need to be consecutive, but it must be used in 1-minute increments. This ability replaces weapon
training.

## Improvised Item Mastery (Su) {#improvised-item-mastery}

At 19th level as a full-round action, the relic master can select one item mastery feat whose
prerequisites she meets but that she doesn't already have. She gains access to this feat, though she
can't use it as a prerequisite for other feats or options. If she selects a different item mastery
feat, she loses access to her previous use of improvised item mastery and any magic effect created
with it ends immediately. Any daily uses of a selected improvised item mastery feat count against
all improvised mastery feats selected in the same day. This ability replaces armor mastery.
