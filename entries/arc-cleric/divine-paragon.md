+++
id = "ref/arc-cleric/divine-paragon"
kind = "archetype"
title = "Divine Paragon"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Divine%20Paragon"
source_ids = ["divine-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_paragon", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "divine-anthology"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "devoted-domain", level = 1 },
  { anchor = "divine-brand", level = 1 },
]
trades = [
  { alters = "Domains", feature = "domains", by = ["devoted-domain"] },
  { alters = "Aura", feature = "aura", by = ["divine-brand"] },
]
+++

Divine paragons strive to emulate their god's ideals as closely as possible. They might see
themselves as an incarnation of their deity in the flesh, or they could simply seek to embody the
physical and spiritual ideals set forth by their deity. Many divine paragons go as far as to alter
their appearance, as best as possible, to look similar to their chosen deity, but such a level of
devotion is not required by the archetype.

## Obedient Archetypes {#obedient-archetypes}

The following archetypes are often taken by those who have studied from _Meditations and
Revelations_ and taken its message to heart. Both archetypes require the character to perform
regular obediences to her chosen deity, just as one must to gain the benefits of the Divine
Obedience feat. These obediences are identical to those required by Divine Obedience—for religions
that do not have official obediences printed, you can either work with your GM to create appropriate
obediences or simply assume that the obedience in question is something relatively minor that your
character can take care of during your spell preparation ritual. Failure to follow this daily
obedience causes you to lose all of the abilities granted by your chosen archetype. In this event,
you do not regain the abilities you altered or replaced via the archetype—you simply lose access to
that element of power granted until you next perform the obedience.

## Devoted Domain {#devoted-domain}

A divine paragon is intensely devoted to a single deity, and her alignment must be identical to her
deity's alignment. She gains [Deific Obedience](ref/feat/deific-obedience) as a bonus feat, even if
she doesn't meet the feat's prerequisites. She gains access to her boons at an accelerated rate (see
below) rather than the standard HD-based rate granted by Deific Obedience (and as such cannot
benefit from the accelerated rate granted by the [Diverse Obedience](ref/feat/diverse-obedience)
feat).

When the divine paragon selects her domains, she must designate one of the two domains she gains as
her devoted domain. She gains all of this domain's granted powers and domain spells normally. For
her other domain, she gains only its domain spells—she does not gain any of the granted powers of
that domain. Instead, she must choose from the evangelist, exalted, or sentinel boons granted by her
deity (as detailed in _Pathfinder Campaign Setting: Inner Sea Gods_). At 5th level, she gains access
to the first boon granted by her deity. At 11th level, she gains access to the second boon. At 14th
level, she gains access to the third boon.

In order to retain access to her domain spells, the domain powers of her devoted domain, and the
boons granted by Deific Obedience, the divine paragon must perform her obedience daily. If she fails
to do so, she loses access to these abilities until she next performs her obedience (but she can
still cast spells, channel energy, and perform other abilities granted by her cleric levels).

This ability alters domains.

## Divine Brand (Ex) {#divine-brand}

At 1st level, a mark appears somewhere on the divine paragon's body. The mark's location varies by
individual and faith, but takes the form of the deity's holy symbol and generally appears in a
location easy to display, such as on the hand, forearm, chest, or face. An uncovered divine brand
functions as a holy (or unholy) symbol and as a divine focus for spellcasting. The divine paragon's
aura is even more powerful than a typical cleric's as a result of her devotion, and her cleric level
is treated as 1 higher for the purpose of determining the strength of her aura when it is viewed by
spells like _[detect good](ref/spell/detect-good)_.

This ability alters aura.
