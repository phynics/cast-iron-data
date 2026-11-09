+++
id = "ref/arc-druid/life-channeler"
kind = "archetype"
title = "Life Channeler"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_channeler", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "horror-adventures"
page = "50"

[fields]
kind = "archetype"
replaces = ["Wild shape", "Venom immunity"]
alters = ["Alignment requirements", "Nature bond"]
+++

Life channelers take the natural cycle to what they believe is its logical conclusion. By
sacrificing the life of a sentient creature, they can generate energy that guarantees fertility and
prosperity for lower creatures like plants and animals. These druids preach to flocks who become
willing sacrifices, each serving as a "king" or "queen" for a short time after being chosen as the
next sacrifice.

**Alignment**

**Alters:** Alignment requirements

**Info:** In addition to a druid's usual alignment requirements, a life channeler must be of a
nongood alignment. If she becomes good, she can no longer take levels in the druid class or fill her
_wicker talismans_ (see below), but she otherwise keeps all her abilities.

**Plant Preservation (Su)**

**Ability:** When she performs a [coup de grace](ref/misc/helpless) that kills a sentient humanoid
creature (not a summoned creature), she can do so ritualistically in order to affect the area
centered on the body with the enrichment version of [plant growth](ref/spell/plant-growth). The
sacrifice is a death effect.

**Alters:** Nature bond

**Choice:** A life channeler must choose the [Plant](ref/domain/plant) domain with her _nature bond_
(she can select the Growth subdomain if she wishes).

**Wicker Talismans (Su)**

**Action:** Ability

**At 6th Level:** A life channeler gathers a flock of willing sacrifices. This grants her the
benefits of the [Leadership](ref/feat/leadership) feat, except that using a follower as a human
sacrifice with this ability doesn't cause the life channeler to take a penalty to her Leadership
score.

**Gained:** At 4th Level

**Replaces:** Wild shape

A life channeler gains a selection of wicker talismans that can store and convert the life energy of
sentient creatures into the growth, health, and fertility of plants around her. The life channeler
gains one wicker talisman corresponding to each level of druid spells she can cast, starting with
1st-level spells. These talismans are initially empty, but can hold life energy.

When the life channeler ritualistically kills a creature with a _coup de grace,_ she can store life
energy in a talisman instead of gaining the _[plant growth](ref/spell/plant-growth)_ effect. The
creature must be of a CR equal to at least twice the spell level of the corresponding talisman. For
instance, a CR 8 creature's life energy could provide energy for a talisman holding up to a
4th-level spell.

A talisman is either full or empty; it can't hold more than one creature's life energy. A life
channeler can expend the energy stored in a talisman to cast her domain spell of the talisman's
level without expending a spell slot.

**Rampant Growth**

**At 12th Level:** If the sacrificed creature was at least CR 12, the effect increases productivity
to two-thirds above normal, instead of one-third above normal.

**At 4th Level:** A life channeler can enrich the land more than usual with her sacrifices. When
ritually killing a creature with a _coup de grace_ for the _[plant growth](ref/spell/plant-growth)_
enrichment effect or casting _[plant growth](ref/spell/plant-growth)_ for the enrichment effect from
one of her talismans, the effect has a range of 1 mile instead of a range of half a mile.

**At 8th Level:** If the sacrificed creature was at least CR 8, the effect lasts for 3 years instead
of 1 year.

**Special:** These effects stack, assuming the creature is high enough CR.

**Stored Life**

**Ability:** A life channeler gains a third option when using a _coup de grace_ on a sentient
humanoid. If the victim had a CR at least as high as the life channeler's class level, the life
channeler can store the creature's life energy in her body. She can have the life energy from only 1
creature in her body at a time. While she is storing life energy, if she would take damage or die
from a death effect or if she would gain negative levels or take energy drain, she can sacrifice the
stored energy to negate the effect without spending an action.

**Gained:** At 9th Level

**Replaces:** Venom immunity
