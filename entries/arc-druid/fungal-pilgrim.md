+++
id = "ref/arc-druid/fungal-pilgrim"
kind = "archetype"
title = "Fungal Pilgrim"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Fungal%20Pilgrim"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fungal_pilgrim", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "devotion-to-ascension", level = 1 },
  { anchor = "spore-spawning", level = 4 },
  { anchor = "fungal-companion", level = 4 },
  { anchor = "mycological-transformation", level = 15 },
]
trades = [
  { replaces = "Wild shape if the fungal pilgrim selected the Plant domain as her nature bond", feature = "wild-shape", by = ["spore-spawning"] },
  { replaces = "Timeless body", feature = "timeless-body", by = ["mycological-transformation"] },
  { alters = "Nature bond", feature = "nature-bond", by = ["devotion-to-ascension"] },
  { replaces = "Wild shape if the fungal pilgrim selected an animal companion as her nature bond", by = ["fungal-companion"] },
]
+++

Druids often work to preserve the natural world, but some seek to further emulate it. Fungal
pilgrims are druids seeking transformation into a more plantlike existence. These unique adherents
of nature's creed see fungi as the means to such ends, as many fungi—particularly those of the
Darklands—naturally work their way into the bodies of living creatures.

## Devotion to Ascension (Ex) {#devotion-to-ascension}

A fungal pilgrim must select the [Plant](ref/domain/plant) domain for her nature bond if she does
not select an animal companion.

This alters nature bond.

## Spore Spawning {#spore-spawning}

At 4th level, a fungal pilgrim who selected the Plant domain for her nature bond gains the ability
to grow fungal creatures from the spores of her body. Once per day, when casting a
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell to summon a single creature, the
fungal pilgrim can infuse her fungal connection into the casting. The creature summoned must be
selected from the _[summon nature's ally](ref/spell/summon-natures-ally)_ list for 1 spell level
lower than the spell cast. For example, if the fungal pilgrim casts
_[summon nature's ally III](ref/spell/summon-natures-ally-3)_, she must choose a creature from the
list in _[summon nature's ally II](ref/spell/summon-natures-ally-2)_.

Creatures summoned in this manner gain the [fungal creature](ref/template/fungal-creature) template,
except they do not gain the create spawn and poison spore cloud special attacks. A creature summoned
in this manner cannot be harvested for its poison.

A druid can use this ability an additional time per day at 6th level and every 2 levels thereafter,
for a total of eight times at 18th level. At 20th level, it can be used any number of times per day.

This ability replaces wild shape if the fungal pilgrim selected the Plant domain as her nature bond.

## Fungal Companion {#fungal-companion}

At 4th level, a fungal pilgrim who selected an animal companion for her nature bond initiates a
transformation in her companion. The animal companion gains the fungal creature template (_Bestiary
4_ 116), but does not gain the create spawn, poison spore cloud, and
[poisonous blood](ref/umr/poisonous-blood) special attacks. At 10th level, the animal companion
gains the [poisonous blood](ref/umr/poisonous-blood) special attack. At 14th level, the animal
companion gains the poison spore cloud special attack. At 20th level, the animal companion gains the
create spawn special attack; created spawn are under the control of the fungal pilgrim. Spawn
created in this way last for only 48 hours before rotting away.

This ability replaces wild shape if the fungal pilgrim selected an animal companion as her nature
bond.

## Mycological Transformation (Ex) {#mycological-transformation}

Fungal spores become fully integrated into the druid's body, inside and out. At 15th level, she
gains all immunities granted by the [plant](ref/type/plant) creature type as well as the
[light sensitivity](ref/umr/light-sensitivity) universal monster rule. She counts as a plant for the
purposes of effects that would negatively affect or damage plants. In addition, she no longer needs
to eat or sleep in the typical manner, and instead gains the fungal creature's rejuvenation ability.
She can perform her daily meditation during her rejuvenation.

This ability replaces timeless body.
