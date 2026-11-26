+++
id = "ref/arc-alchemist/blazing-torchbearer"
kind = "archetype"
title = "Blazing Torchbearer"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Blazing%20Torchbearer"
source_ids = ["dungeoneers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blazing_torchbearer", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "dungeoneers-handbook"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "everburning-flame", level = 1 },
  { anchor = "intense-light", level = 2 },
  { anchor = "explosive-torch", level = 4 },
]
trades = [
  { replaces = "Brew Potion", feature = "brew-potion", by = ["everburning-flame"] },
  { replaces = "Poison use", feature = "poison-use", by = ["intense-light"] },
  { replaces = "The alchemist's 4th-level discovery", feature = "discovery", levels = [4], by = ["explosive-torch"] },
]
+++

The blazing torchbearer is especially adept at manipulating flames of all kinds.

## Everburning Flame (Ex) {#everburning-flame}

Any torch held by a blazing torchbearer is considered to be an
[everburning torch](ref/eq-misc/everburning-torch), although it still sheds heat and can be used as
a weapon. In addition, a blazing torchbearer can cast _[spark](ref/spell/spark)_ as a
[spell-like ability](ref/umr/spell-like-abilities) at will. This ability replaces Brew Potion.

## Intense Light (Ex) {#intense-light}

At 2nd level, a blazing torchbearer has mastered lighting and holding a torch to the point that it
sheds more light than those carried by his peers. The radius of normal and increased
[illumination](ref/rule/vision-and-light) of any torch held by a blazing torchbearer increases by 10
feet. Once per day as a standard action, the blazing torchbearer can create a brilliant flash of
light that [blinds](ref/misc/blinded) everyone within 10 feet (including the torchbearer) for 1
round. This ability replaces poison use.

## Explosive Torch (Ex) {#explosive-torch}

At 4th level, as a standard action, a blazing torchbearer can drop a special blend of explosive
powders onto his torch before using it as a weapon. His next successful melee attack with the torch
deals an additional 2d6 points of fire damage and
[sets the target on fire](ref/rule/catching-on-fire). This attack must be made within 1d4 rounds or
the torch prematurely explodes at the end of the blazing torchbearer's turn, dealing damage to the
blazing torchbearer and setting him on fire. This ability replaces the alchemist's 4th-level
discovery.
