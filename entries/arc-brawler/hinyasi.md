+++
id = "ref/arc-brawler/hinyasi"
kind = "archetype"
title = "Hinyasi"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Hinyasi"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hinyasi", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "humble-beginnings" },
  { anchor = "improvisation-training", level = 2 },
  { anchor = "improvised-maneuver", level = 4 },
  { anchor = "improvisation-mastery", level = 5 },
]
trades = [
  { replaces = "The bonus combat feat gained at 2nd level", feature = "bonus-combat-feats", levels = [2], by = ["improvisation-training"] },
  { replaces = "Knockout", feature = "knockout", by = ["improvised-maneuver"] },
  { replaces = "Close weapon mastery", feature = "close-weapon-mastery", by = ["improvisation-mastery"] },
  { alters = "The brawler's armor proficiencies", feature = "weapon-and-armor-proficiencies", power = "armor", by = ["humble-beginnings"] },
]
+++

After Yamasa seceded from Lirgen, their elite combatants formed a military caste, called hinyasi,
who protected Yamasa for centuries. Their martial traditions were centered on the use of farming
tools and on other improvised weapons.

## Humble Beginnings (Ex) {#humble-beginnings}

A hinyasi gains her choice of [Catch Off-Guard](ref/feat/catch-off-guard) or
[Throw Anything](ref/feat/throw-anything) as a bonus feat. She is not proficient with shields.

This alters the brawler's armor proficiencies.

## Improvisation Training (Ex) {#improvisation-training}

A hinyasi is skilled at fighting with [improvised weapons](ref/misc/improvised-weapons). She deals
damage equal to her unarmed strike damage while fighting with an improvised weapon. A hinyasi treats
improvised weapons as weapons from the close [fighter weapon group](ref/ability/weapon-groups).

This replaces the bonus combat feat gained at 2nd level.

## Improvised Maneuver (Ex) {#improvised-maneuver}

At 4th level, a hinyasi learns to confound and befuddle her opponents with improvised weapons. She
chooses one of the following combat maneuvers: bull rush, drag, disarm, sunder, reposition, or trip.
When she hits an opponent with an improvised weapon, the hinyasi can perform her chosen combat
maneuver against the same target as a free action. She takes a -4 penalty on the combat maneuver
check, and she can't attempt an improvised maneuver check more than once per round. This combat
maneuver still provokes attacks of opportunity unless the hinyasi has a feat or ability that allows
her to perform it without provoking attacks of opportunity.

At 10th level, she chooses a second combat maneuver that she can use with this ability, though she
can still perform only one improvised maneuver per round. At 16th level, she chooses a third, though
she can still perform only one improvised maneuver per round.

This replaces knockout.

## Improvisation Mastery (Ex) {#improvisation-mastery}

At 5th level, a hinyasi picks one type of improvised weapon (light, one-handed, or two-handed) and
gains a +2 bonus on attack and damage rolls with that type of weapon.

This replaces close weapon mastery.
