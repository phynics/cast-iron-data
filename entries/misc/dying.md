+++
id = "ref/misc/dying"
kind = "rule"
title = "Dying"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dying", path = "json/misc.json" },
]
[[sources]]
publication = "core-rulebook"
page = "566"

[fields]
kind = "none"
+++

A dying creature is [unconscious](ref/misc/unconscious) and near death. Creatures that have negative
hit points and have not [stabilized](ref/misc/stable) are dying. A dying creature can take no
actions. On the character's next turn, after being reduced to negative hit points (but not dead),
and on all subsequent turns, the character must make a DC 10 Constitution check to become
[stable](ref/misc/stable). The character takes a penalty on this roll equal to his negative hit
point total. A character that is stable does not need to make this check. A natural 20 on this check
is an automatic success. If the character fails this check, he loses 1 hit point. If a dying
creature has an amount of negative hit points equal to its Constitution score, it dies.
