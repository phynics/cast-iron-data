+++
id = "ref/rule/events-dangerous-settlement"
kind = "rule"
title = "Dangerous Settlement Events"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "events_dangerous_settlement", path = "json/rules_campaign_types05.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 221

**Building Demand (Settlement, Continuous):** The citizens demand a particular building be built
(01-75) or demolished (76-100). Select the building type randomly from those available for the
settlement. If the demand is not met by the next Event phase, Unrest increases by 1. Alternatively,
you can suppress the citizens' demands and negate the event by succeeding at a Loyalty check, but
this reduces Loyalty by 2 and increases Unrest by 1.

**Crop Failure (Settlement):** Pests, blight, and weather ruin the harvest in the settlement's hex
and all adjacent hexes. Attempt two Stability checks. If both succeed, the problem is fixed before
your kingdom takes any penalties from the event. If only one succeeds, affected farms reduce
Consumption by 1 (instead of the normal reduction) in the next Upkeep phase. If neither succeeds,
affected farms do not reduce Consumption at all in the next Upkeep phase.

**Cult Activity (Settlement, Continuous):** A religious cult of an alignment opposed to the
kingdom's alignment begins kidnapping, converting, or even publicly sacrificing citizens. Attempt a
Loyalty check and a Stability check. If both succeed, the cult is disbanded before your kingdom
takes any penalties from the event. For each of these checks you fail, Unrest increases by 1 and
Productivity, Society, and Stability decrease by 1. If both checks fail, the event continues in the
next Event phase.

**Drug Den (Settlement, Continuous):** One of your Houses or Tenements becomes a hive of illicit
drug trade. Attempt a Loyalty check and a Stability check, with a penalty equal to the number of
Brothels, Tenements, Waterfronts, and lots with squatters in the settlement. If you succeed at both
checks, you eliminate the drug den before your kingdom takes any penalties from the event. If you
fail at one check, Crime and Unrest increase by 1. If you fail at both checks, Crime and Unrest
increase by 1; Economy, Loyalty, and Stability decrease by 1; and on the next Event phase, a second
drug den event occurs in the same settlement (01-50) or the nearest settlement (51-100).

**Feud (Settlement, Continuous):** Nobles (or other influential rival groups) are bickering. Attempt
a Loyalty check. If you succeed, you end the event but Unrest increases by 1. If you fail,
Corruption increases by 1, Unrest increases by 1d6, and the event is continuous.

**Inquisition (settlement, continuous):** Zealots mobilize public opinion against a particular race,
religion, kingdom, behavior, or kingdom leader. Attempt a Loyalty check. If you fail, the zealots
run rampant; Infamy and Law increase by 1 and Lore, Loyalty, Productivity, and Stability decrease
by 2. If you succeed, the zealots are somewhat suppressed; Lore, Loyalty, Productivity, and
Stability decrease by 1. Two successful checks in a row end the event (if a check ends the event, no
penalties from it occur that turn).

**Localized Disaster (Settlement):** A fire, a flood, a storm, an earthquake, massive sabotage, or
another disaster strikes the settlement! Roll 1d6 to determine how many lots are threatened by the
disaster. On a result of 6, the disaster is widespread and affects 1d6 additional adjacent lots.
Attempt a Stability check for each threatened lot; failure means the disaster destroys the building
in that lot and Unrest increases by 1. (This Stability check represents your kingdom's ability to
prepare for or react to the disaster as well as the structure's ability to withstand damage.)

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

**Sensational Crime (Settlement, Continuous):** A serial killer, arsonist, or daring bandit plagues
your kingdom. Attempt two Stability checks, adding the settlement's Law and subtracting its Crime.
If you succeed at both checks, the criminal is caught before your kingdom takes any penalties from
the event. If you fail at one, the criminal escapes, Unrest increases by 1, and the event is
continuous. If you fail at both, the criminal makes a fool of the authorities; Law and Loyalty
decrease by 1, Treasury decreases by 1d4 BP, Unrest increases by 2, and the event is continuous.

**Slavers (Settlement, Continuous):** Criminals begin kidnapping citizens and selling them into
slavery. Attempt a Loyalty check and a Stability check, each with a penalty equal to the number of
Brothels, Tenements, Waterfronts, and lots with squatters in the settlement. If you succeed at both
checks, the slavers are caught before your kingdom takes any penalties from the event. If you fail
at one of the checks, Loyalty, Stability, and Unrest decrease by 1, but the event is not continuous.
If you fail at both checks, Loyalty, Stability, and Unrest decrease by 2, and the event is
continuous.

**Squatters (Settlement, Continuous):** An empty settlement lot is taken over by beggars,
troublemakers, and people unable to find adequate work or housing; they camp there with tents,
wagons, and shanties. You cannot use the lot for anything until the squatters are dispersed. Fame
and Stability decrease by 1, and Unrest increases by 2. You may try to disperse the squatters with a
Stability check. Success means the squatters are dispersed and the event is not continuous, but if a
House or Tenement is not built in that lot on the next turn, Infamy increases by 1 and Unrest by 2.
Failing the Stability check means the event is continuous, and you may not build on that lot until
the event is resolved.

**Vandals (Settlement):** Thugs and dissidents riot and destroy property. Attempt a Loyalty check
and a Stability check. If you succeed at both, the vandals are stopped before your kingdom takes any
penalties. If you fail at one check, Society decreases by 1 and one random building in the
settlement is damaged. If you fail at both, one random building is destroyed (Unrest increases by 1
for each lot of the destroyed building), and 1d3 other random buildings are damaged. A damaged
building provides no benefits until half its cost is spent repairing it.
