+++
id = "ref/arc-barbarian/true-primitive"
kind = "archetype"
title = "True Primitive"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20True%20Primitive"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "true_primitive", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-combat"
page = "30"

[fields]
kind = "archetype"
features = [
  { anchor = "illiteracy" },
  { anchor = "favored-terrain", level = 1 },
  { anchor = "trophy-fetish", level = 3 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["favored-terrain"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["trophy-fetish"] },
  { alters = "The barbarian's armor and weapon proficiencies", feature = "weapon-and-armor-proficiencies" },
]
+++

Isolated and xenophobic tribes that dwell in areas untouched by civilization often see anything from
cities and organized settlements as strange, dangerous, and decadent. They gain power from their
truly primitive nature; their bodies and spirits are hardened by the wild and untainted existence
far from the pathetic softness of so-called civilization. Even when forced to mingle with
civilization, the true primitive stays apart in both traditions and trappings.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A true primitive is proficient with [hide armor](ref/eq-armor/hide) and armors made from
[bone](ref/eq-material/bone) (see page 146). A true primitive is also proficient with bone shields
and the following weapons: [battleaxe](ref/eq-weapon/battleaxe), [blowgun](ref/eq-weapon/blowgun),
[club](ref/eq-weapon/club), [greatclub](ref/eq-weapon/greatclub), [handaxe](ref/eq-weapon/handaxe),
[longspear](ref/eq-weapon/longspear), [shortspear](ref/eq-weapon/shortspear),
[sling](ref/eq-weapon/sling), and [spear](ref/eq-weapon/spear).

## Illiteracy {#illiteracy}

A true primitive cannot read or write, and her superstition about such things leads her to refuse to
ever learn to read or write, even if she multiclasses into other classes.

## Favored Terrain (Ex) {#favored-terrain}

A true primitive has a [favored terrain](ref/ability/favored-terrain) representing her native
homeland. This ability functions as the ranger class feature, and the true primitive's bonuses in
that terrain improve by +2 at 5th level and every five levels thereafter. However, she does not gain
any additional favored terrains. This ability replaces fast movement.

## Trophy Fetish (Ex) {#trophy-fetish}

A true primitive collects teeth, bones, hair, and other trophies from vanquished enemies,
representing their power and strength. At 3rd level, a true primitive can attach a trophy fetish to
one of the traditional true primitive weapons listed above. When wielding that weapon, the true
primitive gains a +1 morale bonus on damage rolls. Furthermore, if that weapon has the
[fragile](ref/misc/fragile) property, once per day, the true primitive can ignore the effects of a
single natural 1 roll. A trophy fetish can also be attached to a suit of hide or bone armor,
granting the true primitive a +1 morale bonus on saving throws. Furthermore, if that armor has the
fragile property, once per day, the true primitive can chose not to have the armor break on the
confirmation of a critical hit made against her. Every five levels beyond 3rd, a true primitive can
use an additional trophy fetish. Multiple trophy fetishes can be attached to the same armor or
weapon; their effects stack. A trophy fetish can be sundered ([hardness](ref/umr/hardness) 5, 1 hit
point) but is not damaged by area attacks or attacks that do not specifically target it. It has no
effect if attached to other types of weapons or armor. This ability replaces trap sense.

## Rage Powers {#rage-powers}

The following rage powers complement the true primitive archetype:
[animal fury](ref/ragepower/animal-fury), [eater of magic](ref/ragepower/eater-of-magic),
[ghost rager](ref/ragepower/ghost-rager), [low-light vision](ref/ragepower/low-light-vision),
[night vision](ref/ragepower/night-vision), [primal scent](ref/ragepower/primal-scent),
[scent](ref/ragepower/scent), [spell sunder](ref/ragepower/spell-sunder),
[sunder enchantment](ref/ragepower/sunder-enchantment), [superstition](ref/ragepower/superstition),
and [witch hunter](ref/ragepower/witch-hunter).
