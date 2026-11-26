+++
id = "ref/arc-cavalier/saurian-champion"
kind = "archetype"
title = "Saurian Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Saurian%20Champion"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "saurian_champion", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "savage-combatant" },
  { anchor = "titanic-challenge", level = 1 },
  { anchor = "wild-warrior", level = 1 },
  { anchor = "dinosaur-mount", level = 1 },
  { anchor = "nimble-rider", level = 2 },
  { anchor = "fierce-devotion", level = 5 },
  { anchor = "quick-rider", level = 8 },
  { anchor = "titanic-mount", level = 10 },
  { anchor = "primeval-devotion", level = 14 },
]
trades = [
  { replaces = "Order", feature = "order", by = ["wild-warrior"] },
  { replaces = "Tactician", feature = "tactician", by = ["dinosaur-mount"] },
  { replaces = "greater tactician", feature = "greater-tactician", by = ["dinosaur-mount"] },
  { replaces = "master tactician", feature = "master-tactician", by = ["dinosaur-mount"] },
  { replaces = "Banner", feature = "banner", by = ["fierce-devotion"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["primeval-devotion"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { alters = "Challenge", feature = "challenge", by = ["titanic-challenge"] },
  { alters = "Mount", feature = "mount", by = ["dinosaur-mount"] },
  { alters = "Class skills" },
]
+++

These primeval cavaliers idolize dinosaurs as apex predators and value them as powerful, oversized
mounts.

## Class Skills {#class-skills}

A saurian champion gains Acrobatics, Knowledge (nature), Perception, and Survival as class skills.

This alters the cavalier's class skills.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A saurian champion does not gain proficiency with medium or heavy armor.

This alters the cavalier's weapon and armor proficiencies.

## Savage Combatant (Ex) {#savage-combatant}

A saurian champion does not rely on lethal charges or firing from afar as more "civilized" cavaliers
do, preferring to rampage among his foes instead. Saurian champions do not deal double damage when
[charging](ref/rule/charge) with a [lance](ref/eq-weapon/lance) (or similar weapon) while mounted.
While mounted, a saurian champion cannot attack with ranged weapons other than thrown weapons.

## Titanic Challenge (Ex) {#titanic-challenge}

A saurian champion considers only the largest creatures a true challenge. His titanic challenge adds
only [half](ref/misc/fractions-and-rounding) his level on damage rolls against Medium or smaller
creatures, but he adds a +1 bonus on attack rolls against a target of his challenge that is at least
two size categories larger than himself (Huge for Medium saurian champions) and a +2 bonus on attack
rolls against a Colossal target of his challenge.

This alters challenge.

## Wild Warrior (Ex) {#wild-warrior}

A saurian champion hails from primeval lands where the civilized orders hold little sway. He does
not select an order or gain any order-related benefits.

This replaces order.

## Dinosaur Mount (Ex) {#dinosaur-mount}

A saurian champion bonds with a dinosaur companion that willingly serves as his mount. This mount
functions as a cavalier's normal mount with the following adjustments: The saurian champion's mount
must be a dinosaur (see the various _Pathfinder RPG Bestiary_ volumes). The saurian champion can
ride mounts of his size category and larger, rather than only those of a larger size. Increase the
mount's Strength score by 8 for the purpose of determining its carrying capacity. Whenever an
ability or feat allows the saurian champion's mount to make a hoof attack, the mount can make a claw
or bite attack instead.

This alters the cavalier's mount and replaces tactician, greater tactician, and master tactician.

## Nimble Rider (Ex) {#nimble-rider}

At 2nd level, a saurian champion gains a +1 dodge bonus to AC when mounted. Anything that causes the
saurian champion to lose his Dexterity bonus to AC also causes him to lose this dodge bonus. This
bonus increases by 1 for every 6 levels beyond 2nd (to a maximum of +4 at 20th level).

## Fierce Devotion (Ex) {#fierce-devotion}

At 5th level, a saurian champion's mount gains the devotion ability, and its effects also apply
against emotion and fear effects. The mount is immune to the effects of
[unnatural aura](ref/umr/unnatural-aura).

This replaces banner.

## Quick Rider (Ex) {#quick-rider}

At 8th level, a saurian champion can attempt [Ride](ref/skill/ride) checks to fast mount or fast
dismount his mount even if it's more than one size category larger than himself.

## Titanic Mount (Ex) {#titanic-mount}

At 10th level, a saurian champion's mount increases in size by one category (even if the base
creature normally does not reach that size). The creature receives the appropriate size penalty on
attack rolls and to AC (-1 if growing to Large or -2 if growing to Huge) and a -2 penalty to
Dexterity (to a minimum Dexterity score of 1), its base damage increases by
[one size category](ref/misc/damage-die-adjustments), and its reach increases to 10 feet (if it
wasn't already). It also gains a +2 size bonus to its Strength and Constitution score. At 12th,
14th, 16th, and 18th levels, the bonus to Strength increases by 2 and the mount's natural armor
increases by 1. At 14th and 18th levels, the bonus to Constitution increases by 2. At 15th level,
the mount's reach increases to 15 feet.

## Primeval Devotion (Ex) {#primeval-devotion}

At 14th level, the bonus on saving throws provided by the mount's devotion ability increases by 2.
In addition, the mount adds half this bonus to other saving throws.

This replaces greater banner.
