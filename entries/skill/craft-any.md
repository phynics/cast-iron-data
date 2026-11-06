+++
id = "ref/skill/craft-any"
kind = "rule"
title = "Craft (any)"
source_ids = ["core-rulebook", "technology-guide", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "craft_any", path = "json/skills.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 91

**Associated Skill**

**Details:** Intelligence

**Trained Only**

**Details:** No

**Armor Check Penalty**

**Details:** No

**Optional Unchained Skill**

**Details:** No

**Optional Background Skill**

**Details:** Yes

You are skilled in the creation of a specific group of items, such as armor or weapons. Like
[Knowledge](ref/skill/knowledge-all), [Perform](ref/skill/perform-any), and
[Profession](ref/skill/profession-any), Craft is actually a number of separate skills. You could
have several Craft skills, each with its own ranks. The most common Craft skills are alchemy, armor,
baskets, books, bows, calligraphy, carpentry, cloth, clothing, firearms, glass, jewelry, leather,
locks, paintings, pottery, sculptures, ships, shoes, siege engines, stonemasonry, traps, and
weapons.

A Craft skill is specifically focused on creating something. If nothing is created by the endeavor,
it probably falls under the heading of a Profession skill.

### Check

You can practice your trade and make a decent living, earning half your check result in gold pieces
per week of dedicated work. You know how to use the tools of your trade, how to perform the craft's
daily tasks, how to supervise untrained helpers, and how to handle common problems. (Untrained
laborers and assistants earn an average of 1 silver piece per day.)

The basic function of the Craft skill, however, is to allow you to make an item of the appropriate
type. The DC depends on the complexity of the item to be created. The DC, your check result, and the
price of the item determine how long it takes to make a particular item. The item's finished price
also determines the cost of raw materials.

In some cases, the [fabricate](ref/spell/fabricate) spell can be used to achieve the results of a
Craft check with no actual check involved. You must still make an appropriate Craft check when using
the spell to make articles requiring a high degree of craftsmanship.

A successful Craft check related to woodworking in conjunction with the casting of the
[ironwood](ref/spell/ironwood) spell enables you to make wooden items that have the strength of
steel.

When casting the spell [minor creation](ref/spell/minor-creation), you must succeed on an
appropriate Craft check to make a complex item.

All crafts require [artisan's tools](ref/eq-misc/artisans-tools-common) to give the best chance of
success. If improvised tools are used, the check is made with a -2 penalty. On the other hand,
[masterwork artisan's tools](ref/eq-misc/artisans-tools-masterwork) provide a +2 circumstance bonus
on the check.

To determine how much time and money it takes to make an item, follow these steps.

1. Find the item's price in silver pieces (1 gp = 10 sp).
1. Find the item's DC from the table below.
1. Pay 1/3 of the item's price for the raw material cost.
1. Make an appropriate Craft check representing one week's worth of work. If the check succeeds,
  multiply your check result by the DC. If the result × the DC equals the price of the item in sp,
  then you have completed the item. (If the result × the DC equals double or triple the price of the
  item in silver pieces, then you've completed the task in one-half or one-third of the time. Other
  multiples of the DC reduce the time in the same manner.) If the result × the DC doesn't equal the
  price, then it represents the progress you've made this week. Record the result and make a new
  Craft check for the next week. Each week, you make more progress until your total reaches the
  price of the item in silver pieces.

If you fail a check by 4 or less, you make no progress this week. If you fail by 5 or more, you ruin
half the raw materials and have to pay half the original raw material cost again.

#### Progress by the Day

You can make checks by the day instead of by the week. In this case your progress (check result ×
DC) should be divided by the number of days in a week.

#### Create Masterwork Items

You can make a masterwork item: a [weapon](ref/rule/masterwork-weapons), suit of
[armor](ref/rule/masterwork-armor), shield, or [tool](ref/eq-misc/masterwork-tool) that conveys a
bonus on its use through its exceptional craftsmanship. To create a masterwork item, you create the
masterwork component as if it were a separate item in addition to the standard item. The masterwork
component has its own price (300 gp for a weapon or 150 gp for a suit of armor or a shield, see
Equipment for the price of other masterwork tools) and a Craft DC of 20. Once both the standard
component and the masterwork component are completed, the masterwork item is finished. The cost you
pay for the masterwork component is one-third of the given amount, just as it is for the cost in raw
materials.

#### Repair Items

You can repair an item by making checks against the same DC that it took to make the item in the
first place. The cost of repairing an item is one-fifth of the item's price.

### Table 4-4: Craft Skills

|Item Craft|Skill|Craft DC|
| --- | --- | --- |
|Acid|Alchemy|15|
|Alchemist's fire, smokestick, or tindertwig|Alchemy|20|
|Antitoxin, sunrod, tanglefoot bag, or thunderstone|Alchemy|25|
|[Spontaneous alchemy](ref/rule/spontaneous-alchemy) use|Alchemy|Varies|
|Armor or shield|Armor|10 + AC bonus|
|Longbow, shortbow, or arrows|Bows|12|
|Composite longbow or composite shortbow|Bows|15|
|Composite longbow or composite shortbow with high strength rating|Bows|15 + (2 × rating)|
|Mechanical trap|Traps|Varies|
|Crossbow, or bolts|Weapons|15|
|Simple melee or thrown weapon|Weapons|12|
|Martial melee or thrown weapon|Weapons|15|
|Exotic melee or thrown weapon|Weapons|18|
|Very simple item (wooden spoon)|Varies|5|
|Typical item (iron pot)|Varies|10|
|High-quality item (bell)|Varies|15|
|Complex or superior item (lock)|Varies|20|
|A weapon with the fragile special quality|Weapon or Bow|Normal DC -5|
|One-handed firearm|Firearm|20|
|Two-handed firearm|Firearm|20|
|Siege firearm, heavy|Firearm|25|
|Siege firearm, medium|Firearm|30|
|Siege firearm, light|Firearm|35|
|Ranged siege engine, heavy|Siege Engine|20|
|Ranged siege engine, medium|Siege Engine|25|

[Traps](ref/rule/traps) have their own rules for construction.

### Action

Does not apply. Craft checks are made by the day or week.

### Try Again

Yes, but each time you fail by 5 or more, you ruin half the raw materials and have to pay half the
original raw material cost again.

### Special

You may voluntarily add +10 to the indicated DC to craft an item. This allows you to create the item
more quickly (since you'll be multiplying this higher DC by your Craft check result to determine
progress). You must decide whether to increase the DC before you make each weekly or daily check.

To make an item using Craft (alchemy), you must have alchemical equipment. If you are working in a
city, you can buy what you need as part of the raw materials cost to make the item, but alchemical
equipment is difficult or impossible to come by in some places. Purchasing and maintaining an
alchemist's lab grants a +2 circumstance bonus on Craft (alchemy) checks because you have the
perfect tools for the job, but it does not affect the cost of any items made using the skill.

A gnome receives a +2 bonus on a Craft or Profession skill of her choice.

Craft is also used in the [harvesting poison](ref/rule/harvesting-poisons) rules (to preserve
harvested poison and create antivenoms) and the [salvaging](ref/rule/salvaging) rules.

### Technology

**Sources:** Technology Guide pg 5\
Craft (mechanical) can be used with the [technological equipment](ref/rule/technological-equipment)
rules.

Those who wish to construct or repair [technological equipment](ref/rule/technological-equipment)
use the Craft (mechanical) skill in conjunction with the technological item crafting feats. Without
the [Technologist](ref/feat/technologist) feat, Craft (mechanical) can still be used to craft less
advanced forms of technology such as gears, hinges, and pulleys. Note that in the campaign setting,
NPCs with the means of crafting technological items are extremely rare, and it is not assumed that
PCs have access to such resources. GMs are encouraged to discuss such considerations with their
players before allowing technological crafting into the game.

### Unchained Rogue Skill Unlocks

**Sources:** Pathfinder Unchained pg 83\
If using [skill unlocks](ref/rule/skill-unlocks), with sufficient ranks in Craft, you earn the
following.

**5 Ranks**

**Details:** When determining your weekly progress, double the result of your Craft check before
multiplying the result by the item's DC.

**10 Ranks**

**Details:** You do not ruin any of your raw materials unless you fail a check by 10 or more.

**15 Ranks**

**Details:** When you determine your progress, the result of your check is how much work you
complete each day in silver pieces.

**20 Ranks**

**Details:** You can craft magic armor, magic weapons, magic rings, and wondrous items that fall
under your category of Craft using the normal Craft rules.
