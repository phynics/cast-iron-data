+++
id = "ref/rule/designing-encounters"
kind = "rule"
title = "Designing Encounters"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "designing_encounters", path = "json/rules_gm01.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 397

The heart of any adventure is its encounters. An encounter is any event that puts a specific problem
before the PCs that they must solve. Most encounters present combat with monsters or hostile NPCs,
but there are many other types - a trapped corridor, a political interaction with a suspicious king,
a dangerous passage over a rickety rope bridge, an awkward argument with a friendly NPC who suspects
a PC has betrayed him, or anything that adds drama to the game. Brain-teasing puzzles, roleplaying
challenges, and skill checks are all classic methods for resolving encounters, but the most complex
encounters to build are the most common ones: combat encounters.

When designing a combat encounter, you first decide what level of challenge you want your PCs to
face, then follow the steps outlined below.

**Step 1-Determine APL:** Determine the average level of your player characters - this is their
Average Party Level (APL for short). You should round this value to the nearest whole number (this
is one of the few exceptions to the round down rule). Note that these encounter creation guidelines
assume a group of four or five PCs. If your group contains six or more players, add one to their
average level. If your group contains three or fewer players, subtract one from their average level.
For example, if your group consists of six players, two of which are 4th level and four of which are
5th level, their APL is 6th (28 total levels, divided by six players, rounding up, and adding one to
the final result).

**Step 2-Determine CR:** Challenge Rating (or CR) is a convenient number used to indicate the
relative danger presented by a monster, trap, hazard, or other encounter: the higher the CR, the
more dangerous the encounter. Refer to Table 12-1 to determine the Challenge Rating your group
should face, depending on the difficulty of the challenge you want and the group's APL.

### Table 12-1: Encounter Design

|Difficulty|Challenge Rating Equals...|
| --- | --- |
|Easy|APL -1|
|Average|APL|
|Challenging|APL +1|
|Hard|APL +2|
|Epic|APL +3|

**Step 3-Build the Encounter:** Determine the total XP award for the encounter by looking it up by
its CR on Table 12-2. This gives you an "XP budget" for the encounter. Every creature, trap, and
hazard is worth an amount of XP determined by its CR, as noted on Table 12-2.

### Table 12-2: Experience Point Awards

|CR|Total XP|1-3|4-5|6+|
| --- | --- | --- | --- | --- |
|1/8|50|15|15|10|
|1/6|65|20|15|10|
|1/4|100|35|25|15|
|1/3|135|45|35|25|
|1/2|200|65|50|35|
|1|400|135|100|65|
|2|600|200|150|100|
|3|800|265|200|135|
|4|1,200|400|300|200|
|5|1,600|535|400|265|
|6|2,400|800|600|400|
|7|3,200|1,070|800|535|
|8|4,800|1,600|1,200|800|
|9|6,400|2,130|1,600|1,070|
|10|9,600|3,200|2,400|1,600|
|11|12,800|4,270|3,200|2,130|
|12|19,200|6,400|4,800|3,200|
|13|25,600|8,530|6,400|4,270|
|14|38,400|12,800|9,600|6,400|
|15|51,200|17,100|12,800|8,530|
|16|76,800|25,600|19,200|12,800|
|17|102,400|34,100|25,600|17,100|
|18|153,600|51,200|38,400|25,600|
|19|204,800|68,300|51,200|34,100|
|20|307,200|102,000|76,800|51,200|
|21|409,600|137,000|102,400|68,300|
|22|614,400|205,000|153,600|102,400|
|23|819,200|273,000|204,800|137,000|
|24|1,228,800|410,000|307,200|204,800|
|25|1,638,400|546,000|409,600|273,000|

> _The last three columns are for Individual XP._

To build your encounter, simply add creatures, traps, and hazards whose combined XP does not exceed
the total XP budget for your encounter. It's easiest to add the highest CR challenges to the
encounter first, filling out the remaining total with lesser challenges.

