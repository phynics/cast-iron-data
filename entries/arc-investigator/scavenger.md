+++
id = "ref/arc-investigator/scavenger"
kind = "archetype"
title = "Scavenger"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Scavenger"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scavenger", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "gadgetry", level = 1 },
  { anchor = "mechanical-inspiration", level = 1 },
  { anchor = "jury-rig", level = 2 },
  { anchor = "construct-mastery", level = 2 },
]
trades = [
  { replaces = "Poison lore", feature = "poison-lore", by = ["jury-rig"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["construct-mastery"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [11], by = ["construct-mastery"] },
  { alters = "Alchemy", feature = "alchemy", by = ["gadgetry"] },
  { alters = "Inspiration", feature = "inspiration", by = ["mechanical-inspiration"] },
]
+++

Scavengers are masters of systems: how they fit together, why they work, and how to make the most of
their parts. However, scavengers generally lack other investigative talents such as social skills or
an understanding of history and lore. The ratfolk of Numeria excel at this art, but nearly every
warren across Golarion boasts at least a few resourceful scavengers.

## Gadgetry (Su) {#gadgetry}

A scavenger is a master of mechanical arts rather than alchemical ones, and he gains a competence
bonus on Craft (clockwork) checks equal to his class level. He can use Knowledge (engineering) to
identify wondrous items as if using _[detect magic](ref/spell/detect-magic)_ and Spellcraft. A
scavenger does not gain any bonuses to or special uses of the Craft (alchemy) skill.

Rather than prepare his extracts as consumable liquids, a scavenger constructs small, single-use
devices infused with bits of his own magic aura to achieve the same effects. Alchemist and
investigator discoveries that affect extracts result in identical effects on a scavenger's gadgets
(such as the [infusion](ref/discovery/infusion) discovery, which would allow another creature to use
a gadget, just as it would allow that creature to use an extract).

This ability modifies alchemy.

## Mechanical Inspiration (Ex) {#mechanical-inspiration}

At 1st level, a scavenger can use inspiration to apply a bonus to Appraise, Disable Device, and
Knowledge (engineering) checks without expending a use of inspiration, but he must spend a use of
inspiration to apply a bonus on Knowledge, Linguistics, and Spellcraft checks.

This ability modifies inspiration.

## Jury-Rig (Ex) {#jury-rig}

Beginning at 2nd level, a scavenger can sacrifice one of his gadgets to repair or enhance an
adjacent mechanical device, such as a lock, trap, or vehicle. Doing so either repairs 1d6 points of
damage per extract level of the gadget sacrificed or applies a bonus or penalty to one specific
skill check involved in using the device. The scavenger could, for example, sacrifice a gadget to
impose a penalty on all Disable Device checks to disarm a trap, add a bonus on all Disable Device
checks to open a lock, or add a bonus on all Profession (driver) checks to drive a carriage. This
modifier is equal to twice the extract level of the gadget sacrificed, and lasts for 10 minutes per
class level.

This ability replaces poison lore.

## Construct Mastery (Ex) {#construct-mastery}

At 2nd level, a scavenger gains a +2 bonus on all Craft checks to modify or repair creatures of the
construct type, as well as a +2 bonus on all weapon damage rolls against constructs. This bonus
increases to +4 at 5th level, and to +6 at 8th level. At 11th level, the scavenger gains
[Craft Construct](ref/feat/craft-construct) as a bonus feat, even if he does not meet the
prerequisites.

This ability replaces the investigator's poison resistance and poison immunity.
