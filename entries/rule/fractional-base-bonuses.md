+++
id = "ref/rule/fractional-base-bonuses"
kind = "rule"
title = "Multiclass Fractional Base Bonuses"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fractional_base_bonuses", path = "json/rules_opt_pc_adv01.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "40"

[fields]
kind = "none"
+++

Multiclass characters in the core rules are at a slight disadvantage when it comes to their
statistics. This fractional base bonuses variant is designed to help multiclass characters fulfill
their true potential and stand tall among their single-class peers. It is ideal for campaigns
featuring many multiclass characters, particularly if those characters take levels in many different
classes or prestige classes.

Base attack bonuses and base save bonuses in the Core Rulebook progress at a fractional rate, but
those fractions are eliminated because of rounding; it doesn't make sense to distinguish a base
attack bonus of +6-1/2 from a base attack bonus of +6 when a character with either bonus would hit
AC 17 on a roll of 11 and miss on a 10. For ease of reference, the values in the class tables are
rounded this way since it never makes a difference for single-class characters. However, for
multiclass characters, this rounding often results in a base attack bonus that's too low, as well as
base save bonuses that are imbalanced. The following variant results in more accurate base bonuses
for multiclass characters, based on the formulas behind the class progression tables rather than on
the tables themselves.

For example, a character who's a 1st-level wizard and a 1st-level rogue has a base attack bonus
(BAB) of +0 from each class, resulting in a total BAB of +0 - worse than a 2nd-level wizard or
2nd-level rogue. But that's only because each fraction was rounded down to 0 before adding them
together; the character theoretically has a BAB of +3/4 from her rogue level and +1/2 from her
wizard level. If the rounding was done after adding the fractional values together rather than
before, the character would have a BAB of +1 (rounded down from +1-1/4) - the same as a 2nd-level
wizard or rogue.

### Table 1-7: Fractional Bonuses by Class Level

|Class Level|Base Save Bonus (Good)\*|Base Save Bonus (Poor)|Base Attack Bonus (d10 or d12)|Base Attack Bonus (d8)|Base Attack Bonus (d6)|
| --- | --- | --- | --- | --- | --- |
|1st|+1/2|+1/3|+1|+3/4|+1/2|
|2nd|+1|+2/3|+2|+1-1/2|+1|
|3rd|+1-1/2|+1|+3|+2-1/4|+1-1/2|
|4th|+2|+1-1/3|+4|+3|+2|
|5th|+2-1/2|+1-2/3|+5|+3-3/4|+2-1/2|
|6th|+3|+2|+6|+4-1/2|+3|
|7th|+3-1/2|+2-1/3|+7|+5-1/4|+3-1/2|
|8th|+4|+2-2/3|+8|+6|+4|
|9th|+4-1/2|+3|+9|+6-3/4|+4-1/2|
|10th|+5|+3-1/3|+10|+7-1/2|+5|
|11th|+5-1/2|+3-2/3|+11|+8-1/4|+5-1/2|
|12th|+6|+4|+12|+9|+6|
|13th|+6-1/2|+4-1/3|+13|+9-3/4|+6-1/2|
|14th|+7|+4-2/3|+14|+10-1/2|+7|
|15th|+7-1/2|+5|+15|+11-1/4|+7-1/2|
|16th|+8|+5-1/3|+16|+12|+8|
|17th|+8-1/2|+5-2/3|+17|+12-3/4|+8-1/2|
|18th|+9|+6|+18|+13-1/2|+9|
|19th|+9-1/2|+6-1/3|+19|+14-1/4|+9-1/2|
|20th|+10|+6-2/3|+20|+15|+10|

\*If at least one of the character's classes has a good saving throw progression for the save in
question, add 2 to the total save bonus.
