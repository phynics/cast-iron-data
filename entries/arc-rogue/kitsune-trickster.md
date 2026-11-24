+++
id = "ref/arc-rogue/kitsune-trickster"
kind = "archetype"
title = "Kitsune Trickster"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Kitsune%20Trickster"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kitsune_trickster", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-race-guide"
page = "192"

[fields]
kind = "archetype"
features = [
  { anchor = "kitsune-s-guile", level = 1 },
  { anchor = "kitsune-s-charm", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["kitsune-s-guile"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["kitsune-s-charm"] },
]
+++

The kitsune trickster combines her sharpened wit with minor arcane powers of charm and persuasion.
She uses her talents to spin convincing lies, riddles, and stories. A trickster has the following
class features.

**Prerequisites:** Kitsune

## Kitsune's Guile (Ex) {#kitsune-s-guile}

At 1st level, a trickster relies on her intellect as much as her personality. She adds her
Intelligence modifier on Bluff, Diplomacy, Disguise, and Sense Motive checks. This ability replaces
trapfinding.

## Kitsune's Charm (Sp) {#kitsune-s-charm}

At 3rd level, a kitsune trickster can use _[charm person](ref/spell/charm-person)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities) (caster level equal to her rogue level - 2). At
6th level, and every three levels thereafter, the kitsune trickster gains an additional daily use of
this ability. This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the kitsune trickster archetype: major magic, minor magic
(_Core Rulebook_); false friend, obfuscate story, steal the story (see below); charmer, coax
information, honeyed words (_Advanced Player's Guide_); convincing lie (_Ultimate Combat_).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the kitsune trickster archetype: skill mastery,
slippery mind (_Core Rulebook_); master of disguise (_Advanced Player's Guide_); rumormonger
(_Ultimate Combat_).
