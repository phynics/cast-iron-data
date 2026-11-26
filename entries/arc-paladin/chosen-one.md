+++
id = "ref/arc-paladin/chosen-one"
kind = "archetype"
title = "Chosen One"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Chosen%20One"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chosen_one", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "familiar-folio"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "bondless" },
  { anchor = "divine-emissary", level = 1 },
  { anchor = "religious-mentor" },
  { anchor = "delayed-grace", level = 1 },
  { anchor = "lay-on-paws", level = 2 },
  { anchor = "true-form", level = 7 },
  { anchor = "emissary-s-smite", level = 11 },
]
trades = [
  { alters = "Divine grace", feature = "divine-grace", by = ["delayed-grace"] },
  { alters = "smite evil", feature = "smite-evil", by = ["delayed-grace"] },
  { alters = "Lay on hands", feature = "lay-on-hands", by = ["lay-on-paws"] },
  { alters = "channel positive energy", feature = "channel-positive-energy", by = ["lay-on-paws"] },
]
+++

Most paladins train for years at a temple to attain a holy status, but rarely, an emissary of the
divine appears to one of humble origins and calls her directly to the charge. These chosen ones may
lack experience, but their teamwork with their emissaries allows them to defeat any evil.

## Bondless {#bondless}

A chosen one does not gain the divine bond class feature.

## Divine Emissary (Ex) {#divine-emissary}

At 1st level, a chosen one gains an [emissary](ref/arc-familiar/emissary)
[familiar](ref/ability/familiars) (see page 10), treating her paladin level as her
[wizard](ref/class/wizard) level for the purpose of this ability.

## Religious Mentor (Ex) {#religious-mentor}

The [familiar's](ref/sidekick/familiar) sworn duty is to help train the chosen one for her future
glory. The familiar is treated as having a number of ranks in Knowledge (religion) equal to the
chosen one's paladin level. The chosen one doesn't gain Knowledge (religion) as a class skill.

## Delayed Grace (Su) {#delayed-grace}

A chosen one begins her adventuring career without fully understanding her true potential. The
chosen one uses the Barbarian, Rogue, Sorcerer column on Table 7–1 on page 169 of the _Pathfinder
RPG Core Rulebook_ to calculate her typical starting [age](ref/rule/age). She receives the smite
evil ability at 2nd level and the divine grace ability at 4th level. This does not affect the rate
at which she gains additional uses per day of smite evil, so she still gains her second use at 4th
level, her third at 7th level, and so on. This ability alters divine grace and smite evil.

## Lay on Paws (Su) {#lay-on-paws}

At 2nd level, a chosen one's familiar is able to borrow some of her divine energy to heal itself and
others. The familiar can use the chosen one's lay on hands ability, including all of her mercies,
but each such use consumes two uses of the paladin's lay on hands ability. Starting at 4th level,
the familiar can also channel positive energy, but each such use consumes four uses of the paladin's
lay on hands ability. This ability alters lay on hands and channel positive energy.

## True Form (Ex) {#true-form}

At 7th level, a chosen one's familiar reveals its true form, transforming into an outsider
[improved familiar](ref/ability/improved-familiars) that matches the chosen one's patron's alignment
(typically an [arbiter](ref/monster/inevitable-arbiter), a [cassisian](ref/monster/angel-cassisian),
a [harbinger](ref/monster/archon-harbinger-archon), or a
[silvanshee](ref/monster/agathion-silvanshee), but potentially any lawful neutral, lawful good, or
neutral good outsider familiar depending on the patron). The familiar gains the
[change shape](ref/umr/change-shape) universal monster ability if it doesn't already have it, which
it can use at will to transform into its original form or back to its true form.

## Emissary's Smite (Su) {#emissary-s-smite}

At 11th level, a chosen one's familiar also benefits from the paladin's smite evil ability whenever
the chosen one uses smite evil.
