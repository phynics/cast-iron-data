+++
id = "ref/arc-rogue/consigliere"
kind = "archetype"
title = "Consigliere"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Consigliere"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "consigliere", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "44"

[fields]
kind = "archetype"
features = [
  { anchor = "convincing-attitude", level = 1 },
  { anchor = "combat-advisor", level = 4 },
  { anchor = "field-boss", level = 10 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["convincing-attitude"] },
  { replaces = "evasion", feature = "evasion", by = ["convincing-attitude"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["combat-advisor"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["combat-advisor"] },
  { replaces = "All instances of trap sense", feature = "trap-sense" },
  { replaces = "Rogue talent normally gained at 10th level", feature = "rogue-talents", levels = [10], by = ["field-boss"] },
]
+++

Consiglieres act as trusted mediators and administrators for crime families and various criminal
organizations, and many serve as the right hand to the leaders of such groups. Other consiglieres
prefer to work as independent operators and sell their advice and expertise to the highest bidder.
Though some consiglieres insulate themselves from violence and criminal activities, many enjoy
getting their hands dirty leading strike teams or gangs of hardened thugs.

## Class Skills {#class-skills}

A consigliere adds Knowledge (nobility) to his list of class skills, instead of Knowledge
(dungeoneering).

This alters the rogue's class skills.

## Convincing Attitude (Ex) {#convincing-attitude}

At 1st level, a consigliere gains [Persuasive](ref/feat/persuasive) as a bonus feat. At 2nd level,
he gains the [charmer](ref/talent/charmer) rogue talent (or the [certainty](ref/talent/certainty)
\[Diplomacy\] rogue talent if he is an unchained rogue). At 3rd level, if a consigliere attempts a
Diplomacy check and fails to influence a creature's attitude by 5 or more, the creature's attitude
remains unchanged instead of decreasing by one step.

This ability replaces trapfinding and evasion.

## Combat Advisor (Ex) {#combat-advisor}

At 4th level, whenever a consigliere misses with a melee attack against an opponent, he can
designate an ally within 30 feet of the target to receive a +1 insight bonus on her next attack roll
against that opponent before the consigliere's next turn. At 8th level, the insight bonus increases
to +2.

This ability replaces uncanny dodge and improved uncanny dodge.

## Bonus Feats (Ex) {#bonus-feats}

Starting at 4th level, a consigliere can choose to gain a single teamwork feat instead of a single
rogue talent. Starting at 12th level, the consigliere can choose to gain teamwork feats instead of
rogue talents as many times as he chooses.

This ability replaces all instances of trap sense.

## Field Boss (Ex) {#field-boss}

At 10th level, as a standard action, a consigliere can grant a teamwork feat to all allies within 30
feet who can see and hear her. This teamwork feat must be one the consigliere knows. Allies retain
the use of this feat for 3 rounds plus 1 round for every 2 rogue levels the consigliere has. Allies
do not need to meet the prerequisites of this teamwork feat. The consigliere can use this ability
once per day at 10th level, plus 1 additional time per day every 4 rogue levels thereafter.

This ability replaces the rogue talent normally gained at 10th level.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the consigliere archetype: assault leader, black market
connections, coax information, honeyed words (or certainty \[Bluff\] for an unchained rogue), and
shades of gray.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the consigliere archetype: hard minded, opportunist,
redirect attack, rumormonger, skill mastery, slippery mind, and unwitting ally.
