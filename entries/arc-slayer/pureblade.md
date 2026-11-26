+++
id = "ref/arc-slayer/pureblade"
kind = "archetype"
title = "Pureblade"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Pureblade"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pureblade", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-origins"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "aberration-hunter", level = 1 },
  { anchor = "alien-prescience", level = 2 },
  { anchor = "discern-weakness", level = 7 },
  { anchor = "steely-mind", level = 8 },
  { anchor = "aberration-slayer", level = 20 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["aberration-hunter"] },
  { replaces = "Slayer talent received at 2nd level", feature = "slayer-talents", levels = [2], by = ["alien-prescience"] },
  { replaces = "Stalker", feature = "stalker", by = ["discern-weakness"] },
  { replaces = "Slayer talent received at 8th level", feature = "slayer-talents", levels = [8], by = ["steely-mind"] },
  { alters = "Master slayer", feature = "master-slayer", by = ["aberration-slayer"] },
]
+++

First known in Numeria, these aberration hunters have spread to other regions of Golarion, even as
far as the lands bordering the Mana Wastes. In Numeria, Pureblades are skilled at slaying naturally
arising [aberrations](ref/type/aberration) and any creatures that have been mutated by exposure to
the bizarre alien technology that pervades the land. Pureblades from Alkenstar and Nex lead forays
into the magic-starved Mana Wastes to eliminate aberrations before the creatures can threaten their
lands.

## Aberration Hunter (Ex) {#aberration-hunter}

If a Pureblade deals damage to an aberration, as an immediate action he can apply his studied target
bonus against that target even if he didn't sneak attack it. In addition, a Pureblade can attempt
Knowledge (dungeoneering) skill checks untrained when trying to identify aberrations. This ability
replaces track.

## Alien Prescience (Sp) {#alien-prescience}

At 2nd level, as a standard action a Pureblade can detect aberrations. This works like
_[detect undead](ref/spell/detect-undead)_, except it detects aberrations instead of undead. This
ability replaces the slayer talent received at 2nd level.

## Discern Weakness (Ex) {#discern-weakness}

At 7th level, a Pureblade becomes an expert at locating an aberration's weak points. The Pureblade
rolls twice to confirm critical hits against aberrations and keeps the higher roll. This ability
replaces stalker.

## Steely Mind (Ex) {#steely-mind}

At 8th level, a Pureblade gains a +2 resistance bonus on saving throws against mind-affecting spells
and effects. This bonus increases to +4 at 12th level and +6 at 16th level. In addition, once per
day as a standard action, a Pureblade can shed a magical effect placed on him by an aberration as
_[break enchantment](ref/spell/break-enchantment)_, using his slayer level as his caster level. A
Pureblade can use this ability twice per day at 12th level and three times per day at 16th level.
This ability replaces the slayer talent received at 8th level.

## Aberration Slayer (Ex) {#aberration-slayer}

At 20th level, a Pureblade can use his master slayer ability on any aberration, even if it's not his
studied target. This ability alters master slayer.
