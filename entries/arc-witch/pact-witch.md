+++
id = "ref/arc-witch/pact-witch"
kind = "archetype"
title = "Pact Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Pact%20Witch"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pact_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "planar-adventures"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "planar-pact" },
  { anchor = "planar-familiar" },
]
trades = [
  { replaces = "Patron", feature = "patron-spells", power = "patron", by = ["planar-pact"] },
  { replaces = "Hex normally gained at 6th level", feature = "hex", levels = [6], by = ["planar-familiar"] },
  { alters = "Familiar", feature = "witch-s-familiar", by = ["planar-familiar"] },
]
+++

Though all witches forge bonds with mysterious powers known as patrons, a pact witch takes this bond
to an extreme by forging an inexorable pact with the Outer Planes.

## Alignment {#alignment}

A pact witch's alignment must match that of his chosen plane. A pact witch whose alignment no longer
matches his bonded plane becomes an ex–pact witch and loses all the benefits of this archetype until
he atones for his transgressions. In time, likely after benefitting from an
_[atonement](ref/spell/atonement)_ spell, an ex–pact witch can forge a bond with another plane that
matches his new alignment.

**Table 1–1: Planar Pacts**

|Plane|Alignment|Familiar|
| --- | --- | --- |
|Abaddon|Neutral evil|[Cacodaemon](ref/monster/daemon-cacodaemon) or [doru](ref/monster/div-doru)|
|Abyss|Chaotic evil|[Cythnigot](ref/monster/qlippoth-cythnigot) or [quasit](ref/monster/demon-quasit)|
|Axis|Lawful neutral|[Arbiter](ref/monster/inevitable-arbiter)|
|Boneyard|Neutral|[Nosoi](ref/monster/psychopomp-nosoi)|
|Elysium|Chaotic good|CG [cassisian](ref/monster/angel-cassisian) or [lyrakien](ref/monster/azata-lyrakien)|
|Heaven|Lawful good|LG [cassisian](ref/monster/angel-cassisian) or [harbinger archon](ref/monster/archon-harbinger-archon)|
|Hell|Lawful evil|[Imp](ref/monster/devil-imp) or [tripurasura](ref/monster/asura-tripurasura)|
|Maelstrom|Chaotic neutral|[Voidworm](ref/monster/protean-voidworm)|
|Nirvana|Neutral good|NG cassisian or [silvanshee](ref/monster/agathion-silvanshee)|

## Planar Pact (Su) {#planar-pact}

A pact witch chooses one Outer Plane with which to forge a pact. This plane determines the alignment
a pact witch must maintain and the type of improved familiar he gains at 6th level. Many pact
witches worship specific deities or demigods native to the planes with which they forged their
pacts. When a pact witch chooses his plane, his body transforms in minor, cosmetic ways associated
with that plane. A pact with Hell might give a pact witch small devil horns, while a pact with the
Heaven might cause a pact witch to have a softly glowing golden halo, and a pact with Axis might
give a pact witch's skin strange rune patterns. The nature of this cosmetic change varies from witch
to witch, but has no mechanical effect. Instead of learning new spells from a patron, a pact witch
learns new spells from his planar pact, starting at 2nd level and again every 2 levels thereafter.

_2nd Level: Protection from chaos/evil/good/law_ (choose one appropriate to your plane)

_4th Level: Time shudder_.

_6th Level: Infuse self_ (page 41).

_8th Level: Lesser planar ally._

_10th Level: Plane shift_ (as a 5th level spell).

_12th Level: Planar ally._

_14th Level: Banishment._

_16th Level: Greater planar ally._

_18th Level: Gate._

This replaces patron.

## Planar Familiar {#planar-familiar}

When a pact witch reaches 6th level, his familiar turns into an outsider native to his chosen plane.
The familiar retains its spells known; its memories; and its Intelligence, Wisdom, and Charisma
scores, but is treated as a member of its new race in all other respects. The type of creature the
familiar becomes is indicated above on Table 1–1: Planar Pacts; if more than one type of familiar is
listed, a pact witch can choose which type his familiar becomes.

This alters the witch's familiar and replaces the hex normally gained at 6th level.
