+++
id = "ref/arc-magus/hexbreaker"
kind = "archetype"
title = "Hexbreaker"
aon = "ArchetypeDisplay.aspx?FixedName=Magus%20Hexbreaker"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hexbreaker", path = "json/archetypes_magus.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/magus" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "repel-curse", level = 4 },
  { anchor = "counter-curse", level = 11 },
  { anchor = "hexbreaker-arcana" },
]
trades = [
  { replaces = "Spell recall", feature = "spell-recall", by = ["repel-curse"] },
  { replaces = "Improved spell recall", feature = "improved-spell-recall", by = ["counter-curse"] },
]
+++

Hexbreakers—sometimes called witch-hammers for their proclivity toward warhammers—have borne witness
to the damage of unrestrained arcane power and hone their own arcane arts to battle such abuse. They
train themselves to shatter the curses and dark transformations that can haunt others for a
lifetime.

## Repel Curse (Su) {#repel-curse}

At 4th level, a hexbreaker has the chance to protect others from being cursed. As an immediate
action when a spell with the curse descriptor or a curse-style effect (such as a witch's
[evil eye](ref/hex/evil-eye) or [misfortune](ref/hex/misfortune) hex or a
[sea hag's](ref/monster/hag-sea-hag) evil eye) targets a creature within 30 feet of him, a
hexbreaker can spend 1 point from his arcane pool to attempt to dispel that effect, as if he had
cast _[remove curse](ref/spell/remove-curse)_. This ability has no effect on ongoing effects, such
as a sea hag's horrific appearance or a [pugwampi's](ref/monster/gremlin-pugwampi) unluck aura.

The magus adds _[remove curse](ref/spell/remove-curse)_ to his spell list as a 3rd-level spell and
adds _[break enchantment](ref/spell/break-enchantment)_ as a 4th-level spell.

This replaces spell recall.

## Counter Curse (Su) {#counter-curse}

At 11th level, whenever a hexbreaker successfully dispels a curse effect or spell with the curse
descriptor using his repel curse ability, he can immediately spend 2 points from his arcane pool to
reflect the spell back on the original caster. This otherwise functions as
_[spell turning](ref/spell/spell-turning)_.

This replaces improved spell recall.

## Hexbreaker Arcana {#hexbreaker-arcana}

A hexbreaker can select from the following arcana in addition to those normally available.

### Improved Remove Curse (Su) {#improved-remove-curse}

The hexbreaker can spend additional points from his arcane pool to improve his ability to remove a
curse. Each point spent while casting _[remove curse](ref/spell/remove-curse)_ or
_[break enchantment](ref/spell/break-enchantment)_ grants a +2 bonus to his caster level check. He
can use this arcana after rolling the caster level check, but only before the results are revealed.
This can be used with the hexbreaker's repel curse and counter curse abilities.

### Wracking Dispel (Su) {#wracking-dispel}

Whenever the hexbreaker successfully dispels a spell using
_[break enchantment](ref/spell/break-enchantment)_, _[dispel magic](ref/spell/dispel-magic)_, or
_[remove curse](ref/spell/remove-curse)_, he can expend 1 point from his arcane pool to wrack the
original caster with pain, dealing 1d4 points of damage per spell level of the effect dispelled. If
the target succeeds at a Will save (DC = 15 + the level of the spell dispelled + the hexbreaker's
Intelligence modifier) it takes only 1 point of damage per spell level. The hexbreaker cannot target
the same caster more than once per round with this ability, regardless of how many effects he
dispels.

## Magus Arcana {#magus-arcana}

The following magus arcana complement the hexbreaker: [bane blade](ref/arcana/bane-blade),
[dispelling strike](ref/arcana/dispelling-strike), [disruptive](ref/arcana/disruptive),
[lingering pain](ref/arcana/lingering-pain), [spellbreaker](ref/arcana/spellbreaker), and
[reflection](ref/arcana/reflection).
