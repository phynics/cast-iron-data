+++
id = "ref/arc-familiar/decoy"
kind = "archetype"
title = "Decoy"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "decoy", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "familiar-folio"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "deceitful" },
  { anchor = "mockingbird", level = 5 },
  { anchor = "master-s-guise", level = 11 },
]
trades = [
  { replaces = "Alertness", by = ["deceitful"] },
  { replaces = "Speak with master", by = ["mockingbird"] },
  { replaces = "speak with animals of its kind", by = ["mockingbird"] },
  { replaces = "Spell resistance", by = ["master-s-guise"] },
]
+++

A decoy misdirects its master's enemies, allowing the master to strike by surprise.

## Class Skills {#class-skills}

A decoy treats Bluff as a class skill.

## Deceitful {#deceitful}

A decoy gains [Deceitful](ref/feat/deceitful) as a bonus feat. This replaces alertness.

## Mockingbird (Ex) {#mockingbird}

At 5th level, a decoy can speak any of its master's languages. At 7th level, it can mimic its
master's voice and intonation perfectly. This ability replaces speak with master and speak with
animals of its kind.

## Master's Guise (Sp) {#master-s-guise}

At 11th level, a decoy can transform into a perfect likeness of its master, as the
_[alter self](ref/spell/alter-self)_ spell. It can hold this form for up to 1 minute per caster
level; upon changing back, the decoy must remain in its natural form for an equal amount of time
before transforming again. This ability replaces [spell resistance](ref/rule/spell-resistance).
