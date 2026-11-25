+++
id = "ref/arc-investigator/empiricist"
kind = "archetype"
title = "Empiricist"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Empiricist"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "empiricist", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "advanced-class-guide"
page = "100"

[fields]
kind = "archetype"
features = [
  { anchor = "ceaseless-observation", level = 2 },
  { anchor = "unfailing-logic", level = 4 },
  { anchor = "master-intellect", level = 20 },
]
trades = [
  { replaces = "Poison lore", feature = "poison-lore", by = ["ceaseless-observation"] },
  { replaces = "poison resistance", feature = "poison-resistance", by = ["ceaseless-observation"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["unfailing-logic"] },
  { replaces = "True inspiration", feature = "true-inspiration", by = ["master-intellect"] },
]
+++

Champions of deductive reasoning and logical insight, empiricists put their faith in facts, data,
confirmed observations, and consistently repeatable experiments—these things are their currency of
truth.

## Ceaseless Observation (Ex) {#ceaseless-observation}

An empiricist's ability to notice the minutiae of almost everything that happens around him allows
him to make shrewd and insightful calculations about people and even inanimate objects. At 2nd
level, an empiricist uses his Intelligence modifier instead of the skill's typical ability for all
Disable Device, Perception, Sense Motive, and Use Magic Device checks. He can also use his
Intelligence modifier instead of Charisma on any Diplomacy checks made to gather information. This
ability replaces poison lore and poison resistance.

## Unfailing Logic (Ex) {#unfailing-logic}

An empiricist's grasp of facts and data teaches him to anchor himself in reality, granting
resistance to even the most potent illusions. At 4th level, an empiricist gains a +2 insight bonus
on all Will saving throws against illusion spells or
[spell-like abilities](ref/umr/spell-like-abilities) that allow a save to disbelieve their effects.
In addition he can spend one point from his inspiration pool as an immediate action to use his
Intelligence bonus instead of her Wisdom bonus on all such saves for one round.

At 8th level, the empiricist's insight bonus increases to +4. At 16th level, he gains immunity to
all illusion spells and [spell-like abilities](ref/umr/spell-like-abilities) that allow a save to
disbelieve the effects. This ability replaces swift alchemy.

## Master Intellect (Ex) {#master-intellect}

At 20th level, an empiricist's powers of reason and deduction become almost superhuman, and he is
able to use them in nearly all aspects of life. At 20th level, an empiricist can use inspiration on
all skills (even ones he is not trained in) and all ability checks (including initiative checks)
without spending inspiration. This ability replaces true inspiration.
