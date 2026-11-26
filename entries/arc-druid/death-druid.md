+++
id = "ref/arc-druid/death-druid"
kind = "archetype"
title = "Death Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Death%20Druid"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "death_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "horror-adventures"
page = "50"

[fields]
kind = "archetype"
features = [
  { anchor = "phantom", level = 1 },
  { anchor = "soul-magic", level = 1 },
  { anchor = "resist-death-s-call", level = 4 },
  { anchor = "negative-immunity", level = 9 },
]
trades = [
  { replaces = "Nature bond", feature = "nature-bond", by = ["phantom"] },
  { replaces = "wild shape", feature = "wild-shape", by = ["phantom"] },
  { replaces = "Nature sense", feature = "nature-sense", by = ["soul-magic"] },
  { replaces = "wild empathy", feature = "wild-empathy", by = ["soul-magic"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["resist-death-s-call"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["negative-immunity"] },
]
+++

Some druids believe that birth and death are the most important parts of the natural cycle. They
focus on destroying undead and putting troubled souls to rest.

## Phantom {#phantom}

A death druid attracts phantoms like a [spiritualist](ref/class/spiritualist), though she focuses
her efforts on putting those phantoms to rest. A death druid is continually attempting to figure out
how to send her [phantom](ref/sidekick/phantom) to the afterlife (usually by completing the
phantom's unfinished business as determined by the GM). If she is able to do so, she gains a new
phantom with no additional effort on her part, sometime during the next week. At 1st level, she
gains the spiritualist's phantom and etheric tether class features; at 4th level, she gains the
bonded manifestation class feature; and at 14th level, she gains the spiritual bond class feature.
She does not gain any of the other spiritualist abilities related to phantoms. The death druid
treats her druid level as her spiritualist level for these abilities.

This ability replaces nature bond and wild shape.

## Soul Magic {#soul-magic}

A death druid adds the following spells to her druid spell list at the given spell levels: 0—_grave
words_; 1st—_sanctify corpse_; 2nd—_calm spirit_, _false life_, _ghostbane dirge_, _spiritual
weapon_; 3rd—_speak with dead_; 4th—_speak with haunt_, _spiritual ally_; 5th—_breath of life_,
_call spirit, mass ghostbane dirge_; 6th—_circle of death_, _undeath to death_.

This ability replaces nature sense and wild empathy.

## Resist Death's Call (Ex) {#resist-death-s-call}

At 4th level, a death druid gains a +4 bonus on saving throws against death effects, negative
energy, and energy drain.

This ability replaces resist nature's lure.

## Negative Immunity (Su) {#negative-immunity}

At 9th level, a death druid is immune to negative energy and energy drain.

This ability replaces venom immunity.
