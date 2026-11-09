+++
id = "ref/arc-druid/blight-druid"
kind = "archetype"
title = "Blight Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Blight%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blight_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "98"

[fields]
kind = "archetype"
replaces = ["Wild empathy", "Trackless step", "resist nature's lure", "Venom immunity", "A thousand faces"]
alters = ["Nature bond"]
+++

The devoted servants of nature corrupted, ruined, and destroyed, blight druids are the caretakers of
lands ravaged by natural disaster. While some are devoted to reforming and reclaiming lands
despoiled by the ravages of civilization, others seek out the more rapacious violence inherent in
nature and feed the creeping rot and decay that brings an end to all things.

**Nature Bond (Ex)**

**Alters:** Nature bond

**Choice:** A blight druid may not bond with an animal companion, but may either call a
[familiar](ref/sidekick/familiar) as a [wizard](ref/class/wizard) of her druid level or select from
the Darkness, Death, and [Destruction](ref/domain/destruction) domains in addition to those normally
available.

**Vermin Empathy (Su)**

**Ability:** A blight druid can improve the attitude of vermin as a normal druid can with animals.
Vermin have a starting attitude of unfriendly. The blight druid can also improve the attitude of
animals and mindless undead creatures that were formerly animals, but she takes a -4 penalty on the
check unless the animal or undead has a disease special attack.

**Replaces:** Wild empathy

**Miasma (Ex)**

**Gained:** At 5th Level

**Passive:** If a blight druid is adjacent to a creature at the beginning of its turn, the creature
must succeed at a Fortitude save with a DC of 10 + [half](ref/misc/fractions-and-rounding) the
druid's level + the druid's Wisdom modifier or become [sickened](ref/misc/sickened) for 1 round. A
creature of the animal, fey, or plant type that fails its save is [nauseated](ref/misc/nauseated)
for 1 round and sickened for 1 minute thereafter. If the creature makes its save, it is immune to
this effect for 24 hours, as are creatures immune to disease.

**Replaces:** Trackless step, resist nature's lure

**Blightblooded (Ex)**

**Gained:** At 9th Level

**Passive:** A blight druid gains immunity to all diseases, including natural and supernatural
diseases. She also becomes immune to effects that would cause her to become sickened or nauseated.

**Replaces:** Venom immunity

**Plaguebearer (Su)**

**Gained:** At 13th Level

**Passive:** Any creature that strikes a blight druid with a touch attack, unarmed strike, or
natural weapon must succeed at a Fortitude save with a DC of 10 + 1/2 the druid's level + the
druid's Wisdom modifier or contract a disease, as the [contagion](ref/spell/contagion) spell. If the
creature makes its save, it is immune to this effect for 24 hours.

**Replaces:** A thousand faces
