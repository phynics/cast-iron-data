+++
id = "ref/arc-shifter/verdant-shifter"
kind = "archetype"
title = "Verdant Shifter"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Verdant%20Shifter"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "verdant_shifter", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "83"

[fields]
kind = "archetype"
features = [
  { anchor = "speak-with-plants", level = 1 },
  { anchor = "verdant-body", level = 1 },
  { anchor = "wild-armor", level = 2 },
  { anchor = "plant-shape", level = 6 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["speak-with-plants"] },
  { replaces = "Shifter aspect and all improvements of shifter aspect", feature = "shifter-aspect", by = ["verdant-body"] },
  { replaces = "Defensive instinct", feature = "defensive-instinct", by = ["wild-armor"] },
  { replaces = "Chimeric form", feature = "chimeric-aspect", by = ["plant-shape"] },
  { replaces = "greater chimeric form", feature = "greater-chimeric-aspect", by = ["plant-shape"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["plant-shape"] },
]
+++

Verdant shifters have an affinity for plants rather than animals and gain a plantlike form that
grows in power as they do. Verdant shifters are the enemies of creatures that would despoil the
natural world, and they seek to maintain balance with civilization and industry to ensure the
sanctity of wild spaces.

## Speak with Plants (Sp) {#speak-with-plants}

At 1st level, a verdant shifter gains the ability to cast
_[speak with plants](ref/spell/speak-with-plants)_ as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 3 plus her
Charisma modifier.

This replaces wild empathy.

## Verdant Body (Su) {#verdant-body}

At 1st level, a verdant shifter takes on plant qualities as vines grow over her body, flowers bloom
in her hair, and bark grows from her skin. The verdant shifter is treated as both her normal
creature type and a plant creature for purposes of spells or effects that target a creature by type
(such as _[bane](ref/magic-enh/bane)_ weapons and a ranger's
[favored enemy](ref/ability/favored-enemy)). Verdant body also grants the verdant shifter a 25%
immunity to critical hits and precision damage (such as [sneak attack](ref/ability/sneak-attack)).

At 5th level, the verdant shifter gains a +2 enhancement bonus to her Constitution score. At 8th
level, the enhancement bonus to her Constitution score increases to +4 and her immunity to critical
hits increases to 50%. At 15th level, the enhancement bonus her Constitution score increases to +6.

This replaces shifter aspect and all improvements of shifter aspect.

## Wild Armor (Ex) {#wild-armor}

At 2nd level, a verdant shifter gains a +2 natural armor bonus to her AC while unencumbered and
either wearing no armor or wearing light or medium nonmetal armor. This bonus increases by 1 at 4th
level and every 4 levels thereafter, to a maximum of a +7 natural armor bonus to AC at 20th level.

This replaces defensive instinct.

## Plant Shape (Su) {#plant-shape}

At 6th level, a verdant shifter's wild shape ability instead functions as
_[plant shape I](ref/spell/plant-shape-1)_. The verdant shifter can maintain this form for a number
of rounds per day equal to her shifter level. At 12th level, this ability instead functions as
_[plant shape II](ref/spell/plant-shape-2)_, and at 18th level, it functions as
_[plant shape III](ref/spell/plant-shape-3)_. This ability otherwise functions as the standard wild
shape shifter class feature.

This alters wild shape and replaces chimeric form and greater chimeric form.
