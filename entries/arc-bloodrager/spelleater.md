+++
id = "ref/arc-bloodrager/spelleater"
kind = "archetype"
title = "Spelleater"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Spelleater"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spelleater", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "advanced-class-guide"
page = "85"

[fields]
kind = "archetype"
features = [
  { anchor = "blood-of-life", level = 2 },
  { anchor = "spell-eating", level = 5 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["blood-of-life"] },
  { replaces = "damage reduction", feature = "damage-reduction", by = ["blood-of-life"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["spell-eating"] },
]
+++

Where other bloodragers learn to avoid or shrug off minor damage of all sorts, spelleaters tap into
the power of their bloodline in order to heal damage as it comes, and can even cannibalize their own
magical energy to heal more damage and continue taking the fight to the enemy.

## Blood of Life (Su) {#blood-of-life}

A spelleater's blood empowers him to slowly recover from his wounds. At 2nd level, while bloodraging
a spelleater gains [fast healing 1](ref/umr/fast-healing). At 7th level and every 3 levels
thereafter, this increases by 1 (to a maximum of [fast healing](ref/umr/fast-healing) 6 at 19th
level). If the spelleater gains an increase to [damage reduction](ref/rule/damage-reduction) from a
bloodline, feat, or other ability, he is considered to have an effective
[damage reduction](ref/rule/damage-reduction) of 0, and the increase is added to this effective
damage reduction. This ability replaces uncanny dodge and damage reduction.

## Spell Eating (Su) {#spell-eating}

At 5th level, a spelleater can consume spell slots for an extra dose of healing. As a swift action,
the spelleater can consume one unused bloodrager spell slot to heal 1d8 damage for each level of the
spell slot consumed. This ability replaces improved uncanny dodge.
