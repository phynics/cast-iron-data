+++
id = "ref/arc-rogue/counterfeit-mage"
kind = "archetype"
title = "Counterfeit Mage"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Counterfeit%20Mage"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "counterfeit_mage", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-class-guide"
page = "109"

[fields]
kind = "archetype"
features = [
  { anchor = "magical-expertise", level = 1 },
  { anchor = "signature-wand", level = 4 },
  { anchor = "wand-adept", level = 6 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["magical-expertise"] },
  { replaces = "Rogue talent gained at 4th level", feature = "rogue-talents", levels = [4], by = ["signature-wand"] },
]
+++

Charlatans and stage magicians use sleight of hand to fake magic. A counterfeit mage goes a step
further, parroting the motions and activation phrases used by arcane casters to activate wands or
other magical accoutrements. While counterfeit mages rarely fool a real wizard, their command of the
arcane is enough to convince most lay people.

## Magical Expertise (Ex) {#magical-expertise}

At 1st level, a counterfeit mage adds 1/2 his level to Disable Device checks to disarm magical
traps, Perception checks to find magical traps, and Use Magic Device checks to activate scrolls and
wands. A counterfeit mage can use Disable Device to disarm magic traps. This ability replaces
trapfinding.

## Signature Wand (Ex) {#signature-wand}

At 4th level, a counterfeit mage can spend 1 hour practicing with a wand to designate it as his
signature wand. He can draw that wand as a free action, and can activate it without having to
succeed at a Use Magic Device check. He can change his signature wand once per day. This ability
replaces the rogue talent gained at 4th level.

## Wand Adept (Ex) {#wand-adept}

At 6th level, a counterfeit mage can use his Dexterity modifier in place of his Charisma modifier
when attempting Use Magic Device checks to activate wands.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the counterfeit mage archetype: deft palm, esoteric scholar,
honeyed words, major magic, minor magic, and trap spotter.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the counterfeit mage archetype: dispelling attack,
familiar, and slippery mind.
