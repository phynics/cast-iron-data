+++
id = "ref/rule/step-2-target-statistics"
kind = "rule"
title = "Step 2: Target Statistics"
source_ids = ["bestiary", "bestiary-2"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "step_2_target_statistics", path = "json/rules_gm07.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder RPG Bestiary pg 290, Bestiary 2 pg 293

Once you have a creature's type and CR determined, use Table 1-1 to determine its approximate
statistics by CR. These values are a rough guideline only. You will notice that many of the existing
monsters do not follow these guidelines exactly. Most monsters excel in one of these areas, usually
in the amount of damage dealt, but lag in one or two other areas to help balance them out. When
referring to Table 1-1, keep the following points in mind.

**CR:** This is the approximate CR of the monster. This number might change as design progresses.

**Hit Points:** This is the approximate hit point total for the monster. Note that creatures with
particularly high Armor Classes or saving throws, or a number of resistances, might have a lower
number. Outsiders and constructs typically have lower hit point totals.

**Armor Class:** This is the average Armor Class for a creature of this CR. When it comes time to
design the creature's protections, keep this number in mind. Creatures with hit points above the
average often have lower Armor Class values to compensate.

**High Attack:** This is the average total attack bonus for a creature of this CR. This value is for
creatures that are primarily melee or ranged combatants. Creatures with a higher than normal average
damage typically have a lower attack value to compensate.

**Low Attack:** This is the average total attack bonus for a creature of this CR that does not rely
upon melee or ranged attacks to deal damage. This includes most creatures that rely on spells and
[spell-like abilities](ref/umr/spell-like-abilities) in combat.

**Average Damage:** This is the average amount of damage dealt by a creature of this CR if all of
its attacks are successful. To determine a creature's average damage, add the average value for all
of the damage dice rolled (as determined by [Table 1-5](ref/rule/step-7-other-statistics)) to the
damage modifier for each attack. A creature that relies on melee or ranged weapons in combat should
have average damage within the range of high and low damage. A creature with higher than normal
attack bonuses will often deal lower damage, while a creature with lower than normal attack bonuses
will often deal higher damage.

**Primary Ability DC:** This is the average difficulty class (DC) for any spells,
[spell-like abilities](ref/umr/spell-like-abilities), and special abilities (such as breath weapons)
possessed by a creature of this CR that relies on such attacks in combat. If an ability is
particularly powerful, it might have a lower DC to compensate.

**Secondary Ability DC:** This is the average DC for spells and special abilities for a creature
that does not rely on such attacks in combat. Generally, a DC should not be lower than this number.

**Good Save:** This is the average saving throw bonus for a creature of this CR if the saving throw
is one of the creature's good saving throws.

**Poor Save:** This is the average saving throw bonus for a creature of this CR if the saving throw
is one of the creature's poor saving throws.

### Table 1-1: Monster Statistics by CR

|CR|Hit Points|Armr Class|High Attack|Low Attack|High Avg Dmg|Low Avg Dmg|Primary Ability DC|Secondary Ability DC|Good Save|Poor Save|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|1/2|10|11|1|0|4|3|11|8|3|0|
|1|15|12|2|1|7|5|12|9|4|1|
|2|20|14|4|3|10|7|13|9|5|1|
|3|30|15|6|4|13|9|14|10|6|2|
|4|40|17|8|6|16|12|15|10|7|3|
|5|55|18|10|7|20|15|15|11|8|4|
|6|70|19|12|8|25|18|16|11|9|5|
|7|85|20|13|10|30|22|17|12|10|6|
|8|100|21|15|11|35|26|18|12|11|7|
|9|115|23|17|12|40|30|18|13|12|8|
|10|130|24|18|13|45|33|19|13|13|9|
|11|145|25|19|14|50|37|20|14|14|10|
|12|160|27|21|15|55|41|21|15|15|11|
|13|180|28|22|16|60|45|21|15|16|12|
|14|200|29|23|17|65|48|22|15|17|12|
|15|220|30|24|18|70|52|23|16|18|13|
|16|240|31|26|19|80|60|24|17|19|14|
|17|270|32|27|20|90|67|24|18|20|15|
|18|300|33|28|21|100|75|25|18|20|16|
|19|330|34|29|22|110|82|26|19|21|16|
|20|370|36|30|23|120|90|27|20|22|17|
|21|400|37|31|24|130|98|27|20|23|18|
|22|440|39|32|25|140|105|28|21|23|18|
|23|480|40|33|26|150|113|29|22|24|19|
|24|520|42|35|27|165|124|30|23|25|20|
|25|560|43|36|28|180|135|30|24|26|21|
