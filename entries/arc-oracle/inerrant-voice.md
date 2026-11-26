+++
id = "ref/arc-oracle/inerrant-voice"
kind = "archetype"
title = "Inerrant Voice"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Inerrant%20Voice"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inerrant_voice", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "revelations" },
  { anchor = "vigilant-protector" },
]
trades = [
  { replaces = "Bonus spells at those levels gained from the oracle's mystery", feature = "mystery", levels = [2, 4, 8, 14], power = "bonus spells" },
]
+++

An inerrant voice serves as a spiritual advisor to either a monarch or noble. Most Qadiran nobles
retain one's services, for both guidance and protection.

## Recommended Mysteries {#recommended-mysteries}

Ancestor, intrigue, life, lore.

## Bonus Spells {#bonus-spells}

An inerrant voice gains the following bonus spells: _shield other_ (2nd), _augury_ (4th),
_divination_ (8th), _vision_ (14th).

These replace the bonus spells at those levels gained from the oracle's mystery.

## Revelations {#revelations}

An inerrant voice must take the following revelation at 3rd level.

## Vigilant Protector (Su) {#vigilant-protector}

Each day when you recover your spells, you can select a specific person you know other than yourself
as your ward. When your ward becomes the target of an attack or spell and you are aware of the
attack, you can cast an abjuration spell you know on the ally as an immediate action. You must
expend the appropriate spell slot and be able to target the ally as normal for the spell. At 11th
level, as an immediate action when you know your ward is targeted, you can transpose yourself with
your ward, teleporting into the original target's square (and becoming the new target of the attack
or spell) while your ally is teleported into yours; this is a teleportation effect that doesn't
provoke attacks of opportunity. You can use this revelation once per day, plus an additional time at
7th level and every 4 oracle levels thereafter.
