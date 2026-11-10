+++
id = "ref/arc-kineticist/aquakinetcist"
kind = "archetype"
title = "Aquakinetcist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Aquakinetcist"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aquakinetcist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "aquatic-adventures"
page = "50"

[fields]
kind = "archetype"
replaces = ["Basic hydrokinesis", "2nd and 6th level utility wild talents", "Defense wild talent from elemental defense"]
alters = ["Expanded element", "Elemental focus", "Cold simple blast"]
alters_features = ["expanded-element", "elemental-focus"]
+++

While all hydrokineticists have the ability to control water, aquakineticists' powers are tied to
their determination to explore the world beneath the waves.

**Aquatic Focus**

**Alters:** Expanded element

**Info:** An aquakineticist must choose water as her primary [element](ref/ability/elements) and for
both _expanded elements,_ and must choose [water blast](ref/kinetic/water-blast) as her first simple
blast.

**Basis Aquakinesis (Sp)**

**Ability:** An aquakineticist can create mild currents, as per
[basic hydrokinesis](ref/kinetic/basic-hydrokinesis). Additionally, she can adjust her
[buoyancy](ref/rule/buoyancy) to whatever level she wishes as a **standard action**, lasting until
she uses basic aquakinesis again.

**Alters:** Elemental focus

**Replaces:** Basic hydrokinesis

**Call of the Deep**

**At 2nd Level:** An aquakineticist gains [waterdancer](ref/kinetic/waterdancer) as a bonus utility
wild talent.

**At 6th Level:** She gains [watersense](ref/kinetic/watersense) as a bonus utility wild talent, and
she can choose to ignore the effects of [currents](ref/rule/currents-and-running-water) with speeds
up to 60 feet while her _waterdancer_ ability is active.

**Replaces:** 2nd and 6th level utility wild talents

**Ocean's Caress (Su)**

**Ability:** An aquakineticist can breathe underwater as easily as she breathes air, and she gains
[cold adaptation](ref/kinetic/cold-adaptation) as a bonus utility wild talent, adding half her
kineticist level to her cold [resistance](ref/umr/resistance) from cold adaptation. By accepting 1
point of burn, she can increase her cold resistance by an additional 3, stacking with the resistance
she gains from cold adaptation. If her total cold resistance from this ability would ever be 40 or
higher, she gains cold [immunity](ref/umr/immunity) instead. All cold resistance and immunity from
this ability also applies to [pressure damage](ref/rule/water-dangers), and she
[adjusts to a new pressure](ref/rule/oceanic-zones) all at once after making five Fortitude saves,
rather than 100 feet at a time. Whenever she accepts burn while using a water wild talent, the water
coalescing around her doubles her cold resistance for 1 round (which might trigger cold immunity).
She can dismiss or restore this effect as an **immediate action**.

**Gained:** At 2nd Level

**Replaces:** Defense wild talent from elemental defense

**Ice Propagation (Su)**

**Ability:** An aquakineticist's connection to the water around her allows her greater control over
the ice formed by her cold attacks. When using her cold blast underwater (which
[freezes water into ice](ref/rule/spells) and deals half piercing damage), she can make the cold
blast a physical blast and apply any form or substance infusions that she could apply to an ice
composite blast. This still deals damage as per a simple physical blast, not a composite blast.

**Alters:** Cold simple blast

**Gained:** At 7th Level
