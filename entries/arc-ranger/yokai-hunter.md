+++
id = "ref/arc-ranger/yokai-hunter"
kind = "archetype"
title = "Yokai Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Yokai%20Hunter"
source_ids = ["dragon-empires-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "yokai_hunter", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "dragon-empires-primer"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "favored-yokai", level = 1 },
  { anchor = "yokai-sense", level = 7 },
  { anchor = "resist-yokai", level = 12 },
]
trades = [
  { replaces = "Favored enemy", feature = "favored-enemy", by = ["favored-yokai"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["yokai-sense"] },
  { replaces = "Camouflage", feature = "camouflage", by = ["resist-yokai"] },
]
+++

Yokai hunters possess a supernatural tether to the spirit worlds that shroud mortal existence. They
use their powers to peer into the realm of the dead, and are adept at hunting those who dwell in the
realm between the Material Plane and the Great Beyond, the supernatural beings Tians refer to as
yokai. The yokai hunter is an archetype of the ranger class.

## Favored Yokai (Su) {#favored-yokai}

A yokai hunter possesses a supernatural ability to sense beings connected to the spirit world, such
as [kami](ref/family/kami), [oni](ref/family/oni), and [ghosts](ref/template/ghost), and is
formidable at fighting them. At 1st level, a yokai hunter gains a +2 bonus on weapon attacks and
damage rolls against one of the following creature types (and subtypes, if applicable), which are
considered yokai for the purposes of this archetype: aberration, dragon, fey, magical beast,
outsider (native), and undead (incorporeal). (A GM may choose to alter this list for the purposes of
her campaign.) At 5th level and every five levels thereafter, a yokai hunter may select another
favored yokai from this list, gaining a +2 bonus on weapon attacks and damage rolls against that
yokai.

In addition, whenever a yokai hunter sees a favored yokai that is disguised or has not made its
otherworldly essence known, he gains an automatic check to identify the creature as such. To make
this check, a yokai hunter rolls 1d20 and adds his yokai hunter level and Charisma modifier (DC 10 +
1/2 the yokai's Hit Dice + the yokai's Cha modifier). A successful check means that the yokai hunter
recognizes the creature's ties to the spiritual world. Regardless of whether the check is
successful, a yokai hunter gains the bonus on weapon attacks and damage rolls against favored yokai.

This ability replaces favored enemy. Ranger abilities that rely on a favored enemy instead rely on
this ability.

## Yokai Sense (Su) {#yokai-sense}

At 7th level, a yokai hunter can sense yokai he has identified with his favored yokai ability as
though he had [blindsense](ref/umr/blindsense) out to a range of 60 feet. This ability replaces
woodland stride.

## Resist Yokai (Su) {#resist-yokai}

At 12th level, a yokai hunter can attempt to shrug off the magical energies of a yokai. He gains a
+4 insight bonus on saving throws to resist the spells,
[spell-like abilities](ref/umr/spell-like-abilities), and supernatural abilities of favored yokai.
In addition, once per day as a standard action, a yokai hunter can shed an effect placed on him by a
yokai as _[break enchantment](ref/spell/break-enchantment)_, using his yokai hunter level as his
caster level. This ability replaces camouflage.
