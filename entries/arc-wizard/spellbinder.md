+++
id = "ref/arc-wizard/spellbinder"
kind = "archetype"
title = "Spellbinder"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Spellbinder"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellbinder", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "advanced-race-guide"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "spell-bond", level = 1 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["spell-bond"] },
]
+++

A spellbinder is an elven wizard who forges an arcane bond between himself and one or more wizard
spells. These spells become so well understood by the spellbinder that he can prepare them in spell
slots that already have other spells prepared in them.

## Spell Bond (Su) {#spell-bond}

At 1st level, a spellbinder selects any one spell in his spellbook as a bonded spell. As a
full-round action, the spellbinder may replace a spell of the same or higher level as his bonded
spell with his bonded spell. For example, a spellbinder who selects
_[magic missile](ref/spell/magic-missile)_ as his bonded spell could spend a full-round action to
exchange any 1st-level or higher spell that he has prepared with
_[magic missile](ref/spell/magic-missile)_. At 3rd level, and every two levels thereafter, a
spellbinder may select another spell in his spellbook and add it to his list of bonded spells, to a
maximum of nine bonded spells at 17th level.

Upon reaching 4th level, and every two levels thereafter, a spellbinder can choose to select a new
spell as a bonded spell in place of one with which he is already bonded. In effect, the spellbinder
loses the bond with the old spell (though it remains in his spellbook) in exchange for forging a
spell bond with a new spell. The new spell's level must be the same as that of the spell being
exchanged. A spellbinder can swap only one spell bond at any given level, and must choose whether or
not to swap the spell bond at the same time that he gains two new spells in his spellbook for the
level.

This ability replaces arcane bond.

## Discoveries {#discoveries}

The following discoveries complement the spellbinder archetype:
[Fast Study](ref/arcanedisc/fast-study), [Split Slot](ref/arcanedisc/split-slot) (_Ultimate Magic_).
