+++
id = "ref/rule/sample-armies"
kind = "rule"
title = "Sample Armies"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sample_armies", path = "json/rules_campaign_types05.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "247"

[fields]
kind = "none"
+++

This section details sample armies of various humanoid and monster types. The GM can allow players
to recruit some of these armies, or might reserve most of them as unusual foes for mass battles.
None of these armies has a starting Morale listed, because starting Morale starts at 0, modified by
the commander.

Most of these armies are Medium, showing a player or GM what tactics, resources, and special
abilities a typical army of that type has, yet still keeping it easy to scale the army to a larger
or smaller size. If an army has a resource, the listed Consumption is for an army of the listed
size; if you change the size of the army, remember to subtract the Consumption cost for its original
size, scale that cost to the new size (see [Table 4-16: Resource Scaling](ref/rule/army-resources)),
then add the scaled cost to the army's base Consumption cost. If the army lists an additional cost
for recruiting the army, this recruitment cost scales in the same way.

The special abilities listed for monster armies are approximations to model the unit monster's
special abilities. For example, an individual troglodyte's stench nauseates opponents, but there is
no army special ability that does that, so the troglodyte army has paralysis instead, which has a
comparable effect. Likewise, the astral deva army has the alchemy ability, which is a reasonable
approximation of an individual astral deva's ability to use [heal](ref/spell/heal) once per day; the
one-unit army doesn't actually carry alchemist extracts.

If a special ability provides a constant bonus (such as the bonus from charge or pounce), that bonus
is automatically included in the army's stat block. If the bonus is conditional (like the DV bonus
from rock catching or the ranged damage bonus from rock throwing), you need to account for that
bonus when the conditions are right.

Some armies have custom bonuses built into their DV or OM. This represents the unit's special
defenses (such as [damage reduction](ref/rule/damage-reduction)) and high damage output against
single targets, which should affect an opposing army in a greater way than the standard
monster-to-army conversion rules would indicate. Determining army stat block values for small
numbers of powerful monsters is more of an art than a science.
