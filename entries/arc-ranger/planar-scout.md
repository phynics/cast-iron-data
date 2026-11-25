+++
id = "ref/arc-ranger/planar-scout"
kind = "archetype"
title = "Planar Scout"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Planar%20Scout"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planar_scout", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "planar-adventures"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "planar-empathy" },
  { anchor = "planar-terrains", level = 3 },
  { anchor = "planar-bond", level = 4 },
  { anchor = "planar-adaptation", level = 9 },
]
trades = [
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["planar-bond"] },
  { replaces = "Evasion", feature = "evasion", by = ["planar-adaptation"] },
  { replaces = "improved evasion", feature = "improved-evasion", by = ["planar-adaptation"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["planar-empathy"] },
  { alters = "Favored terrain", feature = "favored-terrain", by = ["planar-terrains"] },
  { alters = "The ranger's skills" },
]
+++

Planar scouts are rangers specializing in traversing the planes—and surviving their journeys.

## Class Skills {#class-skills}

A planar scout gains Knowledge (planes) as a class skill but does not gain Knowledge (dungeoneering)
as a class skill.

This alters the ranger's skills.

## Planar Empathy (Ex) {#planar-empathy}

A planar scout can use wild empathy only on animals with the [extraplanar](ref/subtype/extraplanar)
subtype. He can use this ability to influence outsiders with an Intelligence score of 1 or 2, but he
takes a -4 penalty on the check.

This alters wild empathy.

## Planar Terrains (Ex) {#planar-terrains}

At 3rd level, a planar scout gains a planar terrain (see the sidebar on page 9).
[Planar terrains](ref/rule/planar-terrains) function in all ways like a ranger's favored terrain; he
must select a new plane each time he gains a favored terrain.

This alters favored terrain.

## Planar Bond (Su) {#planar-bond}

At 4th level, rather than forge a bond with an animal or his allies, a planar scout forms a bond
with a specific plane. The planar scout becomes infused with the essence of his plane of choice,
taking on physical characteristics of denizens native to his chosen plane as well as the abilities
listed below.

### Aligned Plane {#aligned-plane}

If the planar scout selects a plane with an alignment trait, he gains a +1 bonus on attack and
damage rolls against outsiders and creatures with the extraplanar subtype whose alignments oppose
this alignment trait. This bonus increases by 1 at 8th level and every 4 levels thereafter.

### Astral Plane {#astral-plane}

Each day, the planar scout can teleport up to 5 feet per ranger level as a move action. This must be
used in 5-foot increments. At 10th level, he can do so as a swift action.

### Ethereal Plane {#ethereal-plane}

The planar scout can damage incorporeal creatures with mundane weapons as if they were
_[ghost touch](ref/magic-enh/ghost-touch-weapon)_ weapons, and at 10th level, he can inflict
critical hits and deal precision damage to incorporeal creatures.

### First World {#first-world}

As a swift action a number of times per day equal to his Wisdom modifier, a planar scout can gain
[fast healing](ref/umr/fast-healing) 2 for a number of rounds equal to his ranger level.

### Plane of Air {#plane-of-air}

As a swift action, the planar scout can gain a fly speed (average) equal to his base speed for a
number of minutes equal to his ranger level (minimum 1 minute). This duration need not be used
consecutively.

### Plane of Earth {#plane-of-earth}

The planar scout gains a +1 bonus to his natural armor. This bonus increases by 1 for every 4 levels
he gains beyond 4th level.

### Plane of Fire {#plane-of-fire}

As a swift action, the planar scout can wreathe his body in flames. This grants the planar scout
fire resistance 5 and causes his melee attacks to each deal 1d4 additional points of fire damage.
The scout's fire resistance increases to 10 at 9th level, and 15 at 14th level. He can use this
ability for a number of rounds per day equal to his level. These rounds need not be used
consecutively.

### Plane of Shadow {#plane-of-shadow}

The planar scout gains [darkvision](ref/rule/darkvision) 60 feet and a +4 bonus on Stealth checks.
The bonus on Stealth checks increases by 2 at 8th level and every 4 levels thereafter.

### Plane of Water {#plane-of-water}

The planar scout gains the [amphibious](ref/umr/amphibious) subtype and a swim speed equal to base
speed.

This replaces hunter's bond.

## Planar Adaptation (Su) {#planar-adaptation}

At 9th level a planar scout gains _[planar adaptation](ref/spell/planar-adaptation)_ when on his
bonded plane. At 16th level he confers this protection to all allies within a 30-foot
[spread](ref/misc/spread).

This replaces evasion and improved evasion.
