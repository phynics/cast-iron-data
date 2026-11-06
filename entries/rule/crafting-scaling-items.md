+++
id = "ref/rule/crafting-scaling-items"
kind = "rule"
title = "Crafting Scaling Items"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crafting_scaling_items", path = "json/rules_opt_magic02.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 161

Scaling items must be crafted at their highest level of power, with a cost determined by referencing
[Table 4-13](ref/rule/adjusting-treasure). Start with the value listed on the table for the item's
category and its highest-level ability. Divide this by 2 to get the crafting cost, and add the value
of any nonmagical armor or weapon component. The crafting cost is always much higher than the market
price of a scaling item, since the crafting cost is based on the full set of abilities but the
market price is based on the minimum caster level. When a PC crafts a scaling item, he doesn't need
to pay any further cost in reduced treasure for keeping the item, because the full value of the item
has already been accounted for. When setting the DC for crafting a scaling item, use the item's
highest-level ability instead of its base caster level.
