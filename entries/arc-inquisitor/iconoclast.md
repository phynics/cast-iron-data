+++
id = "ref/arc-inquisitor/iconoclast"
kind = "archetype"
title = "Iconoclast"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Iconoclast"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "iconoclast", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-combat"
page = "52"

[fields]
kind = "archetype"
features = [
  { anchor = "shake-effects", level = 1 },
  { anchor = "detect-magic", level = 2 },
  { anchor = "dispelling-attack", level = 5 },
  { anchor = "negating-critical", level = 14 },
  { anchor = "destroy-artifact", level = 20 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["shake-effects"] },
  { replaces = "Detect alignment", feature = "detect-alignment", by = ["detect-magic"] },
  { replaces = "Discern lies", feature = "discern-lies", by = ["dispelling-attack"] },
  { replaces = "Exploit weakness", feature = "exploit-weakness", by = ["negating-critical"] },
  { replaces = "True judgment", feature = "true-judgment", by = ["destroy-artifact"] },
]
+++

Some magic items are heretical by nature, enabling the unfaithful to spread wickedness. Iconoclasts
seek out and remove such crutches, cleansing the taint these items exude.

## Shake Effects (Ex) {#shake-effects}

At 1st level, an iconoclast gains a +2 bonus on all saving throws against effects that come from a
magic item. This ability replaces monster lore.

## Detect Magic (Sp) {#detect-magic}

At 2nd level, an iconoclast gains the ability to _[detect magic](ref/spell/detect-magic)_ at will.
This ability replaces _detect alignment_.

## Dispelling Attack (Sp) {#dispelling-attack}

At 5th level, once per day as a standard action, an iconoclast can make a melee or ranged attack
against an opponent, and if she hits, she can affect that opponent as if she had cast
_[dispel magic](ref/spell/dispel-magic)_, using the targeted dispel option. If she misses, this
ability is wasted. Use her inquisitor level as the caster level of the _dispel magic_ effect. This
ability replaces _discern lies_.

## Negating Critical (Sp) {#negating-critical}

At 14th level, when an iconoclast confirms a critical hit, the creature she hit must succeed at a
Fortitude save at DC 10 + 1/2 the iconoclast's caster level + the iconoclast's Wisdom modifier for
each non-artifact magic item the target is wearing or carrying. On a failed saving throw, the target
of the critical hit can neither use nor gain benefit from any
[minor magic item](ref/misc/magic-items-by-category) for 1d4 rounds. This ability can be used in
conjunction with critical feats. This ability replaces exploit weakness.

## Destroy Artifact (Sp) {#destroy-artifact}

At 20th level, an iconoclast has the ability to destroy minor [artifacts](ref/rule/artifacts). The
iconoclast must have possession of the minor artifact for at least a week, which she must spend in
uninterrupted contemplation of the nature of the artifact. At the end of that week, she makes a DC
30 Spellcraft check to unweave the fabric of the item, and if she is successful, the artifact is
destroyed. If the iconoclast fails, she cannot try to destroy the artifact again with this ability,
but another iconoclast can. This ability replaces true judgment.
