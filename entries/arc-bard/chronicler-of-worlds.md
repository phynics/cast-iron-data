+++
id = "ref/arc-bard/chronicler-of-worlds"
kind = "archetype"
title = "Chronicler of Worlds"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Chronicler%20of%20Worlds"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chronicler_of_worlds", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "planar-adventures"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "wanderer-s-insight" },
  { anchor = "planar-lore", level = 1 },
  { anchor = "bardic-performance" },
  { anchor = "quintessence-infusion", level = 9 },
  { anchor = "mantra-of-tabris", level = 15 },
  { anchor = "amoral-scholar", level = 2 },
  { anchor = "scrivener-s-versatility", level = 2 },
]
trades = [
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["quintessence-infusion"] },
  { replaces = "Inspire heroics", feature = "bardic-performance", power = "inspire heroics", by = ["mantra-of-tabris"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["amoral-scholar"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["scrivener-s-versatility"] },
  { alters = "Bardic knowledge", feature = "bardic-knowledge", by = ["planar-lore"] },
]
+++

In eons past, the angel Tabris was tasked with cataloging all knowledge of the Great Beyond, only to
eventually be cast from Heaven for penning the _Book of the Damned_, the perfect catalog of all
planar evil. His dedication and sacrifice to the task have inspired some to follow his example;
these bards are known as the chroniclers of worlds.

A chronicler of worlds forsakes morality in service of understanding; she is both warrior and
mystic, scholar and soldier. Some chroniclers congregate in [Axis](ref/rule/utopia) to share their
discoveries and theories, but the majority wander the planes, steadfastly pushing the boundaries of
what is known.

## Wanderer's Insight {#wanderer-s-insight}

A chronicler of worlds gains power not from her personality but from an analytical understanding of
existence. She uses Intelligence instead of Charisma to determine the effects of bard class
features, including spellcasting and bardic performance. A chronicler of worlds must have an
alignment with at least one neutral component; a character who does not meet this requirement cannot
use or benefit from this archetype's abilities.

## Planar Lore (Ex) {#planar-lore}

A chronicler of worlds can take 10 on Knowledge (planes) checks. A number of times per day equal to
her Intelligence modifier, she can take 20 on a Knowledge (planes) check. This ability stacks with
that gained by lore master at 5th level. A chronicler of worlds can attempt all Knowledge checks
untrained.

This alters bardic knowledge.

## Bardic Performance {#bardic-performance}

The chronicler of worlds gains the following bardic performances.

## Quintessence Infusion (Su) {#quintessence-infusion}

This performance infuses allies with planar quintessence. At 9th level, while on a plane other than
the Material Plane, the chronicler of worlds can use this performance to target an ally within 30
feet. For every 3 bard levels she has beyond 9th, she can affect one additional creature. Affected
allies gain the plane's basic infusion effect (see page 93). If the chronicler of worlds is 13th
level or higher, affected creatures also gain the plane's improved infusion. If she is 16th level or
higher, affected creatures also gain the plane's greater infusion. The first time each day a
creature benefits from quintessence infusion, the plane infused is set for the day and additional
infusions can grant only that plane's infusions. Infusions that have limited uses per day remain
limited in that way, regardless of how many times quintessence infusion is gained. Quintessence
infusion relies on audible and visual components.

This replaces inspire greatness.

## Mantra of Tabris (Su) {#mantra-of-tabris}

Tabris survived his travels through the darkest realms, his dedication to the pursuit of knowledge a
shield against planar horrors. The chronicler of worlds walks in his footsteps. At 15th level, the
chronicler of worlds can create a potent ward against outsiders. While maintaining this performance,
when the chronicler of worlds is hit by an attack from an outsider or fails a saving throw against
an outsider's extraordinary, supernatural, or [spell-like ability](ref/umr/spell-like-abilities), as
an immediate action she can attempt a Knowledge (planes) check and use the result as her Armor Class
or her saving throw result against that attack or effect. The chronicler cannot use her planar lore
ability to take 20 on this Knowledge (planes) check.

This can retroactively alter the results of the attack or ability. The chronicler of worlds must
decide to use this ability before the effects of the successful attack or failed saving throw have
been announced. Mantra of Tabris relies on audible components.

This replaces inspire heroics.

## Amoral Scholar (Ex) {#amoral-scholar}

A chronicler of worlds rejects cosmic morality. At 2nd level, she does not take penalties imposed by
[planar alignment traits](ref/rule/alignment-traits-pa), and she gains a +4 bonus on saving throws
against spells and effects that vary based on their target's alignment.

This replaces well-versed.

## Scrivener's Versatility (Ex) {#scrivener-s-versatility}

A chronicler of worlds seeks to emulate history's greatest scribe; studying the lore of Tabris
grants insight into widely varying subjects, from anatomy to discourse. At 2nd level, a chronicler
of worlds selects a skill from the following list: Bluff, Diplomacy, Disable Device, Heal,
Intimidate, Profession (scribe), Sense Motive, or Survival. When attempting skill checks of that
type, a chronicler can use her Linguistics skill bonus in place of her bonus with the chosen skill.
At 6th level and every 4 levels thereafter, a chronicler of worlds selects an additional skill to
gain this benefit.

This replaces versatile performance.
