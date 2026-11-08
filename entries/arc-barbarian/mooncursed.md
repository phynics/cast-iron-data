+++
id = "ref/arc-barbarian/mooncursed"
kind = "archetype"
title = "Mooncursed"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mooncursed", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]

[fields]
kind = "archetype"
replaces = ["Improved uncanny dodge", "Greater rage", "Mighty rage"]
alters = ["Rage"]
+++

**Sources:** Horror Adventures pg 47\
Some barbarians exhibit an unusual form of lycanthropy powered by their fury. Such a character
transforms willfully but can maintain her animal or hybrid forms only while raging.

**Prerequisites:** A mooncursed must either be a [humanoid](ref/type/humanoid) or
[monstrous humanoid](ref/type/monstrous-humanoid).

**Shifting Rage (Su)**

**Ability:** Choose [bear](ref/monster/bear-grizzly-bear), [boar](ref/monster/boar),
[crocodile](ref/monster/crocodile), [shark](ref/monster/shark), [tiger](ref/monster/tiger), or
[wolf](ref/monster/wolf). Once chosen, this animal can't be changed. When using rounds of her
_shifting rage,_ instead of the usual bonuses and penalties from _rage,_ the mooncursed transforms
into a Medium version of this animal's form as if under the influence of
[beast shape I](ref/spell/beast-shape-1), treating her class level as her caster level whenever
relevant. Other aspects of _rage_ aside from the bonuses and penalties, such as the skill
restrictions on skills and effects that require concentration, still apply during a _shifting rage._

**Alters:** Rage

**Flavor:** A mooncursed can call upon an animal totem or inner curse, transforming her into a
savage beast.

**Gained:** At 1st Level

**Hybrid Rage (Su)**

**Ability:** A mooncursed can choose to assume a hybrid of her base type and alternate form instead
of her usual alternate form during her _shifting rage._ If she does, the animal's forelimbs (or
pectoral fins for the shark) remain hands able to manipulate objects and wield weapons as well as
human hands do, she can walk on two legs (the shark's tail fins remain legs), and she can talk.

**Gained:** At 5th Level

**Replaces:** Improved uncanny dodge

**Greater Shifting Rage (Su)**

**Ability:** A mooncursed can assume larger alternate and hybrid forms. This functions like
[beast shape II](ref/spell/beast-shape-2), and it allows the mooncursed to take on a Medium or Large
version of her animal's form.

**Gained:** At 11th Level

**Replaces:** Greater rage

**Mighty Shifting Rage (Su)**

**Ability:** A mooncursed can assume even larger alternate and hybrid forms. This functions like
[beast shape III](ref/spell/beast-shape-3), and it allows the mooncursed to take on a Medium, Large,
or Huge version of her animal's form.

**Gained:** At 20th Level

**Replaces:** Mighty rage
