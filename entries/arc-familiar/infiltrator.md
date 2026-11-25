+++
id = "ref/arc-familiar/infiltrator"
kind = "archetype"
title = "Infiltrator"
source_ids = ["ultimate-wilderness", "animal-archive"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infiltrator", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "211"
[[sources]]
publication = "animal-archive"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "alertness" },
  { anchor = "share-spells" },
  { anchor = "uncanny-stealth" },
  { anchor = "scry-on-familiar", level = 7 },
  { anchor = "telepathic-bond", level = 11 },
]
trades = [
  { replaces = "Improved evasion", by = ["uncanny-stealth"] },
  { replaces = "Speak with animals of its kind", by = ["scry-on-familiar"] },
  { replaces = "Spell resistance", by = ["telepathic-bond"] },
  { alters = "Alertness", by = ["alertness"] },
  { alters = "Share spells", by = ["share-spells"] },
]
+++

Familiars can be skilled spies, and infiltrators are the very best of their kind at the subtle art
of espionage.

## Infiltrator Skills {#infiltrator-skills}

An infiltrator treats Bluff and Disguise as class skills.

## Alertness (Ex) {#alertness}

An infiltrator gains [Alertness](ref/feat/alertness) as a bonus feat rather than providing that feat
to its master.

This alters alertness.

## Share Spells (Ex) {#share-spells}

An infiltrator can share only divination spells that have a target of "you" via this ability.

This alters share spells.

## Uncanny Stealth (Ex) {#uncanny-stealth}

An infiltrator gains [uncanny dodge](ref/ability/uncanny-dodge) and
[improved uncanny dodge](ref/ability/improved-uncanny-dodge), treating its master's level as its
effective [rogue](ref/class/rogue) level.

This replaces improved evasion.

## Scry on Familiar (Sp) {#scry-on-familiar}

At 7th level, an infiltrator's master can [scry](ref/spell/scrying) on it for up to 1 minute per
level per day. The duration does not need to be consecutive, but it must be used in 1-minute
increments.

This replaces speak with animals of its kind.

## Telepathic Bond (Sp) {#telepathic-bond}

At 11th level, an infiltrator gains a permanent [telepathic bond](ref/spell/telepathic-bond) with
its master. This bond has no range limit as long as the familiar and its master are on the same
plane.

This replaces [spell resistance](ref/rule/spell-resistance).
