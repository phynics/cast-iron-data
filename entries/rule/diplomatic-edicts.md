+++
id = "ref/rule/diplomatic-edicts"
kind = "rule"
title = "Diplomatic Edicts"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "diplomatic_edicts", path = "json/rules_campaign_types05.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "228"

[fields]
kind = "none"
+++

Diplomatic edicts are special edicts that allow you to establish an embassy, treaty, or alliance
with another kingdom. You must have an official representative of your kingdom, such as an
ambassador or leader, present in the other kingdom to make this edict (though the GM may allow
magical communication to handle most of the edict's details and bypass this requirement). Using this
edict costs 1d4 BP in travel and other expenses.

Your representative must attempt a Diplomacy check. The DC is determined using the following
formula:

DC = 10 + your kingdom's Infamy + the target kingdom's special Size modifier + your kingdom's
special Size modifier + alignment difference modifier + relationship modifier + the target kingdom's
attitude - your kingdom's Fame - BP you spend on bribes or gifts

**Special Size Modifier:** This is equal to the kingdom's Size divided by 5.

**Alignment Difference Modifier:** This is based on how close your kingdom's alignment is to the
target kingdom's alignment, according to the following table.

### Table 4-12: Diplomatic Alignment Difference Modifier

|Alignment Difference\*|DC Modifier|
| --- | --- |
|Same|+0|
|1 step|+5|
|2 steps|+15|

\*Per alignment axis.

**Relationship Modifier:** This takes into account your treaties, alliances, and conflicts with the
target kingdom's allies and enemies. If you are friendly with the same kingdoms, the target is more
interested in diplomacy with you. If you are friendly with the target kingdom's enemies, the target
is less interested in negotiating with you. Modify the DC as follows for each third party you have
in common.

### Table 4-13: Diplomatic Relationship Modifier

|Relationship|DC Modifier|
| --- | --- |
|You and the target kingdom both have an alliance with a third party|-8|
|You have a treaty with the target kingdom's ally|-4|
|You and the target kingdom both have a treaty with a third party|-2|
|You have an embassy with the target kingdom's enemy|+2|
|You have a treaty with the target kingdom's enemy|+5|
|You have an alliance with the target kingdom's enemy|+10|

**Attitude:** Much like the starting attitude of an NPC, the target kingdom's initial attitude
toward you is indifferent, though the GM may modify this based on alignment differences, your shared
history, culture, warfare, espionage, racial tensions, and other factors in the campaign world.
These factors may also influence the Diplomacy DC for using this edict (generally increasing the DC
by 5 for every attitude step worse than helpful).

The act of making this Diplomacy check takes place over several days, with the emissary socializing
with representatives of the target kingdom, discussing common interests and the benefits and goals
of entering a diplomatic agreement with your kingdom. Because this check is not a singular event,
abilities and spells that modify a single roll have no effect on this check unless they last at
least 24 hours (for example, glibness does not affect this check).
