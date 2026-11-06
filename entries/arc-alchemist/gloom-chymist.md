+++
id = "ref/arc-alchemist/gloom-chymist"
kind = "archetype"
title = "Gloom Chymist"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gloom_chymist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]

[fields]
kind = "none"
+++

**Sources:** Blood of Shadows pg 18\
A breakthrough in Nidalese alchemy led to the creation of glooms, magical fields of darkness from
the Shadow Plane that can be momentarily animated with the use of strange compounds. These mixtures
are quite efficacious, leading to the spread of their use throughout the rest of the Inner Sea
region.

**Gloom (Su)**

**Ability:** A gloom chymist is skilled at mixing potent concoctions known as glooms, which are
infused with shadow energy. A gloom is identical to a bomb except that it deals 1d6 points of cold
damage + additional damage equal to the gloom chymist's Intelligence modifier. This damage increases
by 1d6 for every 2 alchemist levels beyond 1st the gloom chymist has. A gloom does not qualify as a
bomb for the purposes of feats or discoveries.

**Gained:** At 1st Level

**Replaces:** Bomb

**Umbral Gloom (Su)**

**Ability:** Whenever a gloom chymist makes a gloom, he can have it increase or decrease the
[light level](ref/rule/vision-and-light) by one step within its splash radius, in addition to its
other effects. This change lasts for a number of rounds equal to the gloom chymist's Intelligence
modifier.

**At 8th Level:** The gloom chymist can expend two uses of his daily glooms to increase or decrease
light levels as per [daylight](ref/spell/daylight) or [deeper darkness](ref/spell/deeper-darkness),
respectively, using his alchemist level as the caster level.

**Gained:** At 2nd Level

**Replaces:** Poison resistance, poison use, swift poisoning

### Gloom Discoveries

These discoveries are only available to alchemists with the Gloom feature.

**Bounding Gloom**

**Ability:** The alchemist gains the ability to travel between shadows as if by means of a
[dimension door](ref/spell/dimension-door) spell. The limitation is that the alchemist's beginning
and ending locations must be areas of dim light or darker, or within the radius of an _umbral gloom_
that is lowering the light level. The alchemist can travel up to a total of 100 feet each day in
this way. This distance must be used in 10-foot increments; for example, the alchemist can make a
single jump of 100 feet or 10 jumps of 10 feet each.

**Prereq:** 10th-level alchemist

**Special:** For every 2 levels beyond 10th, the distance the alchemist can jump each day doubles
(200 feet at 12th level, 400 feet at 14th level, and so on).

#### Primary Bomb Discoveries (Gloom)

Only one of these discoveries can be applied to a bomb, and it cannot have another discovery applied
to it with the same one-per-bomb limit (Primary Bomb Discoveries).

**Debilitating Gloom**

**Ability:** A creature struck by the gloom must make a successful Fortitude save or take a penalty
to its Strength equal to 1d4 + 1 per 2 alchemist levels (maximum of 1d4+5) for 1 round per alchemist
level. A target's Strength score cannot drop below 1. This penalty does not stack with itself.

**Prereq:** 6th-level alchemist

**Draining Gloom**

**Ability:** A creature struck by a direct hit with the gloom must make a successful Fortitude save
or gain 1 negative level.

**Prereq:** 8th-level, _debilitating gloom_ discovery

**Greater Draining Gloom**

**Ability:** A creature struck by the gloom must succeed at a Fortitude save or gain 1d4 negative
levels.

**Prereq:** 12th-level alchemist, _debilitating gloom_ and _draining gloom_ discoveries

**Glutinous Gloom**

**Ability:** The gloom creates an area in its splash radius that functions as [web](ref/spell/web).
The webbing lasts for a number of rounds equal to [half](ref/misc/fractions-and-rounding) the
alchemist's level.

**Prereq:** 6th-level alchemist

**Grasping Gloom**

**Ability:** The gloom creates an area equal to double its splash radius that functions as
[black tentacles](ref/spell/black-tentacles). The effect lasts for a number of rounds equal to half
the alchemist's level.

**Prereq:** 8th-level alchemist

**Mucilaginous Gloom**

**Ability:** The gloom leaves a chilly gray residue that turns each square in its splash radius into
[difficult terrain](ref/rule/terrain-and-obstacles). This effect lasts for a number of rounds equal
to the alchemist's level.

**Rime-Bound Gloom**

**Ability:** The gloom creates an area of freezing shadow in its splash radius that deals 2d6 points
of cold damage to all creatures in the area each turn. This effect lasts a number of rounds equal to
half the alchemist's level.

**Prereq:** 6th-level alchemist
