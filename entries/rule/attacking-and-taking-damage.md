+++
id = "ref/rule/attacking-and-taking-damage"
kind = "rule"
title = "Attacking and Taking Damage"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "attacking_and_taking_damage", path = "json/rules_campaign_types05.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "236"

[fields]
kind = "none"
+++

In mass combat, the hundreds of individual attacks that take place in one battle phase overlap each
other enough that who actually attacks first is irrelevant.

When armies attack, each army attempts an Offense check (1d20 + the attacking army's OM) and
compares the result to the target army's DV.

If the Offense check is equal to or less than the target army's DV, the army deals no damage that
phase. If the Offense check is greater than defender's DV, the defending army takes damage equal to
the result of the attacker's Offense check minus the defender's DV. For example, if the attacker's
Offense check is 11 and the defender's DV is 7, the defending army takes 4 points of damage. Because
these attacks are resolved simultaneously, it is possible that both armies may damage or even
destroy each other in the same phase.

If the Offense check is a natural 20, but that check is lower than the enemy army's DV, the
attacking army still deals 1 point of damage. If the Offense check is a natural 1, that army can't
attempt an Offense Check in the next phase, due to some setback: a misheard order, getting stuck in
mud, and so on.
