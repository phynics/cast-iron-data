+++
id = "ref/arc-cleric/iron-priest"
kind = "archetype"
title = "Iron Priest"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Iron%20Priest"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iron_priest", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "technology-guide"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "channel-energy", level = 1 },
  { anchor = "spontaneous-casting" },
]
trades = [
  { alters = "Channel energy", feature = "channel-energy", by = ["channel-energy"] },
  { alters = "Casting", feature = "spells", by = ["spontaneous-casting"] },
]
+++

Iron priests preach of the messengers from beyond the stars, envoys of the divine brought to
Golarion in a falling star. Iron priests can affect robots and other unliving constructs with
channeled energy, but lack power over the undead. Appropriate deities for an Iron Priest include
[Brigh](ref/faith/brigh), [Nethys](ref/faith/nethys), [Gorum](ref/faith/gorum), and
[Haagenti](ref/faith/haagenti). An iron priest has the following class features.

## Class Skills {#class-skills}

The iron priest's class skills are Appraise (Int), Craft (Int), Diplomacy (Cha), Disable Device
(Dex), Heal (Wis), Knowledge (engineering) (Int), Knowledge (history) (Int), Knowledge (local),
Knowledge (religion) (Int), Linguistics (Int), Profession (Wis), Spellcraft (Int), and Survival
(Wis).

## Channel Energy (Su) {#channel-energy}

When an iron priest channels energy to heal or harm living creatures, she heals or harms constructs
with the clockwork or robot subtypes as well. Constructs without those subtypes are also affected,
but gain only half the normal amount of healing or take only half the normal amount of damage, as
appropriate. This ability alters channel energy.

## Spontaneous Casting {#spontaneous-casting}

An iron priest can spontaneously cast _[make whole](ref/spell/make-whole)_ and
_[greater make whole](ref/spell/make-whole-greater)_ in place of _cure/inflict moderate wounds_ and
_cure/inflict critical wounds_, regardless of whether she channels positive or negative energy. This
ability alters casting.
