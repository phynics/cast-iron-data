+++
id = "ref/arc-slayer/covenbane"
kind = "archetype"
title = "Covenbane"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Covenbane"
source_ids = ["blood-of-the-coven"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "covenbane", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "blood-of-the-coven"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "hag-sense", level = 1 },
  { anchor = "studied-coven", level = 2 },
  { anchor = "disrupt-coven" },
  { anchor = "unseen-sense", level = 11 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["hag-sense"] },
  { replaces = "Slayer talent gained at 2nd level", feature = "slayer-talents", levels = [2], by = ["studied-coven"] },
  { replaces = "Stalker", feature = "stalker", by = ["disrupt-coven"] },
  { replaces = "Swift tracker", feature = "swift-tracker", by = ["unseen-sense"] },
  { alters = "Studied target", feature = "studied-target", by = ["studied-coven"] },
]
+++

Covenbane slayers are scarred by arcane magic at a young age, and that resonance gives them
supernatural insight into the psychic bonds between others. They are adept at fighting tight-knit
groups, exploiting their connections to hunt and wound teams. The churches of
[Iomedae](ref/faith/iomedae) and [Milani](ref/faith/milani) in particular dispatch special agents to
rescue hexed children from Irrisen, Razmiran, and other lands plagued by abusive arcanists and then
raise them in this deadly art.

## Hag Sense (Su) {#hag-sense}

A covenbane's magical scars throb in the presence of magic. A covenbane adds half his level (minimum
+1) on Perception, Sense Motive, and Survival checks to identify, recognize, or track a
[hag](ref/family/hag), arcane spellcaster, or creature with
[spell-like abilities](ref/umr/spell-like-abilities). He can also use his hag sense to recognize
whether someone within 30 feet of him is using magic to hide her true form. To do this, he must
succeed at a Perception check against a DC equal to 15 + the target's CR; success indicates the
presence of a magical disguise, but it does not reveal the creature's true form.

This replaces track.

## Studied Coven (Su) {#studied-coven}

At 2nd level, a covenbane can designate an entire coven as his studied target by studying any single
member. He applies his studied target bonus against all members of the studied creature's coven, and
all members of the coven count as one target for the purposes of determining the maximum number of
studied targets a slayer can maintain. This bonus remains even if one or more members of the coven
die after the covenbane studies them. Beginning at 7th level, the covenbane can designate other
magically linked creatures, such as those bound by a [hivemind](ref/template/hivemind-swarm) or a
_[telepathic bond](ref/spell/telepathic-bond)_ spell, as a coven, but he can target only three
members of such a link. Studying a coven always requires a move action, even if the slayer could
normally study a target with a swift or immediate action.

This replaces the slayer talent gained at 2nd level.

## Disrupt Coven (Su) {#disrupt-coven}

Anyone the slayer threatens no longer counts as an ally for the purposes of friendly spellcasting or
employing teamwork feats and cannot access any special abilities gained from being part of a coven
(including coven spellcasting).

This replaces stalker.

## Unseen Sense (Su) {#unseen-sense}

At 11th level, the covenbane learns to use his hag sense to help target concealed or invisible
opponents in combat. He can use his hag sense to detect invisible opponents as well as magically
disguised creatures. He also gains [Blind-Fight](ref/feat/blind-fight) as a bonus feat but gains its
benefits only against spellcasters and creatures with
[spell-like abilities](ref/umr/spell-like-abilities).

This replaces swift tracker.
