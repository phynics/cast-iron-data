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
replaces = ["Nature sense", "Trackless step", "Resist nature's lure"]
alters = ["Spontaneous casting"]
replaces_features = ["nature-sense", "trackless-step", "resist-nature-s-lure"]
alters_features = ["spontaneous-casting"]
+++

Green scourges are militant druids sworn to restore natural order. They're less concerned with
nurturing the natural world than most druids, instead focusing their efforts on slaying corrupted
creatures.

**Nature's Armaments**

**Ability:** A green scourge can lose a prepared 1st- or 2nd-level spell in order to cast
[shillelagh](ref/spell/shillelagh) or [flame blade](ref/spell/flame-blade), respectively. She can
instead choose to lose a higher-level spell in order to increase the enhancement bonus of her
_[shillelagh](ref/spell/shillelagh),_ or to add any of the following weapon special abilities to her
_[shillelagh](ref/spell/shillelagh)_ or _flame blade:_ [bane](ref/magic-enh/bane) (aberrations
only), [frost](ref/magic-enh/frost), [mighty cleaving](ref/magic-enh/mighty-cleaving),
[returning](ref/magic-enh/returning), [shock](ref/magic-enh/shock),
[throwing](ref/magic-enh/throwing), or [vicious](ref/magic-enh/vicious).

**Alters:** Spontaneous casting

**Info:** When adding weapon special abilities or increasing the enhancement bonus, the final level
of the spell expended is 1 higher than the base spell level (2nd for
_[shillelagh](ref/spell/shillelagh)_ and 3rd for _[flame blade](ref/spell/flame-blade)_), increased
by the additional special abilities' total base price modifier. For example, creating an
_aberration-bane vicious flame blade_ requires spending a 5th-level spell slot (3 for
_[flame blade](ref/spell/flame-blade),_ +1 for _[bane](ref/spell/bane),_ +1 for _vicious_ = 5),
which also counts as a 5th-level spell for purposes of dispelling.

**Special:** If the target weapon is a [quarterstaff](ref/eq-weapon/quarterstaff), these bonuses
apply to only one of its ends. If a _[flame blade](ref/spell/flame-blade)_ gains the _frost_ or
_shock_ special ability, the base damage of the spell changes to match the energy type; neither a
_[flame blade](ref/spell/flame-blade)_ nor _[shillelagh](ref/spell/shillelagh)_ can gain both of
these special abilities. A green scourge cannot add the _throwing_ property to a
_[flame blade](ref/spell/flame-blade)_ unless she also adds the _returning_ property.

**Aberration Sense (Ex)**

**Gained:** At 1st Level

**Passive:** A green scourge adds [Knowledge (dungeoneering)](ref/skill/knowledge-dungeoneering)
(INT) to her class skills and gains a +2 bonus on Knowledge (dungeoneering) checks.

**Replaces:** Nature sense

**Scentless (Ex)**

**Gained:** At 3rd Level

**Passive:** A green scourge cannot be detected or tracked with the [scent](ref/umr/scent) ability
or any other special senses that rely on acute smell. She can choose to exude a scent if desired.

**Replaces:** Trackless step

**Resist Unnatural Influence (Ex)**

**Gained:** At 4th Level

**Passive:** A green scourge gains a +4 bonus on saving throws against aberrations'
[spell-like abilities](ref/umr/spell-like-abilities), supernatural abilities, and poisons.

**Replaces:** Resist nature's lure
