+++
id = "ref/arc-druid/fungal-pilgrim"
kind = "archetype"
title = "Fungal Pilgrim"
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
replaces = ["Wild shape", "Wild shape", "Timeless body"]
alters = ["Nature bond"]
+++

Druids often work to preserve the natural world, but some seek to further emulate it. Fungal
pilgrims are druids seeking transformation into a more plant-like existence. These unique adherents
of nature's creed see fungi as the means to such ends, as many fungi - particularly those of the
Darklands' naturally work their way into the bodies of living creatures.

**Devotion to Ascension (Ex)**

**Alters:** Nature bond

**Choice:** A fungal pilgrim must select the [Plant](ref/domain/plant) domain for her nature bond if
she does not select an animal companion.

**Spore Spawning**

**Action:** Ability

**At 20th Level:** The druid can use this ability any number of times a day.

**Gained:** At 4th Level

**Prereq:** Selected the Plant domain for _nature bond_

**Replaces:** Wild shape

**Usage:** 1 time/day + 1 per 2 druid levels beyond 4th

A fungal pilgrim who selected the Plant domain for her nature bond gains the ability to grow fungal
creatures from the spores of her body. Once per day, when casting a
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell to summon a single creature, the
fungal pilgrim can infuse her fungal connection into the casting. The creature summoned must be
selected from the [summon nature's ally](ref/spell/summon-natures-ally) list for 1 spell level lower
than the spell cast. For example, if the fungal pilgrim casts
_[summon nature's ally III](ref/spell/summon-natures-ally-3),_ she must choose a creature from the
list in _[summon nature's ally II](ref/spell/summon-natures-ally-2)._

Creatures summoned in this manner gain the [fungal creature](ref/template/fungal-creature) template,
except they do not gain the _create spawn_ and _poison spore cloud_ special attacks. A creature
summoned in this manner cannot be harvested for its poison.

**Fungal Companion**

**Ability:** A fungal pilgrim who selected an animal companion for her nature bond initiates a
transformation in her companion. The animal companion gains the _fungal creature_ template, but does
not gain the _create spawn, poison spore cloud,_ and _[poisonous blood](ref/umr/poisonous-blood)_
special attacks.

**At 10th Level:** The animal companion gains the _[poisonous blood](ref/umr/poisonous-blood)_
special attack.

**At 14th Level:** The animal companion gains the _poison spore_ cloud special attack.

**At 20th Level:** The animal companion gains the _create spawn_ special attack; created spawn are
under the control of the fungal pilgrim. Spawn created in this way last for only 48 hours before
rotting away.

**Info:** The fungal pilgrim **only** gets this ability if they selected an animal companion as
their _nature bond._

**Gained:** At 4th Level

**Replaces:** Wild shape

**Mycological Transformation (Ex)**

**Flavor:** Fungal spores become fully integrated into the druid's body, inside and out.

**Gained:** At 15th Level

**Passive:** She gains all immunities granted by the [plant](ref/type/plant) creature type as well
as the [light sensitivity](ref/umr/light-sensitivity) universal monster rule. She counts as a plant
for the purposes of effects that would negatively affect or damage plants. In addition, she no
longer needs to eat or sleep in the typical manner, and instead gains the fungal creature's
_rejuvenation_ ability. She can perform her daily meditation during her rejuvenation.

**Replaces:** Timeless body
