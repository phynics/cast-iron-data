+++
id = "ref/arc-spiritualist/totem-spiritualist"
kind = "archetype"
title = "Totem Spiritualist"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Totem%20Spiritualist"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "totem_spiritualist", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "psychic-anthology"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "phantom-animal", level = 1 },
  { anchor = "shared-instincts", level = 1 },
  { anchor = "special" },
  { anchor = "animal-senses", level = 9 },
  { anchor = "twin-phantoms", level = 17 },
]
trades = [
  { replaces = "Phantom", feature = "phantom", by = ["phantom-animal"] },
  { replaces = "See invisibility", feature = "see-invisibility", by = ["animal-senses"] },
  { replaces = "Dual bond", feature = "dual-bond", by = ["twin-phantoms"] },
  { alters = "Shared consciousness", feature = "shared-consciousness", by = ["shared-instincts"] },
]
+++

The god callers of Sarkoris had numerous traditions mixing naturalism with the arcane and occult
arts. One of the few traditions to survive to the present day is that of the totem spiritualists.
These specialized spiritualists call upon phantoms that are manifestations of animals and
personifications of nature.

## Phantom Animal {#phantom-animal}

A totem spiritualist calls upon spirits of nature known as phantom animals to assist her in her
journeys. A phantom animal functions like an [animal companion](ref/sidekick/animal-companion)
except as noted in the descriptions below.

A totem spiritualist begins play with a phantom animal. The phantom animal uses the statistics of an
animal companion and follows the standard animal companion progression in regard to Hit Dice, base
attack bonus, saving throws, skills, feats, natural armor bonus, Strength and Dexterity bonuses, and
[bonus tricks](ref/ability/animal-tricks), but not its special abilities. A phantom animal instead
gains the special abilities of [a standard phantom](ref/sidekick/phantom) listed in the table on
page 77 of _Occult Adventures_. A phantom animal is capable of becoming harbored in the
spiritualist's consciousness or becoming fully or partially manifested. A phantom animal is
otherwise considered a phantom for the purposes of all feats and abilities.

At 7th level and every 5 spiritualist levels thereafter, the totem spiritualist can choose to gain
an additional phantom animal. This additional phantom animal uses the appropriate statistics for a
phantom animal of its level. A totem spiritualist can have only one active phantom animal at a time.
Dismissing an active phantom animal to call another requires a ritual that takes 1 minute to
perform.

Instead of gaining an additional phantom animal, the totem spiritualist can choose to empower a
phantom animal with which she is already bonded. The first time the phantom animal is empowered, it
gains two bonus tricks. The second time it is empowered, the phantom animal gains the
[hunter](ref/class/hunter)'s [animal focus](ref/ability/animal-foci) class ability, treating the
totem spiritualist's spiritualist level as her effective hunter level. The third time it is
empowered, the damage dice of the phantom animal's natural attacks increase
[by one step](ref/misc/damage-die-adjustments).

A totem spiritualist can release a phantom animal from her service much like a
[druid](ref/class/druid) releases an animal companion. If a totem spiritualist releases a phantom
animal from service, she can gain a new one by performing a ritual requiring 24 uninterrupted hours
of meditation in an environment where the animal that the phantom resembles typically lives.

A totem spiritualist treats any druid levels she has as effective spiritualist levels to determine
the abilities of her phantom animals, but does not treat her spiritualist levels as effective druid
levels to determine the abilities of animal companions.

This ability replaces phantom.

## Shared Instincts (Su) {#shared-instincts}

A totem spiritualist doesn't gain Skill Focus feats while a phantom animal is confined in her
consciousness. She instead gains a number of bonus ranks in Knowledge (nature) equal to the phantom
animal's Hit Dice.

This ability alters shared consciousness.

## Special {#special}

Alertness, phantom touch, telepathy, weapon of the mind Quick manifest Ectoplasmic pool Reshape
Phantom tether — Quick reshape — Etheric strikes Soul eater

## Animal Senses (Su) {#animal-senses}

At 9th level, a totem spiritualist shares her phantom animal's senses. If her phantom animal has any
of the following abilities, she gains them whenever the phantom animal is harbored in her
consciousness: [blindsense](ref/umr/blindsense), [darkvision](ref/rule/darkvision),
[low-light vision](ref/rule/low-light-vision), and [scent](ref/umr/scent).

This ability replaces _see invisibility_.

## Twin Phantoms (Su) {#twin-phantoms}

At 17th level, the totem spiritualist can call upon two of her phantom animals at once. As a
standard action, she can manifest a second phantom animal. The phantom animal remains for a number
of rounds per day equal to her spiritualist level and can be dismissed as a free action. This
duration does not need to be consecutive.

This replaces dual bond.
