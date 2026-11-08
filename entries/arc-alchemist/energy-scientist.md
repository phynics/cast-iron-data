+++
id = "ref/arc-alchemist/energy-scientist"
kind = "archetype"
title = "Energy Scientist"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "energy_scientist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "archetype"
replaces = ["Brew potion", "Poison resistance", "poison immunity", "Poison use", "swift poisoning"]
alters = ["Bombs", "Alchemy"]
+++

**Sources:** Elemental Master's Handbook pg 30\
Energy scientists fervently prepare themselves to overcome exposure to specific elemental hazards so
that they can traverse the Elemental Planes in search of novel discoveries and reagents.

**Gained class skills:** kp, swim

**Energy Bombs (Su)**

**Alters:** Bombs

**Gained:** At 1st Level

**Passive:** Whenever an energy scientist regains his daily uses of bombs, he must attune to one
element and its corresponding energy type: air (electricity), earth (acid), fire (fire), or water
(cold). The energy scientist's bombs deal the type of energy damage that corresponds to his attuned
element until he regains his daily uses of bombs, at which point he must attune to one element
again.

**Replaces:** Brew potion

**Special:** If the energy scientist uses a discovery that changes his bomb's damage type to one
that is different from that of his attuned element (such as using the
[acid bomb](ref/discovery/acid-bomb) discovery when the alchemist is attuned to fire), instead of
its normal amount of damage, the bomb deals 1d4 points of damage, plus 1d4 for every odd-numbered
alchemist level.

**Limited Extracts (Ex)**

**Alters:** Alchemy

**Gained:** At 1st Level

**Passive:** An energy scientist reduces his extracts per day by 1 for each extract level he can
create, and he cannot prepare extracts with an elemental or energy descriptor that doesn't match his
attuned element.

**Attuned Resistance (Ex)**

**At 10th Level:** An energy scientist gains the effect of
[planar adaptation](ref/spell/planar-adaptation) for the Elemental Plane tied to his currently
attuned element.

**At 5th Level:** The bonus becomes +3.

**At 8th Level:** The bonus becomes +4.

**Gained:** At 2nd Level

**Passive:** An energy scientist gains a +2 bonus on all saving throws against effects with
descriptors that match his currently attuned element or its corresponding energy type, or that deal
his currently attuned element's corresponding energy damage.

**Replaces:** Poison resistance, poison immunity

**Salvage Energy (Ex)**

**Ability:** An energy scientist can siphon power from slain elementals into temporary alchemical
weapons. While studying the remains of an elemental that has been dead for no longer than 1 minute
per alchemist level, you can attempt a Craft (alchemy) check (DC = 20 + the elemental's CR) as a
standard action. Success means the alchemist produces a number of canisters of
[alchemist's fire](ref/eq-weapon/alchemists-fire) (from fire and magma elementals),
[bottled lightning](ref/eq-weapon/bottled-lightning) (from air and lightning elementals),
[deadground dust](ref/eq-weapon/deadground-dust) (from earth and mud elementals), or
[liquid ice](ref/eq-siegeengine/liquid-ice) (from water and ice elementals) equal to half the
elemental's CR, rounded down. These items cannot be sold and become inert after 24 hours.

**At 6th Level:** The save DCs of the items produced increase by 2.

**Gained:** At 2nd Level

**Replaces:** Poison use, swift poisoning
