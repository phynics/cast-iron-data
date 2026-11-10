+++
id = "ref/rule/kingdom-upkeep-phase"
kind = "rule"
title = "Kingdom Upkeep Phase"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kingdom_upkeep_phase", path = "json/rules_campaign_types04.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "206"

[fields]
kind = "none"
+++

During the Upkeep phase, you adjust your kingdom's scores based on what's happened in the past
month, how happy the people are, how much they've consumed and are taxed, and so on.

**Step 1-Determine Kingdom Stability:** Attempt a Stability check. If you succeed, Unrest decreases
by 1 (if this would reduce Unrest below 0, add 1 BP to your Treasury instead). If you fail by 4 or
less, Unrest increases by 1; if you fail by 5 or more, Unrest increases by 1d4.

**Step 2-Pay Consumption:** Subtract your kingdom's Consumption from the kingdom's Treasury. If your
Treasury is negative after paying Consumption, Unrest increases by 2.

**Step 3-Fill Vacant Magic Item Slots:** If any of your settlement districts have buildings that
produce magic items (such as a Caster's Tower or Herbalist) with vacant magic item slots, there is a
chance of those slots filling with new items (see the
[Magic Items in Settlements](ref/rule/magic-items-in-settlements) section).

**Step 4-Modify Unrest:** Unrest increases by 1 for each kingdom attribute (Economy, Loyalty, or
Stability) that is a negative number.

The Royal Enforcer may attempt to reduce Unrest during this step.

If the kingdom's Unrest is 11 or higher, it loses 1 hex (the leaders choose which hex). See
[Losing Hexes](ref/rule/losing-hexes) for more information.

If your kingdom's Unrest ever reaches 20, the kingdom falls into anarchy. While in anarchy, your
kingdom can take no action and treats all Economy, Loyalty, and Stability check results as 0.
Restoring order once a kingdom falls into anarchy typically requires a number of quests and lengthy
adventures by you and the other would-be leaders to restore the people's faith in you.

Example: Jessica is the Ruler of a kingdom with a Size of 30 and a Control DC of 60. Based on
leadership role bonuses, kingdom alignment bonuses, and buildings in her settlements, the kingdom's
Economy is 52, its Loyalty is 45, and its Stability is 56. Its Unrest is currently 5, its
Consumption is 5, and the Treasury has 12 BP. In Step 1 of the Upkeep phase, Adam, the Warden,
attempts a Stability check to determine the kingdom's stability. Adam rolls a 19, adds the kingdom's
Stability (56), and subtracts its Unrest (5), for a total of 70; that's a success, so Unrest
decreases by 1. In Step 2, the kingdom pays 5 BP for Consumption. None of the kingdom's magic item
slots are empty, so they skip Step 3. In Step 4, none of the attributes are negative, so Unrest
doesn't increase. Mark, the Royal Enforcer, doesn't want to risk reducing the kingdom's Loyalty, so
he doesn't use his leadership role to reduce Unrest. At the end of this phase, the kingdom has
Economy 52, Loyalty 45, Stability 56, Unrest 4, Consumption 5, and Treasury 7 BP.
