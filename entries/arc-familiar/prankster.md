+++
id = "ref/arc-familiar/prankster"
kind = "archetype"
title = "Prankster"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "prankster", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "212"

[fields]
kind = "archetype"
features = [
  { anchor = "autonomous-link" },
  { anchor = "improved-dirty-trick" },
  { anchor = "magical-pranks" },
  { anchor = "glib-comedy", level = 3 },
  { anchor = "greater-dirty-trick", level = 11 },
  { anchor = "unreliable-narrator", level = 13 },
]
trades = [
  { replaces = "Alertness", by = ["improved-dirty-trick"] },
  { replaces = "Improved evasion", by = ["magical-pranks"] },
  { replaces = "share spells", by = ["magical-pranks"] },
  { replaces = "Deliver touch spells", by = ["glib-comedy"] },
  { replaces = "Spell resistance", by = ["greater-dirty-trick"] },
  { alters = "Empathic link", by = ["autonomous-link"] },
  { alters = "Scry on familiar", by = ["unreliable-narrator"] },
]
+++

Some familiars love to perform pranks on their unsuspecting masters, as well as on those around
their masters—allies and enemies alike. While good-aligned pranksters' tricks are usually good
natured except against foes, evil pranksters play tricks that are mean spirited or even downright
cruel.

## Prankster Skills {#prankster-skills}

A prankster treats Bluff, Disguise, Perform (comedy), and Sleight of Hand as class skills.

## Autonomous Link (Ex) {#autonomous-link}

A prankster can hide its feelings from its master via its empathic link at will. It can also try to
project a false emotion through the link by attempting a Bluff check opposed by its master's Sense
Motive.

This alters empathic link.

## Improved Dirty Trick (Ex) {#improved-dirty-trick}

A prankster gains [Improved Dirty Trick](ref/feat/improved-dirty-trick) as a bonus feat.

This replaces alertness.

## Magical Pranks (Sp) {#magical-pranks}

A prankster can cast _[ghost sound](ref/spell/ghost-sound)_, _[mage hand](ref/spell/mage-hand)_, and
_[prestidigitation](ref/spell/prestidigitation)_ at will as
[spell-like abilities](ref/umr/spell-like-abilities).

This replaces improved evasion and share spells.

## Glib Comedy (Ex) {#glib-comedy}

At 3rd level, a prankster gains a competence bonus equal to [half](ref/misc/fractions-and-rounding)
its master's class level on Bluff, Disguise, and Perform (comedy) checks.

This replaces deliver touch spells.

## Greater Dirty Trick (Ex) {#greater-dirty-trick}

At 11th level, a prankster gains [Greater Dirty Trick](ref/feat/greater-dirty-trick) as a bonus
feat.

This replaces [spell resistance](ref/rule/spell-resistance).

## Unreliable Narrator (Sp) {#unreliable-narrator}

At 13th level, whenever its master uses scry on familiar, a prankster can use _false vision_ to fool
that ability; this doesn't affect any other divination (_scrying_) effects in the area, only its
master's scry on familiar ability.

This alters scry on familiar.
