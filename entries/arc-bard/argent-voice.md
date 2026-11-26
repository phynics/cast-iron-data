+++
id = "ref/arc-bard/argent-voice"
kind = "archetype"
title = "Argent Voice"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Argent%20Voice"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "argent_voice", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "adventurers-guide"
page = "174"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "limning-verse", level = 1 },
  { anchor = "shattering-crescendo", level = 6 },
  { anchor = "devilbane-refrain", level = 8 },
  { anchor = "dedicated-performance", level = 2 },
]
trades = [
  { replaces = "Fascinate", feature = "bardic-performance", power = "fascinate", by = ["limning-verse"] },
  { replaces = "Suggestion", feature = "bardic-performance", power = "suggestion", by = ["shattering-crescendo"] },
  { replaces = "mass suggestion", feature = "bardic-performance", power = "mass suggestion", by = ["shattering-crescendo"] },
  { replaces = "Dirge of doom", feature = "bardic-performance", power = "dirge of doom", by = ["devilbane-refrain"] },
  { replaces = "frightening tune", feature = "bardic-performance", power = "frightening tune", by = ["devilbane-refrain"] },
  { alters = "Versatile performance", feature = "versatile-performance", by = ["dedicated-performance"] },
]
+++

As much as the [Silver Ravens](ref/rule/aff-rebels) are freedom fighters, they are also patrons of
the arts. Perhaps owing to the strong ties between the organization's leadership and the Kintargo
Opera House, the Silver Ravens are particularly active in the theater community and count many of
Cheliax's finest singers among their recruits. In part, this is mere shrewdness, as actors and
performers are often invited into the halls of the wealthy and powerful, where a rebellion can do
the most damage.

However, there is another reason for the [Silver Ravens](ref/rule/aff-rebels) to recruit singers
from the Chelish opera. The Silver Ravens rely on talented voices to deploy their most powerful
weapon in the defense of Kintargo—the "Song of Silver." While specially trained
[argent dramaturges](ref/pclass/argent-dramaturge) can create lesser versions of this song, the true
"Song of Silver" must be performed in Kintargo. Those among the Silver Ravens who dedicate
themselves to the study of this magical performance are known as argent voices, and through practice
and experience, these bards are able to modulate their own bardic performance abilities to reflect
some measure of the power found in the "Song of Silver." For this reason, argent voices are among
the most respected and treasured of the Silver Raven's agents. While some argent voices travel the
Inner Sea, fighting tyranny and oppression, many others remain in Kintargo, ready to activate the
city's defenses should the need arise.

Argent voices who wish to further explore the magic and power of the "Song of Silver" often further
focus their training so that they can become [argent dramaturges](ref/pclass/argent-dramaturge) (see
page 172).

## Bardic Performance {#bardic-performance}

An argent voice gains the following bardic performances. The argent voice must use Perform (sing)
with these performances.

## Limning Verse (Su) {#limning-verse}

At 1st level, the argent voice can sing a song that causes fiends to glow with an aura of silvery
light. Outsiders with the evil subtype within 10 feet of the argent voice are affected as per
_[faerie fire](ref/spell/faerie-fire)_. At 4th level and every 4 levels thereafter, the range of
this ability increases by 10 feet, to a maximum of 60 feet at 20th level. Any defense that prevents
the detection of alignment or evil also prevents limning verse from outlining a creature.

This replaces fascinate.

## Shattering Crescendo (Sp) {#shattering-crescendo}

At 6th level, the argent voice learns to sing at frequencies capable of shattering magical effects.
As a full-round action, an argent voice can use 2 rounds of bardic performance to attempt to dispel
a single evil spell or enchantment spell cast by an evil creature. This functions as per
_[dispel magic](ref/spell/dispel-magic)_, using the bard's level as his caster level. At 18th level,
this ability can be used on effects that can be removed by the spell
_[break enchantment](ref/spell/break-enchantment)_.

This replaces suggestion and mass suggestion.

## Devilbane Refrain (Su) {#devilbane-refrain}

At 8th level, the argent voice learns how to mimic aspects of the magical "Song of Silver" with his
performance, enhancing his allies' ability to combat devils and similar fiends. To be affected, a
creature must be able to hear the argent voice's singing and be within 30 feet of him. Natural and
manufactured weapons wielded by affected allies are treated as though they were silver for the
purpose of bypassing [damage reduction](ref/rule/damage-reduction). At 14th level, allies' natural
and manufactured weapons also gain the benefit of the _evil outsider [bane](ref/magic-enh/bane)_
weapon special ability.

This replaces dirge of doom and frightening tune.

## Dedicated Performance (Ex) {#dedicated-performance}

An argent voice can call upon the training of the Chelish opera to influence and scrutinize his
foes. At 2nd level, an argent voice must choose Perform (sing) as his versatile performance skill.
At 6th level, the argent voice gains a bonus on Perform (sing) checks made as part of a versatile
performance equal to the number of additional Perform skills in which he has the maximum number of
ranks possible at his level. This bonus increases by 1 per maximized Perform skill at 10th level and
every four levels thereafter, to a maximum of a +4 bonus per fully ranked Perform skill other than
Perform (sing) at 18th level.

This alters versatile performance.
