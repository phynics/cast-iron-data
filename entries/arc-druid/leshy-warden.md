+++
id = "ref/arc-druid/leshy-warden"
kind = "archetype"
title = "Leshy Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Leshy%20Warden"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "leshy_warden", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "47"
[[sources]]
publication = "familiar-folio"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "leshy-familiar", level = 1 },
  { anchor = "green-empathy", level = 1 },
  { anchor = "leshy-summoner", level = 1 },
  { anchor = "leshy-tender", level = 4 },
  { anchor = "wild-shape", level = 6 },
  { anchor = "plant-whisperer", level = 13 },
]
trades = [
  { replaces = "Nature bond", feature = "nature-bond", by = ["leshy-familiar"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["green-empathy"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["leshy-tender"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["plant-whisperer"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["leshy-summoner"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

The natural world is full of bodiless nature spirits connected to the forces of glades, springs, and
individual plants. Some druids hear their call keenly and are able to effortlessly incarnate them as
the miniature creatures known as leshys (_Pathfinder RPG Bestiary 3_ 176). The leshy warden serves
as these spirits' ally, defender, and voice.

## Leshy Familiar (Ex) {#leshy-familiar}

A leshy warden forms an intimate bond with a nature spirit, incarnating the spirit as a
[leaf leshy](ref/monster/leshy-leaf-leshy). She gains a leaf leshy as a
[familiar](ref/sidekick/familiar) and treats her druid level as her effective
[wizard](ref/class/wizard) level for the purpose of this ability. If the leshy dies, the leshy
warden can incarnate the same spirit again by paying the normal cost to replace a familiar. So long
as the leshy lives, the leshy warden gains access to the [Plant](ref/domain/plant) domain as if
through a druid's nature bond class feature, but she can't choose the Decay subdomain.

This replaces nature bond.

## Green Empathy (Ex) {#green-empathy}

A leshy warden can improve the attitude of a plant creature as if using wild empathy. The typical
wild plant creature has a starting attitude of indifferent. If the plant creature is mindless, the
leshy warden imparts a modicum of intellect to the plant so that it can be interacted with as if it
were an animal. A leshy warden can also use this ability to influence an animal, but she takes a -4
penalty on the check to do so.

This replaces wild empathy.

## Leshy Summoner (Ex) {#leshy-summoner}

A leshy warden is an expert at summoning and growing [leshys](ref/family/leshy). She counts as a
plant creature for the purpose of growing leshys. She adds leaf leshys,
[gourd leshys](ref/monster/leshy-gourd-leshy), [fungus leshys](ref/monster/leshy-fungus-leshy),
[seaweed leshys](ref/monster/leshy-seaweed-leshy), and [lotus leshys](ref/monster/leshy-lotus-leshy)
to her list of creatures she can summon with _summon nature's ally I_, _II_, _III_, _IV_, and _V_,
respectively.

This alters spontaneous casting.

## Leshy Tender (Ex) {#leshy-tender}

At 4th level, a leshy warden can either grant her leaf leshy a +2 increase to Strength and Dexterity
or transform it into a gourd leshy. At 8th level, the leshy warden can either grant her current
leshy a +2 increase to Strength and Dexterity or transform it into a fungus leshy. At 12th level,
she can either grant her current leshy a final +2 increase to Strength and Dexterity or transform it
into a seaweed leshy. If the leshy is transformed, it gains the normal ability scores of its new
form; ability score increases granted by this ability don't carry over to its new form.

This replaces resist nature's lure.

## Wild Shape (Su) {#wild-shape}

A leshy warden gains this ability at 6th level, except her effective druid level for the ability is
equal to her druid level - 2 for the purpose of determining the number of times per day she can use
it. At 6th level, the leshy warden can assume the form of only Small or Medium plant creatures, as
per _[plant shape I](ref/spell/plant-shape-1)_. At 8th level, she can take the form of a Large plant
creature, as per _[plant shape II](ref/spell/plant-shape-2)_. At 10th level, she can take the form
of a Huge plant creature, as per _[plant shape III](ref/spell/plant-shape-3)_.

This alters wild shape.

## Plant Whisperer (Su) {#plant-whisperer}

At 13th level, a leshy warden's connection to the spirits of nature becomes strong enough that she
can always hear them whispering. She is treated as if constantly under the effects of
_[speak with plants](ref/spell/speak-with-plants)_. Once per day, she can spend 10 minutes in
communion with the spirits to learn the answers to her questions, as
_[commune with nature](ref/spell/commune-with-nature)_.

This replaces a thousand faces.
