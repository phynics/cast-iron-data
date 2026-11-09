+++
id = "ref/rule/multiclassing-pu"
kind = "rule"
title = "Multiclassing"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "multiclassing_pu", path = "json/rules_opt_skills01.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "71"

[fields]
kind = "none"
+++

A multiclassed character uses the class with the lowest number of skill ranks per level to determine
her number of skill groups. This doesn't cause her to lose skill groups she's already selected if
she gains a level in a new class that would have fewer skill groups at her character level - once a
skill group has been selected, it can't be unselected. For instance, a character with 6 levels in
rogue would have training in three skill groups. If she then took a level in druid, she would still
have three groups, but the number of skill groups she knows would now increase to four at character
level 18th instead of at character level 8th.
