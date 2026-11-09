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
replaces = ["Haunt channeler", "connection channel", "Location channel", "Astral journey"]
alters = ["Spirit", "spirit power (intermediate)", "Taboo", "Shared seance", "Ask the spirits"]
+++

Rather than invite strange entities and departed souls into their bodies, outer channelers invite
extraplanar entities to inhabit them, allowing the likes of angels and demons to use them as vessels
in exchange for power. However, this bond always comes with a cost.

**Outsider Invocation (Su)**

**Action:** Ability

**Alters:** Spirit, spirit power (intermediate)

**Gained:** At 1st Level

**Special:** An invoked outsider acts as a spirit for all other effects, including the _trance of
three_ and _astral beacon_ class features.

An outer channeler chooses one outsider subtype from among those listed below. His alignment must be
within one step of the outsider's alignment in order to choose it, and once chosen it cannot be
changed. Instead of channeling spirits, an outer channeler invokes outsiders of his chosen subtype
during his _seance._

An outer channeler can invoke creatures from the following outsider subtypes:
[aeon](ref/spirit/aeon), [agathion](ref/spirit/agathion), [angel](ref/spirit/angel),
[archon](ref/spirit/archon), [azata](ref/spirit/azata), [daemon](ref/spirit/daemon),
[demon](ref/spirit/demon), [devil](ref/spirit/devil), and [psychopomp](ref/spirit/psychopomp). The
outsiders associated with each spirit provide no mechanical benefit and are merely suggestions based
on the themes and interests of each creature. At the GM's discretion, he can swap which outsiders
are associated with each spirit and can even use outsiders of the indicated subtype that aren't
listed, though outsiders capable of serving as an
[improved familiar](ref/ability/improved-familiars) and outsiders of CR 20 or higher typically do
not answer an outer channeler's calls.

Each subtype lists six outsiders that, when invoked, provide the outer channeler with the same
benefits as the outsider's associated spirit. For example, an outer channeler with angel as his
chosen subtype can invoke the astral deva, balisse, empyrean, movanic deva, planetar, and solar
outsiders, which function like the trickster, hierophant, archmage, champion, marshal, and guardian
spirits, respectively.

An outer channeler doesn't gain the intermediate power normally granted by his invoked outsider's
associated spirit. Instead, he gains the intermediate power noted in his invoked outsider's subtype,
regardless of which spirit that invoked outsider is associated with. Furthermore, the outer
channeler gains a gift at 13th level, as noted in his invoked outsider subtype.

**Taboo (Ex)**

**Ability:** Whenever he invokes an outsider, an outer channeler must accept one _taboo_ from among
those listed by his chosen outsider's subtype before the outsider will enter his body. Accepting
this _taboo_ provides the outer channeler with no benefits other than those gained from channeling a
spirit; if he wishes to gain additional uses of his _spirit purge_ ability as described by the
_taboo_ class feature, he must accept a second _taboo_ from among those listed by the legend that
his chosen outsider subtype functions as. If the outer channeler breaks this mandatory _taboo,_ the
outsider immediately leaves and the outer channeler can't invoke a new outsider until he atones (as
per [atonement](ref/spell/atonement)).

**Alters:** Taboo

**Shared Seance (Su)**

**Alters:** Shared seance

**Info:** An outer channeler's ally cannot gain the _seance_ boon from an outer channeler's outsider
spirit if that ally's alignment is more than one step away from the outsider's alignment.

**Servitor (Ex)**

**Ability:** An outer channeler can summon the spirit of an outsider of his chosen subtype and house
it within the body of an ordinary animal. The outsider takes the form of this animal and acts in all
ways as an ordinary [familiar](ref/sidekick/familiar) of that type.

**At 7th Level:** The animal transforms into an outsider, taking the form of an
[improved familiar](ref/ability/improved-familiars) with the outer channeler's chosen outsider
subtype (such as a [cassisian](ref/monster/angel-cassisian) for an angel-invoking medium). The outer
channeler doesn't need to meet the prerequisites to gain this improved familiar, and the improved
familiar gains the ability to
_[change shape](ref/carried/bestiary/rules/universal-monster-rules/change-shape)_ between its
outsider form and its animal form at will (as per [beast shape II](ref/spell/beast-shape-2)).

**Gained:** At 3rd Level

**Replaces:** Haunt channeler, connection channel

**Site Channeling (Su)**

**Info:** An outer channeler can invoke outsiders from any site tied to any of the following:
creatures of his chosen subtype, deities that grant his chosen subtype as a cleric subdomain, or
planes that creatures of his chosen subtype are native to. This is in addition to the usual list of
sites from which he can channel his outsiders.

**Gained:** At 5th Level

**Replaces:** Location channel

**Ask the Planes (Sp)**

**Ability:** An outer channeler gains the _ask the spirits_ ability of the standard medium, except
he sends his consciousness to a native plane of his chosen outsider subtype
([Heaven](ref/rule/heaven) for archons, [Hell](ref/rule/hell) for devils, any good-aligned plane for
angels, and so on).

**Alters:** Ask the spirits

**Gained:** At 14th Level

**Replaces:** Astral journey
