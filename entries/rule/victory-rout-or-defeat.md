+++
id = "ref/rule/victory-rout-or-defeat"
kind = "rule"
title = "Victory, Rout, or Defeat"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "victory_rout_or_defeat", path = "json/rules_campaign_types05.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 239

An army is victorious if all of its enemy armies flee the battlefield or are defeated. The aftermath
of the battle can be different for each army, and depends on whether it was defeated, routed, or
victorious.

**Defeated:** If an army's hit points are reduced to 0, it is defeated. A defeated army may have a
few survivors, but they are so demoralized and wounded (and probably captured by the enemy) that the
army no longer exists as a cohesive unit and can't be used again in mass combat. If your army is
defeated, reduce your kingdom's Economy, Loyalty, and Stability according to the size of the army.

|Army Size|Economy|Loyalty|Stability|
| --- | --- | --- | --- |
|Fine|0|0|0|
|Diminutive|0|-1|0|
|Tiny|-1|-1|0|
|Small|-1|-1|-1|
|Medium|-2|-2|-2|
|Large|-3|-2|-2|
|Huge|-4|-2|-2|
|Gargantuan|-4|-2|-3|
|Colossal|-4|-3|-3|

**Routed:** If the army routs, reduce its Morale by 1. If the army's current hp are lower than the
army's ACR, increase its hit points to its ACR. A routed army refuses to fight until you succeed at
a Loyalty check during your kingdom's Upkeep phase (you may attempt this check once per turn). Note
that a routed army can still be attacked by enemy armies, and can attempt Offense checks in
battles - it just can't initiate a battle.

**Victorious:** If your army is the last one left on the battlefield (not counting other friendly
armies), it is victorious. Each time an army wins a battle, you can attempt a Loyalty check against
your kingdom's Control DC. If you succeed at this check, your army learns a new tactic and its
Morale increases by 1 (maximum of Morale +4). If the army's current hit points are lower than the
army's ACR, increase its hit points to its ACR. You may attempt a second Loyalty check; if you
succeed, the army's commander learns a new boon.
