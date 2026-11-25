+++
id = "ref/arc-wizard/spell-sage"
kind = "archetype"
title = "Spell Sage"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Spell%20Sage"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_sage", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "advanced-class-guide"
page = "133"

[fields]
kind = "archetype"
features = [
  { anchor = "focused-spells", level = 1 },
  { anchor = "spell-study", level = 2 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["focused-spells"] },
  { replaces = "Arcane school", feature = "arcane-school", by = ["spell-study"] },
]
+++

A spell sage has mastered spells of all types, and is able to increase the effectiveness of his own
spells and eventually even cast spells from other classes' spell lists. While most wizards focus on
a school, the spell sage looks at the particular aspects of individual spells and is not afraid to
modify them with interesting bits of insight to gain deeper understandings of the formulae.

## Focused Spells (Su) {#focused-spells}

At 1st level, once per day the spell sage's understanding of spells allows him to increase his
caster level by 4 for a single spell cast. He can do this twice per day at 8th level, and three
times per day at 16th level. This ability replaces arcane bond.

## Spell Study (Su) {#spell-study}

At 2nd level, the sage's understanding of the spells of bards, clerics, and druids is so great that
he can use his own magic in an inefficient, roundabout way to duplicate those classes' spells. Once
per day, a spell sage can spontaneously cast any spell on the bard, cleric, or druid spell list as
if it were a wizard spell he knew and had prepared. Casting the spell requires the spell sage to
spend 1 full round per spell level of the desired spell (if the spell is on multiple spell lists
indicated above, using the lowest level from among those lists) and requires expending two prepared
spells of that spell level or higher; if the spell's casting time is normally 1 full round or
longer, this is added to the spell sage's casting time. For example, if a spell sage wants to use
spell study to cast _[cure light wounds](ref/spell/cure-light-wounds)_ (cleric spell level 1st), he
must spend 2 full rounds casting and expend two prepared wizard spells of 1st level or higher.

At 6th level and every 5 levels thereafter, a spell sage can use this ability an additional time per
day (to a maximum of four times per day at 16th level). This ability replaces arcane school.
