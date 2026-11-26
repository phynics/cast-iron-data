+++
id = "ref/arc-slayer/family-hunter"
kind = "archetype"
title = "Family Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Family%20Hunter"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "family_hunter", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "horror-adventures"
page = "66"

[fields]
kind = "archetype"
features = [
  { anchor = "find-family", level = 2 },
  { anchor = "kinslayer", level = 3 },
  { anchor = "studied-target", level = 5 },
  { anchor = "disrupt-teamwork", level = 6 },
]
trades = [
  { replaces = "Slayer talent gained at 2nd level", feature = "slayer-talents", levels = [2], by = ["find-family"] },
  { replaces = "Slayer talent gained at 6th level", feature = "slayer-talents", levels = [6], by = ["disrupt-teamwork"] },
  { alters = "Sneak attack", feature = "sneak-attack", by = ["kinslayer"] },
  { alters = "Studied target", feature = "studied-target", by = ["studied-target"] },
]
+++

Most slayers focus their efforts on single targets, but family hunters try to root out every branch
of a tainted tree of life.

## Find Family (Sp) {#find-family}

At 2nd level, a family hunter chooses a particular family line of mortal creatures to cleanse (she
must choose an actual family line like "The Montrose family," rather than something generic that
would cover all creatures of a given kind like "All humans descended from the first human created by
the gods"). She can target any creature from that family line with
_[discern next of kin](ref/spell/discern-next-of-kin)_ (with a caster level equal to her slayer
level) at will as a [spell-like ability](ref/umr/spell-like-abilities). The save DC is
Charisma-based and is modified by the slayer's studied target bonus if the creature is also her
studied target. A creature that successfully saves against this effect is immune to this ability for
24 hours. If the family hunter's chosen family line is completely eradicated, she can choose a new
one after 1 month of studying.

This ability replaces the slayer talent gained at 2nd level.

## Kinslayer (Su) {#kinslayer}

At 3rd level, a family hunter's sneak attack deals an additional 1d6 points of damage to any
creature with a blood relation to the family line she seeks to cleanse.

This ability alters sneak attack.

## Studied Target (Ex) {#studied-target}

At 5th level and above, a slayer can maintain more than one studied target at a time only if all
targets are closely related to one another (even if they aren't part of the family line she seeks to
cleanse). This includes blood relatives; undead spawn; constructs or undead and their creator;
summoned creatures and their summoner; creatures that are charmed, dominated, or otherwise under
direct magical control and their controller; and cohorts, followers, animal companions, familiars,
and similar associates of one master.

This ability alters studied target.

## Disrupt Teamwork (Ex) {#disrupt-teamwork}

At 6th level, a family hunter's studied target never counts as an ally to its allies for the purpose
of [flanking](ref/rule/flanking) the family hunter or using teamwork feats or the
[aid another](ref/rule/aid-another-2) action against the family hunter.

This ability replaces the slayer talent gained at 6th level.
