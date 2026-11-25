+++
id = "ref/arc-barbarian/flesheater"
kind = "archetype"
title = "Flesheater"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Flesheater"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flesheater", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "occult-adventures"
page = "114"

[fields]
kind = "archetype"
features = [
  { anchor = "rage" },
  { anchor = "one-flesh", level = 2 },
  { anchor = "unbound-rage", level = 11 },
  { anchor = "feast", level = 14 },
  { anchor = "unbound-form", level = 20 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["one-flesh"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["one-flesh"] },
  { replaces = "the 2nd- and 8th-level rage powers", feature = "rage-powers", levels = [2, 8], by = ["one-flesh"] },
  { replaces = "Greater rage", feature = "greater-rage", by = ["unbound-rage"] },
  { replaces = "The 14th-level rage power", feature = "rage-powers", levels = [14], by = ["feast"] },
  { replaces = "Mighty rage", feature = "mighty-rage", by = ["unbound-form"] },
  { alters = "Rage", feature = "rage", by = ["rage"] },
]
+++

A flesheater eats flesh to create a spiritual bond between herself and the consumed creature,
allowing her to take on aspects of the creature that served as the meal.

## Rage {#rage}

In additional to the standard bonuses and penalties of rage, a flesheater takes a -2 penalty to
Intelligence while raging. The additional benefits and penalties from a flesheater's abilities last
only as long as her rage does, and she cannot use these abilities if they would bring the total
penalty to Intelligence to an amount equal to or greater than her Intelligence score. This ability
alters the rage ability.

## One Flesh (Su) {#one-flesh}

At 2nd level when entering a rage, a flesheater can spend an additional round of rage and take an
additional -2 penalty to Intelligence to take on a single ability of the valid consumed creature
whose flesh she ate most recently. For the purpose of this ability, a valid consumed creature is any
dead animal, dragon, humanoid, or magical beast that died and was consumed by the flesheater within
the past 24 hours. She can choose any ability listed under
_[beast shape I](ref/spell/beast-shape-1)_, as long as the creature possessed that ability. At 5th
level, the flesheater can take on any number of the creature's abilities that are listed under
_[beast shape I](ref/spell/beast-shape-1)_. At 8th level, the flesheater can instead take on one of
the creature's abilities listed under _[beast shape II](ref/spell/beast-shape-2)_. The flesheater's
appearance alters to resemble the consumed creature, but she does not change shape. This is a
polymorph effect. This ability replaces uncanny dodge, improved uncanny dodge, and the 2nd- and
8th-level rage powers.

## Unbound Rage (Su) {#unbound-rage}

At 11th level, a flesheater can draw in mass from the Ethereal Plane to enlarge herself when she
enters a rage, as long as the creature whose flesh she last consumed was at least one size category
larger than her base size. Unbound rage affects her as _[enlarge person](ref/spell/enlarge-person)_,
except she receives a +4 size bonus to Strength and an additional -2 penalty to Intelligence. This
ability replaces greater rage.

## Feast (Su) {#feast}

At 14th level, a flesheater can use her one flesh and unbound rage abilities to emulate any one
valid consumed creature of her choice, rather than only the one she consumed most recently. This
ability replaces the 14th-level rage power.

## Unbound Form (Su) {#unbound-form}

At 20th level, a flesheater can use her one flesh ability to assume the shape of a valid consumed
creature. This ability functions as _[alter self](ref/spell/alter-self)_,
_[beast shape IV](ref/spell/beast-shape-4)_,
_[form of the dragon III](ref/spell/form-of-the-dragon-3)_, or
_[giant form II](ref/spell/giant-form-2)_, as appropriate. This is a polymorph effect. This ability
replaces mighty rage.

## Rage Powers {#rage-powers}

The following rage powers complement the flesheater archetype:
[animal fury](ref/ragepower/animal-fury), [beast totem](ref/ragepower/beast-totem) (any),
[inspire ferocity](ref/ragepower/inspire-ferocity),
[internal fortitude](ref/ragepower/internal-fortitude), and
[terrifying howl](ref/ragepower/terrifying-howl).
