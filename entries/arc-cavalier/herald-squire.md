+++
id = "ref/arc-cavalier/herald-squire"
kind = "archetype"
title = "Herald Squire"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Herald%20Squire"
source_ids = ["knights-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "herald_squire", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "knights-of-the-inner-sea"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "introduction", level = 1 },
  { anchor = "fleet-of-foot", level = 2 },
  { anchor = "transcend-language", level = 3 },
]
trades = [
  { replaces = "Tactician", feature = "tactician", by = ["introduction"] },
  { replaces = "The 2nd-level order ability", feature = "order", levels = [2], by = ["fleet-of-foot"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["transcend-language"] },
]
+++

The herald squire is the eyes and ears of a traveling knight, often arriving ahead of her liege to
bring word of his arrival, find lodgings, and get the lay of the land.

## Introduction (Ex) {#introduction}

At 1st level, whenever a herald squire tries to influence a creature's attitude with the Diplomacy
skill for the first time, she may roll her Diplomacy check twice and take the best result. In
addition, any improvement of a creature's attitude toward the herald squire also applies to her
knight. This ability replaces tactician.

## Fleet of Foot (Ex) {#fleet-of-foot}

At 2nd level, a herald squire gains fast movement, as the [barbarian](ref/class/barbarian) class
feature of the same name. If the herald squire gains fast movement from another class, the bonuses
to her speed do not stack. Whenever she makes long [overland journeys](ref/rule/overland-movement)
alone or with only her mount, the distance a herald squire can travel each day increases by 20%.
This ability replaces the 2nd-level order ability.

## Transcend Language (Sp) {#transcend-language}

At 3rd level, three times per day, a herald squire can cast _[tongues](ref/spell/tongues)_ on
herself, using her herald squire level as her caster level. The effects of this ability last for a
number of rounds equal to her herald squire level. This ability replaces cavalier's charge.
