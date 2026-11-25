+++
id = "ref/arc-paladin/holy-guide"
kind = "archetype"
title = "Holy Guide"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Holy%20Guide"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_guide", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-class-guide"
page = "107"

[fields]
kind = "archetype"
features = [
  { anchor = "favored-terrain", level = 3 },
  { anchor = "teamwork-feat", level = 6 },
]
trades = [
  { replaces = "Mercy gained at 3rd level", feature = "mercy", levels = [3], by = ["favored-terrain"] },
  { replaces = "Mercy gained at 6th level", feature = "mercy", levels = [6], by = ["teamwork-feat"] },
]
+++

A holy guide believes that it's his sacred calling to clear the roads of bandits between towns as
well as to escort travelers to safety. He must enforce the rule of law in the wilderness and help
those that cannot defend themselves against the many dangers of the area.

## Class Skills {#class-skills}

A holy guide gains Knowledge (geography) and Survival as class skills.

## Favored Terrain (Ex) {#favored-terrain}

At 3rd level, a holy guide chooses a [favored terrain](ref/ability/favored-terrain) from the
[ranger](ref/class/ranger) favored terrains table. This otherwise functions like the ranger ability
of the same name. This ability replaces the mercy gained at 3rd level. Every time a holy guide would
be able to select another mercy, he can instead select another favored terrain and increase his
bonuses for one existing favored terrain, just like a ranger.

## Teamwork Feat (Ex) {#teamwork-feat}

At 6th level, a holy guide gains a teamwork feat as a bonus feat. He must meet the prerequisites for
this feat. As a standard action, He can expend one use of smite evil to grant this feat to all
allies within 30 feet who can see and hear him. Allies retain the use of this bonus feat for 3
rounds plus 1 round for every 2 levels the holy guide possesses. Allies do not need to meet the
prerequisites of this bonus feat. Evil creatures do not gain the benefit of this teamwork feat, even
if the paladin considers them allies. This ability replaces the mercy gained at 6th level.
