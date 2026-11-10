+++
id = "ref/arc-bard/silver-balladeer"
kind = "archetype"
title = "Silver Balladeer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Silver%20Balladeer"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "silver_balladeer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "occult-adventures"
page = "115"

[fields]
kind = "archetype"
replaces = ["Suggestion", "Inspire greatness", "Mass suggestion", "Well-versed", "The 2nd-level versatile performance"]
replaces_features = ["well-versed"]
+++

The bright purity of silver makes beautiful music, and its vibrations are also anathema to unnatural
creatures. Some bards use a mixture of silver-stringed instruments and esoteric knowledge to battle
the dark forces of the world.

**Prerequisites:** A silver balladeer must have a good alignment.

**Bardic Performance**

**Info:** A silver balladeer gains the bardic performances listed below. These bardic performances
all require the use of a silver or silver-stringed instrument, which costs twice as much as a normal
[masterwork instrument](ref/eq-misc/musical-instrument-masterwork).

**Break Curse (Su)**

**At 6th Level:** A silver balladeer can suppress a single curse affecting an ally within 30 feet
that is able to see and hear her. Each round the silver balladeer uses _break curse,_ she attempts a
Perform check against the original DC of the curse. If successful, she suppresses the curse for 1
round. After she has suppressed the curse for 4 consecutive rounds, she can attempt a caster level
check to remove the curse as if she had cast [remove curse](ref/spell/remove-curse).

**Replaces:** Suggestion

**Holy Vibration (Su)**

**At 9th Level:** A silver balladeer can spend a round of bardic performance to make a single door
or a window within 30 feet resonate with a holy vibration. Undead and creatures with the evil
subtype are unable to open a door or window affected in this way (as
[arcane lock](ref/spell/arcane-lock)) for 10 minutes per bard level. If such a creature has the
incorporeal subtype, it is unable to move through the affected door or window, or through any walls,
floors, or ceilings within 20 feet of it.

**Replaces:** Inspire greatness

**Special:** Incorporeal creatures can attempt Charisma checks to break through areas warded by holy
vibration, using the same break DC as for the object the creature is trying to move through.

**Mass Break Curse (Su)**

**At 18th Level:** A silver balladeer can suppress all curses among any number of allies within 30
feet when using _break curse._ Every 4 consecutive rounds of using this performance, the silver
balladeer can attempt a caster level check to remove a single curse on a single ally affected by
this performance, as if she had cast _[remove curse](ref/spell/remove-curse)._

**Replaces:** Mass suggestion

**Pure Heart (Ex)**

**Gained:** At 2nd Level

**Passive:** A silver balladeer gains a +4 bonus on saving throws against curses, hexes, and charm
effects.

**Replaces:** Well-versed

**Silver Mastery (Su)**

**Gained:** At 2nd Level

**Passive:** A silver balladeer treats silver weapons as if they were also
[cold iron](ref/eq-material/cold-iron) for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). Also,
[alchemical silver](ref/eq-material/alchemical-silver) weapons do not impose a penalty on damage
rolls when wielded by a silver balladeer, and a silver balladeer gains a +1 bonus on attack rolls
made with [mithral](ref/eq-material/mithral) weapons.

**Replaces:** The 2nd-level versatile performance
