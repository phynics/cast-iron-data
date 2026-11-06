+++
id = "ref/rule/modify-an-existing-monster"
kind = "rule"
title = "Modify an Existing Monster"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "modify_an_existing_monster", path = "json/rules_campaign_types06.json" },
]

[fields]
kind = "none"
+++

**Sources:** Mythic Adventures pg 225

Making a mythic monster out of an ordinary monster is fairly straightforward - just follow these
steps.

Step 1-Determine its mythic rank (MR). Divide your monster's CR by 2 to get its approximate mythic
rank. If the result is not a whole number, it just means you have some flexibility in choosing the
MR. For example, if your monster is a CR 7 chimera, half of 7 is 3.5, which means you can try it at
MR 3 or MR 4. It's easier to start with a lower MR - you can always increase the MR later if you
need the monster to be a little more powerful.

Step 2-Add the [mythic subtype](ref/rule/mythic-subtype). The modifications to the creature's
ability scores, hit points, and other game statistics depend on your monster's MR.

Step 3-Add additional mythic abilities. As described in the mythic subtype, the monster gains a
number of mythic abilities equal to its MR + 1.

Step 4-Evaluate the monster at its final CR. Your monster's final CR is its initial CR + 1/2 its MR
(round down; minimum 1). Use
[Table 6-8: Monster Statistics by CR](ref/rule/evaluating-monster-statistics) to evaluate whether
the monster's abilities are appropriately challenging for its final CR. If a creature's mythic
abilities complement its non-mythic abilities particularly well, that mythic creature may be too
powerful for its final CR. If a creature's mythic abilities don't interact with its non-mythic
abilities, that creature may be too weak for its final CR. If either of these situations occur, make
adjustments to the creature so it better fits the intended CR.

If the creature is too weak and you rounded the creature's MR down in Step 1, you can round up
instead (adjusting the modifiers from the mythic subtype). If the creature is too strong and you
rounded the creature's MR up in Step 1, you can round down instead (adjusting the modifiers from the
mythic subtype).

Once the creature's abilities and statistics fit its CR, you're done.
