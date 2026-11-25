+++
id = "ref/arc-kineticist/kinetic-chirurgeon"
kind = "archetype"
title = "Kinetic Chirurgeon"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Kinetic%20Chirurgeon"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kinetic_chirurgeon", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "occult-adventures"
page = "90"

[fields]
kind = "archetype"
features = [
  { anchor = "kinetic-chirurgery", level = 1 },
  { anchor = "metahealer", level = 5 },
  { anchor = "healing-buffer", level = 6 },
]
trades = [
  { replaces = "Infusions", feature = "infusion", by = ["kinetic-chirurgery"] },
  { replaces = "Metakinesis", feature = "metakinesis", by = ["metahealer"] },
  { replaces = "infusion specialization", feature = "infusion-specialization", by = ["metahealer"] },
  { alters = "Internal buffer", feature = "internal-buffer", by = ["healing-buffer"] },
]
+++

While any hydrokineticist or telekineticist can learn the rudiments of healing, some kineticists are
virtuosos of the curative arts.

## Kinetic Chirurgery (Su) {#kinetic-chirurgery}

A kinetic chirurgeon must select either aether or water as her primary
[element](ref/ability/elements). She gains [kinetic healer](ref/kinetic/kinetic-healer) as a bonus
wild talent at 1st level. At 3rd level and every 2 levels thereafter, the kinetic chirurgeon can
select any one [paladin](ref/class/paladin) mercy that a paladin of that level could select. Each
time she uses kinetic healer, she can apply one of these mercies to the target of the healing. A
kinetic chirurgeon can never use infusions. This ability replaces infusions.

## Metahealer (Su) {#metahealer}

Starting at 5th level, a kinetic chirurgeon can apply any one of the following metahealer abilities
to her kinetic healer wild talent instead of using her mercies. At 5th level, she can choose to roll
one additional die when using kinetic healer. This increases to two additional dice at 11th level,
and to three additional dice at 17th level. At 9th level, she can choose to bring an ally who died
within 1 round back from the dead; this functions similarly to the
_[breath of life](ref/spell/breath-of-life)_ spell. The ally regains the normal number of hit points
from kinetic healer. An ally revived in this way takes 1 additional point of burn, beyond the normal
1 point of burn that either the kinetic chirurgeon or the ally must accept as a cost of the kinetic
healer wild talent. At 13th level, a kinetic chirurgeon can choose to use kinetic healer on herself
as a swift action. At 17th level, she can choose to heal both herself and another target with the
same use of kinetic healer, although in that case, both she and her target must each accept 1 point
of burn, instead of only one of them needing to do so as normal for kinetic healer. Regardless of
her level, the kinetic chirurgeon can apply only one metahealer ability to a single use of kinetic
healer. For instance, she could not bring back a dead ally and also roll extra dice for healing.
This ability replaces metakinesis and infusion specialization.

## Healing Buffer (Su) {#healing-buffer}

At 6th level, a kinetic chirurgeon's internal buffer has double the usual maximum size, and she can
use it only when she would accept points of burn for the kinetic healer wild talent. This ability
alters internal buffer.
