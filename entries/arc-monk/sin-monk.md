+++
id = "ref/arc-monk/sin-monk"
kind = "archetype"
title = "Sin Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Sin%20Monk"
source_ids = ["antiheros-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sin_monk", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "antiheros-handbook"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "well-of-sin", level = 4 },
  { anchor = "sinful-strike", level = 7 },
  { anchor = "burden-with-sin", level = 12 },
  { anchor = "simultaneous-sins", level = 19 },
  { anchor = "spawn-of-sin", level = 20 },
]
trades = [
  { replaces = "Ki pool", feature = "ki-pool", by = ["well-of-sin"] },
  { alters = "High jump", feature = "high-jump", by = ["well-of-sin"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["sinful-strike"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["burden-with-sin"] },
  { replaces = "Empty body", feature = "empty-body", by = ["simultaneous-sins"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["spawn-of-sin"] },
]
+++

Some vices prove too tempting even to those who have trained their minds and bodies against such
corruptions, and the seven sins of ancient Thassilon stand among the most alluring. Martial experts
who have allowed such passions to lead them astray may find themselves gaining powers drawn from
their newly embraced sins.

This is an ex-class archetype and can be taken by a character immediately upon becoming an ex-monk.

## Well of Sin (Su) {#well-of-sin}

At 4th level, a sin monk gains a pool of sin points, representing energy he has gained from
indulging in forbidden vices. The sin monk has a number of sin points equal to half his class
level + his Wisdom modifier; these points cannot be used on abilities that require spending ki
points. As a swift action, he can spend 1 point from his sin pool to activate one of the following
abilities until the start of his next turn.

### Envy {#envy}

The sin monk gains a +4 bonus on Perception and Sense Motive checks. This bonus increases to +6 at
10th level and +8 at 16th level.

### Gluttony {#gluttony}

Each time the sin monk deals lethal damage with a melee attack, he regains a number of hit points
equal to the amount of damage dealt (maximum 2). He can't exceed his maximum number of hit points.
The maximum number of hit points he regains increases to 4 at 10th level and 6 at 16th level.

### Greed {#greed}

The sin monk's attacks count as being either cold iron or silver (sin monk's choice) for the purpose
of overcoming DR. At 10th level, he adds adamantine to the list of materials he can choose to have
his attacks count as being for the purpose of overcoming DR. At 16th level, the sin monk's attacks
also ignore [hardness](ref/umr/hardness).

### Lust {#lust}

The sin monk gains a +4 bonus on Bluff and Diplomacy checks. This bonus increases to +6 at 10th
level and +8 at 16th level.

### Pride {#pride}

The sin monk gains one illusory double of himself, which functions as _mirror image_. This double
automatically disappears at the beginning of the sin monk's next turn unless destroyed first. At
10th level, the sin monk gains two such replicas of himself, and at 16th level, he gains three.

### Sloth {#sloth}

The sin monk gains the benefits of [Vital Strike](ref/feat/vital-strike). At 10th level, he also
gains the benefits of [Improved Vital Strike](ref/feat/improved-vital-strike), and at 16th level, he
also gains the benefits of [Greater Vital Strike](ref/feat/greater-vital-strike).

### Wrath {#wrath}

The sin monk increases the save DCs of his attacks with [Stunning Fist](ref/feat/stunning-fist) (and
[Punishing Kick](ref/feat/punishing-kick), if he has that feat) by 1. The save DC instead increases
by 2 at 10th level and by 3 at 16th level.

When a sin monk gains a level in the monk class and would gain one of the following class features,
he can forfeit that class feature to instead increase the size of his sin pool by 1 sin point:
purity of body, diamond body, diamond soul, timeless body, tongue of the sun and moon. Once the
decision is made, it cannot be changed.

This replaces ki pool and alters high jump.

## Sinful Strike (Su) {#sinful-strike}

At 7th level, a sin monk can spend 2 sin points as a swift action to focus his power. The next time
he deals damage before the end of his next turn, he deals an additional amount damage equal to his
monk level.

This replaces wholeness of body.

## Burden with Sin (Su) {#burden-with-sin}

At 12th level, a sin monk can spend a swift action and one daily use of Stunning Fist to draw his
sinful nature to the fore of his consciousness. The next person he hits with a melee attack before
the end of his next turn must succeed at a Will save (DC = 10 + half the sin monk's class level +
his Wisdom modifier) or suffer the burden of the sin monk's sins. The target is treated as if she
were [carrying a load](ref/rule/carrying-capacity) one step heavier (from a light load to a medium
load, and so on) and must succeed at a caster level check to use any form of teleportation (DC =
10 + the monk's class level). This is a curse effect that lasts a number of rounds equal to the sin
monk's Wisdom modifier unless it is removed through _[remove curse](ref/spell/remove-curse)_ or a
similar effect.

This replaces abundant step.

## Simultaneous Sins (Su) {#simultaneous-sins}

At 19th level, a sin monk can spend 3 points from his sin pool as a swift action to gain the
benefits of two different sins simultaneously.

This replaces empty body.

## Spawn of Sin (Ex) {#spawn-of-sin}

At 20th level, the sin monk becomes the physical manifestation of his sins. He is forevermore
treated as an [aberration](ref/type/aberration) rather than a humanoid (or whatever the monk's
creature type was) for the purpose of spells and magical effects, and his mind is so consumed by sin
that he gains immunity to mind-affecting effects. He does not change in appearance or gain other
abilities; however, should the sin monk be slain and brought back from the dead, he returns to life
as a [sinspawn](ref/monster/sinspawn), retaining his class levels but otherwise replacing his
creature type and racial abilities with those of his new form and becoming an NPC under the GM's
control.

This replaces perfect self.
