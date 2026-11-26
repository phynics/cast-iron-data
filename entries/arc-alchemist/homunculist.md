+++
id = "ref/arc-alchemist/homunculist"
kind = "archetype"
title = "Homunculist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Homunculist"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "homunculist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "familiar-folio"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-poisoning" },
  { anchor = "homunculus-familiar", level = 1 },
  { anchor = "experimentation", level = 4 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["homunculus-familiar"] },
]
+++

One of the grand goals of alchemy is the ability to create new life. A homunculist has made this
dream a reality, growing and modifying a familiar in his own laboratory.

## Diminished Poisoning {#diminished-poisoning}

A homunculist doesn't gain the poison use, poison resistance, poison immunity, or swift poisoning
class features.

## Homunculus Familiar (Ex) {#homunculus-familiar}

The homunculist has created a living [homunculus](ref/monster/homunculus) in the shape of an animal
or vermin. It functions in all ways as a [familiar](ref/ability/familiars), treating the
homunculist's alchemist level as his effective wizard level. This ability replaces mutagen.

## Experimentation (Ex) {#experimentation}

A homunculist is constantly experimenting on his [familiar](ref/sidekick/familiar) to give it new
and unusual features and abilities. At 4th level, the homunculist can grant his familiar 1 evolution
point worth of eidolon evolutions (_Pathfinder RPG Advanced Player's Guide_ 60) for every 4
alchemist levels he possesses, though he can't select any evolutions that require a particular base
form. Each time the homunculist gains a level, he can change his familiar's evolutions. These
evolutions stack with those from the [Evolved Familiar](ref/feat/evolved-familiar) feat. The
homunculist can select the Evolved Familiar feat as an alchemist discovery if he meets its
prerequisites.
