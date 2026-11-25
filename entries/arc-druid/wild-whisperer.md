+++
id = "ref/arc-druid/wild-whisperer"
kind = "archetype"
title = "Wild Whisperer"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Wild%20Whisperer"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_whisperer", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-class-guide"
page = "92"

[fields]
kind = "archetype"
features = [
  { anchor = "inspiration", level = 2 },
  { anchor = "wild-shape", level = 4 },
  { anchor = "natural-expertise", level = 6 },
  { anchor = "investigator-talent", level = 8 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["inspiration"] },
  { replaces = "trackless step", feature = "trackless-step", by = ["inspiration"] },
  { replaces = "resist nature's lure", feature = "resist-nature-s-lure", by = ["inspiration"] },
  { replaces = "The additional use of wild shape at 6th level", feature = "wild-shape", levels = [6], by = ["natural-expertise"] },
  { replaces = "The additional use of wild shape at 8th level", feature = "wild-shape", levels = [8], by = ["investigator-talent"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

A wild whisperer is an expert at studying, predicting, and explaining animal behavior. She is less
interested in plants, fey, and other aspects of the natural world, and uses her gifts to tame or
relocate dangerous beasts and soothe the hurts of wounded and sickly creatures.

## Inspiration (Ex) {#inspiration}

At 2nd level, a wild whisperer gains an inspiration pool as the
[investigator](ref/class/investigator) class ability (see page 31). A wild whisperer uses her druid
level as her investigator level when determining the effects of this ability. Instead of free uses
of inspiration on Knowledge, Linguistics, or Spellcraft skill checks, the wild whisperer can use
inspiration on Handle Animal, Heal, Knowledge (geography), Knowledge (nature), Ride, Sense Motive,
and Survival skill checks without expending a use of inspiration, provided she's trained in the
relevant skill. She can also use inspiration on any wild [empathy](ref/invtalent/empathy) check
without expending a use of inspiration. A wild whisperer's inspiration pool refreshes each day when
she prepares spells. This ability replaces woodland stride, trackless step, and resist nature's
lure.

## Wild Shape (Ex) {#wild-shape}

At 4th level, a wild whisperer gains the wild shape ability, but she never gains access to any forms
beyond Small and Medium animal forms, as [beast shape I](ref/spell/beast-shape-1). This ability
alters wild shape.

## Natural Expertise (Ex) {#natural-expertise}

At 6th level, a wild whisperer's powers of observation give her an advantage when she's fighting
natural creatures. When using inspiration on an attack roll against an animal or a vermin or on a
saving throw against an effect from an animal or a vermin, a wild whisperer has to expend only one
use of inspiration instead of two. This ability replaces the additional use of wild shape at 6th
level.

## Investigator Talent {#investigator-talent}

At 8th level, wild whisperer selects an investigator talent (see page 32). This ability replaces the
additional use of wild shape at 8th level.

## Investigator Talents {#investigator-talents}

The following investigator talents complement the wild whisperer archetype:
[amazing inspiration](ref/invtalent/amazing-inspiration),
[effortless aid](ref/invtalent/effortless-aid),
[eidetic recollection](ref/invtalent/eidetic-recollection), empathy,
[inspirational expertise](ref/invtalent/inspirational-expertise),
[inspired alertness](ref/invtalent/inspired-alertness),
[inspired intimidator](ref/invtalent/inspired-intimidator),
[perceptive tracking](ref/invtalent/perceptive-tracking),
[tenacious inspiration](ref/invtalent/tenacious-inspiration).
