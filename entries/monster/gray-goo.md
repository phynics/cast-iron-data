+++
id = "ref/monster/gray-goo"
kind = "creature"
title = "Gray Goo"
source_ids = ["bestiary-5", "numeria-land-of-fallen-stars"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gray_goo", path = "json/monsters12.json" },
]

[fields]
kind = "creature"
cr = "14"
creature_type = "construct"
subtypes = ["swarm"]
size = "fine"
alignment = "neutral"
ac = "29/29/18"
hp = "123~19d10+19"
fortitude = "+8"
reflex = "+18"
will = "+8"
melee = "swarm (6d6 plus dismantle and distraction)"
special_attacks = "dismantle~infest"
abilities = ["1", "30", "-", "5", "10", "1"]
+++

_Droplets of a silvery gray, slightly grainy goo gleam dully as they hang in the air._

**Gray Goo**

**Challenge rating:** 14

**Type:** construct

**Size:** fine

**Initiative:** +10

**Alignment:** Neutral

**Perception:** +13

**Senses:** Darkvision 60 ft., Low-light vision

**Sources:** Bestiary 5 pg 130, Numeria, Land of Fallen Stars pg 50\
**Subtype:** Swarm

**Experience points:** 38,400

**Armor class:** 29/29/18

**Defensive abilities:** dispersion, swarm traits

**Fort:** +8

**Hit points:** 123 (19d10+19)

**Immune:** [construct traits](ref/umr/construct-traits), weapon damage

**Mod:** +10 Dex, +1 dodge, +8 size

**Ref:** +18

**Will:** +8

**Offense**

**Speed:** fly 50 ft. (perfect)

**Distraction:** DC 21

**Melee:** swarm (6d6 plus dismantle and distraction)

**Reach:** 0

**Space:** 10

**Spec Att:** dismantle, infest

**Statistics**

**Ability scores:** Str 1, Dex 30, Con -, Int 5, Wis 10, Cha 1

**Base attack bonus:** +19

**Combat maneuver bonus:** -

**Combat maneuver defense:** -

**Feats:** Ability Focus (distraction), Dodge, Great Fortitude, Improved Lightning Reflexes, Iron
Will, Lightning Reflexes, Lightning Stance, Mobility, Toughness, Wind Stance

**Skills:** Fly +26, Perception +13, Stealth +32 (+42 when dispersed)

**Racial Modifiers:** +10 Stealth when dispersed

**Languages:** Common (can't speak)

**Ecology**

**Environment:** any

**Organization:** solitary, pair, or storm (3-12)

**Treasure:** None

### Special Abilities

**Dismantle (Ex)** Creatures damaged by a gray goo must succeed at a DC 19 Reflex save or a random
piece of their equipment takes the same amount of damage, determined as though the target rolled a
natural 1 on a saving throw, using the rules for items surviving after a saving throw. In addition,
unattended objects in the area of a gray goo take damage if the swarm chooses to harm them. The save
DC is Constitution-based.

**Dispersion (Ex)** As an immediate action, a gray goo can disperse, spreading itself across a
cube-shaped area 30 feet on a side. While dispersed, the goo deals no damage and can't use its other
special abilities until it reforms. A dispersed gray goo can hide in plain sight (as a ranger in her
favored terrain) with a +10 bonus on its Stealth checks and doesn't take additional damage from area
effects for being a swarm. It takes 2 rounds for a dispersed gray goo to reform.

**Infest (Ex)** As a standard action, a gray goo can infest a Medium or larger creature (Fortitude
DC 21 negates), including constructs and undead. The gray goo moves inside the creature's body,
dealing double its normal damage to its host each round. It can't use its dismantle ability while
infesting a creature. A host reduced to 0 hit points while infested by a gray goo is reduced to dust
and destroyed (similar to [disintegrate](ref/spell/disintegrate)). A gray goo infesting a host can
be expelled by any effect that cures disease, with a disease save equal to this ability's DC. The
save DC is Constitution-based and includes a +2 racial bonus.

### Description

Swarms of weaponized nanites-microscopic mechanical constructs designed to work in large groups to
perform varied tasks-reduce anything in their path to wisps of dust. Called "gray goo" by those who
don't understand the true nature of the creature's components, some of these horrific swarms were
activated as weapons of mass destruction. Others were originally benign, intended to enhance crops
and clean them of pests or combat diseases, but malfunctioned and abandoned their programming.
Nanites have limited intelligence and potentially respond to commands. Such controlled swarms are
capable of relatively complex decision making, and they might spare the treasure their victims
carry, for instance, allowing their masters to better loot the bodies.

### Benign Nanites

Nanites meant for benign purposes that retain their original programming are capable of bringing
benefits as great as the devastation wrought by their destructive kin, though it can be difficult to
tell them apart. Harvest nanites that tend a field can enhance production and eliminate pests and
blight, increasing the yield as the [plant growth](ref/spell/plant-growth) spell. Medical nanites
can infest a host body, using their infest ability, but choose not to damage the creature itself,
instead surgically targeting invasive organisms, functioning as a
[remove disease](ref/spell/remove-disease) spell with a caster level equal to the swarm's hit dice.
Crafter nanites can dismantle objects to build others, as [fabricate](ref/spell/fabricate), and
potentially even do the same with flesh, as [regenerate](ref/spell/regenerate).
