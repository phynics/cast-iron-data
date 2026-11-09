+++
id = "ref/rule/fast-play-ship-combat"
kind = "rule"
title = "Fast-Play Ship Combat"
source_ids = ["game-mastery-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fast_play_ship_combat", path = "json/rules_gm06.json" },
]
[[sources]]
publication = "game-mastery-guide"
page = "214"

[fields]
kind = "none"
+++

When ships themselves become a part of a combat, things get more unusual. The following rules are
not meant to accurately simulate all of the complexities of ship-to-ship combat, only to provide you
with a quick and easy set of rules to resolve such situations when they inevitably arise in a
nautical adventure, whether it be a battle between two ships or between a ship and a sea monster.

**Preparation:** Decide what type of ships are involved in the combat. Use a large, blank battle mat
to represent the waters on which the battle occurs. A single square corresponds to 30 feet of
distance. Represent each ship by placing markers that take up the appropriate number of squares
(miniature toy ships make great markers and should be available at most hobby stores).

**Starting Combat:** When combat begins, allow the PCs (and important NPC allies) to roll initiative
as normal; the ship itself moves and attacks on the captain's initiative result. If any of the ships
in the battle rely on sails to move, randomly determine what direction the wind is blowing by
rolling 1d8 and following the guidelines for [missed splash weapons](ref/rule/throw-splash-weapon).

**Movement:** On the captain's initiative count, the ship can move its current speed in a single
round as a move-equivalent action for the captain (or double its speed as a full-round action), as
long as it has its minimum crew complement. The ship can increase or decrease its speed by 30 feet
each round, up to its maximum speed. Alternatively, the captain can change direction (up to one side
of a square at a time) as a standard action. A ship can only change direction at the start of a
turn.

**Attacks:** Crew members in excess of the ship's minimum crew requirement can be allocated to man
siege engines. [Rules for siege engines can be found here](ref/rule/siege-engines-uc). Siege engines
attack on the captain's initiative count.

A ship can also attempt to ram a target if it has its minimum crew. To ram a target, the ship must
move at least 30 feet and end with its bow in a square adjacent to the target. The ship's captain
then makes a Profession (sailor) check; if this check equals or exceeds the target's AC, the ship
hits its target, inflicting damage as indicated on the [ship statistics](ref/rule/ship-statistics)
table to the target, as well as minimum damage to the ramming ship. A ship outfitted with an actual
ram siege engine inflicts an additional 3d6 points of damage to the target (the ramming vessel
suffers no additional damage).

### Sinking

A ship gains the sinking condition if its hit points are reduced to 0 or fewer. A sinking ship
cannot move or attack, and it sinks completely 10 rounds after it gains the sinking condition. Each
hit on a sinking ship that inflicts damage reduces the remaining time for it to sink by 1 round per
25 points of damage inflicted. Magic (such as [make whole](ref/spell/make-whole)) can repair a
sinking ship if the ship's hit points are raised above 0, at which point the ship loses the sinking
condition. Generally, nonmagical repairs take too long to save a ship from sinking once it begins to
go down.
