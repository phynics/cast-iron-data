+++
id = "ref/arc-druid/goliath-druid"
kind = "archetype"
title = "Goliath Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Goliath%20Druid"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "goliath_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-languages" },
  { anchor = "primal-size", level = 1 },
  { anchor = "primal-bond", level = 1 },
  { anchor = "primal-empathy", level = 1 },
  { anchor = "face-nature-s-might", level = 4 },
  { anchor = "wild-shape", level = 4 },
  { anchor = "primal-summons", level = 9 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["primal-size"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["face-nature-s-might"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["primal-bond"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["primal-empathy"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["primal-summons"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["primal-summons"] },
]
+++

Goliath druids hone their spiritual and magical connections to nature's largest creatures,
especially dinosaurs, giants, and megafauna, revering these massive creatures as living relics of a
primeval time when all creatures were more in harmony with nature. Despite this respect, a goliath
druid doesn't hesitate to infiltrate giant groups who defile nature and destroy them from within.

Goliath druids have the following class features.

## Class Skills {#class-skills}

A goliath druid gains Bluff, Diplomacy, and Knowledge (local) as class skills, but does not gain
Craft, Profession, and Ride as class skills.

## Bonus Languages {#bonus-languages}

A goliath druid with an Intelligence bonus can select Giant as a bonus language.

## Primal Size {#primal-size}

A goliath druid adds _[enlarge person](ref/spell/enlarge-person)_ to her list of class spells. She
can cast this spell only on herself. She can also channel stored spell energy to cast this spell
without preparing it—she can lose a prepared spell of 1st level or higher to cast
_[enlarge person](ref/spell/enlarge-person)_. This ability replaces nature sense.

## Primal Bond (Ex) {#primal-bond}

When a goliath druid forms a nature bond, if she selects a cleric domain, she must select from the
[Animal](ref/domain/animal), [Destruction](ref/domain/destruction), or Strength domains, or the
Ferocity, [Growth](ref/domain/plant), or [Rage](ref/domain/destruction) subdomains.

If the goliath druid selects an animal companion, she must select a dinosaur or megafauna. If she
has a dinosaur or megafauna animal companion, she can target it with
_[enlarge person](ref/spell/enlarge-person)_ even though the companion isn't of the humanoid type.

This ability alters nature bond.

## Primal Empathy (Ex) {#primal-empathy}

A goliath druid's wild empathy functions only with creatures that are Large or larger. This ability
alters wild empathy.

## Face Nature's Might (Ex) {#face-nature-s-might}

At 4th level, a goliath druid gains a +4 bonus on saving throws against the spell-like and
supernatural abilities of giants. This ability replaces resist nature's lure.

## Wild Shape (Su) {#wild-shape}

Druids' ability to wild shape into a creature of the animal type allows a goliath druid to assume
only the form of a dinosaur or megafauna. She doesn't gain the ability to become an elemental or
plant.

At 6th level, the goliath druid can use wild shape to become a Large humanoid of the giant subtype.
This functions as the _[alter self](ref/spell/alter-self)_ spell, except the goliath druid gains a
+4 size bonus to Strength, a -2 penalty to Dexterity, and a +1 natural armor bonus. If the Large
humanoid form she takes has [rock throwing](ref/umr/rock-throwing), she gains rock throwing (range
40 feet, 1d8 damage). If the form has the [aquatic](ref/subtype/aquatic) subtype, she gains the
aquatic and [amphibious](ref/umr/amphibious) subtypes.

At 12th level, when taking the form of a giant, the goliath druid's wild shape functions as
_[giant form I](ref/spell/giant-form-1)_.

At 14th level, the goliath druid can also use wild shape to change into a Huge giant. When taking
the form of a giant, the goliath druid's wild shape functions as
_[giant form II](ref/spell/giant-form-2)_. This ability alters wild shape.

## Primal Summons {#primal-summons}

A goliath druid adds the following creatures to the list of creatures she can normally summon using
_[summon nature's ally](ref/spell/summon-natures-ally)_ spells.

_Summon Nature's Ally I:_ Compsognathus.

_Summon Nature's Ally II:_ Dimorphodon.

_Summon Nature's Ally III:_ Velociraptor.

_Summon Nature's Ally IV:_ Ogre, parasaurolophus.

_Summon Nature's Ally V:_ Glyptodon, iguanodon.

_Summon Nature's Ally VI:_ Baluchitherium, megalania.

_Summon Nature's Ally VII:_ Cliff giant.

_Summon Nature's Ally VIII:_ Spinosaurus.

_Summon Nature's Ally IX:_ Diplodocus.

This ability replaces venom immunity and a thousand faces.
