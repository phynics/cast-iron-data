+++
id = "ref/arc-alchemist/inspired-chemist"
kind = "archetype"
title = "Inspired Chemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Inspired%20Chemist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inspired_chemist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "advanced-class-guide"
page = "75"

[fields]
kind = "archetype"
features = [
  { anchor = "inspiring-cognatogen", level = 1 },
  { anchor = "bonus-investigator-talents" },
  { anchor = "languages" },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["inspiring-cognatogen"] },
]
+++

Akin to a mindchemist, inspired chemists use a type of cognatogen that instead of increasing their
mental ability scores grants them inspiration like an investigator. This inspiration also grants an
inspired chemist amazing powers to avoid danger, but takes a toll on both physical power and health.

## Inspiring Cognatogen {#inspiring-cognatogen}

At 1st level, an inspired chemist learns how to create an
[inspiring cognatogen](ref/discovery/inspiring-cognatogen), as the inspiring cognatogen discovery.
This ability replaces the [mutagen](ref/discovery/mutagen) class ability. (This means that an
inspired chemist cannot create mutagens unless he selects the mutagen discovery).

## Bonus Feats {#bonus-feats}

An inspired chemist can select [Skill Focus](ref/feat/skill-focus) (Disable Device, Disguise, Heal,
any Knowledge skill, Sense Motive, Spellcraft, or Use Magic Device) in place of a discovery.

## Bonus Investigator Talents {#bonus-investigator-talents}

An inspired chemist can select any two investigator talents in place of a discovery, but can only
use these talents while under the effect of an inspiring cognatogen.

## Languages {#languages}

An inspired chemist can learn three languages in place of a discovery.

## Discoveries {#discoveries}

The following discoveries complement the inspired chemist archetype:
[grand inspiring cognatogen](ref/discovery/grand-inspiring-cognatogen),
[greater inspiring cognatogen](ref/discovery/greater-inspiring-cognatogen), and
[inspired bomb](ref/discovery/inspired-bomb).
