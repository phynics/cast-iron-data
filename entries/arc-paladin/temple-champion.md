+++
id = "ref/arc-paladin/temple-champion"
kind = "archetype"
title = "Temple Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Temple%20Champion"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "temple_champion", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-class-guide"
page = "107"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "domain-granted-power", level = 4 },
  { anchor = "blessing", level = 5 },
]
trades = [
  { replaces = "Divine bond", feature = "divine-bond", by = ["blessing"] },
  { replaces = "aura of justice", feature = "aura-of-justice", by = ["blessing"] },
]
+++

A temple champion is a powerful warrior dedicated to a good or lawful deity. She thinks of herself
primarily as a servant of her deity and secondarily as an agent of her deity's church. She has a
refined understanding of a specific aspect of that faith and gives up standard paladin spellcasting
in favor of a warpriest's domain-based blessings and granted powers.

## Spells {#spells}

A temple champion does not gain access to paladin spells, and does not have a paladin caster level
or spell list. This is not considered a spellcasting class.

## Domain Granted Power {#domain-granted-power}

At 4th level, a temple champion selects one [domain](ref/ability/domains) granted by her deity (or a
domain suitable for her ethos or goals, subject to GM approval). The temple champion gains the
1st-level granted power of that domain and uses her paladin level as her cleric level for
determining the effects of that granted power. Any Wisdom-based aspects of that granted power
instead use the temple champion's Charisma. The temple champion does not gain access to that
domain's spell list.

## Blessing (Su) {#blessing}

At 5th level, a temple champion gains the minor [blessing](ref/ability/blessings) (as the
[warpriest](ref/class/warpriest) class feature) of the domain she selected at 4th level. She uses
her paladin level as her warpriest level for determining the effects of that blessing. Any
Wisdom-based aspects of that blessing instead use the temple champion's Charisma. At 11th level, she
gains the major blessing of her chosen domain. This ability replaces divine bond and aura of
justice.
