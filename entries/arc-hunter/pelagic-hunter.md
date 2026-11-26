+++
id = "ref/arc-hunter/pelagic-hunter"
kind = "archetype"
title = "Pelagic Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Hunter%20Pelagic%20Hunter"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pelagic_hunter", path = "json/archetypes_hunter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/hunter" },
]
[[sources]]
publication = "aquatic-adventures"
page = "54"

[fields]
kind = "archetype"
features = [
  { anchor = "pelagic-companion", level = 1 },
  { anchor = "pelagic-focus", level = 1 },
  { anchor = "blood-to-water", level = 5 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["blood-to-water"] },
  { alters = "Animal companion", feature = "animal-companion", by = ["pelagic-companion"] },
  { alters = "Animal focus", feature = "animal-focus", by = ["pelagic-focus"] },
]
+++

Pelagic hunters form strong bonds that extend deep beneath the sea, reaching out to whatever heeds
their call, whether it be mundane animals or something far more sinister.

## Pelagic Companion {#pelagic-companion}

A pelagic hunter must select an aquatic animal companion.

This alters animal companion.

## Pelagic Focus (Su) {#pelagic-focus}

Unlike with a normal hunter's [animal focus](ref/ability/animal-foci), pelagic focus allows the
hunter to contact magical deep sea creatures instead of animals, using the options below instead of
the normal hunter options.

This alters animal focus.

### Aboleth {#aboleth}

The creature gains a +1 morale bonus on saves against divine spells and
[spell-like abilities](ref/umr/spell-like-abilities). This bonus increases to +2 at 8th level and +3
at 15th level.

### Cetus {#cetus}

The creature gains [Lunge](ref/feat/lunge) as a bonus feat. At 12th level, instead of gaining Lunge,
the creature increases its reach by 5 feet.

### Charybdis {#charybdis}

The creature's attacks ignore the first 5 points of [hardness](ref/umr/hardness). This improves to
ignore the first 7 points of [hardness](ref/umr/hardness) at 8th level and the first 10 points of
[hardness](ref/umr/hardness) at 15th level.

### Deep One {#deep-one}

The creature reduces [pressure damage](ref/rule/water-dangers) it takes (see page 48) by 10. At 12th
level, the creature is immune to damage from changing pressure.

### Hippocampus {#hippocampus}

The creature gains a +4 competence bonus on Swim checks. This bonus increases to +6 at 8th level and
+8 at 15th level.

### Kraken {#kraken}

The creature gains the [jet](ref/umr/jet) ability with a speed equal to its unmodified base land
speed or four times its swim speed (if it has one), whichever is higher. If it has a swim speed, at
8th level, the jet ability's speed increases to five times its swim speed, and at 15th level, the
speed increases to seven times its swim speed.

### Reefclaw {#reefclaw}

The creature gains [Diehard](ref/feat/diehard) as a bonus feat. At 12th level, instead of gaining
Diehard, the creature gains the [ferocity ability](ref/umr/ferocity).

### Scylla {#scylla}

The creature's attacks deal 1 point of [bleed](ref/rule/bleed) damage in addition to their normal
damage. At 8th level, the bleed damage increases to 1d3, and at 15th level, it increases to 1d6.

### Sea Serpent {#sea-serpent}

The creature is considered to be under a _[nondetection](ref/spell/nondetection)_ spell it cast on
itself, with a caster level equal to the pelagic hunter's class level.

### Selkie {#selkie}

The creature gains a +4 competence bonus on Bluff checks. This bonus increases to +6 at 8th level
and +8 at 15th level.

### Shoggoth {#shoggoth}

The creature gains a +2 competence bonus on Perception checks and reduces the
[flanking](ref/rule/flanking) bonuses of creatures flanking it by 1. This Perception bonus increases
to +3 at 8th level and +4 at 15th level. At 12th level, the creature can't be flanked.

### Siyokoy {#siyokoy}

The creature's attacks deal 1 additional point of electricity damage. At 8th level, the electricity
damage increases to 1d3, and at 15th level, it increases to 1d6.

## Blood to Water (Su) {#blood-to-water}

At 5th level, when a pelagic hunter or her animal companion bleeds underwater into the surrounding
water (whether from piercing or slashing damage, a bleed effect, or another effect that causes blood
to spill), the blood transmutes into ordinary water within 1 round. This prevents sharks and other
predators with [keen scent](ref/umr/keen-scent) from being drawn to the pelagic hunter's position by
the blood and makes it harder for such creatures to track her.

This ability replaces woodland stride.
