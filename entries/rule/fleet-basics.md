+++
id = "ref/rule/fleet-basics"
kind = "rule"
title = "Fleet Basics"
source_ids = ["pathfinder-59-the-price-of-infamy"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fleet_basics", path = "json/rules_campaign_types10.json" },
]
[[sources]]
publication = "pathfinder-59-the-price-of-infamy"
page = "63"

[fields]
kind = "none"
+++

A fleet consists of multiple ships organized under a single admiral. Each individual ship in a fleet
is crewed by a captain and her crew. Technically, it only takes two ships to constitute a fleet for
the purposes of these rules (if you're just doing a battle between a couple of ships, it's generally
better to simply use the [ship-to-ship combat](ref/rule/ship-to-ship-combat) rules).

Fleets consist of a number of squadrons of ships. All of the ships in a squadron must be of the same
type of ship (longship, junk, sailing ship, warship, etc.). Each squadron involved in a fleet battle
is commanded by a single commodore. A squadron consists of at least one ship, and can consist of a
maximum number of ships equal to 3 + the commodore's Charisma modifier. A character whose Charisma
modifier is -3 or worse cannot serve as a commodore.

The fleet as a whole is commanded by a single admiral. An NPC fleet consists of a number of
squadrons equal to 3 + the admiral's Charisma modifier. A PC fleet can have a number of squadrons
equal to the party's [Infamy score](ref/rule/infamy-and-disrepute-scores) divided by 10 (round
down) - this base number is then increased by the admiral's Charisma modifier. A character whose
Charisma modifier is -3 or worse cannot serve as an admiral.
