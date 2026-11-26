+++
id = "ref/arc-druid/green-scourge"
kind = "archetype"
title = "Green Scourge"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Green%20Scourge"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "green_scourge", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "nature-s-armaments", level = 1 },
  { anchor = "aberration-sense", level = 1 },
  { anchor = "scentless", level = 3 },
  { anchor = "resist-unnatural-influence", level = 4 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["aberration-sense"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["scentless"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-unnatural-influence"] },
  { alters = "Spontaneous casting", feature = "spontaneous-casting", by = ["nature-s-armaments"] },
]
+++

Green scourges are militant druids sworn to restore natural order. They're less concerned with
nurturing the natural world than most druids, instead focusing their efforts on slaying corrupted
creatures.

## Nature's Armaments {#nature-s-armaments}

A green scourge can lose a prepared 1st- or 2nd-level spell in order to cast
_[shillelagh](ref/spell/shillelagh)_ or _[flame blade](ref/spell/flame-blade)_, respectively. She
can instead choose to lose a higher-level spell in order to increase the enhancement bonus of her
[shillelagh](ref/spell/shillelagh), or to add any of the following weapon special abilities to her
_[shillelagh](ref/spell/shillelagh)_ or _[flame blade](ref/spell/flame-blade)_:
_[bane](ref/magic-enh/bane)_ (aberrations only), _[frost](ref/magic-enh/frost)_,
_[mighty cleaving](ref/magic-enh/mighty-cleaving)_, _[returning](ref/magic-enh/returning),
[shock](ref/magic-enh/shock)_, _[throwing](ref/magic-enh/throwing)_, or
_[vicious](ref/magic-enh/vicious)_. If the target weapon is a
[quarterstaff](ref/eq-weapon/quarterstaff), these bonuses apply to only one of its ends. If a
[flame blade](ref/spell/flame-blade) gains the _frost_ or _shock_ special ability, the base damage
of the spell changes to match the energy type; neither a [flame blade](ref/spell/flame-blade) nor
[shillelagh](ref/spell/shillelagh) can gain both of these special abilities. A green scourge cannot
add the _throwing_ property to a _[flame blade](ref/spell/flame-blade)_ unless she also adds the
_returning_ property.

When adding weapon special abilities or increasing the enhancement bonus, the final level of the
spell expended is 1 higher than the base spell level (2nd for _[shillelagh](ref/spell/shillelagh)_
and 3rd for _[flame blade](ref/spell/flame-blade)_), increased by the additional special abilities'
total base price modifier (see Table 15–9 on page 469 of the _Core Rulebook_). For example, creating
an _aberration-[bane](ref/spell/bane) vicious flame blade_ requires spending a 5th-level spell slot,
which also counts as a 5th-level spell for purposes of dispelling.

This ability alters spontaneous casting.

## Aberration Sense (Ex) {#aberration-sense}

At 1st level, a green scourge adds [Knowledge (dungeoneering)](ref/skill/knowledge-dungeoneering) to
her class skills and gains a +2 bonus on Knowledge (dungeoneering) checks.

This replaces nature sense.

## Scentless (Ex) {#scentless}

At 3rd level, a green scourge cannot be detected or tracked with the [scent](ref/umr/scent) ability
or any other special senses that rely on acute smell. She can choose to exude a scent if desired.

This ability replaces trackless step.

## Resist Unnatural Influence (Ex) {#resist-unnatural-influence}

At 4th level, a green scourge gains a +4 bonus on saving throws against aberrations'
[spell-like abilities](ref/umr/spell-like-abilities), supernatural abilities, and poisons.

This replaces resist nature's lure.
