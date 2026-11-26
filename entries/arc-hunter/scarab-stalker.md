+++
id = "ref/arc-hunter/scarab-stalker"
kind = "archetype"
title = "Scarab Stalker"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Scarab%20Stalker"
source_ids = ["ultimate-wilderness", "advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scarab_stalker", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "55"
[[sources]]
publication = "advanced-class-origins"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "sacred-animal-focus", level = 1 },
  { anchor = "desert-walker", level = 5 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["desert-walker"] },
  { alters = "Animal focus", feature = "animal-focus", by = ["sacred-animal-focus"] },
]
+++

The forgotten ruins in the desert sands have given rise to a breed of hunters who call upon the
powers of the pyramids to protect and explore the ancient sites of their people. These hunters form
sacred bonds with desert-dwelling denizens.

## Sacred Animal Focus (Su) {#sacred-animal-focus}

A scarab stalker can select from the bull, falcon, and snake [animal foci](ref/ability/animal-foci),
as well as the following new animal foci.

### Bee {#bee}

The creature gains a +4 competence bonus on Fly checks. This bonus increases to +6 at 8th level and
+8 at 15th level.

### Cat {#cat}

The creature gains a +4 competence bonus on Acrobatics checks. This bonus increases to +6 at 8th
level and +8 at 15th level.

### Cow {#cow}

The creature gains a +1 resistance bonus on Fortitude saving throws. This bonus increases to +2 at
8th level and +3 at 15th level.

### Crocodile {#crocodile}

The creature gains a +4 competence bonus on Swim checks. This bonus increases to +6 at 8th level and
+3 at 15th level.

### Ibis {#ibis}

The creature gains a +2 resistance bonus on saving throws against disease. This bonus increases to
+4 at 8th level and +6 at 15th level.

### Jackal {#jackal}

The creature gains a +4 competence bonus on Survival checks. This bonus increases to +6 at 8th level
and +8 at 15th level.

### Kite {#kite}

The creature recovers 1 additional hit point whenever it receives magical healing. This increases to
2 additional hit points at 8th level and 3 additional hit points at 15th level.

### Leopard {#leopard}

The creature gains a +4 competence bonus on Escape Artist checks. This bonus increases to +6 at 8th
level and +8 at 15th level.

### Lion {#lion}

The creature gains a +4 competence bonus on Intimidate checks. This bonus increases to +6 at 8th
level and +8 at 15th level.

### Ram {#ram}

The creature gains a +1 bonus on damage rolls when making charge attacks. This bonus increases to +2
at 8th level and +3 at 15th level.

### Scarab Beetle {#scarab-beetle}

The creature gains a +1 enhancement bonus to its natural armor bonus. This bonus increases to +2 at
8th level and +3 at 15th level.

### Scorpion {#scorpion}

The creature gains a +2 resistance bonus on saving throws against poison. This bonus increases to +4
at 8th level and +6 at 15th level.

### Sha {#sha}

The creature ignores the Perception penalty from sandstorms and can see twice as far in sandstorms.
This increases to three times as far at 8th level and four times as far at 15th level.

### Uraeus {#uraeus}

The creature gains a +2 resistance bonus on saving throws against
[breath weapons](ref/umr/breath-weapon). This bonus increases to +4 at 8th level and +6 at 15th
level.

This alters animal focus.

## Desert Walker (Ex) {#desert-walker}

At 5th level, a scarab stalker and her animal companion can move through desert terrain at normal
speed without taking damage or suffering any other impairments unless that terrain has been
enchanted or magically manipulated.

This replaces woodland stride.
