+++
id = "ref/arc-gunslinger/gulch-gunner"
kind = "archetype"
title = "Gulch Gunner"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Gulch%20Gunner"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gulch_gunner", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "advanced-race-guide"
page = "152"

[fields]
kind = "archetype"
features = [
  { anchor = "grit", level = 1 },
  { anchor = "deeds" },
  { anchor = "flash-and-shock", level = 1 },
  { anchor = "powder-burns", level = 3 },
  { anchor = "staggering-shot", level = 15 },
  { anchor = "belly-shot", level = 9 },
]
trades = [
  { replaces = "The ability to regain grit from a critical hit with a firearm", feature = "critical-hit-with-a-firearm", by = ["grit"] },
  { replaces = "Deadeye deed", feature = "deeds", power = "deadeye", by = ["flash-and-shock"] },
  { replaces = "Pistol whip deed", feature = "deeds", power = "pistol whip", by = ["powder-burns"] },
  { replaces = "Menacing shot deed", feature = "deeds", power = "menacing shot", by = ["staggering-shot"] },
  { replaces = "Gun training ability gained at 9th, 13th, and 17th level", feature = "gun-training", levels = [9, 13, 17], by = ["belly-shot"] },
  { alters = "Grit", feature = "grit", by = ["grit"] },
]
+++

Ratfolk warfare often occurs in cramped, claustrophobic spaces such as the ratfolk's own underground
warrens and heavily trapped gulch fortresses, or the subterranean tunnels of goblins and similar
foes. Since these battlegrounds often have tight corners and few areas with long lines of sight,
those ratfolk who seek to master the use of firearms almost inevitably become experts in
close-quarters combat. These gulch gunners often specialize in proficiency with a single pistol
(easily handled in tight spaces) and wander from warren to warren selling their tunnel-shooting
skills to the highest bidder. A gulch gunner has the following class features.

## Class Skills {#class-skills}

A gulch gunner adds Disable Device, Escape Artist, and Knowledge (dungeoneering) to her list of
class skills and removes Knowledge (local), Ride, and Swim from her list of class skills.

## Grit (Ex) {#grit}

At 1st level, a gulch gunner gains grit as a standard gunslinger. However, the close-combat focus of
the gulch gunner results in a slightly different set of circumstances for regaining grit.

### Daring Adjacent Shot {#daring-adjacent-shot}

The first time each round the gulch gunner makes a ranged firearm attack against an adjacent foe and
provokes an attack of opportunity, she regains 1 grit point. Making an adjacent firearm attack
against a [helpless](ref/misc/helpless) or unaware creature or on a creature that has fewer Hit Dice
than half the gulch gunner's character level does not restore grit, nor do ranged attacks using some
ability that prevents the gulch gunner from provoking an attack of opportunity. This ability
replaces the ability to regain grit from a critical hit with a firearm.

## Deeds {#deeds}

A gulch gunner has some unique deeds, which replace some of the standard gunslinger deeds as listed
in each entry. These deeds follow all the general rules and restrictions of gunslinger deeds.

## Flash and Shock (Ex) {#flash-and-shock}

At 1st level, the gulch gunner can take advantage of the flash and sound of a firearm to throw off
an attacker's aim at close range. When she makes an attack against a foe within her firearm's first
range increment, she may spend 1 grit point to gain a +4 circumstance bonus to AC against that
opponent until the beginning of her next turn. She can only perform this deed while wearing medium,
light, or no armor, and while carrying no more than a light load. This deed replaces the deadeye
deed.

## Powder Burns (Ex) {#powder-burns}

At 3rd level, the gulch gunner learns to maximize the damage dealt by a firearm at extremely close
range.

When the gulch gunner successfully hits an adjacent foe with a ranged firearm attack, she may spend
1 grit point to deal an additional 1d6 points of fire damage from the muzzle flash of her weapon.

The target must also make a Reflex save (DC 10 + 1/2 the gulch gunner's level + the gulch gunner's
Wisdom modifier) or [catch on fire](ref/rule/catching-on-fire). This deed replaces the pistol whip
deed.

## Staggering Shot (Ex) {#staggering-shot}

At 15th level, when the gulch gunner hits an adjacent target with a ranged firearm attack, the
target must also make a Fortitude save (DC 10 + 1/2 the gulch gunner's level + the gulch gunner's
Wisdom modifier) or be [staggered](ref/misc/staggered) for 1d4 rounds. This deed replaces the
menacing shot deed.

## Belly Shot (Ex) {#belly-shot}

At 9th level, a gulch gunner can press her firearm directly against a vulnerable location of an
adjacent target, dealing additional damage. When the gulch gunner successfully hits an adjacent
target with a ranged firearm attack, she deals +1d6 points of damage. This damage increases to +2d6
at 13th level and to +3d6 at 17th level. Creatures immune to precision damage, critical hits, or
sneak attacks do not take this additional damage. This ability replaces the gun training ability
gained at 9th, 13th, and 17th level.
