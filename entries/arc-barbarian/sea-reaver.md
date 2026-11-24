+++
id = "ref/arc-barbarian/sea-reaver"
kind = "archetype"
title = "Sea Reaver"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Sea%20Reaver"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sea_reaver", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "ultimate-combat"
page = "29"

[fields]
kind = "archetype"
features = [
  { anchor = "marine-terror", level = 1 },
  { anchor = "eyes-of-the-storm", level = 2 },
  { anchor = "savage-sailor", level = 3 },
  { anchor = "sure-footed", level = 5 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["marine-terror"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["eyes-of-the-storm"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["savage-sailor"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["sure-footed"] },
]
+++

Not all barbarians hunt forests, plains, and mountains. Some are raiding terrors on the sea and
coasts, pillaging those who hoard treasure and pursuing monsters of the deep. Some sea reavers are
no more than hunters of the open sea, while others are raiders striking fear into coastal
settlements within reach of the sea reavers' longships.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A sea reaver is not proficient with medium armor.

## Marine Terror (Ex) {#marine-terror}

A sea reaver can [hold her breath](ref/misc/hold-your-breath) for a number of rounds equal to four
times her Constitution score. In addition, a sea reaver can move normally though squares of standing
water or bog that is 1 foot deep. It does not cost her extra movement to traverse these terrains.
Lastly, a sea reaver ignores the normal [cover](ref/rule/cover) bonus to AC when attacking creatures
that are partially immersed in water. This ability replaces fast movement.

## Eyes of the Storm (Ex) {#eyes-of-the-storm}

At 2nd level, a sea reaver ignores any [concealment](ref/rule/concealment) provided by fog, rain,
sleet, mist, wind, or other weather effects that is less than total concealment, and any penalties
weather applies on Perception checks are halved. This ability replaces uncanny dodge.

## Savage Sailor (Ex) {#savage-sailor}

At 3rd level, a sea reaver gains a +1 bonus on Acrobatics, Climb, Profession (sailor), Survival, and
Swim checks made in aquatic terrain, including aboard a ship or along shorelines. These bonuses
improve by +1 every three levels after 3rd. This ability replaces trap sense.

## Sure-Footed (Ex) {#sure-footed}

At 5th level, a sea reaver takes no penalties when moving across slick surfaces, whether natural or
magical (e.g., _[grease](ref/spell/grease)_, _[ice storm](ref/spell/ice-storm)_, and
_[sleet storm](ref/spell/sleet-storm)_). She is not at risk of falling, is not denied her Dexterity
bonus when moving across such areas, and does not treat them as difficult terrain. This ability
replaces improved uncanny dodge.

## Rage Powers {#rage-powers}

The following rage powers complement the sea reaver archetype:
[bestial leaper](ref/ragepower/bestial-leaper), [bestial swimmer](ref/ragepower/bestial-swimmer),
[come and get me](ref/ragepower/come-and-get-me), [hurling charge](ref/ragepower/hurling-charge),
[raging leaper](ref/ragepower/raging-leaper), [raging swimmer](ref/ragepower/raging-swimmer),
[rolling dodge](ref/ragepower/rolling-dodge), and [smasher](ref/ragepower/smasher).
