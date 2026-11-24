+++
id = "ref/arc-magus/elemental-knight"
kind = "archetype"
title = "Elemental Knight"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Elemental%20Knight"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_knight", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "advanced-race-guide"
page = "203"

[fields]
kind = "archetype"
features = [
  { anchor = "elemental-arcana", level = 3 },
  { anchor = "assault-synergy" },
  { anchor = "energy-reflection" },
  { anchor = "energy-resistance-boost" },
  { anchor = "elemental-matrix", level = 4 },
]
trades = [
  { replaces = "Spell recall", feature = "spell-recall", by = ["elemental-matrix"] },
]
+++

Elemental knights are born with elemental energies surging through their blood and discover the
secret of reconciling and focusing this primal power into the arcane. An elemental knight has the
following class features.

## Elemental Arcana (Su) {#elemental-arcana}

At 3rd level, elemental knights may select the following magus arcana available only to them.

## Assault Synergy (Su) {#assault-synergy}

As a swift action, the elemental knight can expend 1 round of duration from elemental assault to add
+1d6 points of energy damage to an offensive spell he casts that round. The spell must have the
acid, cold, electricity or fire descriptor. This extra energy damage matches the energy damage of
the spell. At 10th level, he may expend 2 rounds instead of 1 to add +2d6 points of energy damage to
the spell.

## Energy Reflection (Su) {#energy-reflection}

This functions like the [reflection](ref/arcana/reflection) magus arcana, except it only works on
spells that deal acid, cold, electricity, or fire damage. As long as the elemental knight spends at
least 1 point from her arcane pool to activate this arcana, he may expend rounds of elemental
assault as if they were arcane pool points. For example, the knight could spend 1 arcane pool point
and 3 rounds of elemental assault to reflect a spell of 4th-level or lower. The elemental knight
must be at least 12th level before selecting this arcana.

## Energy Resistance Boost (Su) {#energy-resistance-boost}

As a swift action, the elemental knight can expend 1 point from his arcane pool or 1 round of
elemental assault to increase all of his racial energy resistances by +5 for 1 round.

## Elemental Matrix (Su) {#elemental-matrix}

At 4th level, an elemental knight gains
[Incremental Elemental Assault](ref/feat/incremental-elemental-assault) (see below) as a bonus feat.
In addition, at 4th level, as a swift action, an elemental knight may expend rounds of duration from
her elemental assault ability. For every 4 rounds expended, he gains 1 arcane pool point. This
ability replaces spell recall.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the elemental knight archetype:
[empowered magic](ref/arcana/empowered-magic), [pool strike](ref/arcana/pool-strike),
[spell shield](ref/arcana/spell-shield).
