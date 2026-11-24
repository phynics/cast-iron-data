+++
id = "ref/arc-druid/menhir-savant"
kind = "archetype"
title = "Menhir Savant"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Menhir%20Savant"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "menhir_savant", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-magic"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "spirit-sense", level = 1 },
  { anchor = "place-magic", level = 2 },
  { anchor = "walk-the-lines", level = 9 },
  { anchor = "empty-body", level = 13 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["spirit-sense"] },
  { replaces = "wild empathy", feature = "wild-empathy", by = ["spirit-sense"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["place-magic"] },
  { replaces = "trackless step", feature = "trackless-step", by = ["place-magic"] },
  { replaces = "A thousand faces", feature = "a-thousand-faces", by = ["empty-body"] },
]
+++

Some druids study the paths of nature's power through the nodes and ley lines that connect standing
stones and megalithic circles, learning to tap into their energies.

## Spirit Sense (Sp) {#spirit-sense}

At 1st level, a menhir savant can detect the presence of undead; fey; outsiders; and astral,
ethereal, or incorporeal creatures. This ability functions like
_[detect undead](ref/spell/detect-undead)_, and the druid detects all of these creatures rather than
trying to detect one kind. This ability replaces nature sense and wild empathy.

## Place Magic (Su) {#place-magic}

At 2nd level, a menhir savant learns to identify and tap into ley lines in different types of
terrain. As a free action, she can tap into the magic of a nearby ley line and increase her caster
level by +1 for 1 round. She can use this ability a number of times per day equal to 3 + her Wisdom
bonus. This ability replaces woodland stride and trackless step.

## Walk the Lines (Su) {#walk-the-lines}

At 9th level, a menhir savant can use her connection to ley lines to cast
_[transport via plants](ref/spell/transport-via-plants)_ a number of times per day equal to her
Wisdom bonus.

## Empty Body (Su) {#empty-body}

At 13th level, a menhir savant can become ethereal as a standard action, as if using
_[ethereal jaunt](ref/spell/ethereal-jaunt)_. She can remain ethereal for a number of rounds per day
equal to her druid level. These rounds do not need to be consecutive. This ability replaces a
thousand faces.
