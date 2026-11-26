+++
id = "ref/arc-bloodrager/bloody-knuckled-rowdy"
kind = "archetype"
title = "Bloody-Knuckled Rowdy"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Bloody-Knuckled%20Rowdy"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloody_knuckled_rowdy", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "bloody-knuckles" },
  { anchor = "reduced-spells-known" },
  { anchor = "pugilist", level = 1 },
  { anchor = "combat-style-student", level = 2 },
  { anchor = "hand-to-hand-training", level = 3 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["pugilist"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["combat-style-student"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["combat-style-student"] },
  { alters = "Spellcasting", feature = "spells", by = ["reduced-spells-known"] },
]
+++

Bloodragers are frequently rough-and-ready, untrained scrappers who learn to exploit any advantage
to gain the upper hand in a fight. The bloody-knuckled rowdy focuses on tricks and maneuvers that
are quick and effective, duplicating combat styles from professional brawlers, street thugs, and
even trapped animals. Rather than focusing on a single style, most bloody-knuckled rowdies dabble in
multiple techniques, mixing and matching their array of vicious maneuvers to suit the occasion.

## Bloody Knuckles {#bloody-knuckles}

The bloody-knuckled rowdy does not gain [damage reduction](ref/rule/damage-reduction).

## Reduced Spells Known {#reduced-spells-known}

The bloody-knuckled rowdy focuses more on fighting tactics and less on his natural arcane powers. He
receives one fewer spell known at each spell level. This ability modifies bloodrager spellcasting.

## Pugilist (Ex) {#pugilist}

At 1st level, a bloody-knuckled rowdy gains
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat. This ability replaces
fast movement.

## Combat Style Student {#combat-style-student}

At 2nd level, a bloody-knuckled rowdy gains a bonus feat. This bonus feat must be a style feat or a
feat with a style feat as a prerequisite. The bloody-knuckled rowdy treats his bloodrager levels as
monk levels when qualifying for and calculating the effects of style feats and feats that have style
feats as prerequisites. At 5th level, the bloody-knuckled rowdy gains the
[Combat Style Master](ref/feat/combat-style-master) feat. He doesn't need to meet the prerequisites
for this feat. This ability replaces uncanny dodge and improved uncanny dodge.

## Hand-to-Hand Training (Ex) {#hand-to-hand-training}

At 3rd level, a bloody-knuckled rowdy deals unarmed damage as a [monk](ref/class/monk) of a level
equal to his bloodrager level - 2.
