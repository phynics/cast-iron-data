+++
id = "ref/arc-bard/studious-librarian"
kind = "archetype"
title = "Studious Librarian"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Studious%20Librarian"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "studious_librarian", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "46"

[fields]
kind = "archetype"
features = [
  { anchor = "scribe-scroll", level = 1 },
  { anchor = "comparative-arcane-studies", level = 6 },
  { anchor = "critical-research-focus", level = 8 },
  { anchor = "perfect-recollection", level = 19 },
  { anchor = "one-with-the-library", level = 20 },
]
trades = [
  { replaces = "Distraction", feature = "bardic-performance", power = "distraction", by = ["scribe-scroll"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["comparative-arcane-studies"] },
  { replaces = "jack-of-all-trades", feature = "jack-of-all-trades", by = ["comparative-arcane-studies"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["critical-research-focus"] },
  { replaces = "Mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["perfect-recollection"] },
  { replaces = "Deadly performance", feature = "bardic-performance", power = "deadly performance", by = ["one-with-the-library"] },
]
+++

Studious librarians are bards that have studied long in great libraries of the Inner Sea region,
such as Taldor's [Kitharodian Academy](ref/rule/f-bards) in Oppara, Forae Logos and the
[Pathfinder Society's](ref/rule/aff-scholars) Skyreach in Absalom, and the Grand Library of Eto in
Osirion.

## Scribe Scroll {#scribe-scroll}

A studious librarian gains [Scribe Scroll](ref/feat/scribe-scroll) as a bonus feat.

This ability replaces distraction.

## Comparative Arcane Studies (Su) {#comparative-arcane-studies}

At 6th level, the studious librarian is exposed to a wide variety of magical writing, and can use
his own magic to duplicate spells from other classes' spell lists. Once per day, a studious
librarian can cast any spell from the bard, sorcerer/wizard, or witch spell lists from a scroll or
spellbook in hand as if it were one of his bard spells known, expending a bard spell slot of the
same spell level to cast the desired spell. Casting a spell from a scroll this way does not cause
the spell to vanish from the scroll. A spell cast in this way cannot be modified by metamagic. The
studious librarian gains one additional daily use of this ability at 10th level and again every 4
bard levels thereafter, to a maximum of four times per day at 18th level.

This ability replaces _suggestion_ and jack-of-all-trades.

## Critical Research Focus (Ex) {#critical-research-focus}

At 8th level, the studious librarian threatens a critical hit on
[a Research check](ref/rule/research) with a roll of 18, 19, or 20. He gains a +4 bonus on Research
checks to confirm a critical hit.

This ability replaces dirge of doom.

## Perfect Recollection (Ex) {#perfect-recollection}

At 19th level, the studious librarian can always take 20 on Knowledge checks.

This ability replaces _mass suggestion_.

## One with the Library (Ex) {#one-with-the-library}

At 20th level, the studious librarian can replace one of her spells known with any bard spell from a
scroll once per day by studying the scroll for 1 hour. Doing so erases the spell from the scroll.

This ability replaces deadly performance.
