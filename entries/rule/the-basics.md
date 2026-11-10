+++
id = "ref/rule/the-basics"
kind = "rule"
title = "The Basics"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "the_basics", path = "json/rules_opt_combat01.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "110"

[fields]
kind = "none"
+++

When making a full attack, roll only one attack roll and compare your result to the target's AC. If
your attack result is lower than the target's AC by 6 or more, you miss and deal no damage. If your
result is lower than the target's AC by 5 or less, you deliver a glancing blow, dealing an amount of
damage equal to 1/2 the minimum damage you would normally deal on a hit with the weapon you're
using. Effects that trigger on a hit do not trigger on a glancing blow. If your attack result equals
or exceeds the target's AC, you score a hit, plus one additional hit for every 5 by which your roll
exceeds that target's AC, up to your maximum number of hits. At first level, you can score a maximum
of only one hit, but at base attack bonus +6 and at every +5 to your base attack bonus thereafter,
you can score another. This is shown on Table 3-3, and also matches the progression of iterative
attacks you'd gain if you were using the core rules for attacks. For each hit you score, roll damage
separately; [damage reduction](ref/rule/damage-reduction) applies to each hit.

For example, say you have a base attack bonus of +8, are using a melee weapon that deals 1d10 points
of damage on a hit, and have a Strength modifier of +4. Your target has an AC of 21. If your attack
roll result is 15 or lower, you miss. If your result is 16-20, you deal a glancing blow for 2 points
of damage (your damage die's minimum of 1 plus your Strength modifier of +4, divided by 2 and
rounded down). If your result is 21-25, you hit and deal 1d10+4 points of damage. If your result is
26 or higher, you hit twice and deal 1d10+4 points of damage twice. Even if your result were 31 or
higher, you would still hit only twice because your base attack bonus is lower than +11.

**Tracking:** When using this system, it speeds up the game if players calculate in advance the
amount of damage they deal on a glancing blow with each weapon their characters use and write it on
the character sheets. It also helps if the GM notes the monster's AC - 6, AC + 5, AC + 10, and
AC + 15.

### Table 3-2: Attack Results

|Attack Roll Result|Type of Hit|Damage Dealt|
| --- | --- | --- |
|Below AC by 6 or more|Miss|None|
|Below AC by 5 or less|Glancing Blow|1/2 minimum damage|
|Equal or exceed AC|Hit|Normal damage|
|Exceed AC by 5 or more\*|Additional hit|Normal damage|

\* You can gain an additional hit for every 5 by which the attack roll exceeds the target's AC,
limited by your base attack bonus.

### Table 3-3: Maximum Hits

|Base Attack Bonus|Maximum Hits|
| --- | --- |
|+0 to +5|1|
|+6 to +10|2|
|+11 to +15|3|
|+16 to +20|4|
|+21 to +25\*|5|
|+26 to +30\*|6|

\*Typically, only monsters have a base attack bonus this high.
