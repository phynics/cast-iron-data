+++
id = "ref/arc-bard/flame-dancer"
kind = "archetype"
title = "Flame Dancer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Flame%20Dancer"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flame_dancer", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-class-guide"
page = "81"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "fire-dance", level = 1 },
  { anchor = "song-of-the-fiery-gaze", level = 3 },
  { anchor = "fire-break", level = 6 },
  { anchor = "fan-the-flames", level = 8 },
]
trades = [
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["fire-dance"] },
  { replaces = "Inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["song-of-the-fiery-gaze"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["fire-break"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["fan-the-flames"] },
]
+++

A flame dancer studies the movements of fire, adding its grace to his repertoire. He seeks truth in
fire's burning essence, and uses his performance to unleash the power of fire against those who dare
oppose him.

## Bardic Performance {#bardic-performance}

A flame dancer gains the following bardic performances.

## Fire Dance (Su) {#fire-dance}

At 1st level, a fire dancer learns to protect himself and others from the pain of fire, and
discovers how to control the flame while enduring its heat. Each round of the fire dance, he rolls a
Perform (dance or sing) check. Any ally within 30 feet of the bard that has caught on fire or is
affected by a fire effect or extreme heat can use the bard's Perform check result in place of its
saving throw against that fire. Any ally within 30 feet of the bard who is suffering from
[heatstroke](ref/rule/heat-dangers) can ignore the fatigue from heat exposure so long as the bard
maintains this performance. Fire dance relies on audible or visual components. This ability replaces
countersong.

## Song of the Fiery Gaze (Su) {#song-of-the-fiery-gaze}

At 3rd level, a fire dancer can allow allies to see through flames without any distortion. Any ally
within 30 feet of the bard who can hear the performance can see through fire, fog, and smoke without
penalty as long as the light is sufficient to allow him to see normally, as with the base effect of
the [gaze of flames](ref/mystery/flame) oracle revelation (_Advanced Player's Guide_ 47). Song of
the fiery gaze relies on audible components. This ability replaces inspire competence.

## Fire Break (Su) {#fire-break}

At 6th level, a fire dancer's performance can bend flames away from others. Any ally within 30 feet
of the bard who can hear or see the bardic performance gains [resist](ref/umr/resistance) fire 20 as
long as the performance is maintained. At 11th level, this resistance increases to 30. Fire break
relies on audible or visual components. This ability replaces suggestion.

## Fan the Flames (Su) {#fan-the-flames}

At 8th level, a fire dancer adds _[burning hands](ref/spell/burning-hands)_,
_[flaming sphere](ref/spell/flaming-sphere)_, and _[fireball](ref/spell/fireball)_ to his list of
bard spells known (as 1st-, 2nd-, and 3rd-level spells, respectively). This ability replaces dirge
of doom.
