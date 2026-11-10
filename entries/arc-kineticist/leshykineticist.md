+++
id = "ref/arc-kineticist/leshykineticist"
kind = "archetype"
title = "Leshykineticist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Leshykineticist"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "leshykineticist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "23"

[fields]
kind = "archetype"
replaces = ["6th- and 10th-level utility wild talents", "maximize metakinesis", "Omnikinesis"]
alters = ["Element", "expanded element", "Basic phytokinesis", "Internal buffer"]
replaces_features = ["omnikinesis"]
alters_features = ["expanded-element", "internal-buffer"]
+++

Of all those who pursue the path of a kineticist, only leshykineticists are both made of plant
matter and born of nature spirits. These curious creatures wield ancient powers unknown to any other
kineticists.

**Prerequisites:** Vine leshy

**Leshy Element**

**Alters:** Element, expanded element

**At 10th Level:** She gains [greater green tongue](ref/kinetic/greater-green-tongue) as a bonus
utility wild talent, ignoring its prerequisites.

**At 6th Level:** She gains [green tongue](ref/kinetic/green-tongue) as a bonus utility wild talent,
ignoring its prerequisites.

**At 7th Level:** When she first gains _positive blast,_ she gains
[kinetic healer](ref/kinetic/kinetic-healer) and the
[photokinetic infusion](ref/kinetic/photokinetic-infusion) instead of the extra wild talent of 3rd
level or lower for expanding in the same element. Her _kinetic healer_ wild talent restores 1 extra
hit point per die when healing plant creatures.

**At 9th Level:** She gains an extra wild talent of 3rd level or lower of her choice.

**Info:** A leshykineticist must select the wood [element](ref/ability/elements) as her primary
element and for both her _expanded elements._ She must choose [wood blast](ref/kinetic/wood-blast)
as her first simple blast and [positive blast](ref/kinetic/positive-blast) as her second simple
blast.

**Replaces:** 6th- and 10th-level utility wild talents, maximize metakinesis

**Basic Leshykinesis (Su)**

**Ability:** A vine leshy leshykineticist can use her _basic phytokinesis_ to move while in her
alternate vine form, with a base speed of 10 feet and a climb speed of 10 feet. The vine counts as a
prehensile appendage for the purpose of aiming kinetic blasts and _gathering power._

**Alters:** Basic phytokinesis

**Special:** At the GM's discretion, this ability might apply to leshykineticists of other leshy
varieties as long as their alternate forms aren't rooted to the ground (and even then, they might be
able to use something like a branch to aim kinetic blasts).

**Photosynthetic Buffer**

**Ability:** A leshykineticist fills her _buffer_ with energy photosynthesized from sunlight, rather
than from internal energy. Once per day, she can spend 1 hour motionless in her alternate plant form
soaking in sunlight to fill her _internal buffer._ However, she can't fill her _internal buffer_ by
accepting burn, and her _internal buffer_ becomes empty whenever her burn is removed.

**Alters:** Internal buffer

**Special:** She can't benefit from any abilities that increase the maximum burn her _buffer_ can
hold.

**Green Rebirth (Su)**

**Ability:** A leshykineticist taps into the ancient power of the First World. When her _verdant
burst_ ability activates, it heals all allies and plant creatures in the area as if by a maximized
version of her _kinetic healer_ ability, rather than only 1d8 hit points. After 24 hours, one of the
plants that grew in the area serves as a vessel for the leshykineticist's spirit again, allowing her
to return to life without penalty. Killing all the new plants that grew from her _verdant burst_
within 24 hours prevents her from reviving in this way.

**Gained:** At 20th Level

**Replaces:** Omnikinesis
