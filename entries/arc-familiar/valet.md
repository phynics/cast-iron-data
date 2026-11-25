+++
id = "ref/arc-familiar/valet"
kind = "archetype"
title = "Valet"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "valet", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "213"
[[sources]]
publication = "animal-archive"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "able-assistant" },
  { anchor = "magical-manipulation" },
  { anchor = "teammate" },
  { anchor = "deliver-touch-spells", level = 3 },
  { anchor = "deliver-aid", level = 7 },
  { anchor = "aide-to-all", level = 13 },
]
trades = [
  { replaces = "Alertness", by = ["able-assistant"] },
  { replaces = "Share spells", by = ["magical-manipulation"] },
  { replaces = "Improved evasion", by = ["teammate"] },
  { replaces = "Speak with animals of its kind", by = ["deliver-aid"] },
  { replaces = "Scry on familiar", by = ["aide-to-all"] },
  { alters = "Deliver touch spells", by = ["deliver-touch-spells"] },
]
+++

A valet is a consummate personal servant, able to fetch, deliver, and perform for its master's every
need.

## Valet Skills {#valet-skills}

A valet treats Craft, Perform, and Profession as class skills.

## Able Assistant (Ex) {#able-assistant}

A valet's master treats the valet as if it had the
[Cooperative Crafting](ref/feat/cooperative-crafting) feat and shares Craft skills and item creation
feats with the valet.

This replaces alertness.

## Magical Manipulation (Sp) {#magical-manipulation}

A valet can cast _[open/close](ref/spell/open-close)_ and
_[prestidigitation](ref/spell/prestidigitation)_ at will.

This replaces share spells.

## Teammate (Ex) {#teammate}

A valet is considered to have all the teamwork feats its master has.

This replaces improved evasion.

## Deliver Touch Spells (Su) {#deliver-touch-spells}

At 3rd level, when delivering a harmless touch spell to a willing creature, a valet can move before
and after delivering the spell, as long as its total movement does not exceed its speed.

This alters deliver touch spells.

## Deliver Aid (Ex) {#deliver-aid}

At 7th level, a valet can move before and after using the aid another action, as long as its total
movement does not exceed its speed.

This replaces speak with animals of its kind.

## Aide to All (Ex) {#aide-to-all}

At 13th level, a valet can use the aid another action as a full-round action to grant up to three
adjacent creatures bonuses from this action. Each bonus can apply to the same action or check or to
different actions or checks.

This replaces scry on familiar.
