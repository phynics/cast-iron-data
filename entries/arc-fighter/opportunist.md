+++
id = "ref/arc-fighter/opportunist"
kind = "archetype"
title = "Opportunist"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Opportunist"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "opportunist", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "duplicitous", level = 2 },
  { anchor = "underhanded", level = 1 },
  { anchor = "cunning-edge", level = 4 },
  { anchor = "alchemical-onslaught", level = 5 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["duplicitous"] },
  { replaces = "The bonus feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["underhanded"] },
  { replaces = "Bonus feats gained at 4th, 8th, 12th, 16th, and 20th levels", feature = "bonus-feats", levels = [4, 8, 12, 16, 20], by = ["cunning-edge"] },
  { replaces = "Weapon training 1", feature = "weapon-training", levels = [5], by = ["alchemical-onslaught"] },
  { alters = "Class skills", by = ["duplicitous"] },
]
+++

Opportunists believe every battle is one of wits rather than arms. The ratfolk enforcers who protect
Goka's infamous Deepmarket embrace this philosophy, unleashing a disorienting mix of martial skill
and alchemical weaponry.

## Duplicitous (Ex) {#duplicitous}

An opportunist adds [Bluff](ref/skill/bluff), [Sense Motive](ref/skill/sense-motive),
[Sleight of Hand](ref/skill/sleight-of-hand), and [Stealth](ref/skill/stealth) to his list of class
skills. He gains 2 bonus skill ranks at each level, which must be allocated among these skills.

This ability replaces bravery and alters the fighter's class skills.

## Underhanded (Ex) {#underhanded}

An opportunist gains [Improved Dirty Trick](ref/feat/improved-dirty-trick) as a bonus feat at 1st
level even if he does not meet the prerequisites.

This ability replaces the bonus feat gained at 1st level.

## Cunning Edge (Ex) {#cunning-edge}

At 4th level, an opportunist can select an edge from those listed below. Every 4 levels beyond 4th,
he can select one additional edge, to a maximum of five at level 20.

This ability replaces the bonus feats gained at 4th, 8th, 12th, 16th, and 20th levels.

### Alchemical Admixture (Ex) {#alchemical-admixture}

As a full round action that provokes an attack of opportunity, the opportunist can combine two
alchemical weapons into a single vial. When thrown as a splash weapon, the mixture has the effects
of both component substances and targets are affected as if hit by both. The mixture becomes inert
after 1 hour. Combining identical alchemical weapons has no effect. The opportunist can use this
ability once per day for every 4 fighter levels he has.

### Alchemical Refinement (Ex) {#alchemical-refinement}

The opportunist increases the save DC of any alchemical item he crafts by 1 for every 3 fighter
levels he has. Doing so increases the raw material cost to craft that item by 10 gp for every +1
increase. This bonus applies only when the opportunist uses the crafted alchemical item himself; it
functions as a normal item of its type for all other users.

### Bombs (Ex) {#bombs}

The opportunist can make a number of bombs per day equal to his Intelligence modifier (minimum 1).
These bombs act as [alchemist's](ref/class/alchemist) bombs and deal 1d6 points of fire damage, plus
an additional 1d6 points for every 3 fighter levels the opportunist has.

### Clouded Shift (Ex) {#clouded-shift}

As part of the standard action to ignite a [smokestick](ref/eq-misc/smokestick) or
[smoke pellet](ref/eq-misc/smoke-pellet), the opportunist can take a 5-foot step, even if he has
already moved this round. He can use this ability only if he has not already taken a 5-foot step
this round, and only if the smoke from his alchemical tool conceals his starting location.

### Poison Use (Ex) {#poison-use}

The opportunist no longer risks poisoning himself when applying poison to a weapon.

### Rogue Talent (Ex) {#rogue-talent}

The opportunist can select one of the following rogue talents for which he qualifies, treating his
fighter level as his rogue level: [deft palm](ref/talent/deft-palm),
[fast fingers](ref/talent/fast-fingers), [fast stealth](ref/talent/fast-stealth),
[honeyed words](ref/talent/honeyed-words), [lasting poison](ref/talent/lasting-poison),
[minor magic](ref/talent/minor-magic), or [quick trapsmith](ref/talent/quick-trapsmith). The
opportunist can select this edge multiple times.

## Alchemical Onslaught (Ex) {#alchemical-onslaught}

At 5th level, an opportunist gains a +1 bonus on attack rolls with alchemical weapons and bombs and
can add his Intelligence modifier to damage rolls for splash weapons. He can draw an alchemical
weapon as a free action once per round.

This ability replaces weapon training 1.
