+++
id = "ref/rule/adding-racial-hit-dice"
kind = "rule"
title = "Adding Racial Hit Dice"
source_ids = ["bestiary"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "adding_racial_hit_dice", path = "json/rules_gm07.json" },
]
[[sources]]
publication = "bestiary"
page = "295"

[fields]
kind = "none"
+++

Adding racial Hit Dice to a monster is a similar process to building a monster from scratch. As
additional Hit Dice are added, other abilities increase in power as well. Additional Hit Dice
usually results in better attack bonuses, saves, hit points, and skills, as well as more feats. It
can also include additional spellcasting capability and other powers.

### Step 1: Plan the monster

When advancing a monster by adding racial HD, you should start by deciding what you want the monster
to become. In most cases, this means merely a tougher, stronger version of an existing monster. Note
the desired CR of the new monster. This is also the point at which you should decide whether the
creature is going to increase in size. As a general rule, creatures whose Hit Dice increase by 50%
or more should also increase in size, but GMs should feel free to ignore this rule if warranted by
the individual creature or situation.

### Step 2: Add Hit Dice

Next, determine how many Hit Points the base monster receives per Hit Die (see
[Table 1-5](ref/rule/step-7-other-statistics) for average results based on the die type). Using
Table 2-1, add up all of the values in the Hit Point Change column for each increase using the
Higher CR column. For example, if the base monster was CR 3 and the new monster is set to be CR 5,
the total would be 25 hit points. Next, add additional Hit Dice to the monster to increase its hit
points by the desired amount. Note that if the creature increases in size, its Constitution may also
increase, as noted on Table 2-2, granting it additional hit points that might offset the need for
additional Hit Dice (this also applies to any other Constitution increases).

These values are not absolute. Some monsters have fewer hit points than normal for a creature of
their CR and rely on a higher AC or other defenses. Some creatures are primarily spellcasters and
typically have fewer Hit Dice. When advancing your monster in this way, be sure to take these
factors into account and adjust your monster accordingly.

#### Table 2-1: Monster Advancement

|Higher CR|Lower CR|Hit Point Change|AC Change|Attack Bonus Change|Damage Change|
| --- | --- | --- | --- | --- | --- |
|1|Less than 1|5|1|1|2-3|
|2|1|5|2|1|2-3|
|3|2|10|1|1-2|2-3|
|4|3|10|2|2|2-3|
|5|4|15|1|1-2|3-4|
|6|5|15|1|1-2|3-5|
|7|6|15|1|1-2|4-5|
|8|7|15|1|1-2|4-5|
|9|8|15|2|1-2|4-5|
|10|9|15|1|1|3-5|
|11|10|15|1|1|4-5|
|12|11|15|2|1-2|4-5|
|13|12|20|1|1|4-5|
|14|13|20|1|1|3-5|
|15|14|20|1|1|4-5|
|16|15|20|1|1-2|8-10|
|17|16|30|1|1|7-10|
|18|17|30|1|1|8-10|
|19|18|30|1|1|7-10|
|20|19|40|2|1|8-10|
|21+|20+|40|2|1|8-10|

#### Table 2-2: Size Changes

|Old Size\*|New Size|Str|Dex|Con|Natural Armor|
| --- | --- | --- | --- | --- | --- |
|Fine|Diminutive|Same|-2|Same|Same|
|Diminutive|Tiny|+2|-2|Same|Same|
|Tiny|Small|+4|-2|Same|Same|
|Small|Medium|+4|-2|+2|Same|
|Medium|Large|+8|-2|+4|+2|
|Large|Huge|+8|-2|+4|+3|
|Huge|Gargantuan|+8|Same|+4|+4|
|Gargantuan|Colossal|+8|Same|+4|+5|

> _\* Repeat the adjustment if the creature moves up more than one size._

#### Table 2-3: Size Bonuses and Penalties

|Size|AC/Attack|CMB/CMD|Fly Skill|Stealth Skill|
| --- | --- | --- | --- | --- |
|Fine|+8|-8|+8|+16|
|Diminutive|+4|-4|+6|+12|
|Tiny|+2|-2|+4|+8|
|Small|+1|-1|+2|+4|
|Medium|+0|+0|+0|+0|
|Large|-1|+1|-2|-4|
|Huge|-2|+2|-4|-8|
|Gargantuan|-4|+4|-6|-12|
|Colossal|-8|+6|-8|-16|

### Step 3: Ability Scores

Once you have determined the number of additional Hit Dice possessed by the creature, use this
number to modify its other statistics. Start with ability scores. For every 4 additional Hit Dice
gained by the monster, add 1 to one of its ability scores. In addition, make any modifications to
its ability scores based on an increase in size, as noted on Table 2-2.

### Step 4: Skills and Feats

When adding skills, check to see if the creature's Int modifier changed. If it is unchanged, simply
multiply the total number of ranks per Hit Dice gained by a monster of its type times the total
number of added Hit Dice and add that number of ranks to its existing skills. If its Intelligence
modifier has increased, perform the same calculation as if it had not increased and then multiply
the change in its Intelligence modifier times its new total number of Hit Dice and add that number
of additional ranks as well (adding new skills as needed to spend all of the ranks). If the creature
changed size, make sure to adjust its Fly skill and Stealth skill bonuses (if any) as noted on Table
2-3.

Next, give the creature additional feats. Creatures gain one feat at 1 Hit Die and one additional
feat for every 2 Hit Dice above 1. Most additional feats should be focused on increasing the
creature's combat abilities, but metamagic feats and skill feats are also possible choices depending
on the creature's role.

### Step 5: Statistics

Next, adjust the creature's derived statistics, such as its initiative, AC, saving throws, melee and
ranged attack bonuses, BAB, CMB, and CMD. Adjust any special attacks or qualities that are based on
the creature's size, Hit Dice, or ability scores. If the creature changed in size, be sure to adjust
its AC, attack, CMB, and CMD accordingly (as noted on Table 2-3. Table 2-1 also tracks the average
change to the creature's AC, attack rolls, and damage rolls. Add up these values for each step of
change between the creature's original and new CR. If the creature changed size, make sure to make
changes to its natural armor bonus, as noted on Table 2-2. If the creature does not meet these
averages, you should consider adjusting its ability scores or Hit Dice to get it closer to the
target.

### Step 6: Comparison

Finally, compare the new monster's statistics to those presented on
[Table 1-1](ref/rule/step-2-target-statistics) for a creature of its adjusted CR. Note that if the
original creature deviated from these values, the new one should do so in a similar fashion. For
example, if the original creature had higher than normal hit points but a lower than normal CR, the
creature should maintain that balance at a higher CR (even though its hit points and AC both
increased).
