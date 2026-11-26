+++
id = "ref/arc-rogue/bellflower-irrigator"
kind = "archetype"
title = "Bellflower Irrigator"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Bellflower%20Irrigator"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bellflower_irrigator", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "adventurers-guide"
page = "43"

[fields]
kind = "archetype"
features = [
  { anchor = "bellflower-crop" },
  { anchor = "poison-use", level = 1 },
  { anchor = "grafting", level = 4 },
  { anchor = "irrigation", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["poison-use"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["grafting"] },
  { replaces = "rogue talent gained at 4th level", feature = "rogue-talents", levels = [4], by = ["grafting"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["irrigation"] },
]
+++

Bellflower irrigators take on tasks that many other agents of the
[Bellflower Network](ref/rule/aff-antislavery) find distasteful. Rather than focusing on saving
slaves, Bellflower irrigators seek to defeat slavery by aiming to eliminate the source. They gauge
the precise moment to strike from the shadows and annihilate slave traders and masters alike.
Bellflower irrigators realize that for every slave released today, another will be shackled
tomorrow—until all the masters are dead. This cynicism leads Bellflower irrigators to target anyone
who owns or sells slaves on Golarion, especially cruel masters within Cheliax.

Though most Bellflower irrigators are [halflings](ref/race/halfling), this branch of the Network is
more diverse than many of the others—anyone with a hatred of slavery and a talent for stealth and
martial combat is free to join. Bellflower irrigators employ combat methods that many find
questionable, such as the use of poison and calculated strikes meant to kill rather than
incapacitate. The [Bellflower Network](ref/rule/aff-antislavery) does not knowingly allow evil
members, but very few Bellflower irrigators are good—most are chaotic neutral in alignment, as their
methods of solving the problem of slavery often force them into moral and ethical gray areas. A few
Bellflower irrigators are in fact evil, but these rarities do their best to hide their personal lack
of morals and addiction to cruelty in order to maintain their positions and connection to the
Bellflowers, for as evil as they may be, they share a hatred of slavery with their more altruistic
kin. An evil Bellflower irrigator who is found out is typically exiled from the group, yet most
continue to fight slavery even after they are sent away in this way.

## Bellflower Crop (Ex) {#bellflower-crop}

As a standard action, a Bellflower irrigator can designate a number of allies equal to 3 + his
Charisma modifier as part of his Bellflower crop. Members of a Bellflower crop must remain within 30
feet of the Bellflower irrigator to gain any benefits from abilities that affect a Bellflower crop,
regardless of the ability's source (whether it's a Bellflower harvester, irrigator, or tiller). If
the allies leave this range, the Bellflower irrigator must designate them again to include them in
his crop.

## Poison Use (Ex) {#poison-use}

A Bellflower irrigator is trained in the use of poison and cannot accidentally poison himself when
applying poison to a weapon.

This ability replaces trapfinding.

## Grafting (Ex) {#grafting}

At 4th level, a Bellflower irrigator is considered to be [flanking](ref/rule/flanking) an opponent
if at least two members of his Bellflower crop are threatening that opponent, regardless of the
irrigator's actual positioning.

This ability replaces uncanny dodge and the rogue talent gained at 4th level.

## Irrigation (Ex) {#irrigation}

At 8th level, if a Bellflower irrigator studies his target for 3 rounds (spending a standard action
each round to do so) and then makes a sneak attack with a melee weapon that successfully deals
damage, the attack has the additional effect of possibly either [paralyzing](ref/rule/paralyzed) or
killing the target (Bellflower irrigator's choice). The death attack fails if the target detects the
Bellflower irrigator or recognizes him as an enemy. If the victim of the attack fails a Fortitude
save (DC = 10 + 1/2 the Bellflower irrigator's class level + the Bellflower irrigator's Intelligence
modifier) against the kill effect, she dies. If the saving throw fails against the paralysis effect,
the victim is rendered helpless and unable to act for 1d6 rounds plus 1 round per 2 rogue levels
that the Bellflower irrigator has. If the victim's saving throw succeeds, the attack is just a
normal sneak attack. Once the Bellflower irrigator has completed the 3 rounds of study, he must make
the irrigation attempt within the next 3 rounds. A Bellflower irrigator can attempt to kill or
paralyze a creature in this way once per day, plus one additional time per day for every 4
additional rogue levels he has after 8th.

This ability replaces improved uncanny dodge.
