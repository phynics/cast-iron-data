+++
id = "ref/arc-druid/dinosaur-druid"
kind = "archetype"
title = "Dinosaur Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Dinosaur%20Druid"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dinosaur_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "summon-dinosaur" },
  { anchor = "dinosaur-bond" },
  { anchor = "dinosaur-shape" },
  { anchor = "primeval-voice", level = 4 },
]
trades = [
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["primeval-voice"] },
  { alters = "Nature's bond", feature = "nature-bond", by = ["dinosaur-bond"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["dinosaur-shape"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["summon-dinosaur"] },
]
+++

A dinosaur druid speaks for the spirit of prehistoric nature, even taking the form of great beasts
of legend.

## Summon Dinosaur (Sp) {#summon-dinosaur}

A dinosaur druid can summon a wide range of dinosaurs and related prehistoric beasts using _summon
nature's ally_ spells. She adds the following options to these spells when using spontaneous casting
to cast such a spell.

_Summon Nature's Ally I:_ Compsognathus.

_Summon Nature's Ally II:_ Dimorphodon, troodon.

_Summon Nature's Ally III:_ Plesiosaurus, velociraptor.

_Summon Nature's Ally IV:_ Dimetrodon, pachycephalosaurus, parasaurolophus.

_Summon Nature's Ally V:_ Amargasaurus, ceratosaurus, iguanodon, kentrosaurus, styracosaurus.

_Summon Nature's Ally VI:_ Allosaurus, quetzalcoatlus, tylosaurus.

_Summon Nature's Ally VII:_ Therizinosaurus.

_Summon Nature's Ally VIII:_ Diplodocus, spinosaurus.

_Summon Nature's Ally IX:_ Giganotosaurus.

This alters spontaneous casting.

## Dinosaur Bond (Ex) {#dinosaur-bond}

A dinosaur druid must choose an animal companion as her nature's bond, and the animal companion must
be a dinosaur (including those detailed in _Pathfinder RPG Bestiary_ volumes).

This alters nature's bond.

## Dinosaur Shape (Su) {#dinosaur-shape}

A dinosaur druid specializes in assuming the form of dinosaurs when using wild shape. When she
assumes the form of a dinosaur via wild shape, she gains a +2 size bonus to her Constitution in
addition to the other modifiers granted by _[beast shape](ref/spell/beast-shape)_. When she uses
wild shape to assume the form of a creature other than a dinosaur, the wild shape effect lasts for
only 1 minute per level, rather than 1 hour per level.

This alters wild shape.

## Primeval Voice (Su) {#primeval-voice}

At 4th level, a dinosaur druid gains the ability to speak with dinosaurs (as per
_[speak with animals](ref/spell/speak-with-animals)_) at all times.

This replaces resist nature's lure.
