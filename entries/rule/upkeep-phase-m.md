+++
id = "ref/rule/upkeep-phase-m"
kind = "rule"
title = "Upkeep Phase"
source_ids = ["lands-of-conflict"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "upkeep_phase_m", path = "json/rules_campaign_types01.json" },
]
[[sources]]
publication = "lands-of-conflict"
page = "54"

[fields]
kind = "none"
+++

The key to the militia's growth is to constantly run drills and regimens to increase its training
score. To do this, the PCs must perform the [Drill Militia](ref/rule/drill-militia) action during
the Activity phase. Constantly sparring will take its toll on the militia's members, though, and
some will become injured or skip training to attend to other matters, reducing the amount of
training within the militia's camp. The amount of this attrition is determined during the Upkeep
Phase in three separate ways (see steps 1, 2, and 3 below). During the militia's first week, skip
the Upkeep phase.

The five steps of the Upkeep phase always play out in the following order.

**Step 1 - Training Attrition:** The PCs attempt a DC 10 Loyalty Check. If they're successful, the
militia's training score decreases by 1d6. If the roll is a natural 20, the militia instead adds 1d6
to its training score. On a failed check, the militia's training score decreases by an amount equal
to 2d4 + the militia's [rank](ref/rule/rank-mt).

**Step 2 - Maximum-Notoriety Penalties:** If the militia's [Notoriety](ref/rule/notoriety-mt) score
is 100, enemy organizations have an easier time tracking its people down. In this case, the
militia's training score is reduced by a number equal to 1d20 + the militia's rank. The militia must
also attempt a DC 15 Loyalty check or its [reputation](ref/rule/reputation-mt) in the nearest
settlement is reduced by one step (though it can never be made worse than unfriendly in this way).

**Step 3 - Treasury-Shortage Penalties:** If the militia's [treasury](ref/rule/treasury-mt) is below
its minimum during Upkeep, its training score decreases by an amount equal to 2d4 + the militia's
rank.

**Step 4 - Increase Rank:** Apply any increases to the militia's rank based on its current training
score. If its training score currently exceeds the minimum amount needed for the next rank, and that
rank would not exceed the most experienced PC's level, increase the militia's rank and award the
appropriate [boon](ref/rule/pc-boons). The militia can gain multiple ranks at once in this way.

**Step 5 - Deposits and Withdrawals:** Any officer can deposit gold to or withdraw gold from the
militia's treasury.
