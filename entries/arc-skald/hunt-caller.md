+++
id = "ref/arc-skald/hunt-caller"
kind = "archetype"
title = "Hunt Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Hunt%20Caller"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunt_caller", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "85"

[fields]
kind = "archetype"
features = [
  { anchor = "song-of-the-senses", level = 2 },
  { anchor = "call-of-the-wild", level = 6 },
  { anchor = "wilderness-magic", level = 5 },
  { anchor = "inspire-scent", level = 6 },
]
trades = [
  { replaces = "Well-versed", feature = "well-versed", by = ["song-of-the-senses"] },
  { replaces = "Song of strength", feature = "song-of-strength", by = ["call-of-the-wild"] },
  { replaces = "song of the fallen", feature = "song-of-the-fallen", by = ["call-of-the-wild"] },
  { replaces = "rage power gained at 18th level", feature = "rage-powers", levels = [18], by = ["call-of-the-wild"] },
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["wilderness-magic"] },
  { replaces = "Rage power gained at 6th level", feature = "rage-powers", levels = [6], by = ["inspire-scent"] },
]
+++

Hunt callers are skalds whose songs draw their allies into the animal world. They can invoke the
inner beasts of those who observe their supernatural performances—a talent that causes many to
mistake the hunt caller and her allies for lycanthropes or other shapechanging creatures.

## Raging Song (Su) {#raging-song}

A hunt caller gains access to the following raging songs.

## Song of the Senses (Su) {#song-of-the-senses}

At 2nd level, the hunt caller's raging song unlocks animalistic senses in her allies. By spending 1
round of raging song, the hunt caller can affect all allies within 60 feet for 1 hour. The allies
gain [low-light vision](ref/rule/low-light-vision) and a +2 competence bonus on Perception and
Survival checks. If an ally already has [low-light vision](ref/rule/low-light-vision), the range
doubles. The skald must continue to perform the song for the remainder of the hour; otherwise, its
effects end, but only 1 round of raging song is expended for that hour.

This raging song replaces well-versed.

## Call of the Wild (Su) {#call-of-the-wild}

At 6th level, the hunt caller's raging song can transform herself and her allies within 60 feet into
animalistic shapes, as per _[beast shape I](ref/spell/beast-shape-1)_ (Small animals only) at her
caster level. The same transformation applies to all targets. By spending 1 round of raging song per
target, the hunt caller can affect any number of allies within 60 feet for 1 hour. When in animal
form, the hunt caller is treated as able to speak normally for the purpose of using raging song, but
not for using other abilities that require speech (such as spellcasting). The skald must continue to
perform the song for the remainder of the hour; otherwise, its effects end, but only 1 round of
raging song per target is expended for that hour.

At 10th level, the hunt caller can instead choose a Medium animal shape. At 14th level, the hunt
caller can choose _[shapechanger's gift](ref/spell/shapechangers-gift)_ or the effects of
_[beast shape II](ref/spell/beast-shape-2)_. At 18th level, she can choose the effects of
_[beast shape III](ref/spell/beast-shape-3)_.

This raging song replaces song of strength, song of the fallen, and the rage power gained at 18th
level.

## Wilderness Magic (Su) {#wilderness-magic}

At 5th level and again at 11th level and 17th level, the hunt caller adds two spells of any level
she can cast from the druid spell list to her class spell list and list of skald spells known.

This replaces spell kenning.

## Inspire Scent (Ex) {#inspire-scent}

At 6th level, the hunt caller gains the [scent](ref/ragepower/scent) rage power. Her song of the
senses and inspired rage raging songs both grant affected allies this rage power.

This replaces the rage power gained at 6th level.

## Rage Powers {#rage-powers}

The following rage powers complement the hunt caller archetype: animal fury, battle roar, beast
totem (lesser, normal, and greater), intimidating glare, low-light vision, no escape, primal scent,
quick reflexes, sprint, and swift foot.
