+++
id = "ref/arc-druid/urban-druid"
kind = "archetype"
title = "Urban Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Urban%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "urban_druid", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "101"

[fields]
kind = "archetype"
features = [
  { anchor = "spontaneous-casting" },
  { anchor = "nature-bond" },
  { anchor = "lorekeeper", level = 2 },
  { anchor = "resist-temptation", level = 4 },
  { anchor = "a-thousand-faces", level = 6 },
  { anchor = "wild-shape", level = 8 },
  { anchor = "mental-strength", level = 9 },
]
trades = [
  { replaces = "Ability to spontaneously cast summon nature's ally spells", feature = "spontaneous-casting", by = ["spontaneous-casting"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["lorekeeper"] },
  { replaces = "trackless step", feature = "trackless-step", by = ["lorekeeper"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-temptation"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["mental-strength"] },
]
+++

While many druids keep to the wilderness, some make their way within settlements, communing with the
animals and vermin who live there and speaking for the nature that runs rampant in civilization's
very cradle.

## Spontaneous Casting {#spontaneous-casting}

An urban druid can channel stored spell energy into domain spells that she has not prepared ahead of
time. She can "lose" a prepared spell in order to cast any domain spell of the same level or lower.
This ability replaces the ability to spontaneously cast summon nature's ally spells.

## Nature Bond (Ex) {#nature-bond}

An urban druid may not select an animal companion. Instead, she must choose from the following
domains, rather than those usually available to druids: [Charm](ref/domain/charm), Community,
Knowledge, Nobility, [Protection](ref/domain/protection), Repose, Rune, or
[Weather](ref/domain/weather).

## Lorekeeper (Ex) {#lorekeeper}

At 2nd level, an urban druid adds [Diplomacy](ref/skill/diplomacy),
[Knowledge (history)](ref/skill/knowledge-history), [Knowledge (local)](ref/skill/knowledge-local),
and [Knowledge (nobility)](ref/skill/knowledge-nobility) skills to her list of class skills. She
also receives a +2 bonus on these skill checks. This ability replaces a druid's woodland stride and
trackless step abilities.

## Resist Temptation (Ex) {#resist-temptation}

At 4th level, an urban druid gains a +2 bonus on saves vs. divinations and enchantments. This
replaces the resist nature's lure ability.

## A Thousand Faces (Su) {#a-thousand-faces}

An urban druid gains this ability at 6th level.

## Wild Shape (Su) {#wild-shape}

An urban druid gains this ability at 8th level, except that her effective druid level for the
ability is equal to her druid level - 4.

## Mental Strength (Ex) {#mental-strength}

At 9th level, an urban druid gains immunity to charm and compulsion effects. This ability replaces
venom immunity.
