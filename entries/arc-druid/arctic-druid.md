+++
id = "ref/arc-druid/arctic-druid"
kind = "archetype"
title = "Arctic Druid"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Arctic%20Druid"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arctic_druid", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "advanced-players-guide"
page = "98"

[fields]
kind = "archetype"
features = [
  { anchor = "arctic-native", level = 2 },
  { anchor = "icewalking", level = 3 },
  { anchor = "arctic-endurance", level = 4 },
  { anchor = "wild-shape" },
  { anchor = "snowcaster", level = 9 },
  { anchor = "flurry-form", level = 13 },
]
trades = [
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["arctic-native"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["icewalking"] },
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["arctic-endurance"] },
  { replaces = "Venom immunity", feature = "venom-immunity", by = ["snowcaster"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["flurry-form"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["wild-shape"] },
]
+++

An arctic druid watches over the stark landscape of the far frozen reaches of the world, tending the
stunted and rugged life that ekes out its survival in the least habitable climes.

## Arctic Native (Ex) {#arctic-native}

At 2nd level, an arctic druid gains a bonus on Initiative checks and Knowledge (geography),
Perception, Stealth, and Survival checks equal to 1/2 her druid level in cold or icy terrain, and
she cannot be tracked in cold or icy terrain. This ability replaces woodland stride.

## Icewalking (Ex) {#icewalking}

At 3rd level, an arctic druid suffers no penalty to speed or on Acrobatics, Climb, or Stealth checks
in snowy or icy terrain or weather conditions and can walk across snow crusts or thin ice without
breaking through. This ability replaces trackless step.

## Arctic Endurance (Ex) {#arctic-endurance}

At 4th level, an arctic druid ignores the effects of a cold climate as if using
_[endure elements](ref/spell/endure-elements)_. She is also immune to being dazzled. This ability
replaces resist nature's lure.

## Wild Shape (Su) {#wild-shape}

An arctic druid gains this ability at 6th level, except that her effective druid level for this
ability is equal to her druid level - 2.

## Snowcaster (Su) {#snowcaster}

At 9th level, an arctic druid can see normally in _ice storm_, _sleet storm_, or similar natural
snowstorms. In addition, she can prepare any druid spell with the fire subtype as a cold spell, with
an identical effect but inflicting cold damage instead of fire damage. This ability replaces venom
immunity.

## Flurry Form (Ex) {#flurry-form}

At 13th level, an arctic druid can assume the form of a swirling column of snow equivalent to
_[gaseous form](ref/spell/gaseous-form)_ at will. While in this form, she gains a circumstance bonus
on Stealth checks made in cold terrain equal to her druid level. This ability replaces a thousand
faces.
