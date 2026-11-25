+++
id = "ref/arc-witch/mountain-witch"
kind = "archetype"
title = "Mountain Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Mountain%20Witch"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mountain_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "advanced-class-guide"
page = "132"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "stone-spirit-hex" },
  { anchor = "mountain-beast-empathy", level = 2 },
]
trades = [
  { replaces = "Hex gained at 2nd level", feature = "hex", levels = [2], by = ["mountain-beast-empathy"] },
  { alters = "Hex", feature = "hex", by = ["stone-spirit-hex"] },
]
+++

Mountains can be sanctuaries for witches hunted by society. Here they form bonds with the spirits of
the lofty reaches.

## Spells {#spells}

A mountain witch replaces some of her patron spells with the following: 2nd—_magic stone_,
4th—_stone call_, 6th—_meld into stone_, 8th—_stoneskin_, 10th—_wall of stone_, 12th—_stone tell_,
14th—_statue_, 16th—_repel metal or stone_, 18th—_clashing rocks_.

## Stone Spirit Hex {#stone-spirit-hex}

A mountain witch can select hexes from the shaman's [stone spirit](ref/shamanspirit/stone) (see page
44) as if they were witch hexes. She uses her witch level as her shaman level to determine the
effect of the hex, and Intelligence instead of Wisdom to determine its DC. This ability alters hex.

## Mountain Beast Empathy (Ex) {#mountain-beast-empathy}

At 2nd level, a mountain witch can influence the attitude of mountain-dwelling animals, as the
druid's [wild empathy](ref/ability/wild-empathy) class feature but only on animals native to
mountainous environments. The mountain witch uses her witch level as her druid level for this
ability. This ability replaces the hex gained at 2nd level.

## Hexes {#hexes}

The following witch hexes complement the mountain witch archetype: beast of ill-omen, crystal sight,
lodestone, metal curse, stone stability, and ward of stone. (Those with asterisks \[\*\] are
detailed in the shaman class.)

## Major Hexes {#major-hexes}

The following major hexes complement the mountain witch archetype: beast eye, hidden home,
hoarfrost, and weather control.

## Grand Hexes {#grand-hexes}

The following grand hexes complement the mountain witch archetype: eternal slumber, natural
disaster, and witch's hut.
