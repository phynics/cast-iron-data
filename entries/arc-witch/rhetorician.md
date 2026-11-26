+++
id = "ref/arc-witch/rhetorician"
kind = "archetype"
title = "Rhetorician"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Rhetorician"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rhetorician", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "arcane-anthology"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "debater", level = 1 },
  { anchor = "eldritch-glibness", level = 2 },
  { anchor = "public-speaker" },
]
trades = [
  { replaces = "Hex gained at 1st level", feature = "hex", levels = [1], by = ["debater"] },
  { replaces = "All the spells the witch gains from her patron", feature = "patron-spells", by = ["eldritch-glibness"] },
]
+++

Rhetoricians feel driven to engage in debate, learn as much as they can about their potential foes,
and seek ways to use information and quick talking to handle problems before resorting to raw
violence. Regardless of their shadowy patrons, rhetoricians are granted a series of spells through
their familiars that boost their ability to outtalk and outthink their foes, leading some to believe
they are destined to be emissaries for their patrons once some long-term plans of their patrons'
come to fruition.

## Debater (Ex) {#debater}

A rhetorician is an expert at making counterarguments and treating everything as a debate. When an
opponent attempts a Diplomacy check to change another target's attitude or request aid, the
rhetorician can attempt to make a counterargument to negate the opponent's efforts. The rhetorician
attempts a Diplomacy check as an immediate action, with a DC equal to the result of the opponent's
Diplomacy check. The target of the opponent's Diplomacy check must be able to see and hear the
rhetorician. If the rhetorician's Diplomacy check is successful, the opponent's Diplomacy check
fails. This ability replaces the hex gained at 1st level.

## Eldritch Glibness {#eldritch-glibness}

At 2nd level and every two witch levels thereafter, a rhetorician gains the following spells as
spells known at the spell levels listed in parentheses. These spells are automatically added to the
list of spells stored by her familiar. She treats these as being on the witch class spell list:
2nd—_confusion, lesser_ (1st), 4th—_detect thoughts_ (2nd), 6th—_glibness_ (3rd), 8th—_sculpt sound_
(4th), 10th—_modify memory_ (5th), 12th—_symbol of persuasion_ (6th), 14th—_song of discord_ (7th),
16th—_greater shout_ (8th), 18th—_weird_ (9th). This ability replaces all the spells the witch gains
from her patron.

## Public Speaker (Ex) {#public-speaker}

A rhetorician gains Perform as a class skill. In addition, she is trained to project her voice with
great skill and effect; the DC to hear her speak in difficult conditions is reduced by an amount
equal to her class level + her Intelligence modifier (minimum 0).
