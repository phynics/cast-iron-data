+++
id = "ref/arc-companion/feytouched-companion"
kind = "archetype"
title = "Feytouched Companion"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feytouched_companion", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "188"

[fields]
kind = "archetype"
features = [
  { anchor = "not-quite-animal" },
  { anchor = "small-but-fierce" },
  { anchor = "fey-magic" },
  { anchor = "iron-bane", level = 3 },
]
trades = [
  { replaces = "The 4th- or 7th-level ability score and size advancement", by = ["small-but-fierce"] },
  { replaces = "Share Spells", by = ["fey-magic"] },
  { replaces = "Multiattack", by = ["fey-magic"] },
  { replaces = "Evasion", by = ["iron-bane"] },
  { replaces = "Devotion", by = ["iron-bane"] },
  { replaces = "Improved Evasion", by = ["iron-bane"] },
]
+++

Feytouched companions are strangely colored fauna native to the First World, the primal realm of the
fey. They gain strange abilities tied to the fey.

## Feytouched Skills {#feytouched-skills}

Feytouched companions treat Perform as a class skill.

## Not Quite Animal {#not-quite-animal}

The DC to use Handle Animal on a feytouched companion is 5 higher, as if it were a nonanimal with an
Intelligence score of 1 or 2.

## Small but Fierce (Ex) {#small-but-fierce}

A feytouched companion must be an animal companion that normally starts as Small or smaller. At 4th
or 7th level, whenever the feytouched companion would normally gain the choice of a listed
advancement or a +2 bonus to its Dexterity and Constitution scores, it instead gains a +2 bonus to
its Strength, Dexterity, and Constitution scores.

This replaces the 4th- or 7th-level ability score and size advancement.

## Fey Magic (Sp) {#fey-magic}

A feytouched companion can cast _[dancing lights](ref/spell/dancing-lights)_ at will as a
[spell-like ability](ref/umr/spell-like-abilities) as a full-round action. At 3rd level, a
feytouched companion can [ready](ref/rule/ready) an action for its master's spellcasting while
adjacent to its master, to allow its master to spontaneously cast one of the following spells by
sacrificing a spell slot of equal or higher level: _[faerie fire](ref/spell/faerie-fire)_ (1st),
_[glitterdust](ref/spell/glitterdust)_ (2nd), _[deep slumber](ref/spell/deep-slumber)_ (3rd),
_[major image](ref/spell/major-image)_ (4th), _[confusion](ref/spell/confusion)_ (5th),
_[feeblemind](ref/spell/feeblemind)_ (7th), _[mislead](ref/spell/mislead)_ (8th). A feytouched
companion's master can cast each of the spells on the list only once each day in this way.

This replaces share spells and Multiattack.

## Iron Bane (Ex) {#iron-bane}

At 3rd level, a feytouched companion gains [damage reduction](ref/rule/damage-reduction) 1/cold
iron. This damage reduction increases by 1 for every 3 levels beyond 3rd. Any creature holding or
wearing an item made out of cold iron takes a -10 penalty on Handle Animal checks to handle the
feytouched companion.

This replaces evasion, devotion, and improved evasion.
