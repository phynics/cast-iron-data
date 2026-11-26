+++
id = "ref/arc-druid/planar-extremist"
kind = "archetype"
title = "Planar Extremist"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Planar%20Extremist"
source_ids = ["antiheros-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_extremist", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "antiheros-handbook"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "aura" },
  { anchor = "spells", level = 1 },
  { anchor = "planar-bond", level = 1 },
  { anchor = "spontaneous-casting", level = 1 },
  { anchor = "resist-the-opposite", level = 4 },
  { anchor = "planar-aspect", level = 4 },
]
trades = [
  { replaces = "Nature's bond", feature = "nature-bond", by = ["planar-bond"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-the-opposite"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["planar-aspect"] },
  { alters = "Spells", feature = "spells", by = ["spells"] },
  { alters = "A druid's spontaneous casting", feature = "spontaneous-casting", by = ["spontaneous-casting"] },
  { alters = "Alignment" },
]
+++

Through determined interest or repeated exposure to those places where the borders between planes
are weaker, some druids lose their neutral stance and find themselves gravitating toward one of the
four most extreme alignments: chaotic evil, chaotic good, lawful evil, or lawful good. While no
longer able to harness the forces of nature like their neutral kin, these planar extremists find
that their powers have shifted to reflect the Outer Plane most closely associated with their
alignment.

This is an ex-class archetype and can be taken by a character immediately upon becoming an ex-druid.

## Alignment {#alignment}

A planar extremist must have an alignment of chaotic evil, chaotic good, lawful evil, or lawful
good.

This alters the druid's alignment.

## Aura (Ex) {#aura}

The planar extremist radiates an aura matching her alignment as if she were a
[cleric](ref/class/cleric) of her druid level.

## Spells {#spells}

A planar extremist gains one fewer spell slot per spell level than normal in which to prepare
spells. The planar extremist removes all _[summon nature's ally](ref/spell/summon-natures-ally)_
spells from her spell list and replaces them with the _[summon monster](ref/spell/summon-monster)_
spells of the same levels. The druid can otherwise cast spells as normal for a druid of her level.

This alters the druid's spells.

## Planar Bond {#planar-bond}

A planar extremist forms a bond with a manifestation of the Outer Plane with which she is aligned.
This bond can take one of two forms. The first is a close tie to the plane to which she is aligned,
granting the planar extremist one of the domains of her alignment (for example, a lawful good planar
extremist could take either the Lawful or Good domain). This option otherwise functions as a druid's
nature bond if she chose a close tie to the natural world.

The second option is to form a close bond with an outsider from an Outer Plane. The abilities of
this outsider companion are determined using the rules for
[eidolons](ref/sidekick/unchained-eidolon) for the
[unchained summoner](ref/class/unchained-summoner) class, as if the planar extremist were a summoner
of her druid level, except the outsider companion gains no additional evolution pool (only the
evolutions from its base form and base evolutions for its subtype), and it must be of a subtype
whose alignment exactly matches the alignment of the planar extremist. The planar extremist can
summon her outsider companion with the same 1-minute ritual a summoner normally uses to do so, but
she can't cast _summon monster_ spells if she currently has her outsider companion summoned, and she
can't summon her companion if she already has a creature summoned through other means.

As the planar ally gains class levels, her eidolon's base statistics and base evolutions increase as
if her druid level were her summoner level. The eidolon gains the darkvision, link, share spells,
evasion, ability score increase, devotion, multiattack, and improved evasion abilities at the
appropriate levels, but never gains an evolution pool. Abilities and spells that grant additional
evolution points to eidolons do not function for her outsider companion, though any abilities that
would grant evolution points to an animal companion do work. The planar extremist does not gain life
link or any other class features a summoner gains in relation to her eidolon.

This replaces nature's bond.

## Spontaneous Casting {#spontaneous-casting}

A planar extremist can channel stored spell energy into summoning spells that she hasn't prepared
ahead of time. She can lose a prepared spell in order to cast a
_[summon monster](ref/spell/summon-monster)_ spell of the same level or lower, but only to summon
creatures whose alignment matches hers.

This alters a druid's spontaneous casting.

## Resist the Opposite (Ex) {#resist-the-opposite}

At 4th level, a planar extremist gains a +2 bonus on saving throws against the spell-like and
supernatural abilities of creatures whose alignment is diametrically opposed to her own.

This replaces resist nature's lure.

## Planar Aspect (Su) {#planar-aspect}

At 4th level, as a standard action, a planar extremist can gain the benefits of the
[bloodrager](ref/class/bloodrager) bloodline associated with her alignment (choosing from
[Abyssal](ref/blrgbloodline/abyssal), [Celestial](ref/blrgbloodline/celestial), or
[Infernal](ref/blrgbloodline/infernal)), as if she were a bloodrager of her druid level. She can
gain these benefits for 1 minute per druid level as if she were bloodraging (but she gains no other
benefits or penalties of bloodrage) or until she dismisses it as a swift action; this duration need
not be used consecutively but must be spent in 1-minute increments. She can use this ability an
additional time per day at 6th level and every 4 levels thereafter, for a total of five times per
day at 18th level. At 20th level, a planar extremist can use planar aspect at will.

This replaces wild shape.
