+++
id = "ref/arc-bloodrager/greenrager"
kind = "archetype"
title = "Greenrager"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Greenrager"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "greenrager", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "advanced-class-guide"
page = "83"

[fields]
kind = "archetype"
features = [
  { anchor = "unfettered-fury", level = 3 },
  { anchor = "summoning-rager", level = 6 },
  { anchor = "furious-summoning", level = 9 },
]
trades = [
  { replaces = "Blood sanctuary", feature = "blood-sanctuary", by = ["unfettered-fury"] },
  { replaces = "The bloodline feat gained at 6th level", feature = "bloodline", levels = [6], power = "bloodline feat", by = ["summoning-rager"] },
  { replaces = "The bloodline feat at 9th level", feature = "bloodline", levels = [9], power = "bloodline feat", by = ["furious-summoning"] },
]
+++

Typically, nature finds its greatest harmony with divine magic, but sometimes a connection with the
natural world manifest itself through the arcane current in the veins of the bloodragers called
greenragers. These bloodragers funnel their eldritch heritage into abilities that allow them to call
powerful allies from nature and empower them with their bloodrage.

## Unfettered Fury (Ex) {#unfettered-fury}

At 3rd level, a greenrager's fury allows him to move through undergrowth with frightening speed and
grace. This functions as the druid's [woodland stride](ref/ability/woodland-stride) class feature,
but only while the greenrager is bloodraging. This ability replaces blood sanctuary.

## Summoning Rager (Sp) {#summoning-rager}

At 6th level, a greenrager's magic unlocks the secrets of summoning allies from nature. He adds
_[summon nature's ally I](ref/spell/summon-natures-ally-1)_ to his list of 1st-level bloodrager
spells known as a bonus spell, as if it were a bonus bloodrager spell. At 7th level, he adds
_[summon nature's ally II](ref/spell/summon-natures-ally-2)_ as a bonus 2nd-level bloodrager spell,
at 10th level he adds _[summon nature's ally III](ref/spell/summon-natures-ally-3)_ as a bonus 3rd
level bloodrager spell, and at 13th level he adds
_[summon nature's ally IV](ref/spell/summon-natures-ally-4)_ as a bonus 4th-level bloodrager spell.
This ability replaces the bloodline feat gained at 6th level.

## Furious Summoning (Su) {#furious-summoning}

At 9th level, creatures summoned by the bloodrager's
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell gain a +4 morale bonus to Strength and
Constitution and gain the druid's woodland stride ability. At 11th level, this bonus increases to
+6. At 20th level, it increases to +8. This ability replaces the bloodline feat at 9th level.