For example, let's say you want your group of six 8th-level PCs to face a challenging encounter
against a group of gargoyles (each CR 4) and their stone giant boss (CR 8). The PCs have an APL of
9, and table 12-1 tells you that a challenging encounter for your APL 9 group is a CR 10 encounter -
worth 9,600 XP according to Table 12-2. At CR 8, the stone giant is worth 4,800 XP, leaving you with
another 4,800 points in your XP budget for the gargoyles. Gargoyles are CR 4 each, and thus worth
1,200 XP apiece, meaning that the encounter can support four gargoyles in its XP budget. You could
further refine the encounter by including only three gargoyles, leaving you with 1,200 XP to spend
on a trio of Small earth elemental servants (at CR 1, each is worth 400 XP) to further aid the stone
giant.

**Adding NPCs:** Creatures whose Hit Dice are solely a factor of their class levels and not a
feature of their race are factored into combats a little differently than normal monsters or
monsters with class levels. A creature that possesses class levels, but does not have any racial Hit
Dice, is factored in as a creature with a CR equal to its class levels -1. A creature that only
possesses non-player class levels ([Adept](ref/npcclass/adept),
[Aristocrat](ref/npcclass/aristocrat), [Commoner](ref/npcclass/commoner),
[Expert](ref/npcclass/expert), or [Warrior](ref/npcclass/warrior)) is factored in as a creature with
a CR equal to its class levels -2. If this reduction would reduce a creature's CR to below 1, its CR
drops one step on the following progression for each step below 1 this reduction would make: 1/2,
1/3, 1/4, 1/6, 1/8.

**High CR Encounters:** The XP values for high-CR encounters can seem quite daunting. Table 12-3
provides some simple formulas to help you manage these large numbers. When using a large number of
identical creatures, this chart can help simplify the math by combining them into one CR, making it
easier to find their total XP value. For example, using this chart, four CR 8 creatures (worth 4,800
XP each) are equivalent to a CR 12 creature (worth 19,200 XP).

### Table 12-3: High CR Equivalencies

|Number of Creatures|Equal to...|
| --- | --- |
|1 Creature|CR|
|2 Creatures|CR +2|
|3 Creatures|CR +3|
|4 Creatures|CR +4|
|6 Creatures|CR +5|
|8 Creatures|CR +6|
|12 Creatures|CR +7|
|16 Creatures|CR +8|

**Ad Hoc CR Adjustments:** While you can adjust a specific monster's CR by
[advancing](ref/template/advanced) it, applying templates, or giving it class levels, you can also
adjust an encounter's difficulty by applying ad hoc adjustments to the encounter or creature itself.
Listed here are three additional ways you can alter an encounter's difficulty.

**Favorable Terrain for the PCs:** An encounter against a monster that's out of its favored element
(like a yeti encountered in a sweltering cave with lava, or an enormous dragon encountered in a tiny
room) gives the PCs an advantage. Build the encounter as normal, but when you award experience for
the encounter, do so as if the encounter were one CR lower than its actual CR.

**Unfavorable Terrain for the PCs:** Monsters are designed with the assumption that they are
encountered in their favored terrain - encountering a water-breathing aboleth in an underwater area
does not increase the CR for that encounter, even though none of the PCs breathe water. If, on the
other hand, the terrain impacts the encounter significantly (such as an encounter against a creature
with [blindsight](ref/rule/blindsight-and-blindsense) in an area that suppresses all light), you
can, at your option, increase the effective XP award as if the encounter's CR were one higher.

**NPC Gear Adjustments:** You can significantly increase or decrease the power level of an NPC with
class levels by adjusting the NPC's gear. The combined value of an NPC's gear is given in on
[Table 14-9](ref/rule/step-6-gear). A classed NPC encountered with no gear should have his CR
reduced by 1 (provided that loss of gear actually hampers the NPC), while a classed NPC that instead
has gear equivalent to that of a PC (as listed on [Table 12-4](ref/rule/placing-treasure)) has a CR
of 1 higher than his actual CR. Be careful awarding NPCs this extra gear, though - especially at
high levels, where you can blow out your entire adventure's treasure budget in one fell swoop!
