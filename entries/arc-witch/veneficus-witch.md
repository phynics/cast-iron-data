+++
id = "ref/arc-witch/veneficus-witch"
kind = "archetype"
title = "Veneficus Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Veneficus%20Witch"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "veneficus_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "people-of-the-river"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "poisoner" },
  { anchor = "poison-use", level = 2 },
  { anchor = "toxic-words", level = 2 },
]
trades = [
  { replaces = "2nd- and 10th-level hexes", feature = "hex", levels = [2, 10], by = ["toxic-words"] },
]
+++

Veneficus witches specialize in poisons—brewing both magical and traditional concoctions, and
applying them to weapons, traps or even her potent hexes. Whether they're members of Daggermark's
Poisoners' Guild or followers of Gyronna, veneficus witches are commonly found in the River
Kingdoms.

## Poisoner {#poisoner}

A veneficus witch can select the following alchemist discoveries as hexes, major hexes, or grand
hexes, as indicated below. The witch's effective alchemist level is equal to her witch level for the
purpose of qualifying for these discoveries. Unless otherwise noted, these alchemist discoveries can
be located in the _Pathfinder RPG Advanced Player's Guide_.

### Hexes {#hexes}

[Concentrate poison](ref/discovery/concentrate-poison),
[poison conversion](ref/discovery/poison-conversion), [sticky poison](ref/discovery/sticky-poison).

### Major Hexes {#major-hexes}

[Malignant poison](ref/discovery/malignant-poison),
[nauseating flesh](ref/discovery/nauseating-flesh).

### Grand Hexes {#grand-hexes}

[Poison touch](ref/discovery/poison-touch) (grand discovery).

## Poison Use (Ex) {#poison-use}

At 2nd level, a veneficus witch cannot accidentally poison herself when applying poison to a weapon.

## Toxic Words (Ex) {#toxic-words}

At 2nd level, whenever a veneficus witch targets a single creature with a hex, she can imbue her hex
with a dose of injury or contact poison she is holding. The DCs of her hex and the poison are each
reduced by 2; if the creature fails its save against the hex, the poison is expended and the
creature must succeed at a Fortitude save against the poison or become poisoned. At 10th level, the
DC of the witch's hex and poison are each reduced by only 1 and the witch can imbue her hexes with
inhaled and ingested poisons as well. This ability replaces the witch's 2nd- and 10th-level hexes.

## Hexes {#toxic-words-hexes}

The following witch hexes complement the veneficus witch archetype: blight, cauldron, disguise,
poison steep.

## Major Hexes {#toxic-words-major-hexes}

The following major hexes complement the veneficus witch archetype: cook people, witch's brew.

## Grand Hex {#grand-hex}

The following grand hex complements the veneficus witch archetype: eternal slumber.
