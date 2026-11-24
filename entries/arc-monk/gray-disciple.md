+++
id = "ref/arc-monk/gray-disciple"
kind = "archetype"
title = "Gray Disciple"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Gray%20Disciple"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gray_disciple", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-race-guide"
page = "187"

[fields]
kind = "archetype"
features = [
  { anchor = "fade-from-sight", level = 4 },
  { anchor = "gray-heart", level = 6 },
  { anchor = "born-in-darkness", level = 7 },
  { anchor = "earth-glide", level = 12 },
  { anchor = "entomb", level = 15 },
  { anchor = "earthen-thrall", level = 17 },
]
trades = [
  { replaces = "Slow fall", feature = "slow-fall", by = ["fade-from-sight"] },
  { replaces = "still mind", feature = "still-mind", by = ["fade-from-sight"] },
  { replaces = "High jump", feature = "high-jump", by = ["gray-heart"] },
  { replaces = "bonus feat gained at 6th level", feature = "bonus-feat", levels = [6], by = ["gray-heart"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["born-in-darkness"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["earth-glide"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["entomb"] },
  { replaces = "Tongue of the sun and moon", feature = "tongue-of-the-sun-and-moon", by = ["earthen-thrall"] },
  { replaces = "empty body", feature = "empty-body", by = ["earthen-thrall"] },
]
+++

The gray disciple contemplates the inner voice of duergar magic and the silent eternity of stone,
mastering these dual mysteries and combining them to deadly effect.

**Prerequisites:** Duergar

## Fade from Sight (Sp) {#fade-from-sight}

At 4th level, as a swift action, the gray disciple can become invisible (as the
_[invisibility](ref/spell/invisibility)_ spell) for 1 round by spending 1 ki point. To use this
ability, the gray disciple must already have _invisibility_ as a
[spell-like ability](ref/umr/spell-like-abilities). This ability replaces slow fall and still mind.

## Gray Heart (Sp) {#gray-heart}

At 6th level, as a swift action, the gray disciple can enlarge himself (as the
_[enlarge person](ref/spell/enlarge-person)_ spell) for 1 minute by spending 1 ki point. To use this
ability, the gray disciple must already have _[enlarge person](ref/spell/enlarge-person)_ available
as a [spell-like ability](ref/umr/spell-like-abilities). This ability replaces high jump and the
bonus feat gained at 6th level.

## Born in Darkness (Sp) {#born-in-darkness}

At 7th level, as a standard action, the gray disciple can radiate _[darkness](ref/spell/darkness)_
(as the spell, except originating from the disciple's person) for 1 round per level by spending 1 ki
point. This ability replaces wholeness of body.

## Earth Glide (Su) {#earth-glide}

At 12th level, as a swift action, the gray disciple can spend a ki point to walk through solid stone
for 1 round. This functions as the [earth glide](ref/umr/earth-glide) universal monster ability. The
gray disciple may continue earth gliding as long as he spends 1 ki point every round as a swift
action. If he ceases earth gliding within a solid object, he is violently ejected and takes 5d6
points of damage. The gray disciple is not harmed by damage caused to material he is earth gliding
through, but a _[stone to flesh](ref/spell/stone-to-flesh)_ spell cast upon it causes violent
ejection as described above. This ability replaces abundant step.

## Entomb (Su) {#entomb}

At 15th level, a gray disciple can phase a foe into solid rock, killing it instantly. To use this
ability, he expends 1 ki point as part of a [bull rush](ref/rule/bull-rush) or
[reposition](ref/rule/reposition) combat maneuver against a creature adjacent to unworked earth or
stone. If the attempt succeeds, the gray disciple pushes his foe inside the rock using his
[earth glide](ref/spell/earth-glide) ability. If the creature succeeds at a Reflex save (DC 10 + 1/2
the gray disciple's monk level + the gray disciple's Wisdom modifier), it is ejected in the nearest
open space and takes 5d6 points of damage. If it fails, it dies instantly as its body merges with
the surrounding stone. [Entomb](ref/spell/entomb) is usable once per day, but a failed bull rush or
reposition attempt does not count as a use of the ability. [Entomb](ref/spell/entomb) has no effect
on creatures that can [earth glide](ref/spell/earth-glide), are [incorporeal](ref/umr/incorporeal),
or can otherwise can survive merging with a solid object. This ability replaces quivering palm.

## Earthen Thrall (Sp) {#earthen-thrall}

At 17th level, a gray disciple can attempt to control a creature with the earth subtype once per
day. This ability is treated as _[dominate monster](ref/spell/dominate-monster)_ (DC 10 + 1/2 the
gray disciple's monk level + the gray disciple's Wisdom modifier), but is only effective against
creatures with the earth subtype, and the gray disciple can keep only a single creature enthralled.
If he attempts to control a second creature with this ability, the first creature is automatically
released from domination whether or not the second attempt succeeds. This ability replaces tongue of
the sun and moon and empty body.
