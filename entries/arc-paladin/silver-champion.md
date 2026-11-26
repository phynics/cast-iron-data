+++
id = "ref/arc-paladin/silver-champion"
kind = "archetype"
title = "Silver Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Silver%20Champion"
source_ids = ["legacy-of-dragons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "silver_champion", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "legacy-of-dragons"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "deity" },
  { anchor = "drake-mount", level = 5 },
  { anchor = "dragon-magic" },
]
trades = [
  { replaces = "Divine bond", feature = "divine-bond", by = ["drake-mount"] },
  { replaces = "channel energy", feature = "channel-energy", by = ["drake-mount"] },
  { replaces = "aura of justice", feature = "aura-of-justice", by = ["drake-mount"] },
  { replaces = "aura of righteousness", feature = "aura-of-righteousness", by = ["drake-mount"] },
  { alters = "Smite evil", feature = "smite-evil", by = ["drake-mount"] },
  { alters = "mercy", feature = "mercy", by = ["drake-mount"] },
  { alters = "Spellcasting", feature = "spells", by = ["dragon-magic"] },
]
+++

Paladins who serve as priests of [Apsu](ref/faith/apsu) are almost always on the move, wandering
from place to place and trying to show their dedication to the Waybringer in their deeds rather than
depending on mere words. Good-aligned dragons are more likely to treat such paladins as they would
treat other dragons (though perhaps not with the respect reserved for other true dragons), and evil
dragons often target them as special threats.

More rarely a drake is so inspired by a paladin of [Apsu](ref/faith/apsu) that it chooses to assist
the paladin in all her actions. These drake allies see the benefit of a silver champion remaining
mobile and understand the powerful threats the champion must face, and in time even consent to serve
their chosen paladins as a steed. Silver champions are often concerned by their drake allies'
pragmatic natures, however, and are sure to treat them with respect, knowing that these lesser
dragons must constantly be inspired to act on their better natures.

## Deity {#deity}

A silver champion must worship Apsu.

## Drake Mount {#drake-mount}

At 5th level, a silver champion gains a [drake companion](ref/sidekick/drake). If the drake
companion is at least one size larger than the silver champion, it gains the
[mount](ref/spell/mount) drake power as a bonus power. However, a silver champion doesn't gain
additional uses per day of smite evil at 4th, 10th, and 16th levels, and doesn't gain mercies at
6th, 12th, and 18th levels.

This ability replaces divine bond, channel energy, aura of justice, and aura of righteousness, and
alters smite evil and mercy.

## Dragon Magic {#dragon-magic}

The silver champion does not have access to the normal paladin spell list. She instead adds the 1st-
through 4th-level spells from the domains granted by Apsu (Artifice, Good, Law,
[Scalykind](ref/domain/scalykind), [Travel](ref/domain/travel)) and the god's associated subdomains
(Archon, Construct, Dragon, Exploration, Toil, and Trade) to her class spell list. A silver champion
casts one fewer spell of each level than normal. If this reduces the number to less than 0, she
can't cast spells of that level.

This ability modifies the paladin's spellcasting.
