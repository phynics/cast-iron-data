+++
id = "ref/arc-wizard/spell-sage"
kind = "archetype"
title = "Spell Sage"
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
replaces = ["Arcane bond", "Arcane school"]
replaces_features = ["arcane-bond", "arcane-school"]
+++

A spell sage has mastered spells of all types, and is able to increase the effectiveness of his own
spells and eventually even cast spells from other classes' spell lists. While most wizards focus on
a school, the spell sage looks at the particular aspects of individual spells and is not afraid to
modify them with interesting bits of insight to gain deeper understandings of the formulae.

**Focused Spells (Su)**

**Ability:** Once per day the spell sage's understanding of spells allows him to increase his caster
level by 4 for a single spell cast.

**At 16th Level:** He can do this three times per day.

**At 8th Level:** He can do this twice per day.

**Gained:** At 1st Level

**Replaces:** Arcane bond

**Spell Study (Su)**

**Ability:** A spell sage can spontaneously cast any spell on the bard, cleric, or druid spell list
as if it were a wizard spell he knew and had prepared.

Casting the spell requires the spell sage to spend 1 full round per spell level of the desired spell
(if the spell is on multiple spell lists indicated above, using the lowest level from among those
lists) and requires expending two prepared spells of that spell level or higher; if the spell's
casting time is normally 1 full round or longer, this is added to the spell sage's casting time. For
example, if a spell sage wants to use spell study to cast
[cure light wounds](ref/spell/cure-light-wounds) (cleric spell level 1st), he must spend 2 full
rounds casting and expend two prepared wizard spells of 1st level or higher.

**Flavor:** The sage's understanding of the spells of bards, clerics, and druids is so great that he
can use his own magic in an inefficient, roundabout way to duplicate those classes' spells.

**Gained:** At 2nd Level

**Replaces:** Arcane school

**Usage:** 1 time/day + 1 per 5 wizard levels beyond 1st
