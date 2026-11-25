+++
id = "ref/arc-familiar/pilferer"
kind = "archetype"
title = "Pilferer"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pilferer", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "212"
[[sources]]
publication = "animal-archive"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "improved-steal" },
  { anchor = "nondetection" },
  { anchor = "sneak", level = 3 },
  { anchor = "greater-steal", level = 9 },
]
trades = [
  { replaces = "Alertness", by = ["improved-steal"] },
  { replaces = "Improved evasion", by = ["nondetection"] },
  { replaces = "Deliver touch spells", by = ["sneak"] },
  { replaces = "Speak with animals of its kind", by = ["greater-steal"] },
]
+++

Some familiars are stealthy pilferers that perform tricks of thievery or simple spying on their
master's behalf.

## Pilferer Skills {#pilferer-skills}

A pilferer treats Disable Device, Escape Artist, and Sleight of Hand as class skills.

## Improved Steal (Ex) {#improved-steal}

A pilferer gains [Improved Steal](ref/feat/improved-steal) as a bonus feat.

This replaces alertness.

## Nondetection (Su) {#nondetection}

A pilferer is under the constant effect of _[nondetection](ref/spell/nondetection)_ with a caster
level equal to its master's class level. The DC of the caster level check to penetrate this
_nondetection_ effect is equal to 15 + the master's caster level.

This replaces improved evasion.

## Sneak (Ex) {#sneak}

At 3rd level, a pilferer gains a competence bonus equal to [half](ref/misc/fractions-and-rounding)
its master's class level on Sleight of Hand and Stealth checks.

This replaces deliver touch spells.

## Greater Steal (Ex) {#greater-steal}

At 9th level, a pilferer gains [Greater Steal](ref/feat/greater-steal) as a bonus feat.

This replaces speak with animals of its kind.
