+++
id = "ref/rule/performance-combat-check"
kind = "rule"
title = "Performance Combat Check"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "performance_combat_check", path = "json/rules_adv_gm01.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "154"

[fields]
kind = "none"
+++

Whenever a combatant has a chance to affect the crowd's attitude, she makes a performance combat
check. The check is a Charisma ability check modified by the base attack bonus of the character plus
any ranks the character has in Perform (act), Perform (comedy), or Perform (dance), whichever is
highest. Making a performance combat check is usually a swift action, triggered when a combatant
performs a trigger action (see
[Affecting the Crowd's Attitude](ref/rule/affecting-the-crowds-attitude)).

### Base Attack Bonus

|Base Attack Bonus|Bonus on Performance Combat Check|
| --- | --- |
|0|+0|
|1-5|+1|
|6-10|+2|
|11-15|+3|
|16+|+4|

### Perform Ranks

|Highest Perform Rank|Bonus on Performance Combat Check|
| --- | --- |
|0|+0|
|1-5|+1|
|6-10|+2|
|11-15|+3|
|16+|+4|

Using a performance weapon grants a combatant a +2 bonus on performance combat checks. Some feats,
spells, or other circumstances may grant a combatant a bonus on performance combat checks.

Succeeding at a performance combat check improves the attitude of the crowd by one step. Unlike
skill checks, a roll of a natural 20 on a performance combat check always succeeds. Failing the
check either leaves the attitude unchanged or, if the check fails by 5 or more, causes the attitude
of the crowd to decrease by one step. The DC of the check is determined by the crowd's current
attitude, with a number of adjustments to the DC granted by the circumstances of the performance
combat. If the crowd's current attitude is helpful, a successful check grants the favored side 1
victory point.

### Performance Combat Check DC

The performance combat check's DC is based on a number of factors, including the starting or current
attitude of the crowd, the size of the crowd, and the number of creatures participating in the
performance combat. The base DC of the performance combat check is determined by the current
attitude of the crowd toward the side of combat.

|Starting or Current Attitude|Base DC to Improve Attitude|
| --- | --- |
|Hostile|20|
|Unfriendly|15|
|Indifferent|10|
|Friendly|15|
|Helpful|20^[1](ref/rule/performance-combat-check#footnote-1)^|

**Size of the Crowd:** Larger crowds are harder to sway to one side or the other. It takes great
shows of daring or a progression of numerous displays of crowd-pleasing actions to get them to
change their attitude. Presented here are the general crowd sizes and their effects on the DC to
improve crowd attitudes and gain victory points.

**Small Crowd:** A small crowd contains no fewer than two and no more than 25 creatures. It does not
increase the base DC of all performance combat checks.

**Medium Crowd:** A medium crowd contains no fewer than 26 and no more than 100 creatures. A medium
crowd increases the DC of all performance combat checks by +2.

**Large Crowd:** A large crowd contains no fewer than 101 and no more than 300 creatures. A large
crowd increases the DC of all performance combat checks by +3.

**Massive Mob:** A massive mob is made up of no fewer than 301 creatures, and its numbers can expand
into the thousands. A massive mob increases the DC of all performance combat checks by +4.

**Total Number of Combatants:** The participation of a large number of combatants increases the
difficulty of swaying the crowd. Large groups of combatants make it difficult for a crowd to follow
the entire battle and to catch actions from individuals that could possibly sway the audience's
attitude. Adjust these modifications as combatants enter or leave the battle.

**Small Battle:** If the battle is between a total of 2-8 combatants, there is no change to the base
DC to improve the attitude of the crowd or gain victory points.

**Medium Battle:** If the battle is between 9-16 combatants, the DC to improve the attitude of the
crowd or gain victory points increases by +4.

**Large Battle:** A battle with 17 or more total combatants increases the DC to improve the attitude
of the crowd by +8.

**Other Circumstances That Affect DC:** Other circumstances that always affect the DC to improve the
attitude of the crowd or gain victory points include the following.

**Cheating:** If one side visibly cheats or breaks the rules, the DC for that side of the
performance combat to improve the attitude of the crowd increases by 2 for the remainder of the
performance combat. This increase can occur multiple times in a battle. For the purpose of spotting
cheating, determine the base Perception and Sense Motive for the average member of a crowd (usually
+0 if you assume an average human) and apply the following modifiers based on crowd size. The DC is
based on whatever action the combatant is using to hide any cheating (usually Bluff or Stealth).

|Crowd Size|Bonus on Perception and Sense Motive Checks to Spot Cheating|
| --- | --- |
|Small crowd|+8|
|Medium crowd|+12|
|Large crowd|+16|
|Massive mob|+20|

**Outnumbered:** If one side of the battle outnumbers the others by less than a 2:1 ratio, the DC
for that side to improve the attitude of the crowd or to gain victory points increases by 2. If one
side outnumbers all others by a ratio of 2:1 or more, the DC for that side to improve the attitude
of the crowd increases by 6. These increases to the DC end or are reduced to the appropriate level
if the numbers become even or if the 2:1 ratio of combatants is ever brought down to outnumbering
the other sides by less than a 2:1 ratio.

**Unfair Advantage:** If one side of the battle has an obvious unfair advantage (for example, one
side starts the battle in a fortified position or has better weapons and armor, or its opponents are
not armed at all), the DC to improve the attitude of the crowd is increased by 2. A GM can increase
the DC by as much as 6 if the unfair advantage is severe enough.

**Bribery or Coercion:** Crowds can be bribed or coerced. Typically a successful bribe or attempt at
coercion involves paying some amount of gold based on the crowd size, and succeeding at a Diplomacy
check with a DC based on the size of the crowd. If the gold is paid and the Diplomacy check fails,
the side gains a penalty for cheating instead, though the gold is still spent. If the check
succeeds, the DC to improve crowd reaction and gain victory points decreases by 2. For every 5
points over the DC by which the combatants make the check, the DC to improve the crowd's attitude or
to gain a victory point decreases by 1.

|Crowd Size|Diplomacy DC|Gold Paid|
| --- | --- | --- |
|Small crowd|DC 15|25 gp|
|Medium crowd|DC 20|250 gp|
|Large crowd|DC 25|750 gp|
|Massive mob|DC 30|2,000 gp|

###### ^1^ {#footnote-1}

This is the DC to gain a victory point. The base DC is modified by the size of the crowd, the number
of participants on each side, and a number of other circumstances.
