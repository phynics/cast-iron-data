+++
id = "ref/arc-companion/precocious-companion"
kind = "archetype"
title = "Precocious Companion"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "precocious_companion", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "188"

[fields]
kind = "archetype"
features = [
  { anchor = "expanded-tricks", level = 3 },
  { anchor = "perspicacious-mind" },
]
trades = [
  { replaces = "Evasion", by = ["expanded-tricks"] },
  { replaces = "Improved Evasion", by = ["expanded-tricks"] },
  { replaces = "The 4th- or 7th-level ability score advancement", by = ["perspicacious-mind"] },
]
+++

Precocious companions are able to learn far more tricks than other companions; this ability to learn
allows their masters to use them for a wider variety of tasks.

## Expanded Tricks (Ex) {#expanded-tricks}

At 3rd level, a precocious companion gains twice as many bonus tricks as normal for an animal
companion. A [hunter's](ref/class/hunter) animal companion can't use the additional bonus tricks to
learn hunter's tricks. At 15th level, the DC of the Handle Animal check to push a precocious
companion to perform an unlearned trick is only 15, instead of 25.

This replaces evasion and improved evasion.

## Perspicacious Mind (Ex) {#perspicacious-mind}

At 4th or 7th level, whenever the precocious companion would normally gain the choice of a listed
score advancement or a +2 bonus to Dexterity and Constitution, it instead gains a +2 bonus to its
Intelligence score and a +4 bonus to +4 its Wisdom and Charisma scores.

This replaces the 4th- or 7th-level ability score advancement.
