+++
id = "ref/arc-magus/esoteric"
kind = "archetype"
title = "Esoteric"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Esoteric"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "esoteric", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "occult-adventures"
page = "120"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting" },
  { anchor = "arcane-pool", level = 1 },
  { anchor = "unarmed-strike", level = 1 },
  { anchor = "unarmed-spellstrike", level = 1 },
  { anchor = "ki-arcana", level = 4 },
  { anchor = "tattooed-spell", level = 5 },
  { anchor = "ac-bonus", level = 7 },
  { anchor = "improved-tattooed-spell", level = 11 },
]
trades = [
  { replaces = "Spell recall", feature = "spell-recall", by = ["ki-arcana"] },
  { replaces = "Bonus feats", feature = "bonus-feats", by = ["tattooed-spell"] },
  { replaces = "Medium armor", feature = "medium-armor", by = ["ac-bonus"] },
  { replaces = "heavy armor", feature = "heavy-armor", by = ["ac-bonus"] },
  { replaces = "Improved spell recall", feature = "improved-spell-recall", by = ["improved-tattooed-spell"] },
  { alters = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { alters = "Spellcasting", feature = "spells", by = ["diminished-spellcasting"] },
  { alters = "Arcane pool", feature = "arcane-pool", by = ["arcane-pool"] },
  { alters = "Spellstrike", feature = "spellstrike", by = ["unarmed-spellstrike"] },
]
+++

Esoterics are drawn to the mysticism of the occult and spend their lives delving into forgotten
texts and forbidden tomes. Each esoteric learns to inscribe his spells on his flesh in a complex
series of occult symbols and arcane equations.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

An esoteric is proficient with simple weapons only. This alters the magus's weapon and armor
proficiency.

## Diminished Spellcasting {#diminished-spellcasting}

An esoteric has one fewer spell slot of each level than a regular magus. If this reduces his number
of spell slots of a particular level to zero, he can cast spells of that level only if his
Intelligence allows [bonus spells](ref/rule/determine-bonuses) of that level. This ability alters
the magus's spellcasting.

## Arcane Pool (Su) {#arcane-pool}

At 1st level, an esoteric can use his arcane pool to enhance his unarmed strikes as if they were
manufactured weapons. At 5th level, he can use these bonuses to add any of the following weapon
special abilities to his weapons or unarmed strikes: _[defending](ref/magic-enh/defending)_,
_[flaming](ref/magic-enh/flaming)_, _[flaming burst](ref/magic-enh/flaming-burst)_,
_[frost](ref/magic-enh/frost)_, _[icy burst](ref/magic-enh/icy-burst)_,
_[impact](ref/magic-enh/impact)_, _[shock](ref/magic-enh/shock)_,
_[shocking burst](ref/magic-enh/shocking-burst)_, _[speed](ref/magic-enh/speed)_, or
_[thundering](ref/magic-enh/thundering)_.

This ability alters arcane pool.

## Unarmed Strike {#unarmed-strike}

At 1st level, an esoteric gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a
bonus feat. He also treats his magus levels as [monk](ref/class/monk) levels when determining the
amount of damage he deals with his unarmed strikes.

## Unarmed Spellstrike (Su) {#unarmed-spellstrike}

At 1st level, an esoteric gains the magus spellstrike class feature. However, an esoteric can
deliver spells with spellstrike only with his unarmed strikes. This ability alters spellstrike.

## Ki Arcana (Su) {#ki-arcana}

At 4th level, an esoteric's arcane pool is also considered a ki pool for the purposes of meeting
feat and ability requirements. Points from an esoteric's arcane pool can be used for abilities that
normally require ki. If an esoteric gains a ki pool, he can use points from his arcane pool and ki
pool interchangeably (though not special points such as drunken ki). This ability replaces spell
recall.

## Tattooed Spell (Sp) {#tattooed-spell}

At 5th level and every 6 levels thereafter, an esoteric can permanently tattoo one spell from his
magus spellbook onto his body; the first tattooed spell must be of 2nd level or lower, the second
must be of 4th level or lower, and the last can be of any level. The spell that is tattooed must not
have an expensive material component or a focus. The esoteric can prepare any tattooed spell without
needing his spellbook. Additionally, he can cast each of his tattooed spells as a
[spell-like ability](ref/umr/spell-like-abilities) once per day. When the esoteric uses these
spell-like abilities, the tattoo associated with the spell-like ability glows as
_[light](ref/spell/light)_ for a number of rounds equal to the spell's level. This ability replaces
bonus feats.

## AC Bonus (Ex) {#ac-bonus}

At 7th level when an esoteric wears light or no armor, he gains a +1 dodge bonus to AC and CMD. This
bonus increases by 1 at 13th level. He loses these bonuses while immobilized or helpless, or while
wearing medium or heavy armor, using a shield, or carrying a medium or heavy load. This ability
replaces medium armor and heavy armor.

## Improved Tattooed Spell (Sp) {#improved-tattooed-spell}

At 11th level, an esoteric can use each of his [spell-like abilities](ref/umr/spell-like-abilities)
from tattooed spell one additional time per day. This ability replaces improved spell recall.
