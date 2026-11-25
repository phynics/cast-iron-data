+++
id = "ref/arc-brawler/living-avalanche"
kind = "archetype"
title = "Living Avalanche"
aon = "ArchetypeDisplay.aspx?FixedName=Brawler%20Living%20Avalanche"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "living_avalanche", path = "json/archetypes_brawler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/brawler" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "42"

[fields]
kind = "archetype"
features = [
  { anchor = "earth-discipline", level = 2 },
  { anchor = "landslide", level = 3 },
  { anchor = "unyielding", level = 4 },
  { anchor = "avalanche", level = 16 },
  { anchor = "improved-avalanche", level = 20 },
]
trades = [
  { replaces = "Bonus feats gained at 2nd and 5th levels", feature = "bonus-combat-feats", levels = [2, 5], by = ["earth-discipline"] },
  { replaces = "The brawler's AC bonus", feature = "ac-bonus", by = ["unyielding"] },
  { replaces = "Awesome blow", feature = "awesome-blow", by = ["avalanche"] },
  { replaces = "Improved awesome blow", feature = "improved-awesome-blow", by = ["improved-avalanche"] },
  { alters = "Maneuver training", feature = "maneuver-training", by = ["landslide"] },
]
+++

When a living avalanche is on the move, no one can stand in her way.

## Earth Discipline (Ex) {#earth-discipline}

At 2nd level, a living avalanche gains [Improved Overrun](ref/feat/improved-overrun) as a bonus
feat, even if she doesn't meet the prerequisites. At 5th level, she gains
[Improved Bull Rush](ref/feat/improved-bull-rush) as a bonus feat, even if she doesn't meet the
prerequisites.

This replaces the bonus feats gained at 2nd and 5th levels.

## Landslide (Ex) {#landslide}

At 3rd level, a living avalanche must choose [overrun](ref/rule/overrun) as her first combat
maneuver for maneuver training. At 7th level, she must choose [bull rush](ref/rule/bull-rush) as her
second combat maneuver for maneuver training. She doesn't gain training in any new combat maneuvers
at later levels, but her bonuses on combat maneuver checks and to CMD for bull rush and overrun
combat maneuvers increase as normal. She gains the following benefits at the listed levels.

At 11th level, if she succeeds at an overrun combat maneuver as part of a [charge](ref/rule/charge),
she automatically knocks her target [prone](ref/rule/prone) (no matter the result of her check). In
addition, if the living avalanche succeeds at a bull rush combat maneuver as part of a charge, she
reduces the penalty combat maneuver checks to bull rush each creature beyond the first by 2.

At 15th level, the living avalanche can attempt bull rush and overrun combat maneuvers against
creatures two sizes larger than herself, but only as part of a charge.

At 19th level, if the living avalanche succeeds at a bull rush combat maneuver as part of a charge,
she reduces the penalty on combat maneuver checks to bull rush each creature beyond the first by an
additional 2. When attempting an overrun combat maneuver as part of a charge, she also ignores any
increase to a creature's CMD from having more than two legs.

This alters maneuver training.

## Unyielding (Ex) {#unyielding}

At 4th level, when a living avalanche wears light armor or no armor, she gains DR 1/adamantine. This
damage reduction increases by 1 at 9th, 13th, and 18th levels.

This replaces the brawler's AC bonus.

## Avalanche (Ex) {#avalanche}

At 16th level, a living avalanche can attempt to overrun multiple creatures as a full-round action.
The living avalanche moves up to twice her speed in a straight line and attempts an overrun combat
maneuver against each creature in her path, as long as that creature is no more than two size
categories larger than herself. Each creature she succeeds against is knocked prone and takes damage
as if the living avalanche hit it with a close weapon she is wielding or an unarmed strike. If she
fails her combat maneuver check against a creature, she stops her movement in the space directly in
front of the creature.

This replaces awesome blow.

## Improved Avalanche (Ex) {#improved-avalanche}

At 20th level, if a living avalanche rolls a natural 20 on an overrun combat maneuver check as part
of the avalanche ability, she can immediately attempt to confirm the critical hit by attempting
another combat maneuver check with the same modifiers as the previous one; if the critical hit is
confirmed, the attack deals double damage.

This replaces improved awesome blow.
