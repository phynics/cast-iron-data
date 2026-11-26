+++
id = "ref/arc-spiritualist/usher-of-lost-souls"
kind = "archetype"
title = "Usher of Lost Souls"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Usher%20of%20Lost%20Souls"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "usher_of_lost_souls", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "psychic-anthology"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "etheric-channel" },
  { anchor = "spirit-senses", level = 2 },
  { anchor = "disrupting-phantom" },
  { anchor = "locate-haunts", level = 9 },
  { anchor = "disruptive-influence", level = 14 },
]
trades = [
  { replaces = "Bonded senses", feature = "bonded-senses", by = ["spirit-senses"] },
  { replaces = "Spiritual interference", feature = "spiritual-interference", by = ["disrupting-phantom"] },
  { replaces = "greater spiritual interference", feature = "greater-spiritual-interference", by = ["disrupting-phantom"] },
  { replaces = "See invisibility", feature = "see-invisibility", by = ["locate-haunts"] },
  { replaces = "Spiritual bond", feature = "spiritual-bond", by = ["disruptive-influence"] },
]
+++

Ushers of lost souls are spiritualists who focus on bringing the souls of the dead to their final
judgments at the end of the River of Souls. To this end, they specialize in destroying undead and in
laying haunts to rest. Skeptics who point out the apparent contradiction that ushers of lost souls
use phantoms to aid them are quickly told that their ectoplasmic allies hail from the Ethereal Plane
and are not actually undead. Ushers of lost souls are common among the clergy of Pharasma and are
seen throughout the Inner Sea region.

## Etheric Channel (Su) {#etheric-channel}

An usher of lost souls can focus ethereal energies to channel waves of disruption. The spiritualist
can [channel positive energy](ref/ability/channel-energy) a number of times per day equal to 3 + her
Charisma modifier (minimum 1). She channels energy like a cleric of her spiritualist level, except
the channeled energy can be used only to harm undead or haunts. This otherwise functions as channel
energy for the purposes of feats and abilities. The spiritualist does not require a holy symbol to
use this ability.

## Spirit Senses (Ex) {#spirit-senses}

At 2nd level, an usher of lost souls gains a bonus equal to [half](ref/misc/fractions-and-rounding)
her spiritualist level on Perception checks to detect haunts and incorporeal creatures and on Sense
Motive checks to determine whether a creature is possessed, under the effects of an enchantment or
curse, or otherwise magically controlled.

This ability replaces bonded senses.

## Disrupting Phantom (Ex) {#disrupting-phantom}

When an usher of lost souls reaches 4th level, her phantom gains the ability to directly harm
haunts. The phantom can make an attack while within a haunt's area against an AC equal to 10 + the
haunt's caster level. On a hit, the phantom deals its slam damage to the haunt; the haunt is immune
to critical hits from the phantom. When an usher of lost souls reaches 12th level, her phantom can
deal critical hits to a haunt, and the critical threat range for its slam attacks against haunts
increases to 19–20.

This ability replaces spiritual interference and greater spiritual interference.

## Locate Haunts (Su) {#locate-haunts}

At 9th level, an usher of lost souls can locate inactive haunts. As a standard action, she can
enhance her vision to detect haunts within 60 feet of her. A haunt's area glows with a bright light
for an untriggered haunt or dim light for a haunt that is waiting to reset. She can use this ability
for 10 minutes per day per spiritualist level. This duration doesn't need to be consecutive, but it
must be spent in 10-minute increments.

This ability replaces _see invisibility_.

## Disruptive Influence (Su) {#disruptive-influence}

At 14th level, the usher of lost souls can put spirits to rest. She can use one of her uses of
_[calm spirit](ref/spell/calm-spirit)_ to instead cast _[purge spirit](ref/spell/purge-spirit)_ as a
[spell-like ability](ref/umr/spell-like-abilities). She can expend two uses of her etheric channel
to cast either of these spells as a spell-like ability.

This ability replaces spiritual bond.
