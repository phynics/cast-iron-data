+++
id = "ref/arc-familiar/emissary"
kind = "archetype"
title = "Emissary"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "emissary", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "210"
[[sources]]
publication = "familiar-folio"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "divine-guidance" },
  { anchor = "share-will" },
  { anchor = "domain-influence", level = 3 },
]
trades = [
  { replaces = "Alertness", by = ["divine-guidance"] },
  { replaces = "Share spells", by = ["share-will"] },
  { replaces = "Deliver touch spells", by = ["domain-influence"] },
]
+++

The emissary is touched by the divine, serving as a font of wisdom and a moral compass for its
master.

## Special Requirement {#special-requirement}

An emissary familiar can serve only a master who worships a single deity.

## Emissary Skills {#emissary-skills}

An emissary treats Heal, Knowledge (religion), and Sense Motive as class skills.

## Divine Guidance (Sp) {#divine-guidance}

An emissary can cast _[guidance](ref/spell/guidance)_ at will.

This replaces alertness.

## Share Will (Su) {#share-will}

Whenever an emissary or its master fails a saving throw against a mind-affecting effect that affects
only one of them, the other can attempt the saving throw as well. If this second saving throw is a
success, treat the original result as a success, and the emissary and its master can't use this
ability again for 24 hours. On a failure, both the emissary and its master suffer the effects of the
failed saving throw, even if one of them wouldn't ordinarily be a valid target.

This replaces share spells.

## Domain Influence (Sp or Su) {#domain-influence}

At 3rd level, the emissary gains a spark of divine power from the deity its master worships. Choose
one of that deity's domains that grants a 1st-level domain power usable a number of times per day
equal to 3 + the user's Wisdom modifier. The emissary can use that power once per day.

This replaces deliver touch spells.
