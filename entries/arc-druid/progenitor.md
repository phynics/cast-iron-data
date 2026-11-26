+++
id = "ref/arc-druid/progenitor"
kind = "archetype"
title = "Progenitor"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Progenitor"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "progenitor", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "planar-adventures"
page = "19"

[fields]
kind = "archetype"
features = [
  { anchor = "infused-summoning", level = 1 },
  { anchor = "primal-bond", level = 1 },
  { anchor = "fey-shape" },
]
trades = [
  { replaces = "Nature bond", feature = "nature-bond", by = ["primal-bond"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["infused-summoning"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["fey-shape"] },
]
+++

Some druids forge powerful bonds with the raw, natural power of the First World. Progenitors are
druids who tap into the vibrant power of the First World to propagate natural and supernatural
wonders.

## Infused Summoning (Ex) {#infused-summoning}

When a progenitor casts _[summon nature's ally](ref/spell/summon-natures-ally)_ to summon a
creature, the summoned creature gains [fast healing](ref/umr/fast-healing) equal to the progenitor's
level (maximum equal to the progenitor's Wisdom modifier).

This alters spontaneous casting.

## Primal Bond (Ex) {#primal-bond}

A progenitor infuses herself with fey magic so that she is treated as either her original creature
type or the fey type for the purposes of spells or effects that target a creature by type, whichever
is more beneficial to her. Additionally, the progenitor chooses one of two forms through which this
bond expresses itself: magic or nature.

A progenitor who chooses magic as her primal bond can draw upon wild magic as a swift action to
attempt to cast a prepared spell without losing that spell from its spell slot. To use this ability,
she casts the spell as she would normally, but as the spell's effects take place, she must attempt a
[concentration](ref/rule/concentration) check (DC = 20 + twice the spell's level). If she fails, she
expends the spell normally as if she had cast it, but its effects are replaced by
[a wild magic effect](ref/rule/magic-traits-pa) (see page 63) with a CR equal to her caster level
and she is [staggered](ref/misc/staggered) until the end of her next turn. If she succeeds, she
casts the spell normally and it is not expended from her prepared spell slot, allowing her to cast
that spell again at a later point. A progenitor can use wild magic in this manner once per day plus
one additional time per day at 5th level and every 5 levels thereafter.

A progenitor who chooses nature as her primal bond can create plants as a full-round action. She can
do so once per day plus one additional time per day per 5 levels. At the start of her next turn, so
long as she is touching a solid surface underfoot, a 5-foot radius of mobile undergrowth springs to
life around the progenitor for a number of rounds equal to 3 plus the progenitor's Wisdom bonus.
Upon activating this ability, the progenitor chooses whether the undergrowth provides
[cover](ref/rule/cover) or [difficult terrain](ref/rule/terrain-and-obstacles). If the progenitor
chooses cover, her undergrowth provides a cover bonus to AC to the progenitor and allies within the
radius. If she chooses difficult terrain, enemies who enter the radius of undergrowth treat it as
difficult terrain. A progenitor's undergrowth is treated as forest terrain if it provides cover and
plains terrain if it provides difficult terrain. This radius increases by 5 feet at 5th level and
every 5 levels thereafter.

This replaces nature bond.

## Fey Shape (Su) {#fey-shape}

A progenitor never gains the ability to use wild shape to transform into an elemental.

At 6th level, a progenitor can use wild shape to change into a Small or Medium fey. When doing so,
her wild shape functions as _[fey form I](ref/spell/fey-form-1)_.

At 8th level, a progenitor can use wild shape to change into a Tiny or Large fey. When she does so,
her wild shape functions as _[fey form II](ref/spell/fey-form-2)_.

At 10th level, a progenitor can use wild shape to change into a Diminutive or Huge fey. When she
does so, her wild shape functions as _[fey form III](ref/spell/fey-form-3)_.

At 14th level, when a progenitor uses wild shape to assume a fey form, her wild shape functions as
_[fey form IV](ref/spell/fey-form-4)_.

This alters wild shape.
