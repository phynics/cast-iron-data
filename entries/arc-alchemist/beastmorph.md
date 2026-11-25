+++
id = "ref/arc-alchemist/beastmorph"
kind = "archetype"
title = "Beastmorph"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Beastmorph"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "beastmorph", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "ultimate-combat"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "beastform-mutagen", level = 3 },
  { anchor = "improved-beastform-mutagen", level = 6 },
  { anchor = "greater-beastform-mutagen", level = 10 },
  { anchor = "grand-beastform-mutagen", level = 14 },
]
trades = [
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["beastform-mutagen"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["improved-beastform-mutagen"] },
  { replaces = "Poison resistance +2, +4, and +6", feature = "poison-resistance", levels = [2, 5, 8], by = ["greater-beastform-mutagen"] },
  { replaces = "poison immunity", feature = "poison-resistance", levels = [10], by = ["greater-beastform-mutagen"] },
  { replaces = "Persistent mutagen", feature = "persistent-mutagen", by = ["grand-beastform-mutagen"] },
]
+++

Beastmorphs study the anatomy of monsters, learning how they achieve their strange powers. They use
their knowledge to duplicate these abilities, but at the cost of taking on inhuman shapes when they
use mutagens.

## Beastform Mutagen {#beastform-mutagen}

At 3rd level, a beastmorph's mutagen causes him to take on animalistic features—whether those of an
animal, a magical beast, an animal-like humanoid (such as a lizardfolk), or a monstrous humanoid.
For example, when the beastmorph uses his mutagen, he may gain a furry muzzle and pointed ears like
a werewolf, scaly skin like a lizardfolk or sahuagin, or compound eyes and mandibles like a giant
insect. The beastmorph also gains his choice of one of the abilities listed in the
_[alter self](ref/spell/alter-self)_ spell, which persists as long as the mutagen. He may select a
different ability each time he creates a mutagen. This ability replaces swift alchemy.

## Improved Beastform Mutagen {#improved-beastform-mutagen}

At 6th level, a beastmorph's mutagen grants him additional abilities and options. The alchemist
gains his choice of two of the abilities listed in the _[beast shape I](ref/spell/beast-shape-1)_
spell, which persist as long as the mutagen. He may select two different abilities each time he
creates a mutagen. This ability replaces swift poisoning.

## Greater Beastform Mutagen {#greater-beastform-mutagen}

At 10th level, a beastmorph's mutagen grants him three of the abilities listed in the
_[beast shape II](ref/spell/beast-shape-2)_ spell, which persist as long as the mutagen. He may
select three different abilities each time he creates a mutagen. This ability replaces poison
resistance +2, +4, and +6, as well as poison immunity.

## Grand Beastform Mutagen {#grand-beastform-mutagen}

At 14th level, a beastmorph's mutagen grants him four of the abilities listed in the
_[beast shape III](ref/spell/beast-shape-3)_ spell, which persist as long as the mutagen. He may
select four different abilities each time he creates a mutagen. This ability replaces persistent
mutagen.

## Discoveries {#discoveries}

The following discoveries complement the beastmorph archetype:
[feral mutagen](ref/discovery/feral-mutagen), [grand mutagen](ref/discovery/grand-mutagen),
[greater mutagen](ref/discovery/greater-mutagen), [infuse mutagen](ref/discovery/infuse-mutagen),
[mummification](ref/discovery/mummification),
[spontaneous healing](ref/discovery/spontaneous-healing), [tentacle](ref/discovery/tentacle), and
[wings](ref/discovery/wings).
