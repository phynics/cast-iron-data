+++
id = "ref/rule/events-dangerous-kingdom"
kind = "rule"
title = "Dangerous Events"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "events_dangerous_kingdom", path = "json/rules_campaign_types05.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 221

**Assassination Attempt:** One of your leaders (determined randomly) is the target of an
assassination attempt. If the target is a PC, the GM should run the attempt as an encounter, using
an assassin of a CR equal to the targeted PC's level. If the target is an NPC, you must succeed at a
Stability check to prevent the assassination. If the assassination occurs, Unrest increases by 1d6
and the kingdom immediately incurs the penalties for not having a leader in that role.

**Bandit Activity:** Bandits are preying upon those who travel through your kingdom. Attempt a
Stability check. If you succeed, your kingdom's defenses stop the bandits before they cause any
harm. If you fail, the bandits reduce your kingdom's Treasury by 1d6 BP (each time you roll a 6, add
the result to the total and roll again).

**Feud (Settlement, Continuous):** Nobles (or other influential rival groups) are bickering. Attempt
a Loyalty check. If you succeed, you end the event but Unrest increases by 1. If you fail,
Corruption increases by 1, Unrest increases by 1d6, and the event is continuous.

**Food Shortage:** Spoilage, treachery, or bad luck has caused a food shortage this turn. Attempt a
Stability check. If you succeed, Consumption in the next Upkeep phase increases by 50%. If you fail,
Consumption in the next Upkeep phase increases by 100%.

**Food Surplus:** Farmers produce an unexpected windfall! In the next Upkeep phase, the kingdom's
Consumption is halved (but returns to normal on the next turn).

**Good Weather:** Good weather raises spirits and productivity. Economy, Loyalty, and Productivity
increase by 2 until the next Event phase.

**Improvement Demand (hex):** This event is identical to the building demand event, but the citizens
want the construction or destruction of a terrain improvement in the hex.

**Inquisition (settlement, continuous):** Zealots mobilize public opinion against a particular race,
religion, kingdom, behavior, or kingdom leader. Attempt a Loyalty check. If you fail, the zealots
run rampant; Infamy and Law increase by 1 and Lore, Loyalty, Productivity, and Stability decrease
by 2. If you succeed, the zealots are somewhat suppressed; Lore, Loyalty, Productivity, and
Stability decrease by 1. Two successful checks in a row end the event (if a check ends the event, no
penalties from it occur that turn).

**Large Disaster (Hex):** A fire, storm, earthquake, flood, massive sabotage, or other disaster
strikes! Roll 1d6; on a result of 1-5, the disaster threatens only 1 improved hex. On a result of 6,
the disaster is widespread and threatens 1d6 additional improved hexes adjacent to the target hex.
Attempt a Stability check for each threatened hex; failure means the disaster destroys one terrain
improvement in the hex and Unrest increases by 1. (This Stability check represents your kingdom's
ability to prepare for or react to the disaster as well as the structure's ability to withstand
damage.)

**Monster Attack (Settlement, Continuous):** A monster (or group of monsters) attacks the kingdom.
The GM picks a claimed hex in the kingdom in which the monster is active. The CR of the monster
encounter is equal to the party's APL + 1d4 - 1. You can personally deal with the monster (earning
XP and treasure normally for your efforts) or succeed at a Stability check to eliminate it (which
doesn't affect you or the kingdom's statistics). If the monster is not defeated this turn, Unrest
increases by 4. If the kingdom's Unrest is 5 or higher, the monster's hex becomes unclaimed - this
is in addition to losing control of hexes in the Upkeep phase because of the kingdom's high Unrest
score.

**Plague (Hex or Settlement, Continuous):** A deadly sickness strikes the target hex or settlement.
You cannot construct terrain improvements or buildings there while plague persists. Attempt two
Stability checks, each with a penalty equal to the number of Brothels, Foreign Quarters, Highways,
Inns, Piers, Roads, Stables, Stockyards, Tenements, and Waterfronts in the hex, and a bonus equal to
the number of Alchemists, Cathedrals, Herbalists, Hospitals, and Temples in the hex. If you succeed
at both checks, the event ends, but Stability decreases by 2 and Treasury by 1d3 BP. If you fail at
one check, Stability decreases by 4, Treasury decreases by 1d6 BP, and Unrest increases by 1d3. If
you fail at both, Stability decreases by 4, Treasury decreases by 1d6 BP, Unrest increases by 1d6,
and in the next Event phase the plague spreads to an adjacent hex.

**Public Scandal:** One of your leaders is implicated in a crime or an embarrassing situation, such
as an affair with another leader's spouse. Infamy increases by 1. Attempt a Loyalty check. If you
fail, Unrest increases by 2 and you take a -4 penalty on all Loyalty checks until the next Event
phase.

**Smugglers (Continuous):** Unscrupulous merchants are subverting legitimate businesses. Attempt a
Loyalty check and a Stability check, each with a penalty equal to the number of Piers, Waterfronts,
and trade routes in the kingdom. If you succeed at both checks, the smugglers are stopped before
your kingdom takes any penalties from the event. If you fail at one of the checks, Corruption
increases by 1d2 in each settlement, [Crime](ref/rule/settlement-modifiers) increases by 1 for the
kingdom, Productivity for the kingdom decreases by 1d3, Treasury decreases by 1d3 BP, and the event
is not continuous. If you fail at both of the checks, Corruption increases by 1d4, Crime for the
kingdom increases by 1, Productivity for the kingdom decreases by 1d6, Treasury decreases by 1d6 BP,
and the event is continuous.
