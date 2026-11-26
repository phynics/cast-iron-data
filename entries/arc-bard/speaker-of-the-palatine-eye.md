+++
id = "ref/arc-bard/speaker-of-the-palatine-eye"
kind = "archetype"
title = "Speaker of the Palatine Eye"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Speaker%20of%20the%20Palatine%20Eye"
source_ids = ["heroes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "speaker_of_the_palatine_eye", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "heroes-of-golarion"
page = "8"

[fields]
kind = "archetype"
features = [
  { anchor = "angelic-grace" },
  { anchor = "spells", level = 1 },
  { anchor = "corpse-speaker", level = 1 },
  { anchor = "keen-ritualist", level = 10 },
]
trades = [
  { replaces = "Countersong", feature = "bardic-performance", power = "countersong", by = ["corpse-speaker"] },
  { replaces = "Jack-of-all-trades", feature = "jack-of-all-trades", by = ["keen-ritualist"] },
  { alters = "The bard's class skills", by = ["angelic-grace"] },
  { alters = "Spells", feature = "spells", by = ["spells"] },
]
+++

Working from the shadows of Ustalav's high society, the Esoteric Order of the Palatine Eye is a
mystical cult built around the quest for immortality. Founded by a count who claimed to have been
enlightened by angels, the Order follows a strict hierarchy, and membership is open only to the
elite. The more money a member provides the Order, the more secrets he learns to aid his path toward
angelic ascension. More information on the Esoteric Order of the Palatine Eye can be found in
_Pathfinder Adventure Path \#44: Trial of the Beast_.

A speaker of the Palatine Eye influences others using his occult knowledge rather than the
boisterous enthusiasm of most bards. He must be a worshipper of [Pharasma](ref/faith/pharasma), but
he may worship additional deities as well.

## Angelic Grace (Ex) {#angelic-grace}

Members of the Order of the Palatine Eye carry themselves with the austerity and import their
heavenly aspirations demand. A speaker of the Palatine Eye does not have Acrobatics or Escape Artist
as class skills, but he gains Celestial as a bonus language. This does not count toward the number
of languages he is otherwise able to learn.

This alters the bard's class skills.

## Spells {#spells}

A speaker of the Palatine Eye draws his powers from the mysterious rites of the Esoteric Order of
the Palatine Eye. He casts psychic spells from the mesmerist list instead of arcane spells from the
bard spell list. He otherwise casts spells, learns spells, and determines his spell allotment and
spell DCs as a bard.

This alters spells.

## Corpse Speaker (Su) {#corpse-speaker}

A speaker of the Palatine Eye can make it appear as if a corpse is speaking, similar to
_[ventriloquism](ref/spell/ventriloquism)_. A creature must succeed at a Will saving throw (DC =
10 + [half](ref/misc/fractions-and-rounding) the bard's level + the bard's Charisma modifier) to see
through the ruse. A creature that fails the saving throw is convinced that the corpse is speaking of
its own volition.

This replaces countersong.

## Keen Ritualist (Ex) {#keen-ritualist}

At 10th level, a speaker of the Palatine Eye reduces the number of secondary casters required to
cast a [ritual](ref/rule/occult-rituals) by 2. At 16th level, the DCs of skill checks the speaker of
the Palatine Eye attempts during a ritual are reduced by 2. At 19th level, a speaker of the Palatine
Eye can perform any ritual by himself without needing to satisfy any secondary caster requirements.
The DCs of skill checks he attempts during a ritual are reduced by an additional 2, for a maximum DC
reduction of 4.

This replaces jack-of-all-trades.
