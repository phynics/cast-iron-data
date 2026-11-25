+++
id = "ref/arc-summoner/shadow-caller"
kind = "archetype"
title = "Shadow Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Shadow%20Caller"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_caller", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "advanced-race-guide"
page = "110"

[fields]
kind = "archetype"
features = [
  { anchor = "shadow-summoning" },
  { anchor = "shadow-eidolon" },
  { anchor = "shadow-blend" },
  { anchor = "shadow-form" },
]
trades = [
  { replaces = "Magical symbol that identifies the summoner and his eidolon", by = ["shadow-eidolon"] },
  { alters = "Eidolon", feature = "eidolon", by = ["shadow-eidolon"] },
  { replaces = "Summon monster spell-like abilities", feature = "summon-monster-i", by = ["shadow-summoning"] },
]
+++

While most summoners can call any manner of creature from across the planes to serve them in combat,
supplementing the skills of their eidolon with a diverse range of creatures, others eschew this
broad utility and instead concentrate upon calling forth entities from the
[Shadow Plane](ref/rule/shadow-plane). A [shadow](ref/template/shadow) caller has the following
class features.

## Class Skills {#class-skills}

The shadow caller adds Stealth to his list of class skills and removes Use Magic Device from his
list of class skills.

## Shadow Summoning (Sp) {#shadow-summoning}

When a shadow caller uses his _summon monster_ ability or casts the _summon monster_ spell, he
typically summons creatures from the Shadow Plane or creatures closely associated with shadow. When
a creature on the _summon monster_ spell list indicates that it is summoned with either the
celestial or the fiendish template based on the alignment of the caster, the creature summoned by
the shadow caller has the shadow creature template instead (see sidebar). Furthermore, the _summon
monster_ lists are modified in the following ways (these changes also apply to using a higher-level
summon spell to summon multiple creatures from a lower-level list).

_Summon Monster I_: No changes.

_Summon Monster II_: A shadow caller cannot summon Small elementals or lemures, but instead can
summon zoogs.

_Summon Monster III_: A shadow caller cannot summon dretches or lantern archons, but can summon
augur kytons.

_Summon Monster IV_: A shadow caller cannot summon Medium elementals, hell hounds, hound archons, or
mephits, but can summon allips, gloomwings, and shadows.

_Summon Monster V_: A shadow caller cannot summon babau, bearded devils, bralani azatas, Large
elementals, salamanders, or xills, but can summon shadow mastiffs and shae.

_Summon Monster VI_: A shadow caller cannot summon Huge elementals, erinyes, lillend azatas, or
succubi, but can summon cloakers.

_Summon Monster VII_: A shadow caller cannot summon bebiliths, bone devils, greater elementals, or
vrocks, but can summon greater shadows.

_Summon Monster VIII_: A shadow caller can only summon derghodaemons and young umbral dragons.

_Summon Monster IX_: A shadow caller can only summon interlocutor kytons and nightwings.

This ability otherwise functions as and replaces the summoner's normal _summon monster_ spell-like
abilities.

## Shadow Eidolon {#shadow-eidolon}

A shadow caller's eidolon is at once a thing of shadow called from the deep of the Shadow Plane and
his own shadow; the two are inseparable. When his eidolon manifests, his shadow lengthens and
finally detaches from him as a creature unto itself. For as long as the shadow caller's eidolon is
manifested, he and the eidolon do not have distinct shadows, regardless of the presence or absence
of light. This lack of a shadow replaces the magical symbol that identifies the summoner and his
eidolon.

This ability alters the summoner's eidolon ability. The following evolutions are available to all
summoners. 2-Point Evolutions

## Shadow Blend (Su) {#shadow-blend}

In any condition of illumination other than bright light, the eidolon disappears into the shadows,
giving it concealment (20% miss chance). If it has the shadow form evolution, it instead gains total
concealment (50% miss chance). The eidolon can suspend or resume this ability as a free action.

## Shadow Form (Su) {#shadow-form}

The eidolon's body becomes shadowy and more indistinct. This shadow form grants the eidolon constant
concealment (20% miss chance), and its melee attacks affect incorporeal creatures as if it had the
_ghost touch_ weapon property. The eidolon's melee attacks deal only half damage to corporeal
creatures.
