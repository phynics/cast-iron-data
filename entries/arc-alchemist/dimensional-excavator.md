+++
id = "ref/arc-alchemist/dimensional-excavator"
kind = "archetype"
title = "Dimensional Excavator"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Dimensional%20Excavator"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dimensional_excavator", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "extradimensional-extract", level = 4 },
  { anchor = "precipitous-discoveries", level = 6 },
]
trades = [
  { replaces = "Discovery gained at 4th level", feature = "discovery", levels = [4], by = ["extradimensional-extract"] },
  { alters = "Discovery", feature = "discovery", by = ["extradimensional-extract", "precipitous-discoveries"] },
]
+++

Alchemists are often drawn to the Mana Wastes to study the strange energies and interactions that
can be found there. Though many overeager alchemists ultimately disappear during research
expeditions, more cautious scholars of alchemy in Alkenstar are content to simply read the notes
left behind by their more adventurous kindred. Some of these scholars have discovered and recorded
ways to cause their bombs to create minor tears in the fabric of reality, forming extradimensional
pits to vex their foes.

## Extradimensional Extract (Su) {#extradimensional-extract}

The intense study a dimensional excavator applies to dimensional forces causes him to treat his
class level as 2 lower when qualifying for alchemist discoveries other than those granted by
Precipitous Discoveries (see below). At 4th level, the dimensional excavator adds
_[create pit](ref/spell/create-pit)_ to his list of extracts known, treating it as a 2nd-level
alchemist extract. He can create an extract of this spell, which can then be thrown as a ranged
attack, targeting a creature or square. If it strikes a square, the pit manifests in that area and
all nearby creatures are affected normally. If a creature is struck, the pit manifests in the
creature's location, and the struck creature must succeed at a Reflex save with a -2 penalty or fall
into the pit.

This alters the discovery ability, and replaces the discovery gained at 4th level.

## Precipitous Discoveries (Su) {#precipitous-discoveries}

At 6th level, a dimensional excavator can choose to learn an additional pit spell in place of
learning a new discovery. The alchemist must be able to use an extract of the appropriate level to
select a pit spell as an extract. He can add the following spells to his extracts known, and use
them as per the extradimensional extract ability: _[spiked pit](ref/spell/spiked-pit)_ (3rd-level
extract), _[acid pit](ref/spell/acid-pit)_ (4th-level extract), _[hungry pit](ref/spell/hungry-pit)_
(5th-level extract).

This alters the discovery ability.
