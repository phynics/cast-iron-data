+++
id = "ref/rule/climb"
kind = "rule"
title = "Climb"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "climb", path = "json/rules_opt_skills01.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "56"

[fields]
kind = "none"
+++

Using Athletics, you can advance up, down, or across a slope, wall, or other steep incline (or a
ceiling if it has handholds). You move at one-quarter your speed, though you can move at half your
speed if you take a -5 penalty. If you fail the check by 4 or less, you make no progress. If you
fail by 5 or more, you fall. A perfectly smooth vertical (or inverted) surface can't be climbed.

You need both hands free to climb, but can cling with one hand while using the other to cast a spell
or take some other action. You can't use a shield while climbing. You lose your Dexterity bonus to
AC while climbing. If you take damage while climbing, you must succeed at an Athletics check against
the DC of the surface or fall.

|Surface or Activity|Athletics DC|
| --- | --- |
|Slope too steep to walk up|0|
|Knotted rope with a wall to brace against|0|
|Knotted rope or rope affected by [rope trick](ref/spell/rope-trick)|5|
|Rope with a wall to brace against|5|
|Surface with ledges to hold on to or stand on|10|
|Pull yourself up when dangling|15|
|Surface with handholds and footholds|15|
|Unknotted rope|15|
|Uneven surface with handholds (dungeon wall)|20|
|Rough surface (natural rock or brick wall)|25|
|Overhang or ceiling with handholds only|30|

**Climbing Modifiers:** The circumstances listed on the table modify Athletics DCs. They stack with
each other.

|Climbing Circumstance|Athletics DC Modifier|
| --- | --- |
|Bracing against two opposite walls (chimney)|-10|
|Bracing against perpendicular walls (corner)|-5|
|Surface is slippery|+5|

**Action:** None. Each move action you take requires a separate Athletics check.

**Making Handholds and Footholds:** You can pound pitons into a wall to change the wall's base DC
to 15. This takes 1 minute per piton, and one piton is needed per 5 feet of distance. You can cut
your own handholds into an ice wall for the same purpose if you have a handaxe or similar implement.

**Climb Speeds:** A creature with a climb speed gains a +8 racial bonus on Athletics checks to
climb. See the [Climb skill](ref/skill/climb) for more information on climb speeds.

**Hauling:** You can haul a character up or down on a rope by sheer strength so that character
doesn't need to attempt Athletics checks. You can lift double your maximum load in this manner.
