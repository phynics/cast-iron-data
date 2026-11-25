+++
id = "ref/arc-sorcerer/eldritch-scrapper"
kind = "archetype"
title = "Eldritch Scrapper"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Eldritch%20Scrapper"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "eldritch_scrapper", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "advanced-class-guide"
page = "122"

[fields]
kind = "archetype"
features = [
  { anchor = "martial-flexibility", level = 1 },
  { anchor = "bloodline-weapons" },
]
trades = [
  { replaces = "Sorcerer's bloodline powers gained 1st, 9th, and 15th levels", feature = "bloodline", levels = [1, 9, 15], power = "bloodline power", by = ["martial-flexibility"] },
]
+++

An eldritch scrapper is usually spoiling for a fight, looking to prove that she's just as tough as a
martial character. A veteran of many brawls against opponents who were suspicious of her manifesting
magic, an eldritch scrapper has a thick skin and a fighting style that blends weapons with spells.

## Martial Flexibility (Ex) {#martial-flexibility}

At 1st level, an eldritch scrapper gains the [brawler's](ref/class/brawler) martial flexibility
class feature, using her sorcerer level as her brawler level for the purposes of uses per day. The
scrapper treats [Arcane Strike](ref/feat/arcane-strike) and
[Combat Casting](ref/feat/combat-casting) as combat feats for the purpose of this ability.

At 9th level, an eldritch scrapper can use this ability to gain the benefit of two combat feats at
the same time. She can select one feat as a move action or two feats as a standard action. She can
use one of these feats to meet a prerequisite of the second feat; doing so means she cannot replace
the feat that is currently fulfilling another feat's prerequisites without also replacing all feats
that require it. Each individual feat selected counts toward her daily uses of this ability.

At 15th level, an eldritch scrapper can use this ability to gain the benefit of three combat feats
at the same time. She can select one feat as a swift action, two feats as a move action, or three
feats as a standard action. She can use one of the feats to meet a prerequisite of the second and
third feats, and use the second feat to meet a prerequisite of the third feat. Each individual feat
selected counts toward her daily uses of this ability.

This ability replaces the sorcerer's bloodline powers gained 1st, 9th, and 15th levels.

## Bloodline Weapons {#bloodline-weapons}

If an eldritch scrapper's 1st-level bloodline power would normally grant her natural attacks (such
as bite or claws), at 3rd level she can select that 1st-level bloodline power in place of her
3rd-level bloodline power.
