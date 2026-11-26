+++
id = "ref/arc-shaman/crystal-tender"
kind = "archetype"
title = "Crystal Tender"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Crystal%20Tender"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crystal_tender", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "scion-of-the-stones", level = 1 },
  { anchor = "reciprocal-resonance", level = 4 },
  { anchor = "invoke-latent-facets", level = 8 },
  { anchor = "cabochon-form", level = 20 },
]
trades = [
  { replaces = "Shaman hex gained at 8th level", feature = "hex", levels = [8], by = ["invoke-latent-facets"] },
  { replaces = "Manifestation", feature = "manifestation", by = ["cabochon-form"] },
  { alters = "Spirit animal", feature = "spirit-animal", by = ["scion-of-the-stones"] },
  { alters = "Wandering spirit", feature = "wandering-spirit", by = ["reciprocal-resonance"] },
]
+++

Crystal tenders are most often found among subterranean races and races bearing a strong connection
to the earth. A crystal tender focuses on the spirits of metal and stone, using crystals as a means
to focus the power of the spirits she venerates. Many crystal tenders take it upon themselves to
guard rich gem veins and other mineral treasures from those who would mine them out of greed, much
in the way that surface-dwelling druids might defend a sacred grove from woodcutters.

The crystal tenders of Orv meditate within the Crystal Womb, often near the churning vortex that
makes up the heart of the Vault. They learn to focus the cavern's energies through ley lines in the
stone, and they study the birth of crystals within the Womb in order to mimic the process.

## Scion of the Stones (Ex) {#scion-of-the-stones}

A crystal tender forms a mystic connection with the precious stones and gems she has sworn to
protect. Her spirit animal always appears to be composed of a crystalline substance and gains a +2
bonus to its natural armor. Her spirit animal is treated as an outsider with both the earth and
native subtypes, and counts as a crystalline creature for the purposes of spells and abilities. The
unique nature of her spirit animal increases the cost of replacing it to 750 gp per shaman level.

This alters spirit animal.

## Reciprocal Resonance (Su) {#reciprocal-resonance}

At 4th level, a crystal tender learns to form a temporary bond with a spirit of crystal. When
selecting her wandering spirit, she can forgo gaining a spirit ability to instead grant herself and
her spirit animal DR 1/adamantine as long as they're within 10 feet of one another. While benefiting
from this ability, the crystal tender's skin takes on a crystalline sheen.

The DR gained from this ability increases to 2/adamantine at 8th level, 3/adamantine at 12th level,
4/adamantine at 16th level, and 5/adamantine at 20th level.

This alters wandering spirit.

## Invoke Latent Facets (Su) {#invoke-latent-facets}

At 8th level, both a crystal tender and her spirit animal gain all of the benefits of any
_[ioun stones](ref/magic-wondrous/ioun-stone)_ worn by one another, as long as they're within 100
feet of each other.

The crystal tender's spirit animal can also embed a number of _ioun stones_ equal to the crystal
tender's Charisma modifier into its crystalline form. Embedded _ioun stones_ don't gain any
additional abilities, save that they don't orbit the spirit animal and can't be separately targeted.
A slain or unconscious spirit animal immediately loses all embedded _ioun stones_, which tumble to
the ground beside its body.

This replaces the shaman hex gained at 8th level.

## Cabochon Form (Sp) {#cabochon-form}

At 20th level, as a standard action, a crystal tender can transform her body into a living gemstone
as per _[iron body](ref/spell/iron-body)_ with a duration of 12 hours. Instead of being vulnerable
to effects that can harm an iron golem while in this form, she is vulnerable to effects that can
harm a crystalline creature (such as _[shatter](ref/spell/shatter)_). She can use this ability once
per day.

This replaces manifestation.
