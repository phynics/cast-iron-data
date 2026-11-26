+++
id = "ref/arc-ranger/sable-company-marine"
kind = "archetype"
title = "Sable Company Marine"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Sable%20Company%20Marine"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sable_company_marine", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "inner-sea-combat"
page = "43"

[fields]
kind = "archetype"
features = [
  { anchor = "hippogriff-companion", level = 2 },
]
trades = [
  { replaces = "Hunter's bond (but see text)", by = ["hippogriff-companion"] },
]
+++

Sable Company marines receive their training at the elite Endrin Military Academy in Korvosa. A
large portion of their education is the handling and riding of hippogriffs, the iconic mounts of
members of the company.

## Hippogriff Companion {#hippogriff-companion}

At 2nd level, a Sable Company marine adds [Monstrous Mount](ref/feat/monstrous-mount) (see page 14)
to the list of bonus feats made available to him by his chosen
[combat style](ref/ability/combat-styles), regardless of the style chosen. He can only use this feat
to select a [hippogriff](ref/companion/hippogriff) mount (see page 14). If he does so, he treats his
ranger level - 1 as his effective druid level. A marine who takes this option does not gain the
hunter's bond class feature at 4th level.

At 6th level, a Sable Company marine adds
[Monstrous Mount Mastery](ref/feat/monstrous-mount-mastery) (see page 14) to the list of available
bonus feats granted by his chosen combat style. If he takes this feat as his 6th-level combat style
bonus feat, note that he must wait until 8th level before he meets the effective druid level
prerequisite to utilize his mount's mastery abilities.
