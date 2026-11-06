+++
id = "ref/rule/kingdom-income-phase"
kind = "rule"
title = "Kingdom Income Phase"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "kingdom_income_phase", path = "json/rules_campaign_types04.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 207

During the Income phase, you may add to or withdraw from the Treasury as well as collect taxes.

**Step 1-Make Withdrawals from the Treasury:** The kingdom-building rules allow you to expend BP on
things related to running the kingdom. If you want to spend some of the kingdom's resources on
something for your own personal benefit (such as a new magic item), you may withdraw BP from the
Treasury and convert it into gp once per turn, but there is a penalty for doing so.

Each time you withdraw BP for your personal use, Unrest increases by the number of BP withdrawn.
Each BP you withdraw this way converts to 2,000 gp of personal funds.

**Step 2-Make Deposits to the Treasury:** You can add funds to a kingdom's Treasury by donating your
personal wealth to the kingdom - coins, gems, jewelry, weapons, armor, magic items, and other
valuables you find while adventuring, as long as they are individually worth 4,000 gp or less. For
every full 4,000 gp in value of the deposit, increase your kingdom's BP by 1.

If you want to donate an item that is worth more than 4,000 gp, refer to Step 3 instead.

**Step 3-Sell Expensive Items for BP:** You can attempt to sell expensive personal items (that is,
items worth more than 4,000 gp each) through your kingdom's markets to add to your Treasury. You may
sell one item per settlement district per turn. You must choose the settlement where you want to
sell the item, and the item cannot be worth more than the base value of that settlement (see
[Table 4-5](ref/rule/settlements-and-districts)). To sell an item, divide its price by half (as if
selling it to an NPC for gp), divide the result by 4,000 (rounded down), and add that many BP to
your Treasury.

You cannot use this step to sell magic items held or created by buildings in your settlements; those
items are the property of the owners of those businesses. (See
[Magic Items in Settlements](ref/rule/magic-items-in-settlements) for more information on this
topic.)

**Step 4-Collect Taxes:** Attempt an Economy check, divide the result by 3 (round down), and add a
number of BP to your Treasury equal to the result.

Example: Jessica and the other leaders need to keep BP in the kingdom for future plans, so they skip
Step 1 of the Income phase. They are worried that they won't collect enough taxes this turn, so just
in case, in Step 2 they deposit 8,000 gp worth of coins, gems, and small magic items (Treasury +2
BP). The leaders aren't selling any expensive items, so nothing happens in Step 3. In Step 4, Rob,
the Treasurer, rolls the Economy check to collect taxes. Rob rolls a 9 on the 1d20, adds the
kingdom's Economy score (55), and subtracts Unrest (4) for a total of 60, which means the kingdom
adds 20 BP (the Economy check result of 60, divided by 3) to the Treasury. At the end of this phase,
the kingdom has Economy 55, Loyalty 42, Stability 55, Unrest 4, Consumption 4, and Treasury 27 BP.
