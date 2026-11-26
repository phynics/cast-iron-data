+++
id = "ref/arc-druid/tempest-tamer"
kind = "archetype"
title = "Tempest Tamer"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Tempest%20Tamer"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tempest_tamer", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "speech-of-the-sea" },
  { anchor = "whirlpool-walker", level = 4 },
  { anchor = "tempest-wild-shape", level = 4 },
]
trades = [
  { replaces = "Resist nature's lure", feature = "resist-nature-s-lure", by = ["whirlpool-walker"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["tempest-wild-shape"] },
  { alters = "Bonus languages", feature = "bonus-languages", by = ["speech-of-the-sea"] },
]
+++

Druids draw upon the fiercest powers of nature, and tsunamis, typhoons, and whirlpools are among the
most powerful forces in the ocean. Tempest tamers are at one with the water and gain the ability to
soothe these dangerous phenomena. Tempest tamers can be found in many of Golarion's oceans, but all
avoid the spectacular Eye of Abendego—they are all keenly aware of the supernatural origin of that
massive hurricane, and they know they cannot quell its fury without first acquiring extraordinary
power.

## Speech of the Sea {#speech-of-the-sea}

A tempest tamer's bonus language options include Aquan and Auran, in addition to the bonus languages
available to the character from her race. However, the tempest tamer does not gain Sylvan as a bonus
language option.

This ability alters bonus languages.

## Whirlpool Walker (Ex) {#whirlpool-walker}

At 4th level, a tempest tamer can resist winds and the unnatural powers of sea creatures. The
tempest tamer gains a +4 bonus on saving throws against spells with the air or water descriptor and
the spell-like and supernatural abilities of creatures with the air, aquatic, or water subtype. This
bonus also applies to saving throws to avoid damage from a vortex, whirlpool, or similar effects, as
well as to saving throws to prevent being pulled into or moved by such effects.

This ability replaces resist nature's lure.

## Tempest Wild Shape (Su) {#tempest-wild-shape}

At 4th level, a tempest tamer gains the ability to turn herself into a Small water elemental. This
ability functions as per the _[elemental body I](ref/spell/elemental-body-1)_ spell except as noted
here. The effect lasts for 1 hour per druid level or until she changes back. Changing form (to an
elemental or back) is a standard action and doesn't provoke attacks of opportunity.

At 6th level, a tempest tamer can use tempest wild shape to change into a Small air elemental. At
8th level, a tempest tamer can use tempest wild shape to change into a Medium air or water
elemental, as per _[elemental body II](ref/spell/elemental-body-2)_. At 10th level, a tempest tamer
can use tempest wild shape to change into a Large air or water elemental, as per
_[elemental body III](ref/spell/elemental-body-3)_. At 12th level, a tempest tamer can use tempest
wild shape to change into a Huge air or water elemental, as per
_[elemental body IV](ref/spell/elemental-body-4)_.

A tempest tamer can use this ability once per day plus an additional time per day at 6th level and
every 2 levels thereafter (up to a total of eight times at 18th level). At 20th level, she can use
tempest wild shape at will.

This ability replaces wild shape.
