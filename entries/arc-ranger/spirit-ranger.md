+++
id = "ref/arc-ranger/spirit-ranger"
kind = "archetype"
title = "Spirit Ranger"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Spirit%20Ranger"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_ranger", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-players-guide"
page = "129"

[fields]
kind = "archetype"
features = [
  { anchor = "spirit-bond", level = 4 },
  { anchor = "wisdom-of-the-spirits", level = 12 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["spirit-bond"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["wisdom-of-the-spirits"] },
]
+++

Some rangers nurture a connection with the spirits that reside in all things. By communing with
these spirits, the spirit ranger can gain glimpses of things to come. A spirit ranger has the
following class features.

## Spirit Bond (Ex) {#spirit-bond}

At 4th level, instead of forming a bond with his hunting companions or an animal companion, the
spirit ranger forms a bond with the spirits of nature themselves. Each day, as long as he is within
one of his favored terrains, the ranger can cast _[augury](ref/spell/augury)_ as a
[spell-like ability](ref/umr/spell-like-abilities) with a caster level equal to his ranger level. In
addition, he can call upon these spirits to cast any one ranger spell that he is capable of casting,
without having to prepare the spell. At 8th level, and every four levels thereafter, he can cast an
additional spell in this way. This replaces hunter's bond.

## Wisdom of the Spirits (Sp) {#wisdom-of-the-spirits}

At 12th level, the spirit ranger can use his _[augury](ref/spell/augury)_
[spell-like ability](ref/umr/spell-like-abilities) even when he is not in one of his favored
terrains. If he is within one of his favored terrains, the ranger can cast
_[divination](ref/spell/divination)_ instead. Like _[augury](ref/spell/augury)_, the caster level of
the _divination_ is equal to the ranger's level. This ability replaces camouflage.
