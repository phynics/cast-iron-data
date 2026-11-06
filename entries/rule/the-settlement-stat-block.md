+++
id = "ref/rule/the-settlement-stat-block"
kind = "rule"
title = "The Settlement Stat Block"
source_ids = ["game-mastery-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "the_settlement_stat_block", path = "json/rules_gm05.json" },
]

[fields]
kind = "none"
+++

**Sources:** GameMastery Guide pg. 203-205, 207

A settlement stat block is organized as follows.

**Name:** The settlement's name is presented first.

**Alignment and Type:** A settlement's alignment is the general alignment of its citizens and
government; individuals who dwell therein can still be of any alignment, but the majority of its
citizens should be within one step of the settlement's overall alignment.
[Alignment](ref/rule/alignment) influences a city's modifiers. The type is the size category the
settlement falls into, be it thorp, hamlet, village, town (small or large), city (small or large),
or metropolis. In most cases, rules play off of a settlement's type rather than its exact population
total. A settlement's type determines many of its statistics (see Table 7-36: Settlement
Statistics).

**Modifiers:** Settlements possess six modifiers that apply to specific skill checks made in the
settlement. A settlement's starting modifier values are determined by its type. This value is
further adjusted by the settlement's alignment, government, qualities, and disadvantages. Note that
introducing settlement modifiers to your game will somewhat increase the complexity of skill checks
by adding a variable modifier each time the PCs visit a new town or city-consider the use of these
modifiers an optional rule.

**Qualities:** All settlements have a certain number of qualities that further adjust their
statistics - think of qualities as feats for settlements. A settlement's type determines how many
qualities it can have.

**Danger:** A settlement's danger value is a number that gives a general idea of how dangerous it is
to live in the settlement. If you use the urban [encounters charts](ref/rule/urban-toolbox) for
random encounters in your city (or any similar wandering monster chart that uses percentile dice and
ranks its encounters from lowest CR to highest CR), use the modifier associated with the
settlement's danger value to adjust rolls on the encounter chart. A settlement's base danger value
depends on its type.

**Disadvantages:** Any disadvantages a settlement might be suffering from are listed on this line. A
settlement can have any number of disadvantages you wish to inflict on it, although most settlements
have no disadvantages.

**Government:** This entry lists how the settlement is governed and ruled. The type of government a
settlement follows affects its statistics.

**Population:** This number represents the settlement's population. Note that the exact number is
flexible; a settlement's actual population can swell on market days or dwindle during winter; this
number lists the average population of the settlement. Note that this number is generally used for
little more than flavor; since actual population totals fluctuate, it's pointless to tether rules to
this number. After the settlement's total population, a breakdown of its racial mix is listed in
parentheses.

**Notable NPCs:** This section lists any notable NPCs who live in the city, sorted by their role in
the community, followed by their name and then their alignment, gender, race, class, and level in
parentheses.

**Base Value and Purchase Limit:** This section lists the community's base value for available magic
items in gp. There is a 75% chance that any item of this value or lower can be found for sale in the
community with little effort. If an item is not available, a new check to determine if the item has
become available can be made in 1 week. A settlement's purchase limit is the most money a shop in
the settlement can spend to purchase any single item from the PCs. If the PCs wish to sell an item
worth more than a settlement's purchase limit, they'll either need to settle for a lower price,
travel to a larger city, or (with the GM's permission) search for a specific buyer in the city with
deeper pockets. A settlement's type sets its purchase limit.

**Spellcasting:** Unlike magic items, spellcasting for hire is listed separately from the town's
base value, since spellcasting is limited by the level of the available spellcasters in town. This
line lists the highest-level spell available for purchase from spellcasters in town. Prices for
spellcasting [can be found here](ref/eq-misc/spellcasting). A town's base spellcasting level depends
on its type.

**Minor Items/Medium Items/Major Items:** This line lists the number of magic items above a
settlement's base value that are available for purchase. In some city stat blocks, the actual items
are listed in parentheses after the die range of items available - in this case, you can use these
pre-rolled resources when the PCs first visit the city as the magic items available for sale on that
visit. If the PCs return to that city at a later date, you can roll up new items as you see fit. See
below for the number ranges determining how many items can be found in a community.

### Table 7-36: Settlement Statistics

|Type|Population|Modifiers|Qualities|Danger|Base Value|Purchase Limit|Spellcasting|
| --- | --- | --- | --- | --- | --- | --- | --- |
|Thorp|Fewer than 20|-4|1|-10|50 gp|500 gp|1st|
|Hamlet|21-60|-2|1|-5|200 gp|1,000 gp|2nd|
|Village|61-200|-1|2|0|500 gp|2,500 gp|3rd|
|Small town|201-2,000|0|2|0|1,000 gp|5,000 gp|4th|
|Large town|2,001-5,000|0|3|5|2,000 gp|10,000 gp|5th|
|Small city|5,001-10,000|+1|4|5|4,000 gp|25,000 gp|6th|
|Large city|10,001-25,000|+2|5|10|8,000 gp|50,000 gp|7th|
|Metropolis|More than 25,000|+4|6|10|16,000 gp|100,000 gp|8th|

### Table 7-37: Available Magic Items

|Community Size|Base Value|Minor|Medium|Major|
| --- | --- | --- | --- | --- |
|Thorp|50 gp|1d4 items|-|-|
|Hamlet|200 gp|1d6 items|-|-|
|Village|500 gp|2d4 items|1d4 items|-|
|Small town|1,000 gp|3d4 items|1d6 items|-|
|Large town|2,000 gp|3d4 items|2d4 items|1d4 items|
|Small city|4,000 gp|4d4 items|3d4 items|1d6 items|
|Large city|8,000 gp|4d4 items|3d4 items|2d4 items|
|Metropolis|16,000 gp|\*|4d4 items|3d4 items|

\* In a metropolis, nearly all minor magic items are available.
