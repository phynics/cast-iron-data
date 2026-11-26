+++
id = "ref/arc-vigilante/ferocious-hunter"
kind = "archetype"
title = "Ferocious Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Ferocious%20Hunter"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ferocious_hunter", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "hidden-heritage", level = 1 },
  { anchor = "symbol-of-pride", level = 2 },
  { anchor = "spirit-of-ferocity", level = 3 },
  { anchor = "symbol-of-mastery", level = 8 },
]
trades = [
  { replaces = "Vigilante talent gained at 2nd level", feature = "vigilante-talent", levels = [2], by = ["symbol-of-pride"] },
  { replaces = "Unshakable", feature = "unshakable", by = ["spirit-of-ferocity"] },
  { replaces = "Vigilante talent gained at 8th level", feature = "vigilante-talent", levels = [8], by = ["symbol-of-mastery"] },
  { alters = "Dual identity", feature = "dual-identity", by = ["hidden-heritage"] },
]
+++

Half-orcs with more distant orc ancestry often look almost indistinguishable from humans, aside from
a slightly greenish tint to their skin or sharp teeth. The ability to move through the world without
experiencing the same discrimination many of their kin face opens doors that might otherwise be
closed, yet many of these half-orcs still take great pride in their heritage and have a powerful
desire to show the world that half-orcs are deserving of respect. By taking on an alter-ego that
allows them to show their true colors, they can become a champion of the downtrodden and a hero
among half-orcs.

## Hidden Heritage (Ex) {#hidden-heritage}

A ferocious hunter must present as human for his social identity and as a half-orc for his vigilante
identity in order to gain the benefits of dual identity. He gains
[Pass for Human](ref/feat/pass-for-human) as a bonus feat. In addition, his alignment stays the same
when he switches between identities.

This alters dual identity.

## Symbol of Pride {#symbol-of-pride}

At 2nd level, a ferocious hunter gains the [signature weapon](ref/vigtalent/signature-weapon)
vigilante talent, but must select a [falchion](ref/eq-weapon/falchion),
[greataxe](ref/eq-weapon/greataxe), or a weapon with "orc" in its name as his chosen weapon. He
gains this talent regardless of his chosen vigilante specialization.

This replaces the vigilante talent gained at 2nd level.

## Spirit of Ferocity (Ex) {#spirit-of-ferocity}

Starting at 3rd level, when using orc ferocity to continue fighting after falling below 0 hit
points, a ferocious hunter fights on for a number of rounds equal to his Constitution modifier.

This replaces unshakable.

## Symbol of Mastery {#symbol-of-mastery}

At 8th level, a ferocious hunter gains [Improved Critical](ref/feat/improved-critical) with the
weapon chosen for the symbol of pride ability. His base attack bonus is equal to his vigilante level
for the purpose of qualifying for [Critical Focus](ref/feat/critical-focus) and any feats that
require Critical Focus as a prerequisite.

This replaces the vigilante talent gained at 8th level.
