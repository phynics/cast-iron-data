+++
id = "ref/arc-ranger/nirmathi-irregular"
kind = "archetype"
title = "Nirmathi Irregular"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Nirmathi%20Irregular"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nirmathi_irregular", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "inner-sea-magic"
page = "37"

[fields]
kind = "archetype"
features = [
  { anchor = "focused-enemy", level = 1 },
  { anchor = "forest-ghost", level = 1 },
  { anchor = "focused-terrain", level = 3 },
  { anchor = "spells", level = 4 },
]
trades = [
  { replaces = "Armor and weapon proficiency", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["forest-ghost"] },
  { replaces = "Favored enemy", feature = "favored-enemy", by = ["focused-enemy"] },
  { replaces = "Favored terrain", feature = "favored-terrain", by = ["focused-terrain"] },
]
+++

The forested country of Nirmathas is known for its rangers—skilled trackers, marksmen, and silent
stalkers under the leafy canopy. Nirmathas has no formal military, for her people love their freedom
and are reluctant to take orders from anyone, so her defense falls to individual scouts and small
groups of allied commandos. Many of Nirmathas's rangers take the [guide](ref/arc-ranger/guide) or
[skirmisher](ref/arc-ranger/skirmisher) archetypes (see the _Advanced Player's Guide_), but some
focus on the magic of stealth. These irregular troops fight against the frequent invasions by
Molthuni soldiers, striking quickly and melting into the green shadows as soon as their opponents
rally themselves for a counterattack. A Nirmathi irregular has the following class features.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A Nirmathi irregular is proficient with all simple and martial weapons and with light armor. This
replaces the normal ranger armor and weapon proficiency.

## Focused Enemy (Ex) {#focused-enemy}

At 1st level, a Nirmathi irregular selects one favored enemy (usually "humanoid \[human\]"). He does
not gain additional favored enemies at higher levels. He does get to increase his favored enemy
bonus by +2 at 5th, 10th, 15th, and 20th level. This otherwise acts as and replaces the standard
favored enemy ability.

## Forest Ghost (Ex) {#forest-ghost}

At 1st level, a Nirmathi irregular adds a bonus equal to 1/2 his level on all Perception and
Survival skill checks he makes while located in forest terrain. This ability replaces wild empathy.

## Focused Terrain {#focused-terrain}

At 3rd level, a Nirmathi irregular selects one favored terrain (usually "forest"). He does not gain
additional favored terrains at higher levels. He does get to increase his favored terrain bonus by
+2 at 8th, 13th, and 18th level. This otherwise acts as and replaces the standard favored terrain
ability.

## Spells {#spells}

At 4th level, a Nirmathi irregular increases his number of spells per day by +1 for every spell
level. This means the irregular gets at least 1 spell per day as soon as he gains access to a level
of spells, even if Table 3–12: Ranger in the _Core Rulebook_ lists 0 for spells per day.

A Nirmathi irregular also learns to draw upon druidic magic, perhaps from association with the
druids of Crystalhurst or a natural connection to the magic of the Fangwood. Each day when the
ranger prepares spells, he may choose one druid spell and prepare it as if it were on the ranger
spell list as a ranger spell of its druid spell level.
