+++
id = "ref/arc-barbarian/mooncursed"
kind = "archetype"
title = "Mooncursed"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Mooncursed"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mooncursed", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "horror-adventures"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "race" },
  { anchor = "shifting-rage" },
  { anchor = "hybrid-rage", level = 5 },
  { anchor = "greater-shifting-rage", level = 11 },
  { anchor = "mighty-shifting-rage", level = 20 },
]
trades = [
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["hybrid-rage"] },
  { replaces = "Greater rage", feature = "greater-rage", by = ["greater-shifting-rage"] },
  { replaces = "Mighty rage", feature = "mighty-rage", by = ["mighty-shifting-rage"] },
  { alters = "Rage", feature = "rage", by = ["shifting-rage"] },
]
+++

Some barbarians exhibit an unusual form of lycanthropy powered by their fury. Such a character
transforms willfully but can maintain her animal or hybrid forms only while raging.

## Race {#race}

A mooncursed must either be a humanoid or monstrous humanoid.

## Shifting Rage (Su) {#shifting-rage}

A mooncursed can call upon an animal totem or inner curse, transforming her into a savage beast.
Starting at 1st level, she chooses [bear](ref/monster/bear-grizzly-bear), [boar](ref/monster/boar),
[crocodile](ref/monster/crocodile), [shark](ref/monster/shark), [tiger](ref/monster/tiger), or
[wolf](ref/monster/wolf). Once chosen, this animal can't be changed. When using rounds of her
shifting rage, instead of the usual bonuses and penalties from rage, the mooncursed transforms into
a Medium version of this animal's form as if under the influence of
_[beast shape I](ref/spell/beast-shape-1)_, treating her class level as her caster level whenever
relevant. Other aspects of rage aside from the bonuses and penalties, such as the skill restrictions
on skills and effects that require concentration, still apply during a shifting rage.

This ability alters rage.

## Hybrid Rage (Su) {#hybrid-rage}

Beginning at 5th level, a mooncursed can choose to assume a hybrid of her base type and alternate
form instead of her usual alternate form during her shifting rage. If she does, the animal's
forelimbs (or pectoral fins for the shark) remain hands able to manipulate objects and wield weapons
as well as human hands do, she can walk on two legs (the shark's tail fins remain legs), and she can
talk.

This ability replaces improved uncanny dodge.

## Greater Shifting Rage (Su) {#greater-shifting-rage}

At 11th level, a mooncursed can assume larger alternate and hybrid forms. This functions like
_[beast shape II](ref/spell/beast-shape-2)_, and it allows the mooncursed to take on a Medium or
Large version of her animal's form.

This ability replaces greater rage.

## Mighty Shifting Rage (Su) {#mighty-shifting-rage}

At 20th level, a mooncursed can assume even larger alternate and hybrid forms. This functions like
_[beast shape III](ref/spell/beast-shape-3)_, and it allows the mooncursed to take on a Medium,
Large, or Huge version of her animal's form.

This ability replaces mighty rage.
