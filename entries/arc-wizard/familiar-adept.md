+++
id = "ref/arc-wizard/familiar-adept"
kind = "archetype"
title = "Familiar Adept"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Familiar%20Adept"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "familiar_adept", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "familiar-folio"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-expertise", level = 1 },
  { anchor = "school-familiar", level = 1 },
  { anchor = "familiar-spells" },
  { anchor = "focused-school", level = 1 },
]
trades = [
  { replaces = "Scribe scroll", feature = "scribe-scroll", by = ["diminished-expertise"] },
  { replaces = "Bonus feats at 5th and 10th levels", feature = "bonus-feats", levels = [5, 10], by = ["diminished-expertise"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["school-familiar"] },
  { alters = "Spellbook", feature = "spellbooks", by = ["familiar-spells"] },
]
+++

Many wizards employ familiars to assist them, but only a few have unlocked the true power of their
school of magic through the familiar itself.

## Diminished Expertise {#diminished-expertise}

A familiar adept doesn't gain Scribe Scroll at 1st level or the wizard's bonus feats at 5th and 10th
levels. He must also choose one additional opposition school, even if he is a universalist.

## School Familiar (Ex) {#school-familiar}

At 1st level, a familiar adept must select a familiar for his arcane bond. His familiar
automatically gains the [school familiar](ref/arc-familiar/school-familiar) archetype (see page 14),
but it cannot use its lesser school power until 4th level. At 8th level, it gains access to its
greater school power. This ability alters arcane bond.

## Familiar Spells (Ex) {#familiar-spells}

A familiar adept stores his spells in his familiar rather than in a spellbook, exactly as a
[witch](ref/class/witch) does. His familiar can freely trade spells known with a witch's familiar,
provided the spells traded are on both casters' class spell lists. The familiar adept's familiar
uses the witch rules for familiars, including the increased cost of replacing the familiar. This
ability alters spellbooks.

## Focused School (Ex) {#focused-school}

A familiar adept's training is focused more deeply on his familiar and his school of magic. At 1st
level, 5th level, and every 5 levels thereafter, his familiar gains the ability to use the wizard's
1st-level school ability one time per day without it counting against the wizard's daily uses.
