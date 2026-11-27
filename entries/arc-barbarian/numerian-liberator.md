+++
id = "ref/arc-barbarian/numerian-liberator"
kind = "archetype"
title = "Numerian Liberator"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Numerian%20Liberator"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "numerian_liberator", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "people-of-the-river"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skill" },
  { anchor = "hard-hitter", level = 2 },
  { anchor = "disruptor", level = 5 },
  { anchor = "hide-from-constructs", level = 14 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["hard-hitter"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["disruptor"] },
  { replaces = "Indomitable will", feature = "indomitable-will", by = ["hide-from-constructs"] },
]
+++

The Kellid barbarians that roam Numeria's badlands have a healthy mistrust of technology and its
corruptive influence. Since the cataclysmic Rain of Stars millennia ago, these warriors have
developed numerous techniques and skills to protect themselves from the strange mechanical monsters
that roam Numeria. While many native Kellids oppose the Technic League and its espousal of foul
alien artifacts, the most stalwart and staunchly dedicated of these technophobic traditionalists
refer to themselves as Numerian liberators.

## Class Skill {#class-skill}

A Numerian liberator gains Stealth as a class skill and removes Climb from her list of barbarian
class skills.

## Hard Hitter (Ex) {#hard-hitter}

At 2nd level, a Numerian liberator can make devastating attacks against objects and foes with
breakable components. Damage dealt by the barbarian's attacks ignores an amount of an object's or
creature's [hardness](ref/umr/hardness) (if any) equal to 1/2 her class level. This ability replaces
the uncanny dodge.

## Disruptor {#disruptor}

At 5th level, for any foes in a Numerian liberator's threatened area, the DC to cast spells
defensively increases by 1. The DC increases by 1 again for every 5 levels thereafter (to a maximum
increase of 4 at 20th level). If the barbarian gains the [disruptive](ref/ragepower/disruptive) rage
power, the two abilities stack. This ability replaces improved uncanny dodge.

## Hide from Constructs (Su) {#hide-from-constructs}

At 14th level, a Numerian liberator can control her movement, breathing, body temperature, and other
physiological signs to confuse the artificial visions of constructs. At will, the barbarian can make
herself undetectable to constructs as if she were affected by a
[hide from undead](ref/spell/hide-from-undead) spell that instead hides the subject from constructs.
Intelligent constructs receive a Will save (DC 10 + 1/2 the barbarian's level + the barbarian's
Constitution modifier) to see through this effect. The barbarian must expend 1 round of rage for
each round she uses this ability. This ability replaces indomitable will.

## Rage Powers {#rage-powers}

The following rage powers complement the Numerian liberator archetype (rage powers marked with an
asterisk \[\*\] are detailed in this section): [deadly accuracy](ref/ragepower/deadly-accuracy),
[energy absorption (fire)](ref/ragepower/energy-absorption),
[energy resistance (fire)](ref/ragepower/energy-resistance),
[greater energy resistance (fire)](ref/ragepower/greater-energy-resistance),
[gearbreaker](ref/ragepower/gearbreaker)\*, [guarded stance](ref/ragepower/guarded-stance),
[lethal accuracy](ref/ragepower/lethal-accuracy),
[low-light vision](ref/ragepower/low-light-vision), [night vision](ref/ragepower/night-vision),
[rolling dodge](ref/ragepower/rolling-dodge), [reflexive dodge](ref/ragepower/reflexive-dodge),
[surprise accuracy](ref/ragepower/surprise-accuracy).
