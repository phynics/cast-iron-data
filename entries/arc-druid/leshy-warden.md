+++
id = "ref/arc-druid/leshy-warden"
kind = "archetype"
title = "Leshy Warden"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "leshy_warden", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]

[fields]
kind = "archetype"
replaces = ["Nature bond", "Wild empathy", "Resist nature's lure", "A thousand faces"]
alters = ["Spontaneous casting", "Wild shape"]
+++

**Sources:** Ultimate Wilderness pg 47, Familiar Folio pg 7\
The natural world is full of bodiless nature spirits connected to the forces of glades, springs, and
individual plants. Some druids hear their call keenly and are able to effortlessly incarnate them as
the miniature creatures known as leshys. The leshy warden serves as these spirits' ally, defender,
and voice.

**Leshy Familiar (Ex)**

**Ability:** A leshy warden forms an intimate bond with a nature spirit, incarnating the spirit as a
[leaf leshy](ref/monster/leshy-leaf-leshy). She gains a leaf leshy as a
[familiar](ref/sidekick/familiar) and treats her druid level as her effective
[wizard](ref/class/wizard) level for the purpose of this ability. If the leshy dies, the leshy
warden can incarnate the same spirit again by paying the normal cost to replace a familiar. So long
as the leshy lives, the leshy warden gains access to the [Plant](ref/domain/plant) domain as if
through a druid's _nature bond_ class feature, but she can't choose the Decay subdomain.

**Replaces:** Nature bond

**Green Empathy (Ex)**

**Ability:** A leshy warden can improve the attitude of a plant creature as if using _wild empathy._
The typical wild plant creature has a starting attitude of indifferent. If the plant creature is
mindless, the leshy warden imparts a modicum of intellect to the plant so that it can be interacted
with as if it were an animal. A leshy warden can also use this ability to influence an animal, but
she takes a -4 penalty on the check to do so.

**Replaces:** Wild empathy

**Leshy Summoner (Ex)**

**Ability:** A leshy warden is an expert at summoning and growing [leshys](ref/family/leshy). She
counts as a plant creature for the purpose of growing leshys. She adds leaf leshys,
[gourd leshys](ref/monster/leshy-gourd-leshy), [fungus leshys](ref/monster/leshy-fungus-leshy),
[seaweed leshys](ref/monster/leshy-seaweed-leshy), and [lotus leshys](ref/monster/leshy-lotus-leshy)
to her list of creatures she can summon with
[summon nature's ally I, II, III, IV, and V](ref/spell/summon-natures-ally-1), respectively.

**Alters:** Spontaneous casting

**Leshy Tender (Ex)**

**At 12th Level:** She can either grant her current leshy a final +2 increase to Strength and
Dexterity or transform it into a seaweed leshy.

**At 4th Level:** A leshy warden can either grant her leaf leshy a +2 increase to Strength and
Dexterity or transform it into a gourd leshy.

**At 8th Level:** The leshy warden can either grant her current leshy a +2 increase to Strength and
Dexterity or transform it into a fungus leshy.

**Replaces:** Resist nature's lure

**Special:** If the leshy is transformed, it gains the normal ability scores of its new form;
ability score increases granted by this ability don't carry over to its new form.

**Wild Shape (Su)**

**Alters:** Wild shape

**At 10th Level:** She can take the form of a Huge plant creature, as per
[plant shape III](ref/spell/plant-shape-3).

**At 8th Level:** She can take the form of a Large plant creature, as per
[plant shape II](ref/spell/plant-shape-2).

**Gained:** At 6th Level

**Passive:** A leshy warden gains _wild shape,_ except her effective druid level for the ability is
equal to her druid level - 2 for the purpose of determining the number of times per day she can use
it. The leshy warden can assume the form of only Small or Medium plant creatures, as per
[plant shape I](ref/spell/plant-shape-1).

**Plant Whisperer (Su)**

**Ability:** Once per day, she can spend 10 minutes in communion with the spirits to learn the
answers to her questions, as [commune with nature](ref/spell/commune-with-nature).

**Flavor:** A leshy warden's connection to the spirits of nature becomes strong enough that she can
always hear them whispering.

**Gained:** At 13th Level

**Passive:** She is treated as if constantly under the effects of
[speak with plants](ref/spell/speak-with-plants).

**Replaces:** A thousand faces
