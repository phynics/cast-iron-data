+++
id = "ref/arc-hunter/verminous-hunter"
kind = "archetype"
title = "Verminous Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Verminous%20Hunter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "verminous_hunter", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "advanced-class-guide"
page = "98"

[fields]
kind = "archetype"
features = [
  { anchor = "vermin-companion", level = 1 },
  { anchor = "vermin-empathy" },
  { anchor = "vermin-focus", level = 1 },
  { anchor = "swarm-stride", level = 5 },
]
trades = [
  { replaces = "Animal focus", feature = "animal-focus", by = ["vermin-focus"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["swarm-stride"] },
  { alters = "Animal companion", feature = "animal-companion", by = ["vermin-companion"] },
  { alters = "hunter tactics", feature = "hunter-tactics", by = ["vermin-companion"] },
  { alters = "Wild empathy", feature = "wild-empathy", by = ["vermin-empathy"] },
]
+++

A verminous hunter calls on the ceaseless, single-minded dedication of vermin to hunt and overwhelm
her prey. Where other hunters invoke the cunning, animalistic powers of the alpha predators, she
calls on the powers of the lowest life forms, reaching out to the spider instead of the monkey, the
mantis instead of the snake, or the moth instead of the owl.

## Vermin Companion (Ex) {#vermin-companion}

At 1st level, a verminous hunter must choose a vermin companion instead of an animal companion
(_Ultimate Magic_ 36). This ability alters animal companion. The hunter tactics class ability allows
a verminous hunter to grant her teamwork feats to a mindless vermin companion.

## Vermin Empathy (Ex) {#vermin-empathy}

A verminous hunter gains the wild empathy ability, but can use it only to influence vermin (not
animals or magical beasts). This ability alters wild empathy.

## Vermin Focus (Su) {#vermin-focus}

A verminous hunter can take on the aspect of a vermin. This functions as
[animal focus](ref/ability/animal-foci), but allows only the following choices.

### Ant {#ant}

The creature gains a +2 enhancement bonus to Strength. This bonus increases to +4 at 8th level and
+6 at 15th level.

### Beetle {#beetle}

The creature gains a +2 enhancement bonus to its natural armor bonus. This bonus increases to +4 at
8th level and +6 at 15th level. (A creature without natural armor has an effective natural armor
bonus of +0.)

### Centipede {#centipede}

The creature gains a +2 competence bonus on Climb checks and a +2 bonus to CMD against pull, push,
reposition, and trip combat maneuvers. These bonuses increase to +4 at 8th level and +6 at 15th
level.

### Cockroach {#cockroach}

The creature gains a +4 bonus on saves against cold dangers, disease, heat dangers, starvation,
thirst, and on Constitution checks to avoid [suffocation](ref/rule/suffocation). These bonuses
increase to +6 at 8th level and +8 at 15th level.

### Crab {#crab}

The creature gains a +4 competence bonus on Swim checks and a +2 competence bonus on
[grapple](ref/rule/grapple) combat maneuver checks. These bonuses increase to +6 and +4 respectively
at 8th level, and +8 and +6 at 15th level.

### Flea {#flea}

The creature gains a +4 competence bonus on saves against disease and Acrobatics checks to jump.
These bonuses increase to +6 at 8th level and +8 at 15th level.

### Fly {#fly}

The creature gains a +2 bonus on Perception checks and on Acrobatics checks to balance or fall
safely. These bonuses increase to +4 at 8th level and +6 at 15th level.

### Leech {#leech}

The creature gains a +2 competence bonus on grapple combat maneuver checks, and deals 1 point of
[bleed](ref/rule/bleed) damage every time it succeeds at a grapple combat maneuver check to damage
an opponent. These benefits increase to a +4 bonus and 3 points of bleed at 8th level, and a +6
bonus and 5 points of bleed at 15th level. Bleed damage from this ability does not stack with
itself.

### Mantis {#mantis}

The creature gains a +2 bonus on attack of opportunity attack rolls and a +2 competence bonus on
grapple combat maneuver checks. These bonuses increase to +4 at 8th level and +6 at 15th level.

### Moth {#moth}

The creature gains [darkvision](ref/rule/darkvision) to a range of 60 feet. At 8th level, the range
increases by 30 feet. At 15th level, the creature gains [blindsense](ref/umr/blindsense) to a range
of 10 feet.

### Phasmid {#phasmid}

The creature gains [low-light vision](ref/rule/low-light-vision) and a +4 competence bonus on
Stealth checks in forests or plains. This bonus increases to +6 at 8th level and +8 at 15th level.

### Scorpion {#scorpion}

The creature gains a +2 competence bonus on Stealth checks and grapple combat maneuver checks. These
bonuses increase to +6 and +4 respectively at 8th level, and +8 and +6 at 15th level.

### Spider {#spider}

The creature gains a +2 competence bonus on Stealth checks, saving throws against
[web](ref/spell/web) effects (magical or otherwise), and checks to break free of webs. This bonus
increases to +4 at 8th level and +6 at 15th level.

### Wasp {#wasp}

The creature gains a +4 competence bonus on Perception checks. This bonus increases to +6 at 8th
level and +8 at 15th level.

### Worm {#worm}

The creature gains a 25% chance to treat any critical hit or sneak attack as a normal hit (as the
_[fortification](ref/magic-enh/fortification)_ armor special ability). This increases to 50% at 8th
level, and 75% at 15th level.

This ability replaces animal focus.

## Swarm Stride (Ex) {#swarm-stride}

At 5th level, a verminous hunter learns to move through vermin without danger. He can safely pass
through [swarms](ref/subtype/swarm) of vermin and does not take swarm damage while within a vermin
swarm's space. In addition, he is immune to a swarm's distraction ability. If the hunter or his
animal companion attacks a swarm, they lose this protection against only that swarm. This ability
replaces woodland stride.
