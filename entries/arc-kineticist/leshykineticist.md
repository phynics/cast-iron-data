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
features = [
  { anchor = "leshy-element", level = 6 },
  { anchor = "basic-leshykinesis" },
  { anchor = "photosynthetic-buffer", level = 6 },
  { anchor = "green-rebirth", level = 20 },
]
trades = [
  { replaces = "6th- and 10th-level utility wild talents", feature = "wild-talents", levels = [6, 10], by = ["leshy-element"] },
  { replaces = "maximize metakinesis", feature = "metakinesis", power = "maximize", by = ["leshy-element"] },
  { replaces = "Omnikinesis", feature = "omnikinesis", by = ["green-rebirth"] },
  { alters = "Element", feature = "elemental-focus", by = ["leshy-element"] },
  { alters = "expanded element", feature = "expanded-element", by = ["leshy-element"] },
  { alters = "Basic phytokinesis", feature = "elemental-focus", power = "basic utility wild talent", by = ["basic-leshykinesis"] },
  { alters = "Internal buffer", feature = "internal-buffer", by = ["photosynthetic-buffer"] },
]
+++

Of all those who pursue the path of a kineticist, only leshykineticists are both made of plant
matter and born of nature spirits. These curious creatures wield ancient powers unknown to any other
kineticists.

## Leshy Element {#leshy-element}

A leshykineticist must select the wood [element](ref/ability/elements) (see page 58) as her primary
element and for both her expanded elements. She must choose [wood blast](ref/kinetic/wood-blast) as
her first simple blast and [positive blast](ref/kinetic/positive-blast) as her second simple blast.
At 6th level, she gains [green tongue](ref/kinetic/green-tongue) as a bonus utility wild talent,
ignoring its prerequisites. At 7th level, when she first gains positive blast, she gains
[kinetic healer](ref/kinetic/kinetic-healer) and the
[photokinetic infusion](ref/kinetic/photokinetic-infusion) instead of the extra wild talent of 3rd
level or lower for expanding in the same element. Her kinetic healer wild talent restores 1 extra
hit point per die when healing plant creatures. At 9th level, she gains an extra wild talent of 3rd
level or lower of her choice. At 10th level, she gains
[greater green tongue](ref/kinetic/greater-green-tongue) as a bonus utility wild talent, ignoring
its prerequisites.

This alters element and expanded element, and replaces the 6th- and 10th-level utility wild talents
and maximize metakinesis.

## Basic Leshykinesis (Su) {#basic-leshykinesis}

A vine leshy leshykineticist can use her basic phytokinesis to move while in her alternate vine
form, with a base speed of 10 feet and a climb speed of 10 feet. The vine counts as a prehensile
appendage for the purpose of aiming kinetic blasts and gathering power. At the GM's discretion, this
ability might apply to leshykineticists of other leshy varieties as long as their alternate forms
aren't rooted to the ground (and even then, they might be able to use something like a branch to aim
kinetic blasts).

This alters basic phytokinesis.

## Photosynthetic Buffer {#photosynthetic-buffer}

A leshykineticist fills her buffer with energy photosynthesized from sunlight, rather than from
internal energy. Once per day, she can spend 1 hour motionless in her alternate plant form soaking
in sunlight to fill her internal buffer. However, she can't fill her internal buffer by accepting
burn, and her internal buffer becomes empty whenever her burn is removed. She can't benefit from any
abilities that increase the maximum burn her buffer can hold.

This alters internal buffer.

## Green Rebirth (Su) {#green-rebirth}

At 20th level, a leshykineticist taps into the ancient power of the First World. When her verdant
burst ability activates, it heals all allies and plant creatures in the area as if by a maximized
version of her kinetic healer ability, rather than only 1d8 hit points. After 24 hours, one of the
plants that grew in the area serves as a vessel for the leshykineticist's spirit again, allowing her
to return to life without penalty. Killing all the new plants that grew from her verdant burst
within 24 hours prevents her from reviving in this way.

This replaces omnikinesis.
