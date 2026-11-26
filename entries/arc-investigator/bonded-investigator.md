+++
id = "ref/arc-investigator/bonded-investigator"
kind = "archetype"
title = "Bonded Investigator"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Bonded%20Investigator"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bonded_investigator", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "familiar", level = 2 },
  { anchor = "inspired-familiar", level = 4 },
  { anchor = "studied-strike", level = 6 },
  { anchor = "improved-familiar", level = 7 },
]
trades = [
  { replaces = "Poison lore", feature = "poison-lore", by = ["familiar"] },
  { replaces = "poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["familiar"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [11], by = ["familiar"] },
  { replaces = "Studied strike damage gained at 4th level", feature = "studied-strike", levels = [4], by = ["inspired-familiar"] },
  { replaces = "Investigator talent gained at 7th level", feature = "investigator-talent", levels = [7], by = ["improved-familiar"] },
  { alters = "Studied strike", feature = "studied-strike", by = ["studied-strike"] },
]
+++

Bonded investigators use intelligent familiars to assist them in their investigations. They are
common in the Inner Sea region's bustling cities, where a rat, cat, raven, or another small animal
can go largely unnoticed.

## Familiar (Ex) {#familiar}

At 2nd level, a bonded investigator gains a [familiar](ref/ability/familiars) to aid him. This
[familiar](ref/sidekick/familiar) functions as the [wizard](ref/class/wizard) arcane bond class
feature, using the bonded investigator's class level to determine the familiar's special abilities.
The bonded investigator's extracts are considered spells for the purposes of familiar abilities like
share spell and deliver touch spells.

This ability replaces poison lore, poison resistance, and poison immunity.

## Inspired Familiar (Ex) {#inspired-familiar}

At 4th level, a bonded investigator's familiar becomes a cunning assistant to the investigator. The
familiar can access the investigator's inspiration pool to augment its own actions; the use of
inspiration is deducted from the investigator's number of daily uses as normal. The familiar can use
the inspiration ability (and gains the increased benefits of investigator talents that affect the
bonus dice used in this ability) but cannot expend uses of inspiration for other purposes.

This ability replaces the studied strike damage gained at 4th level.

## Studied Strike (Ex) {#studied-strike}

At 6th level, a bonded investigator gains studied strike +1d6. At 10th level and every 4
investigator levels thereafter, this damage increases by +1d6.

This ability alters studied strike.

## Improved Familiar (Ex) {#improved-familiar}

At 7th level, a bonded investigator gains the [Improved Familiar](ref/feat/improved-familiar) feat
as a bonus feat, treating his investigator level as his arcane caster level for the purposes of
determining what familiars are available to him.

This replaces the investigator talent gained at 7th level.

## Investigator Talents {#investigator-talents}

The following investigator talents complement the bonded investigator archetype:
[effortless aid](ref/invtalent/effortless-aid),
[perceptive tracking](ref/invtalent/perceptive-tracking),
[tenacious inspiration](ref/invtalent/tenacious-inspiration), and
[unconventional inspiration](ref/invtalent/unconventional-inspiration).
