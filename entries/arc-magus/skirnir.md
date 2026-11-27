+++
id = "ref/arc-magus/skirnir"
kind = "archetype"
title = "Skirnir"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Skirnir"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "skirnir", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "ultimate-combat"
page = "56"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting", level = 1 },
  { anchor = "arcane-bond", level = 1 },
  { anchor = "arcane-pool", level = 1 },
  { anchor = "sorcerous-shield", level = 1 },
  { anchor = "spellstrike", level = 1 },
  { anchor = "shield-pool", level = 4 },
  { anchor = "spellshield", level = 7 },
  { anchor = "shielded-spell-combat", level = 8 },
  { anchor = "greater-spellshield", level = 16 },
]
trades = [
  { replaces = "Spell combat", feature = "spell-combat", by = ["sorcerous-shield"] },
  { replaces = "Spell recall", feature = "spell-recall", by = ["shield-pool"] },
  { replaces = "Knowledge pool", feature = "knowledge-pool", by = ["spellshield"] },
  { replaces = "Improved spell combat", feature = "improved-spell-combat", by = ["shielded-spell-combat"] },
  { replaces = "greater spell combat", feature = "greater-spell-combat", by = ["shielded-spell-combat"] },
  { replaces = "greater spell access", feature = "greater-spell-access", by = ["shielded-spell-combat"] },
  { replaces = "Counterstrike", feature = "counterstrike", by = ["greater-spellshield"] },
  { alters = "Spellstrike", feature = "spellstrike", by = ["spellstrike"] },
  { alters = "Spell combat", feature = "spell-combat", by = ["sorcerous-shield", "shielded-spell-combat"] },
]
+++

Sometimes called a shield-vassal or shieldmaiden, the skirnir has learned to infuse his power into
his shield.

## Diminished Spellcasting {#diminished-spellcasting}

A skirnir casts one fewer spell of each level than normal. If this reduces the number to 0, he may
cast spells of that level only if his Intelligence allows [bonus spells](ref/rule/determine-bonuses)
of that level.

## Arcane Bond (Su) {#arcane-bond}

At 1st level, a skirnir gains a shield (except for a tower shield) as an arcane bond item. This is
identical to the [wizard](ref/class/wizard) class ability, but the skirnir may only bond with a
shield, not a familiar or other item.

## Arcane Pool {#arcane-pool}

At 1st level, a skirnir can use his arcane pool to grant an enhancement bonus to a weapon as normal,
as well as to his shield, paying the arcane pool cost separately for each. At 5th level and above,
he can also add the following shield special abilities: _[animated](ref/magic-enh/animated)_,
_[arrow catching](ref/magic-enh/arrow-catching)_,
_[arrow deflection](ref/magic-enh/arrow-deflection)_, _[bashing](ref/magic-enh/bashing)_,
_[blinding](ref/magic-enh/blinding)_, _[fortification](ref/magic-enh/fortification)_ (any),
_[reflecting](ref/magic-enh/reflecting)_, _[spell resistance](ref/magic-enh/spell-resistance)_
(any).

## Sorcerous Shield (Ex) {#sorcerous-shield}

At 1st level, skirnirs are proficient with all types of shields, including tower shields, and do not
suffer an arcane spell failure chance when casting magus spells while using a shield. They treat
their magus levels as their fighter levels for the purpose of qualifying for shield-related feats.
This ability replaces spell combat.

## Spellstrike (Su) {#spellstrike}

At 1st level, a skirnir may use this ability with a weapon or [shield bash](ref/misc/shield-bash)
attack.

## Shield Pool (Ex) {#shield-pool}

At 4th level, as a free action, a skirnir may spend 1 point from his arcane pool to add his shield
bonus to AC (not including enhancement bonuses) on a [concentration](ref/rule/concentration) check
to cast defensively. He may also use a touch attack or shield bash with his shield in conjunction
with any pool strike magus arcana. This ability replaces spell recall.

## Spellshield (Su) {#spellshield}

At 7th level, as a standard action, a skirnir may store a magus spell in his shield by spending 1
point from his arcane pool per level of the spell. This functions as the
_[spell storing](ref/magic-enh/spell-storing)_ weapon special ability, but activates only on a
successful shield bash by the skirnir and is not limited to spells of 3rd level or less. This
ability replaces knowledge pool.

## Shielded Spell Combat (Su) {#shielded-spell-combat}

At 8th level, a skirnir gains the spell combat ability, but only when wielding his bonded shield. A
skirnir may use his shield hand to perform somatic components for magus spells, forfeiting the
shield's bonus to AC until the beginning of his next turn; if the bonded shield is a buckler, he
retains its bonus to AC. At 14th level, he gains the benefits of improved spell combat.

At 19th level, he retains his shield's bonus to AC when using any type of shield with spell combat.
This ability replaces improved spell combat, greater spell combat, and greater spell access.

## Greater Spellshield (Su) {#greater-spellshield}

At 16th level, a skirnir may activate a stored spell as an immediate action after being struck in
combat. He may choose to have the spell affect himself or the creature that struck him. This ability
replaces counterstrike.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the skirnir archetype:
[arcane redoubt](ref/arcana/arcane-redoubt), arcane redoubt (greater),
[enduring blade](ref/arcana/enduring-blade) (may use on weapon or shield),
[pool strike](ref/arcana/pool-strike), pool strike (arcing, clinging, thunderous),
[prescient defense](ref/arcana/prescient-defense), [reflection](ref/arcana/reflection).
