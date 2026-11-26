+++
id = "ref/arc-cleric/asmodean-advocate"
kind = "archetype"
title = "Asmodean Advocate"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Asmodean%20Advocate"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "asmodean_advocate", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "16"

[fields]
kind = "archetype"
features = [
  { anchor = "pact-bound", level = 1 },
  { anchor = "serpent", level = 1 },
  { anchor = "devil-in-the-details", level = 1 },
  { anchor = "shoulder-devil", level = 8 },
]
trades = [
  { alters = "Domains", feature = "domains", by = ["pact-bound"] },
]
+++

For the faithful of [Asmodeus](ref/faith/asmodeus), the words used in a negotiation or contract
matter more than their intent. The word of the law is to be respected, but loopholes and vague
wording are part of every law. Asmodean advocates are master wordsmiths who ally themselves with
creatures that—much like their words—seem insignificant but are treacherous.

## Pact-Bound (Ex) {#pact-bound}

An Asmodean advocate must choose Asmodeus as her deity and select the Trickery domain. She does not
gain a second domain. If she ever changes her deity, she loses this archetype and becomes a normal
ex-cleric. This ability alters domains.

## Serpent (Su) {#serpent}

At 1st level, an Asmodean advocate gains a [familiar](ref/ability/familiars) as the arcane bond
class feature, using her cleric level as her [wizard](ref/class/wizard) level. She must choose a
[viper](ref/monster/familiar-viper) familiar. The viper speaks one language of the Asmodean
advocate's choice as a supernatural ability.

## Devil in the Details (Ex) {#devil-in-the-details}

At 1st level, an Asmodean advocate learns to choose her words so carefully that even when she says
something designed to deceive listeners, the words are phrased to be technically true. She can use
her Profession (barrister) skill for Bluff and Diplomacy checks. This benefit also extends to her
familiar. The Asmodean advocate gains an insight bonus equal to 1/2 her cleric level (minimum +1) on
Linguistics checks related to forgeries and on all Profession (barrister) checks.

## Shoulder Devil (Su) {#shoulder-devil}

At 8th level, an Asmodean advocate can choose an [imp](ref/monster/devil-imp) familiar as though she
had the [Improved Familiar](ref/feat/improved-familiar) feat.
