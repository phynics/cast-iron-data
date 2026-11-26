+++
id = "ref/arc-ranger/guide"
kind = "archetype"
title = "Guide"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Guide"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guide", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-players-guide"
page = "125"

[fields]
kind = "archetype"
features = [
  { anchor = "ranger-s-focus", level = 1 },
  { anchor = "terrain-bond", level = 4 },
  { anchor = "ranger-s-luck" },
  { anchor = "inspired-moment", level = 11 },
  { anchor = "improved-ranger-s-luck", level = 16 },
]
trades = [
  { replaces = "Favored enemy", feature = "favored-enemy", by = ["ranger-s-focus"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["terrain-bond"] },
  { replaces = "Evasion", feature = "evasion", by = ["ranger-s-luck"] },
  { replaces = "Quarry", feature = "quarry", by = ["inspired-moment"] },
  { replaces = "improved quarry", feature = "improved-quarry", by = ["inspired-moment"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["improved-ranger-s-luck"] },
]
+++

Many rangers are loners, but some choose to use their familiarity with the land to guide others
safely through the wilderness. The guide forgoes a _favored enemy_ to focus on the task or foe at
hand, and can pass his knowledge and luck on to his charges. A guide has the following class
features.

## Ranger's Focus (Ex) {#ranger-s-focus}

At 1st level, once per day, the guide can focus on a single enemy within line of sight as a swift
action. That creature remains the ranger's focus until it is reduced to 0 or fewer hit points or
surrenders, or until the ranger designates a new focus, whichever occurs first. The ranger gains a
+2 bonus on attack and damage rolls against the target of his focus. At 5th level, and every five
levels thereafter, this bonus increases by +2.

At 4th level, and every 3 levels thereafter, the ranger can use this ability one additional time per
day. This ability replaces favored enemy.

## Terrain Bond (Ex) {#terrain-bond}

At 4th level, the guide forms a bond with the land itself, enabling him to direct others in such
terrain. When in his favored terrain, the ranger grants all allies within line of sight and that can
hear him a +2 bonus on initiative checks and Perception, Stealth, and Survival skill checks. Also,
as long as they travel with him, the ranger's allies leave no trail and can't be tracked. The ranger
can choose for the group to leave a trail, or even specific members of the group to leave a trail if
he so desires. This ability replaces hunter's bond.

## Ranger's Luck (Ex) {#ranger-s-luck}

Upon reaching 9th level, once per day the guide can either reroll one of his attack rolls or force
an enemy who just hit him with an attack to reroll the attack roll. The ranger must take the result
of the second roll even if it is worse. A ranger can use this ability once per day at 9th level,
plus one additional time per day at 14th and 19th levels. This ability replaces evasion.

## Inspired Moment (Ex) {#inspired-moment}

At 11th level, the guide can have an inspired moment once per day as a free action. The ranger gains
the following benefits until the end of his next turn. His speed increases by 10 feet. He can take
an extra move or swift action on his turn. He gains a +4 bonus to AC and on attack rolls, skill
checks, or ability checks. Finally, he automatically confirms any critical threat he scores. He can
use this ability one additional time per day at 19th level. This ability replaces quarry and
improved quarry.

## Improved Ranger's Luck (Ex) {#improved-ranger-s-luck}

Upon reaching 16th level, the ranger's luck increases. He gains a +4 bonus on his rerolls made with
the ranger's luck ability, or if he forces an enemy to reroll an attack, that enemy takes a -4
penalty on the roll. This bonus or penalty is also applied on any roll to confirm critical hits.
This ability replaces improved evasion.
