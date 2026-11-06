+++
id = "ref/rule/alternate-crafting-rules"
kind = "rule"
title = "Alternate Crafting Rules"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "alternate_crafting_rules", path = "json/rules_opt_skills01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 72

While the rules for crafting in the Core Rulebook are perfectly suitable for the needs of most
campaigns, they can sometimes be cumbersome to use. Those rules assume that a character spends a
full week crafting an item. They also involve complex multiplication to determine the degree of
success and speed with which the item can be crafted. Not only are these rules significantly
different from those for other skill checks, but they can slow down play at the table and give rise
to strange circumstances where it takes an unreasonably long time to create relatively simple items
that happen to have a high gold piece cost. Furthermore, while the system features rules for
attempting daily checks, these rules can be cumbersome for players.

The following system presents crafting rules that are a little easier to use, especially in
conjunction with the [downtime system](ref/rule/downtime).

With this alternative system, use the following version of the Craft skill instead of the one
presented in the Core Rulebook.

### Craft (Int)

You are skilled in the creation of a specific group of items, such as armor or weapons. Like
Knowledge, Perform, and Profession, Craft is actually a number of separate skills. You could have
several Craft skills, each with its own ranks. The most common Craft skills are alchemy, armor,
baskets, books, bows, calligraphy, carpentry, cloth, clothing, glass, jewelry, leather, locks,
paintings, pottery, sculptures, ships, shoes, stonemasonry, traps, and weapons.

A Craft skill is specifically focused on creating something. If an endeavor does not result in a
created product, it probably falls under the heading of a Profession skill.

**Check:** You can practice your trade and make a decent living, earning your check result in silver
pieces per day. You know how to use the tools of your trade, how to perform the craft's daily tasks,
how to supervise untrained helpers, and how to handle common problems. (Untrained laborers and
assistants earn an average of 1 silver piece per day.)

The basic function of the Craft skill, however, is to make an item of the appropriate type. Most
items created with a Craft skill fall into one of several broad categories of complexity. Others
have Craft DCs based on CR (in the case of traps) or on the Fortitude saves required to avoid or
minimize their effects (in the case of poisons).

Before crafting an item, you must have tools and an appropriate workshop or area. If you don't have
access to artisan tools, you can still attempt a Craft check, but you take a -2 penalty when
attempting a check without such tools or with improvised tools. If you have masterwork artisan
tools, you gain a +2 circumstance bonus on the skill check.

After you have a suitable area to craft and you've gathered your tools, you must then acquire raw
materials whose value is equal to 1/4 the cost of the item or items you wish to craft. Given the
necessary tools, materials, and workspace, you can attempt a Craft check of the appropriate DC each
day. If you succeed, you make an amount of progress equal to the silver piece or gold piece value
listed in the appropriate entry in the Base Progress per Day column of Table 2-4: Crafting DCs and
Progress Values. If you exceed the DC by at least 5, your progress doubles. If you exceed the DC by
at least 10, your progress triples, if you exceed it by at least 15, you quadruple your progress,
and so on. When your total progress equals the cost of the item, that item is completed. Any
remaining progress can be applied to a similar item; otherwise, all excess progress is lost.

If you fail the check, no progress is made that day. If you fail the check by 5 or more, you waste
an amount of your raw materials equal to the item's base progress per day, up to a maximum of the
initial cost of the raw materials. Such wasted material must be replenished before you can continue
crafting the item.

**Setting Aside Crafting Items:** As long as you can store an item in a secure and safe place, you
can set aside an item that you began crafting and return to it again later with little or no effect.
Your GM may rule that this is not possible, especially in the case of volatile alchemical items or
perishable goods.

**Crafting Masterwork and Special Material Items:** When you're crafting a masterwork item or an
item made of a special material, its crafting difficulty increases by one step. For example, a
longsword (which has a base difficulty of normal) is considered a complex item when crafted as a
masterwork item (DC 20; 4 gp base progress per day). In the case of items crafted from special
materials that also count as masterwork (such as adamantine armor and weapons), the complexity of
the item increases by two steps.

**Repairing Items:** You can use the appropriate Craft skill to repair items of that type. Repairing
an item with the broken condition or that has taken damage (or both) requires tools and a work area,
and you must pay 1/10 the item's cost in raw materials. Repairing an item has the same DC as
crafting the item, but takes an amount of time based on the item's complexity. Extremely simple
items take an hour to repair. Simple and normal items take 1d4 hours to repair. Complex and
intricate items take a day to repair, and all other items take 1d4 days to repair.

### Table 2-4: Crafting DCs and Progress Values

|Crafting Difficulty|Craft DC|Base Progress per Day|
| --- | --- | --- |
|Extremely simple|DC 5|5 sp|
|Simple|DC 10|1 gp|
|Normal|DC 15|2 gp|
|Complex|DC 20|4 gp|
|Intricate|DC 25|8 gp|
|Very intricate|DC 30|16 gp|
|Extremely intricate|DC 35|32 gp|
|Poisons|DC = the Fortitude DC of the poison|32 gp|
|Traps|Based on complexity, see text|32 gp|
