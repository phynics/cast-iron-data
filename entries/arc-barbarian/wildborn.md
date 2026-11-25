+++
id = "ref/arc-barbarian/wildborn"
kind = "archetype"
title = "Wildborn"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Wildborn"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wildborn", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "39"

[fields]
kind = "archetype"
features = [
  { anchor = "illiteracy" },
  { anchor = "live-off-the-land", level = 3 },
  { anchor = "inexhaustible" },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["live-off-the-land"] },
  { alters = "The barbarian's normal weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { alters = "Rage powers", feature = "rage-powers" },
  { alters = "Damage reduction", feature = "damage-reduction", by = ["inexhaustible"] },
]
+++

Some barbarians are born or bred outside the reach of civilization. These wildborn fight and survive
without ever seeing a forge or worked stone, and only dare a trip into the city when no other option
is available.

## Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}

A wildborn is proficient with leather and hide armors (but not shields) and all simple weapons that
can be crafted from bone, stone, or wood. In addition, a wildborn gains
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) and
[Catch Off Guard](ref/feat/catch-off-guard) as bonus feats at 1st level. If she uses any other kind
of weapon or armor, she loses her abilities from this archetype (except illiteracy) for the next 24
hours.

This alters the barbarian's normal weapon and armor proficiencies.

## Illiteracy {#illiteracy}

A wildborn cannot read or write. She can learn to read or write a language only if she takes a level
in another class, and even then only by taking 1 or more ranks in Linguistics.

## Live Off the Land (Ex) {#live-off-the-land}

At 3rd level, a wildborn can survive capably in the wilderness without any sort of manufactured
equipment or gear. She adds [half](ref/misc/fractions-and-rounding) her barbarian level as a bonus
on Survival checks to hunt or gather food and gains a +1 bonus on Fortitude saves to resist the
effects of extreme temperatures or other environmental effects; the Fortitude save bonus increases
by 1 at 6th level and every 3 levels thereafter.

This replaces trap sense.

## Bonus Feats {#bonus-feats}

At 4th level, 10th level and 16th level, a wildborn can choose a bonus feat from the following
rather than select a rage power: [Alertness](ref/feat/alertness),
[Animal Affinity](ref/feat/animal-affinity), [Athletic](ref/feat/athletic),
[Great Fortitude](ref/feat/great-fortitude),
[Improvised Weapon Mastery](ref/feat/improvised-weapon-mastery), [Iron Will](ref/feat/iron-will),
[Lightning Reflexes](ref/feat/lightning-reflexes), [Self-Sufficient](ref/feat/self-sufficient),
[Stealthy](ref/feat/stealthy), or [Throw Anything](ref/feat/throw-anything).

This alters rage powers.

## Inexhaustible (Ex) {#inexhaustible}

Wildborn live ruggedly and sleep lightly. At 7th level, a wildborn recovers nonlethal damage for
each minute of rest as if an hour had passed. She applies twice her
[damage reduction](ref/rule/damage-reduction) gained from barbarian levels against nonlethal damage.

This alters [damage reduction](ref/rule/damage-reduction).

## Rage Powers {#rage-powers}

The following rage powers complement the wildborn archetype:
[animal fury](ref/ragepower/animal-fury), [beast totem](ref/ragepower/beast-totem),
[bestial climber](ref/ragepower/bestial-climber), [bestial swimmer](ref/ragepower/bestial-swimmer),
[greater beast totem](ref/ragepower/greater-beast-totem),
[lesser beast totem](ref/ragepower/lesser-beast-totem),
[low-light vision](ref/ragepower/low-light-vision), [raging climber](ref/ragepower/raging-climber),
[raging leaper](ref/ragepower/raging-leaper), [raging swimmer](ref/ragepower/raging-swimmer), and
[swift foot](ref/ragepower/swift-foot).
