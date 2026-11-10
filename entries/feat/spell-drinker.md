+++
id = "ref/feat/spell-drinker"
kind = "feat"
title = "Spell Drinker"
aon = "FeatDisplay.aspx?ItemName=Spell%20Drinker"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_drinker", path = "json/feat14.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/lightning-reflexes", label = "or" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "4"

[fields]
kind = "feat"
prerequisites = "Con 13; Great Fortitude, Iron Will, or Lightning Reflexes."
prerequisite_feats = ["ref/feat/great-fortitude", "ref/feat/iron-will", "ref/feat/lightning-reflexes"]
benefit = "Once per hour, as an immediate action after you succeed at a saving throw against a creature's spell or spell-like ability, you gain a number of temporary hit points equal to 1d6 plus the spell's level for 1 minute. While these temporary hit points last, you gain a +2 bonus on saving throws against spells and spell-like abilities cast by that creature. If you have 10 or more Hit Dice, the number of temporary hit points you gain from this feat doubles. These temporary hit points stack with those gained from other sources, but not with each other."
+++

The magic that cannot harm you only makes you stronger.\
**Prerequisites:** Con 13; [Great Fortitude](ref/feat/great-fortitude),
[Iron Will](ref/feat/iron-will), or [Lightning Reflexes](ref/feat/lightning-reflexes).\
**Benefit:** Once per hour, as an immediate action after you succeed at a saving throw against a
creature's spell or [spell-like ability](ref/umr/spell-like-abilities), you gain a number of
temporary hit points equal to 1d6 plus the spell's level for 1 minute. While these temporary hit
points last, you gain a +2 bonus on saving throws against spells and spell-like abilities cast by
that creature. If you have 10 or more Hit Dice, the number of temporary hit points you gain from
this feat doubles. These temporary hit points stack with those gained from other sources, but not
with each other.
