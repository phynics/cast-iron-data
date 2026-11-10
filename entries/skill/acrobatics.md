+++
id = "ref/skill/acrobatics"
kind = "rule"
title = "Acrobatics"
source_ids = ["core-rulebook", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "acrobatics", path = "json/skills.json" },
]
[[sources]]
publication = "core-rulebook"
page = "87"

[fields]
kind = "none"
+++

**Associated Skill**

**Details:** Dexterity

**Trained Only**

**Details:** No

**Armor Check Penalty**

**Details:** Yes

**Optional Unchained Skill**

**Details:** No

**Optional Background Skill**

**Details:** No

### Action

None. An Acrobatics check is made as part of another action or as a reaction to a situation.

### Special

If you have 3 or more ranks in Acrobatics, you gain a +3 dodge bonus to AC when
[fighting defensively](ref/misc/fighting-defensively) instead of the usual +2, and a +6 dodge bonus
to AC when taking the [total defense](ref/misc/total-defense) action instead of the usual +4.

If you have the [Acrobatic](ref/feat/acrobatic) feat, you get a bonus on Acrobatics checks.

### Moving Carefully

You can use Acrobatics to move on narrow surfaces and uneven ground without falling. A successful
check allows you to move at half speed across such surfaces - only one check is needed per round.
Use the following table to determine the base DC, which is then modified by the Acrobatics skill
modifiers noted below. While you are using Acrobatics in this way, you are considered
[flat-footed](ref/rule/flat-footed) and lose your Dexterity bonus to your AC (if any). If you take
damage while using Acrobatics, you must immediately make another Acrobatics check at the same DC to
avoid falling or being knocked [prone](ref/rule/prone).

|Surface Width|Base Acrobatics DC|
| --- | --- |
|Greater than 3 feet wide|0|
|1-3 feet wide|5|
|7-11 inches wide|10|
|2-6 inches wide|15|
|Less than 2 inches wide|20|

No Acrobatics check is needed to move across surfaces at least 1 foot wide unless the modifiers to
the surface (see "Other Modifiers" below) increase the DC to 10 or higher.

### Avoiding Attacks

You can move through a threatened square without provoking an attack of opportunity from an enemy by
using Acrobatics. When moving in this way, you move at half speed. You can move at full speed by
increasing the DC of the check by 10. You cannot use Acrobatics to move past foes if your speed is
reduced due to carrying a medium or heavy load or wearing medium or heavy armor. If an ability
allows you to move at full speed under such conditions, you can use Acrobatics to move past foes.
You can use Acrobatics in this way while prone, but doing so requires a **full-round action** to
move 5 feet, and the DC is increased by 5. If you attempt to move through an enemy's space and fail
the check, you lose the move action and provoke an attack of opportunity.

|Situation|Base Acrobatics DC|
| --- | --- |
|Move through a threatened area|Opponent's [CMD](ref/rule/combat-maneuvers)|
|Move through an enemy's space|5 + opponent's CMD|

This DC increases by 2 for each additional opponent avoided in 1 round.

### Jumping

You can use the Acrobatics skill to make jumps or to soften a fall. The base DC to make a jump is
equal to the distance to be crossed (if horizontal) or four times the height to be reached (if
vertical). These DCs double if you do not have at least 10 feet of space to get a running start. The
only Acrobatics modifiers that apply are those concerning the surface you are jumping from (see
"Other Modifiers" below). If you fail this check by 4 or less, you can attempt a DC 20 Reflex save
to grab hold of the other side after having missed the jump. If you fail by 5 or more, you fail to
make the jump and fall (or land prone, in the case of a vertical jump).

Creatures with a base land speed above 30 feet receive a +4 racial bonus on Acrobatics checks made
to jump for every 10 feet of their speed above 30 feet. Creatures with a base land speed below 30
feet receive a -4 racial bonus on Acrobatics checks made to jump for every 10 feet of their speed
below 30 feet.

No jump can allow you to exceed your maximum movement for the round. For a running jump, the result
of your Acrobatics check indicates the distance traveled in the jump (and if the check fails, the
distance at which you actually land and fall prone). Halve this result for a standing long jump to
determine where you land.

|Long Jump|Acrobatics DC|High Jump|Acrobatics DC|
| --- | --- | --- | --- |
|5 feet|5|1 foot|4|
|10 feet|10|2 feet|8|
|15 feet|15|3 feet|12|
|20 feet|20|4 feet|16|
|Greater than 20 feet|+5 per 5 feet|Greater than 4 feet|+4 per foot|

### Falling

When you deliberately fall any distance, even as a result of a missed jump, a DC 15 Acrobatics skill
check allows you to ignore the first 10 feet fallen, although you still end up prone if you take
damage from a fall. See the [falling](ref/rule/falling) rules for further details.

### Other Modifiers

Many conditions can affect your chances of success with Acrobatics checks. The following modifiers
to target DCs apply to all Acrobatics skill checks. The modifiers stack with one another, but only
the most severe modifier for any one condition applies.

|Acrobatics Modifiers|DC Modifier|
| --- | --- |
|Slightly obstructed (gravel, sand)|+2|
|Severely obstructed (cavern, rubble)|+5|
|Slightly slippery (wet)|+2|
|Severely slippery (icy)|+5|
|Slightly sloped (up to 45°)|+2|
|Severely sloped (over 45°)|+5|
|Slightly unsteady (boat in rough water)|+2|
|Moderately unsteady (boat in a storm)|+5|
|Severely unsteady (earthquake)|+10|
|Move at full speed on narrow or uneven surfaces (not jumping)|+5|

### Unchained Rogue Skill Unlocks

**Sources:** Pathfinder Unchained pg 82\
If using [skill unlocks](ref/rule/skill-unlocks), with sufficient ranks in Acrobatics, you earn the
following.

**5 Ranks**

**Details:** You can move at normal speed through a threatened square without provoking an attack of
opportunity by increasing the DC of the check by 5 (instead of by 10). You aren't denied your
Dexterity bonus when attempting Acrobatics checks with DCs of 20 or lower.

**10 Ranks**

**Details:** You can attempt an Acrobatics check at a -10 penalty and use the result as your CMD
against trip maneuvers. You can also attempt an Acrobatics check at a -10 penalty in place of a
Reflex save to avoid falling. You must choose to use this ability before the trip attempt or Reflex
save is rolled. With a successful DC 20 Acrobatics check, you treat an unintentional fall as 10 feet
shorter plus 10 feet for every 10 by which you exceed the DC, and treat an intentional fall as 10
feet shorter for every 10 by which you exceed the DC.

**15 Ranks**

**Details:** You do not provoke attacks of opportunity when standing up from prone.

**20 Ranks**

**Details:** You double the result of any Acrobatics check when jumping and never fall prone at the
end of a fall as long as you remain conscious.
