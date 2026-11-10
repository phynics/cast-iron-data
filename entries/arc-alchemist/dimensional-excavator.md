+++
id = "ref/arc-alchemist/dimensional-excavator"
kind = "archetype"
title = "Dimensional Excavator"
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
replaces = ["4th-level discovery"]
alters = ["Discovery", "Discovery"]
alters_features = ["discovery", "discovery"]
+++

Alchemists are often drawn to the Mana Wastes to study the strange energies and interactions that
can be found there. Though many overeager alchemists ultimately disappear during research
expeditions, more cautious scholars of alchemy in Alkenstar are content to simply read the notes
left behind by their more adventurous kindred. Some of these scholars have discovered and recorded
ways to cause their bombs to create minor tears in the fabric of reality, forming extradimensional
pits to vex their foes.

**Extradimensional Extract (Su)**

**Alters:** Discovery

**At 1st Level:** The intense study a dimensional excavator applies to dimensional forces causes him
to treat his class level as 2 lower when qualifying for alchemist discoveries other than those
granted by _Precipitous Discoveries_ (see below).

**At 4th Level:** The dimensional excavator adds [create pit](ref/spell/create-pit) to his list of
extracts known, treating it as a 2nd-level alchemist extract. He can create an extract of this
spell, which can then be thrown as a ranged attack, targeting a creature or square. If it strikes a
square, the pit manifests in that area and all nearby creatures are affected normally. If a creature
is struck, the pit manifests in the creature's location, and the struck creature must succeed at a
Reflex save with a -2 penalty or fall into the pit.

**Replaces:** 4th-level discovery

**Precipitous Discoveries (Su)**

**Alters:** Discovery

**Gained:** At 6th Level

**Passive:** A dimensional excavator can choose to learn an additional _pit_ spell in place of
learning a new discovery. The alchemist must be able to use an extract of the appropriate level to
select a _pit_ spell as an extract. He can add the following spells to his extracts known, and use
them as per the extradimensional extract ability: [spiked pit](ref/spell/spiked-pit) (3rd-level
extract), [acid pit](ref/spell/acid-pit) (4th-level extract), [hungry pit](ref/spell/hungry-pit)
(5th-level extract).
