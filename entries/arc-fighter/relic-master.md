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
replaces = ["Armor training", "Weapon training", "Armor mastery"]
replaces_features = ["armor-training", "weapon-training", "armor-mastery"]
+++

Commonly trained in the well-funded temples of Osirion or Qadira, the relic master is skilled in
magic item mastery.

**Gained class skills:** ka, umd

**Lost class skills:** ha, ride

**Improved Item Mastery (Su)**

**Ability:** A relic master can use an item mastery feat she knows with a magic item that doesn't
have an appropriate spell in its construction requirements. The magic item must meet all other
requirements of the item mastery feat. Alternatively, if she is using a magic item with an
appropriate spell in its construction requirements, she can use an item mastery feat without it
counting against the feat's total uses per day.

**Gained:** At 3rd Level

**Replaces:** Armor training

**Usage:** 1 time/day + 1 per 4 fighter levels beyond 3rd

**Relic Channeler (Su)**

**Gained:** At 5th Level

**Replaces:** Weapon training

**Swift:** A relic master can increase the potency of a magic item she wields by investing it with a
bit of her vitality. If the item is armor, a shield, or a weapon, its enhancement bonus increases by
1 to a maximum of +5. If the magic item creates a spell or has a save DC, its effective caster level
increases by 1.

**Usage:** Con1 modifier minutes/day; these minutes need not be consecutive, but must be spent in
1-minute increments (minimum 1)

**Improvised Item Mastery (Su)**

**Fullround:** The relic master can select one item mastery feat whose prerequisites she meets but
that she doesn't already have. She gains access to this feat, though she can't use it as a
prerequisite for other feats or options. If she selects a different item mastery feat, she loses
access to her previous use of _improvised item mastery_ and any magic effect created with it ends
immediately. Any daily uses of a selected _improvised item mastery_ feat count against all
_improvised mastery feats_ selected in the same day.

**Gained:** At 19th Level

**Replaces:** Armor mastery
