+++
id = "ref/arc-bard/first-world-minstrel"
kind = "archetype"
title = "First World Minstrel"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20First%20World%20Minstrel"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "first_world_minstrel", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "fey-magic" },
  { anchor = "wild-empathy", level = 1 },
  { anchor = "echoes-of-the-first-world", level = 1 },
  { anchor = "gremlin-s-luck", level = 8 },
  { anchor = "resist-nature-s-lure", level = 2 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["wild-empathy"] },
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["echoes-of-the-first-world"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["gremlin-s-luck"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["resist-nature-s-lure"] },
  { alters = "Spell list", feature = "spells", power = "spell list", by = ["fey-magic"] },
]
+++

Most cultures tell stories of people stolen away by the fey, only to return years later, forever
changed. The First World minstrel was changed in such a way by the fey, and his performances channel
the mysterious powers of the First World.

## Fey Magic {#fey-magic}

A First World minstrel adds _[summon nature's ally](ref/spell/summon-natures-ally)_ spells to his
spell list instead of the equivalent _[summon monster](ref/spell/summon-monster)_ spells.

This ability alters the First World minstrel's spell list.

## Wild Empathy (Ex) {#wild-empathy}

A First World minstrel gains the [wild empathy](ref/ability/wild-empathy) druid class feature, using
his bard level as his druid level for this ability.

This ability replaces bardic knowledge.

## Bardic Performance {#bardic-performance}

A First World minstrel gains the following types of bardic performance.

## Echoes of the First World (Su) {#echoes-of-the-first-world}

A First World minstrel infuses himself or a single willing ally within 30 feet with the strange
magic of the First World, granting the target one of the special abilities from the
[fey creature template](ref/template/fey-creature) (see _Pathfinder RPG Bestiary 3_ 116) other than
[change shape](ref/carried/bestiary/rules/universal-monster-rules/change-shape) for 1 round. For
every 3 levels beyond 1st the First World minstrel has, he can target one additional ally or add an
additional special ability to one of his targets. This is a polymorph effect that relies on audible
components.

This ability replaces inspire courage.

## Gremlin's Luck (Su) {#gremlin-s-luck}

A First World minstrel of 8th level or higher can use his performance to inflict bad luck on a
target within 30 feet for 1 round. Whenever the target rolls an ability check, attack roll, saving
throw, or skill check, it must roll twice and take the worse result. A target that succeeds at a
Will save (DC 10 + [half](ref/misc/fractions-and-rounding) the First World minstrel's level + his
Charisma modifier) negates the effect and is immune to this ability for 24 hours. This is a
mind-affecting effect that relies on audible components.

This ability replaces dirge of doom.

## Resist Nature's Lure (Ex) {#resist-nature-s-lure}

At 2nd level, a First World minstrel gains the
[resist nature's lure](ref/ability/resist-natures-lure) druid class feature.

This ability replaces well-versed.
