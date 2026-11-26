+++
id = "ref/arc-cavalier/fell-rider"
kind = "archetype"
title = "Fell Rider"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Fell%20Rider"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fell_rider", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "advanced-race-guide"
page = "122"

[fields]
kind = "archetype"
features = [
  { anchor = "brute-steed", level = 1 },
  { anchor = "rampage", level = 3 },
  { anchor = "dread-rider", level = 4 },
  { anchor = "fell-presence", level = 5 },
  { anchor = "deadly-rampage", level = 11 },
  { anchor = "terror", level = 14 },
  { anchor = "unstoppable-rampage", level = 20 },
]
trades = [
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["rampage"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["dread-rider"] },
  { replaces = "Banner", feature = "banner", by = ["fell-presence"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["deadly-rampage"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["terror"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["unstoppable-rampage"] },
  { alters = "Mount", feature = "mount", by = ["brute-steed"] },
]
+++

The fell rider rides a bestial steed, a mount mastered by him alone. He tramples his enemies down,
leaving twisted bodies in his wake, and fear rides with him.

## Brute Steed (Ex) {#brute-steed}

A fell rider's mount is unusually large and fierce. It gains a +2 bonus to Strength, but takes a -2
penalty to Dexterity. This otherwise works like the cavalier's mount ability and alters that
ability.

## Rampage (Ex) {#rampage}

At 3rd level, a fell rider gains [Trample](ref/feat/trample) as a bonus feat. The fell rider
receives a +2 bonus on [overrun](ref/rule/overrun) attempts made while mounted. In addition, his
mount gains a +2 bonus on damage rolls when making hoof attacks or using the
[trample](ref/umr/trample) monster ability, even when not overrunning. This ability replaces
cavalier's charge.

## Dread Rider (Ex) {#dread-rider}

At 4th level, a fell rider gains a bonus equal to 1/2 his level on Intimidate checks made while
mounted. Once per round as a free action, he can make an Intimidate check to demoralize a foe he has
trampled or charged while mounted. This ability replaces expert trainer.

## Fell Presence (Ex) {#fell-presence}

At 5th level, a fell rider inspires dread while mounted. As long as the fell rider is mounted, all
enemies within 60 feet receive a -2 penalty on savings throws against fear. At 10th level and every
5 levels thereafter, this penalty increases by -1. This ability replaces banner.

## Deadly Rampage (Ex) {#deadly-rampage}

At 11th level, a mounted fell rider no longer provokes attacks of opportunity when he attempts to
overrun a creature. He can make a single melee attack against the creature as a free action if the
overrun attempt succeeds. This ability replaces mighty charge.

## Terror (Ex) {#terror}

At 14th level, a fell rider can rear up his mount as a standard action, spreading terror among his
enemies. Enemies within 60 feet who can see the fell rider must succeed at a Will save (DC 10 + 1/2
the fell rider's level + the fell rider's Charisma modifier) or be [shaken](ref/misc/shaken) for 1
round per level the fell rider possesses. Creatures with [half](ref/misc/fractions-and-rounding) or
fewer Hit Dice than the fell rider become [frightened](ref/misc/frightened) instead. An opponent
that succeeds at the saving throw is immune to that fell rider's terror ability for 24 hours. This
ability is a mind-affecting fear effect, and replaces greater banner.

## Unstoppable Rampage (Ex) {#unstoppable-rampage}

At 20th level, a mounted fell rider can overrun up to four creatures as part of a single overrun
combat maneuver. Each attempt made against a creature after the first receives a cumulative -5
penalty (for example, the fourth overrun attempt would be at a -15 penalty). If any overrun attempt
fails, the fell rider cannot make further overrun attempts that round. Attacks made by the fell
rider or his mount as part of the overrun, such as those provided by the Trample feat or the deadly
rampage ability, receive a +4 bonus to hit, and any critical threats from these attacks
automatically confirm. This ability replaces supreme charge.
