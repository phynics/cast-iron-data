+++
id = "ref/arc-alchemist/gloom-chymist"
kind = "archetype"
title = "Gloom Chymist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Gloom%20Chymist"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gloom_chymist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "blood-of-shadows"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "gloom", level = 1 },
  { anchor = "umbral-gloom", level = 2 },
]
trades = [
  { replaces = "Bomb", feature = "bomb", by = ["gloom"] },
  { replaces = "Poison resistance", feature = "poison-resistance", by = ["umbral-gloom"] },
  { replaces = "poison use", feature = "poison-use", by = ["umbral-gloom"] },
  { replaces = "swift poisoning", feature = "swift-poisoning", by = ["umbral-gloom"] },
]
+++

A breakthrough in Nidalese alchemy led to the creation of glooms, magical fields of darkness from
the Shadow Plane that can be momentarily animated with the use of strange compounds. These mixtures
are quite efficacious, leading to the spread of their use throughout the rest of the Inner Sea
region.

## Gloom (Su) {#gloom}

A gloom chymist is skilled at mixing potent concoctions known as glooms, which are infused with
shadow energy. A gloom is identical to a bomb except that it deals 1d6 points of cold damage +
additional damage equal to the gloom chymist's Intelligence modifier. This damage increases by 1d6
for every 2 alchemist levels beyond 1st the gloom chymist has. A gloom does not qualify as a bomb
for the purposes of feats or discoveries.

This ability replaces bomb.

## Umbral Gloom (Su) {#umbral-gloom}

At 2nd level, whenever a gloom chymist makes a gloom, he can have it increase or decrease the
[light level](ref/rule/vision-and-light) by one step within its splash radius, in addition to its
other effects. This change lasts for a number of rounds equal to the gloom chymist's Intelligence
modifier. At 8th level, the gloom chymist expend two uses of his daily glooms to increase or
decrease light levels as per _[daylight](ref/spell/daylight)_ or
_[deeper darkness](ref/spell/deeper-darkness)_, respectively, using his alchemist level as the
caster level.

This ability replaces poison resistance, poison use, and swift poisoning.

## Discoveries {#discoveries}

The following new discoveries can be taken by any alchemist who meets the prerequisites and has the
gloom class feature. Discoveries that modify glooms are marked with a single asterisk (\*) and do
not stack. Only one such discovery can be applied to an individual gloom.

### Bounding Gloom {#bounding-gloom}

The alchemist gains the ability to travel between shadows as if by means of a
_[dimension door](ref/spell/dimension-door)_ spell. The limitation is that the alchemist's beginning
and ending locations must be areas of dim light or darker, or within the radius of an umbral gloom
that is lowering the light level. The alchemist can travel up to a total of 100 feet each day in
this way. This distance must be used in 10-foot increments; for example, the alchemist can make a
single jump of 100 feet or 10 jumps of 10 feet each. For every 2 levels beyond 10th, the distance
the alchemist can jump each day doubles (200 feet at 12th level, 400 feet at 14th level, and so on).
An alchemist must be at least 10th level before selecting this discovery.

### Debilitating Gloom\* {#debilitating-gloom}

A creature struck by the gloom must make a successful Fortitude save or take a penalty to its
Strength equal to 1d4 + 1 per 2 alchemist levels (maximum of 1d4+5) for 1 round per alchemist level.
A target's Strength score cannot drop below 1. This penalty does not stack with itself. An alchemist
must be at least 6th level before selecting this discovery.

### Draining Gloom\* {#draining-gloom}

A creature struck by a direct hit with the gloom must make a successful Fortitude save or gain 1
negative level. An alchemist must be at least 8th level and must have the debilitating gloom
discovery before selecting this discovery.

### Glutinous Gloom\* {#glutinous-gloom}

The gloom creates an area in its splash radius that functions as _[web](ref/spell/web)_. The webbing
lasts for a number of rounds equal to 1/2 the alchemist's level. An alchemist must be at least 6th
level before selecting this discovery.

### Grasping Gloom\* {#grasping-gloom}

The gloom creates an area equal to double its splash radius that functions as
_[black tentacles](ref/spell/black-tentacles)_. The effect lasts for a number of rounds equal to
[half](ref/misc/fractions-and-rounding) the alchemist's level. An alchemist must be at least 8th
level before selecting this discovery.

### Greater Draining Gloom\* {#greater-draining-gloom}

A creature struck by the gloom must succeed at a Fortitude save or gain 1d4 negative levels. An
alchemist must be at least 12th level and must have the debilitating gloom and draining gloom
discoveries before selecting this discovery.

### Mucilaginous Gloom\* {#mucilaginous-gloom}

The gloom leaves a chilly gray residue that turns each square in its splash radius into
[difficult terrain](ref/rule/terrain-and-obstacles). This effect lasts for a number of rounds equal
to the alchemist's level.

### Rime-Bound Gloom\* {#rime-bound-gloom}

The gloom creates an area of freezing shadow in its splash radius that deals 2d6 points of cold
damage to all creatures in the area each turn. This effect lasts 1 round for every 2 alchemist
levels. An alchemist must be at least 6th level to select this discovery.
