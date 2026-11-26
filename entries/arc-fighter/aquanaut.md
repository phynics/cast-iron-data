+++
id = "ref/arc-fighter/aquanaut"
kind = "archetype"
title = "Aquanaut"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Aquanaut"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aquanaut", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "aquatic-adventures"
page = "51"

[fields]
kind = "archetype"
features = [
  { anchor = "piercing-focus", level = 1 },
  { anchor = "tidal-celerity", level = 2 },
  { anchor = "aquadynamic-paragon", level = 3 },
  { anchor = "underwater-training", level = 5 },
]
trades = [
  { replaces = "Bravery", feature = "bravery", by = ["tidal-celerity"] },
  { replaces = "Armor training", feature = "armor-training", by = ["aquadynamic-paragon"] },
  { replaces = "armor mastery", feature = "armor-mastery", by = ["aquadynamic-paragon"] },
  { replaces = "Weapon training", feature = "weapon-training", by = ["underwater-training"] },
  { alters = "Armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor" },
  { alters = "Bonus feats", feature = "bonus-feats", by = ["piercing-focus"] },
  { alters = "weapon mastery", feature = "weapon-mastery", by = ["piercing-focus"] },
]
+++

Aquanaut fighters master the movement of water, using its flow to their advantage in combat.

## Armor Proficiency {#armor-proficiency}

An aquanaut is proficient with light and medium armor, but not with shields.

This alters the fighter's armor proficiency.

## Piercing Focus {#piercing-focus}

If an aquanaut takes a fighter bonus feat that normally requires selecting a single weapon (except
weapon proficiency feats), he can instead apply the feat to all melee piercing weapons with which he
is already proficient and that meet all other prerequisites for that feat. This ability counts as
having the feat for each such individual weapon for the purpose of meeting prerequisites. This
ability also applies to the weapon mastery class feature.

This alters bonus feats and weapon mastery.

## Tidal Celerity {#tidal-celerity}

At 2nd level, an aquanaut gains a +1 bonus on Reflex saves and saving throws against effects that
would immobilize or paralyze him. This bonus increases by 1 for every 4 levels beyond 2nd.

This ability replaces bravery.

## Aquadynamic Paragon {#aquadynamic-paragon}

At 3rd level, an aquanaut gains a swim speed equal to his unmodified base land speed (if he has a
racial swim speed, he instead increases it by 10 feet) and can choose to have a neutral
[buoyancy](ref/rule/buoyancy) once per turn as a free action. At 7th level, he can choose any of the
five states of buoyancy once per turn as a free action, and can take his buoyancy movement as part
of that free action instead of at the end of his turn without becoming
[off-balance](ref/rule/off-balance-and-prone-underwater) and without requiring a Swim check;
additionally, he can choose to double or halve how far a
[current](ref/rule/currents-and-running-water) moves him. At 11th level, whenever he takes a move,
double move, withdraw, or run action underwater, he can leave a current behind him in the squares
along his path; this current has a speed of 10 feet in the direction of his movement (if his
movement was circuitous, so is the current) and lasts until the beginning of his next turn. At 15th
level, as a full round action, an aquanaut can spin ferociously underwater, creating a whirlpool
around himself with a spinning force that drags all creatures within 120 feet of him 30 feet closer
to him. Creatures closer than 30 feet spend the 30 feet of movement circling around the aquanaut in
a single direction of his choice. The whirlpool isn't fast enough to deal damage, but the aquanaut
is unaffected by his own whirlpool, allowing him to make attacks of opportunity against creatures
moving in it. At 19th level, the aquanaut learns to use the water around him to soften blows,
gaining DR 5/— while underwater.

This ability replaces armor training and armor mastery.

## Underwater Training {#underwater-training}

At 5th level, an aquanaut chooses bludgeoning, slashing, or piercing melee weapons. If he chooses
piercing melee weapons, he gains a +1 bonus on attack and damage rolls with those weapons when
attacking underwater. If he chooses bludgeoning or slashing melee weapons, he can ignore
[the usual underwater penalties](ref/rule/physical-attacks-underwater) for attacking with those
weapons (see page 44). At 9th and 13th levels, he can choose another type of melee weapon, applying
this ability's initial benefit to his new choice and gaining an additional +1 bonus on attack and
damage rolls to his previously chosen weapon types. At 17th level, he gains an additional +1 bonus
on attack and damage rolls with all three types.

This ability replaces weapon training.
