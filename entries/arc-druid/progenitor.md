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
replaces = ["Nature bond"]
alters = ["Spontaneous casting", "Wild shape"]
+++

Some druids forge powerful bonds with the raw, natural power of the First World. Progenitors are
druids who tap into the vibrant power of the First World to propagate natural and supernatural
wonders.

**Infused Summoning (Ex)**

**Alters:** Spontaneous casting

**Passive:** When a progenitor casts _[summon nature's ally](ref/spell/summon-natures-ally)_ to
summon a creature, the summoned creature gains [fast healing](ref/umr/fast-healing) equal to the
progenitor's level (maximum equal to the progenitor's Wisdom modifier).

**Primal Bond (Ex)**

**Choice:** A progenitor infuses herself with fey magic so that she is treated as either her
original creature type or the fey type for the purposes of spells or effects that target a creature
by type, whichever is more beneficial to her. Additionally, the progenitor chooses one of two forms
through which this bond expresses itself: magic or nature.

**Replaces:** Nature bond

**Magic**

**Info:** A progenitor who chooses magic as her primal bond can draw upon wild magic to attempt to
cast a prepared spell without losing that spell from its spell slot.

**Swift:** To use this ability, she casts the spell as she would normally, but as the spell's
effects take place, she must use a **swift action** to attempt a
[concentration](ref/rule/concentration) check (DC = 20 + twice the spell's level). If she fails, she
expends the spell normally as if she had cast it, but its effects are replaced by
[a wild magic effect](ref/rule/magic-traits-pa) with a CR equal to her caster level and she is
[staggered](ref/misc/staggered) until the end of her next turn. If she succeeds, she casts the spell
normally and it is not expended from her prepared spell slot, allowing her to cast that spell again
at a later point.

**Usage:** 1 time/day + 1 per 5 druid levels

**Nature**

**Fullround:** At the start of her next turn, so long as she is touching a solid surface underfoot,
a 5-foot radius of mobile undergrowth springs to life around the progenitor for a number of rounds
equal to 3 plus the progenitor's Wisdom bonus. Upon activating this ability, the progenitor chooses
whether the undergrowth provides [cover](ref/rule/cover) or
[difficult terrain](ref/rule/terrain-and-obstacles). If the progenitor chooses cover, her
undergrowth provides a cover bonus to AC to the progenitor and allies within the radius. If she
chooses difficult terrain, enemies who enter the radius of undergrowth treat it as difficult
terrain. A progenitor's undergrowth is treated as forest terrain if it provides cover and plains
terrain if it provides difficult terrain. This radius increases by 5 feet at 5th level and every 5
levels thereafter.

**Info:** A progenitor who chooses nature as her primal bond can create plants.

**Usage:** 1 time/day + 1 per 5 druid levels

**Fey Shape (Su)**

**Alters:** Wild shape

**At 10th Level:** A progenitor can use _wild shape_ to change into a Diminutive or Huge fey. When
she does so, her _wild shape_ functions as [fey form III](ref/spell/fey-form-3).

**At 14th Level:** When a progenitor uses _wild shape_ to assume a fey form, her _wild shape_
functions as [fey form IV](ref/spell/fey-form-4).

**At 6th Level:** A progenitor can use _wild shape_ to change into a Small or Medium fey. When doing
so, her _wild shape_ functions as [fey form I](ref/spell/fey-form-1).

**At 8th Level:** A progenitor can use _wild shape_ to change into a Tiny or Large fey. When she
does so, her _wild shape_ functions as [fey form II](ref/spell/fey-form-2).

**Info:** A progenitor never gains the ability to use _wild shape_ to transform into an elemental.

**Gained:** At 4th Level
