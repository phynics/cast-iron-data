+++
id = "ref/arc-wizard/arcane-physician"
kind = "archetype"
title = "Arcane Physician"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Arcane%20Physician"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_physician", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "healers-handbook"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "medicinal-alchemy", level = 1 },
  { anchor = "brew-potion", level = 1 },
]
trades = [
  { replaces = "Arcane school", feature = "arcane-school", by = ["medicinal-alchemy"] },
  { replaces = "Scribe scroll", feature = "scribe-scroll", by = ["brew-potion"] },
]
+++

Arcane physicians use their scholarly knowledge and arcane mastery to achieve incredible feats of
medicine. Most worship [Qi Zhong](ref/faith/qi-zhong), [Nethys](ref/faith/nethys), or other patrons
of disparate sorts of magic.

## Medicinal Alchemy {#medicinal-alchemy}

The arcane physician treats all spells of the healing subschool on the alchemist extract list as if
they were on the wizard spell list for the purpose of activating magic items.

Additionally, he can expend a spell slot of the appropriate level to meet the spell requirements for
magic item construction (including potions) as if the expended spell slot contained any alchemist
spell that belongs to the healing subschool. If the spell is on both the wizard and alchemist lists,
the arcane physician may expend a slot equal to the spell's alchemist level instead of the spell's
wizard level.

At 8th level, the arcane physician can expend a spell slot of 1st level or higher as a standard
action to alter a potion or alchemical remedy held in hand. An alchemical remedy can become any
other alchemical remedy of the same or lower price of the arcane physician's choice. A potion can
change to contain any alchemist extract of the arcane physician's choice that belongs to the healing
subschool and is of the same level as or lower than the expended spell slot. The extract must have
no material component costing more than 1 gp, and it must be one that it is possible to make into a
potion.

This ability replaces arcane school.

## Brew Potion {#brew-potion}

At 1st level, an arcane physician gains [Brew Potion](ref/feat/brew-potion) as a bonus feat.

This replaces scribe scroll.
