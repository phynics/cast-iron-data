+++
id = "ref/arc-kineticist/aquakinetcist"
kind = "archetype"
title = "Aquakineticist"
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
features = [
  { anchor = "aquatic-focus", level = 7 },
  { anchor = "basis-aquakinesis", level = 1 },
  { anchor = "call-of-the-deep", level = 2 },
  { anchor = "ocean-s-caress", level = 2 },
  { anchor = "ice-propagation", level = 7 },
]
trades = [
  { replaces = "Basic hydrokinesis as her basic utility talent", feature = "elemental-focus", power = "basic utility wild talent", by = ["basis-aquakinesis"] },
  { replaces = "2nd and 6th level utility wild talents", feature = "wild-talents", levels = [2, 6], by = ["call-of-the-deep"] },
  { replaces = "Defense wild talent from elemental defense", feature = "elemental-defense", by = ["ocean-s-caress"] },
  { alters = "Expanded element", feature = "expanded-element", by = ["aquatic-focus"] },
  { alters = "Elemental focus", feature = "elemental-focus", by = ["basis-aquakinesis"] },
  { alters = "Cold simple blast", by = ["ice-propagation"] },
]
+++

While all hydrokineticists have the ability to control water, aquakineticists' powers are tied to
their determination to explore the world beneath the waves.

## Aquatic Focus {#aquatic-focus}

An aquakineticist must choose water as her primary [element](ref/ability/elements) and for both
expanded elements, and must choose [water blast](ref/kinetic/water-blast) as her first simple blast.

This ability alters expanded element.

## Basis Aquakinesis (Sp) {#basis-aquakinesis}

An aquakineticist can create mild currents, as per
[basic hydrokinesis](ref/kinetic/basic-hydrokinesis). Additionally, she can adjust her
[buoyancy](ref/rule/buoyancy) (see page 43) to whatever level she wishes as a standard action,
lasting until she uses basic aquakinesis again.

This ability replaces basic hydrokinesis as her basic utility talent, and alters elemental focus.

## Call of the Deep {#call-of-the-deep}

At 2nd level, an aquakineticist gains [waterdancer](ref/kinetic/waterdancer) as a bonus utility wild
talent. At 6th level, she gains [watersense](ref/kinetic/watersense) as a bonus utility wild talent,
and she can choose to ignore the effects of [currents](ref/rule/currents-and-running-water) with
speeds up to 60 feet while her waterdancer ability is active.

This replaces the 2nd and 6th level utility wild talents.

## Ocean's Caress (Su) {#ocean-s-caress}

At 2nd level, an aquakineticist can breathe underwater as easily as she breathes air, and she gains
[cold adaptation](ref/kinetic/cold-adaptation) as a bonus utility wild talent, adding half her
kineticist level to her cold [resistance](ref/umr/resistance) from cold adaptation. By accepting 1
point of burn, she can increase her cold resistance by an additional 3, stacking with the resistance
she gains from cold adaptation. If her total cold resistance from this ability would ever be 40 or
higher, she gains cold [immunity](ref/umr/immunity) instead. All cold resistance and immunity from
this ability also applies to [pressure damage](ref/rule/water-dangers), and she
[adjusts to a new pressure](ref/rule/oceanic-zones) all at once after making five Fortitude saves,
rather than 100 feet at a time (see Pressure on page 48).

Whenever she accepts burn while using a water wild talent, the water coalescing around her doubles
her cold resistance for 1 round (which might trigger cold immunity).

She can dismiss or restore this effect as an immediate action.

This ability replaces the defense wild talent from elemental defense.

## Ice Propagation (Su) {#ice-propagation}

At 7th level, an aquakineticist's connection to the water around her allows her greater control over
the ice formed by her cold attacks. When using her cold blast underwater (which
[freezes water into ice](ref/rule/spells) and deals half piercing damage; see cold spells on page
46), she can make the cold blast a physical blast and apply any form or substance infusions that she
could apply to an ice composite blast. This still deals damage as per a simple physical blast, not a
composite blast.

This ability alters her cold simple blast.
