+++
id = "ref/arc-barbarian/superstitious"
kind = "archetype"
title = "Superstitious"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Superstitious"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "superstitious", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "advanced-players-guide"
page = "79"

[fields]
kind = "archetype"
features = [
  { anchor = "sixth-sense", level = 3 },
  { anchor = "keen-senses", level = 7 },
]
trades = [
  { replaces = "Trap sense", feature = "trap-sense", by = ["sixth-sense"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["keen-senses"] },
]
+++

Many barbarians distrust magic. While most just shy away from magic, others focus their rage on
users of such foul arts. These barbarians are naturally distrusting, and develop keen senses to
protect them from harm. A superstitious barbarian has the following class features.

## Sixth Sense (Ex) {#sixth-sense}

At 3rd level, the superstitious barbarian gains a +1 bonus on initiative and a +1 insight bonus to
AC during surprise rounds. This bonus increases by +1 for every three levels after 3rd. This ability
replaces trap sense.

## Keen Senses (Ex) {#keen-senses}

At 7th level, the superstitious barbarian gains [low-light vision](ref/umr/low-light-vision) (triple
normal vision range in dim light if she already has [low-light vision](ref/rule/low-light-vision)).
At 10th level, she gains [darkvision](ref/umr/darkvision) 60 feet (or adds 60 feet to the range of
any [darkvision](ref/rule/darkvision) already possessed). At 13th level, she gains
[scent](ref/umr/scent). At 16th level, she gains [blindsense](ref/umr/blindsense) 30 feet. At 19th
level, she gains [blindsight](ref/umr/blindsight) 30 feet. This ability replaces
[damage reduction](ref/rule/damage-reduction).

## Rage Powers {#rage-powers}

The following rage powers complement the superstitious archetype:
[clear mind](ref/ragepower/clear-mind), [disruptive](ref/ragepower/disruptive),
[roused anger](ref/ragepower/roused-anger), [spellbreaker](ref/ragepower/spellbreaker),
[superstition](ref/ragepower/superstition), and [witch hunter](ref/ragepower/witch-hunter).
