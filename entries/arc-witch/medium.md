+++
id = "ref/arc-witch/medium"
kind = "archetype"
title = "Medium"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Medium"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "medium", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "undead-slayers-handbook"
page = "20"

[fields]
kind = "archetype"
features = [
  { anchor = "ectoplasmic-aptitude", level = 2 },
  { anchor = "shared-subconscious", level = 6 },
  { anchor = "soul-walker", level = 20 },
]
trades = [
  { replaces = "Hex gained at 2nd level", feature = "hex", levels = [2], by = ["ectoplasmic-aptitude"] },
  { replaces = "Hex gained at 6th level", feature = "hex", levels = [6], by = ["shared-subconscious"] },
  { replaces = "Hex gained at 20th level", feature = "hex", levels = [20], by = ["soul-walker"] },
]
+++

Mediums tap into the spiritual power of those who have yet to find their final rest. Their ability
to interact with these souls allows mediums to learn about the physical world through the
experiences of those who came before them. Eventually, mediums of immeasurable power learn to walk
alongside the very souls that haunt their dreams and visions.

## Patron {#patron}

A medium has a limited choice of patrons, and must select one of the following themes:
[ancestors](ref/patron/ancestors), [death](ref/patron/death), [occult](ref/patron/occult), or
[spirits](ref/patron/spirits).

## Ectoplasmic Aptitude (Su) {#ectoplasmic-aptitude}

At 2nd level, the medium can sling spells at ghosts and spirits as surely as at corporeal foes. She
gains the [Ectoplasmic Spell](ref/feat/ectoplasmic-spell) metamagic feat as a bonus feat. In
addition, as an immediate action a number of times per day equal to her Intelligence modifier, the
medium can apply the Ectoplasmic Spell feat to any spell she is casting without increasing its spell
level. This ability replaces the witch's hex gained at 2nd level.

## Shared Subconscious (Su) {#shared-subconscious}

At 6th level, a medium can temporarily link her subconscious to that of an undead creature in order
to gain preternatural knowledge. As long as the medium is within 100 feet of an intelligent undead
creature, as a swift action she can target said creature and attempt any trained Knowledge check. If
the target has ranks in the same Knowledge skill, it also attempts the Knowledge check (if it
doesn't have ranks, this effect fails). If the target's result is higher than the medium's, the
medium may choose to use the undead creature's Knowledge result instead of her own, learning any
information the undead creature has about the subject in question. This ability does not allow a
medium to attempt a previously failed Knowledge check again. This replaces the witch's hex gained at
6th level.

## Soul Walker (Ex) {#soul-walker}

At 20th level, a medium can drift into the spirit world, becoming
[incorporeal](ref/subtype/incorporeal) for 1 minute per class level. When she does so, the medium
gains the incorporeal subtype, taking only half damage from corporeal magical attacks and no damage
from nonmagical weapons and objects. Her spells deal only half damage to corporeal creatures, but
spells and abilities that do not deal damage function normally. The duration of this ability need
not be continuous, but it must be used in 1-minute increments. This replaces the witch's hex gained
at 20th level.

## Hexes {#hexes}

The following witch hexes complement the medium archetype: charm, healing, scar, tongues, ward.

## Major Hexes {#major-hexes}

The following major hexes complement the medium archetype: speak in dreams, vision.

## Grand Hexes {#grand-hexes}

The following grand hex complements the medium archetype: summon spirit.
