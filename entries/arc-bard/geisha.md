+++
id = "ref/arc-bard/geisha"
kind = "archetype"
title = "Geisha"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Geisha"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "geisha", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "ultimate-magic"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "tea-ceremony" },
  { anchor = "geisha-knowledge" },
  { anchor = "scribe-scroll" },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["geisha-knowledge"] },
  { replaces = "Armor and weapon proficiencies", feature = "weapon-and-armor-proficiencies" },
]
+++

In some cultures, the professional entertainer is a prestigious role. Specially trained entertainers
called geisha are praised for their appearance and skill at conversation, music, dancing, singing,
poetry, and calligraphy. A geisha provides social intimacy and status but not physical intimacy.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Geisha are proficient in all simple weapons and one [monk](ref/class/monk) weapon. Geisha are not
proficient in any armor or shield; unlike bards, geisha are subject to arcane spell failure even
when casting in light armor or when using a shield. This replaces the normal bard armor and weapon
proficiencies.

## Tea Ceremony (Su) {#tea-ceremony}

By spending 10 minutes preparing an elaborate tea ceremony, a geisha may affect her allies with
inspire courage, inspire competence, inspire greatness, or inspire heroics. The ceremony's effects
last 10 minutes. The geisha must spend 4 rounds of bardic performance for each creature to be
affected.

## Geisha Knowledge {#geisha-knowledge}

A geisha adds [half](ref/misc/fractions-and-rounding) her class level (minimum 1) on Craft
(calligraphy) checks, Diplomacy checks, Knowledge (nobility) checks, and one type of Perform check
(act, dance, oratory, percussion, string instruments, or sing); she may make checks with these
skills untrained. This replaces bardic knowledge.

## Scribe Scroll {#scribe-scroll}

A geisha gains [Scribe Scroll](ref/feat/scribe-scroll) as a bonus feat.
