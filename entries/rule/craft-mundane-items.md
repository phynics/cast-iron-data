+++
id = "ref/rule/craft-mundane-items"
kind = "rule"
title = "Craft Mundane Items"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "craft_mundane_items", path = "json/rules_subsystems02.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "84"

[fields]
kind = "none"
+++

The Craft skill allows you to spend time creating mundane items such as armor, weapons, and
alchemist's fire. The standard rules presented in the Core Rulebook assume you spend a week on
crafting, but give you the option to make progress by the day. If you use the downtime system, make
your Craft checks by the day instead of by the week. The steps for crafting by day are as follows.

1. Find the item's price in silver pieces (1 gp = 10 sp).
1. Find the item's DC from [Table 4-4: Craft Skills](ref/skill/craft-any).
1. Pay 1/3 of the item's price in gp for the raw material cost. You may also spend Goods toward this
  cost.
1. Attempt an appropriate Craft check representing 1 day's worth of work. You may spend Labor to
  modify your check result, with 1 point of Labor adding 2 to your total.

If your check succeeds, multiply your check result by the DC and divide by 7. If this value equals
or exceeds the price of the item in sp, then you complete the item. If the result × the DC equals
double or triple the price of the item in silver pieces, then you've completed the task in 1/2 or
1/3 of the time. Other multiples of the DC reduce the time in the same manner.

If the value is less than the price, the check represents the progress you've made this day. Record
the result of your check. Each downtime day you spend crafting, you make more progress until your
total reaches the price of the item in silver pieces.

If you fail a check by 4 or less, you make no progress that day. If you fail by 5 or more, you ruin
some of the raw materials and have to pay 1/10 of the original raw material cost again.
