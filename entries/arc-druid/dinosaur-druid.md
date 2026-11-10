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
replaces = ["Resist nature's lure"]
alters = ["Nature's bond", "Wild shape"]
replaces_features = ["resist-nature-s-lure"]
alters_features = ["wild-shape"]
+++

A dinosaur druid speaks for the spirit of prehistoric nature, even taking the form of great beasts
of legend.

;;;ab\{title="Summon Dinosaur (Sp)" action=Ability icon=magic alter="Spontaneous casting"\}

A dinosaur druid can summon a wide range of dinosaurs and related prehistoric beasts using
[summon nature's ally](ref/spell/summon-natures-ally) spells. She adds the following options to
these spells when using _spontaneous casting_ to cast such a spell.

**Summon Nature's Ally I:** Compsognathus

**Summon Nature's Ally II:** Dimorphodon, troodon

**Summon Nature's Ally III:** Plesiosaurus, velociraptor

**Summon Nature's Ally IV:** Dimetrodon, pachycephalosaurus, parasaurolophus

**Summon Nature's Ally V:** Amargasaurus, ceratosaurus, iguanodon, kentrosaurus, styracosaurus

**Summon Nature's Ally VI:** Allosaurus, quetzalcoatlus, tylosaurus

**Summon Nature's Ally VII:** Therizinosaurus

**Summon Nature's Ally VIII:** Diplodocus, spinosaurus

**Summon Nature's Ally IX:** Giganotosaurus

;;;

**Dinosaur Bond (Ex)**

**Alters:** Nature's bond

**Choice:** A dinosaur druid must choose an animal companion as her _nature's bond,_ and the animal
companion must be a dinosaur.

**Dinosaur Shape (Su)**

**Ability:** When she assumes the form of a dinosaur via _wild shape,_ she gains a +2 size bonus to
her Constitution in addition to the other modifiers granted by
_[beast shape](ref/spell/beast-shape)._ When she uses _wild shape_ to assume the form of a creature
other than a dinosaur, the _wild shape_ effect lasts for only 1 minute per level, rather than 1 hour
per level.

**Alters:** Wild shape

**Flavor:** A dinosaur druid specializes in assuming the form of dinosaurs when using _wild shape._

**Primeval Voice (Su)**

**Ability:** A dinosaur druid gains the ability to speak with dinosaurs (as per
[speak with animals](ref/spell/speak-with-animals)) at all times.

**Gained:** At 4th Level

**Replaces:** Resist nature's lure
