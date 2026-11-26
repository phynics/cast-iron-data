+++
id = "ref/arc-medium/outer-channeler"
kind = "archetype"
title = "Outer Channeler"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Outer%20Channeler"
source_ids = ["psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "outer_channeler", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "psychic-anthology"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "outsider-invocation", level = 1 },
  { anchor = "taboo" },
  { anchor = "shared-seance" },
  { anchor = "servitor", level = 3 },
  { anchor = "site-channeling", level = 5 },
  { anchor = "ask-the-planes", level = 14 },
]
trades = [
  { replaces = "Haunt channeler", feature = "haunt-channeler", by = ["servitor"] },
  { replaces = "connection channel", feature = "connection-channel", by = ["servitor"] },
  { replaces = "Location channel", feature = "location-channel", by = ["site-channeling"] },
  { replaces = "Astral journey", feature = "astral-journey", by = ["ask-the-planes"] },
  { alters = "Spirit", feature = "spirit", by = ["outsider-invocation"] },
  { alters = "spirit power (intermediate)", by = ["outsider-invocation"] },
  { alters = "Taboo", feature = "taboo", by = ["taboo"] },
  { alters = "Shared seance", feature = "shared-seance", by = ["shared-seance"] },
  { alters = "Ask the spirits", feature = "ask-the-spirits", by = ["ask-the-planes"] },
]
+++

Rather than invite strange entities and departed souls into their bodies, outer channelers invite
extraplanar entities to inhabit them, allowing the likes of angels and demons to use them as vessels
in exchange for power. However, this bond always comes with a cost.

## Outsider Invocation (Su) {#outsider-invocation}

At 1st level, an outer channeler chooses one outsider subtype from among those listed in the
Outsider Spirits section on pages 13–15. His alignment must be within one step of the outsider's
alignment in order to choose it, and once chosen it cannot be changed. Instead of channeling
spirits, an outer channeler invokes outsiders of his chosen subtype during his seance.

Each subtype lists six outsiders that, when invoked, provide the outer channeler with the same
benefits as the outsider's associated spirit. For example, an outer channeler with
[angel](ref/spirit/angel) as his chosen subtype can invoke the astral deva, balisse, empyrean,
movanic deva, planetar, and solar outsiders, which function like the trickster, hierophant,
archmage, champion, marshal, and guardian spirits, respectively.

An outer channeler doesn't gain the intermediate power normally granted by his invoked outsider's
associated spirit. Instead, he gains the intermediate power noted in his invoked outsider's subtype,
regardless of which spirit that invoked outsider is associated with. Furthermore, the outer
channeler gains a gift at 13th level, as noted in his invoked outsider subtype.

An invoked outsider acts as a spirit for all other effects, including the trance of three and astral
beacon class features.

This ability alters spirit and spirit power (intermediate).

## Taboo (Ex) {#taboo}

Whenever he invokes an outsider, an outer channeler must accept one taboo from among those listed by
his chosen outsider's subtype before the outsider will enter his body. Accepting this taboo provides
the outer channeler with no benefits other than those gained from channeling a spirit; if he wishes
to gain additional uses of his spirit purge ability as described by the taboo class feature, he must
accept a second taboo from among those listed by the legend that his chosen outsider subtype
functions as. If the outer channeler breaks this mandatory taboo, the outsider immediately leaves
and the outer channeler can't invoke a new outsider until he atones (as per
_[atonement](ref/spell/atonement)_).

This ability alters taboo.

## Shared Seance (Su) {#shared-seance}

An outer channeler's ally cannot gain the seance boon from an outer channeler's outsider spirit if
that ally's alignment is more than one step away from the outsider's alignment.

This ability alters shared seance.

## Servitor (Ex) {#servitor}

At 3rd level, an outer channeler can summon the spirit of an outsider of his chosen subtype and
house it within the body of an ordinary animal. Initially, the outsider takes the form of this
animal and acts in all ways as an ordinary [familiar](ref/sidekick/familiar) of that type. At 7th
level, the animal transforms into an outsider, taking the form of an
[improved familiar](ref/ability/improved-familiars) with the outer channeler's chosen outsider
subtype (such as a [cassisian](ref/monster/angel-cassisian) for an angel-invoking medium). The outer
channeler doesn't need to meet the prerequisites to gain this
[improved familiar](ref/ability/improved-familiars), and the improved familiar gains the ability to
[change shape](ref/carried/bestiary/rules/universal-monster-rules/change-shape) between its outsider
form and its animal form at will (as per _[beast shape II](ref/spell/beast-shape-2)_).

This ability replaces a medium's haunt channeler and connection channel.

## Site Channeling (Su) {#site-channeling}

At 5th level, an outer channeler can invoke outsiders from any site tied to any of the following:
creatures of his chosen subtype, deities that grant his chosen subtype as a cleric subdomain, or
planes that creatures of his chosen subtype are native to. This is in addition to the usual list of
sites from which he can channel his outsiders.

This ability replaces location channel.

## Ask the Planes (Sp) {#ask-the-planes}

At 14th level, an outer channeler gains the ask the spirits ability of the standard medium, except
he sends his consciousness to a native plane of his chosen outsider subtype
([Heaven](ref/rule/heaven) for archons, [Hell](ref/rule/hell) for devils, any good-aligned plane for
angels, and so on).

This ability alters ask the spirits and replaces astral journey.
