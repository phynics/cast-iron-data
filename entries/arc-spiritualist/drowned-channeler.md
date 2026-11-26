+++
id = "ref/arc-spiritualist/drowned-channeler"
kind = "archetype"
title = "Drowned Channeler"
aon = "ArchetypeDisplay.aspx?FixedName=Spiritualist%20Drowned%20Channeler"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drowned_channeler", path = "json/archetypes_spiritualist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/spiritualist" },
]
[[sources]]
publication = "aquatic-adventures"
page = "52"

[fields]
kind = "archetype"
features = [
  { anchor = "drowned-phantom", level = 1 },
  { anchor = "drowned-spells", level = 2 },
  { anchor = "drowned-powers", level = 5 },
]
trades = [
  { replaces = "Bonded senses", feature = "bonded-senses", by = ["drowned-spells"] },
  { replaces = "Detect undead", feature = "detect-undead", by = ["drowned-powers"] },
  { replaces = "calm spirit", feature = "calm-spirit", by = ["drowned-powers"] },
  { replaces = "see invisibility", feature = "see-invisibility", by = ["drowned-powers"] },
  { replaces = "call spirit", feature = "call-spirit", by = ["drowned-powers"] },
  { alters = "Phantom", feature = "phantom", by = ["drowned-phantom"] },
  { alters = "shared consciousness", feature = "shared-consciousness", by = ["drowned-phantom"] },
  { alters = "etheric tether", feature = "etheric-tether", by = ["drowned-phantom"] },
  { alters = "bonded manifestation", feature = "bonded-manifestation", by = ["drowned-phantom"] },
  { alters = "Class skills" },
]
+++

When a drowned spirit doomed to a watery grave descends toward the evil of undeath and seeks refuge
in a mortal shell, the result is an unusual spiritualist with powers that resonate with the drowned
spirit's demise.

## Class Skills {#class-skills}

A drowned channeler has Swim as a class skill instead of Fly.

This alters the spiritualist's class skills.

## Drowned Phantom {#drowned-phantom}

A drowned channeler has a drowned phantom. A drowned phantom's ectoplasmic body drips with
[water](ref/subtype/water) and seems to bleed off watery droplets even its incorporeal form. A
drowned phantom gains a swim speed of 30 feet in both forms and gains the water subtype in addition
to the phantom subtype, meaning that it can use its natural slam attacks underwater without taking
the penalty for bludgeoning attacks underwater. The drowned channeler's etheric tether extends twice
as far underwater, but only half as far above water. Additionally, the drowned phantom doesn't grant
any of the usual benefits while confined in the drowned channeler's consciousness unless the drowned
channeler is within 25 feet of an ocean, sea, lake, or other large body of water. Both forms of
bonded manifestation grant the drowned phantom's swim speed of 30 feet to the drowned channeler, and
attacks from the ectoplasmic bonded manifestation's tendrils don't take the typical penalties for
bludgeoning attacks underwater, as if the phantom itself made them.

This ability alters phantom, shared consciousness, etheric tether, and bonded manifestation.

## Drowned Spells {#drowned-spells}

At 2nd level, a drowned channeler adds _control water_, _fluid form_, _hydraulic push_, _hydraulic
torrent_, _life current_\*, _pressure adaptation_\*, _ride the waves_, _slipstream_, _stabilize
pressure_\*, _unlife current_\*, _water breathing_, and _wave form_\* to the spiritualist spell list
at the same spell level as they appear on the cleric list or sorcerer/wizard list, whichever is
lower. Spells marked with an asterisk (\*) appear in the Aquatic Spells section of this book (see
page 59). The drowned channeler must still select them as spells known as normal.

This ability replaces bonded senses.

## Drowned Powers (Sp) {#drowned-powers}

At 5th level, a drowned channeler can use _[hydraulic push](ref/spell/hydraulic-push)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day, with an additional use each day at
9th level and every 4 levels thereafter. At 7th level, she can use
_[slipstream](ref/spell/slipstream)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities), with an additional use each day at 11th level
and every 4 levels thereafter. At 9th level, she can use
_[ride the waves](ref/spell/ride-the-waves)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities). Finally, at 16th level, she can use
_[fluid form](ref/spell/fluid-form)_ once per day as a
[spell-like ability](ref/umr/spell-like-abilities).

This ability replaces _detect undead_, _calm spirit_, _see invisibility_, and _call spirit_.
