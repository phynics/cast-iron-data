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
replaces = ["Cavalier's charge", "Expert trainer", "Banner", "Mighty charge", "Greater banner", "Supreme charge"]
alters = ["Mount"]
+++

The fell rider rides a bestial steed, a mount mastered by him alone. He tramples his enemies down,
leaving twisted bodies in his wake, and fear rides with him.

**Prerequisites:** Hobgoblin

**Brute Steed (Ex)**

**Alters:** Mount

**Passive:** A fell rider's mount is unusually large and fierce. It gains a +2 bonus to Strength,
but takes a -2 penalty to Dexterity.

**Rampage (Ex)**

**Ability:** A fell rider gains [Trample](ref/feat/trample) as a bonus feat. The fell rider receives
a +2 bonus on [overrun](ref/rule/overrun) attempts made while mounted. In addition, his mount gains
a +2 bonus on damage rolls when making hoof attacks or using the [trample](ref/umr/trample) monster
ability, even when not overrunning.

**Gained:** At 3rd Level

**Replaces:** Cavalier's charge

**Dread Rider (Ex)**

**Free:** Once per round, he can make an Intimidate check to demoralize a foe he has trampled or
charged while mounted.

**Gained:** At 4th Level

**Passive:** A fell rider gains a bonus equal to [half](ref/misc/fractions-and-rounding) his level
on Intimidate checks made while mounted.

**Replaces:** Expert trainer

**Fell Presence (Ex)**

**At 10th Level:** The penalty becomes -3.

**At 15th Level:** The penalty becomes -4.

**At 20th Level:** The penalty becomes -5.

**At 5th Level:** A fell rider inspires dread while mounted. As long as the fell rider is mounted,
all enemies within 60 feet receive a -2 penalty on savings throws against fear.

**Replaces:** Banner

**Deadly Rampage (Ex)**

**Ability:** A mounted fell rider no longer provokes attacks of opportunity when he attempts to
overrun a creature. He can make a single melee attack against the creature as a **free action** if
the overrun attempt succeeds.

**Gained:** At 11th Level

**Replaces:** Mighty charge

**Terror (Ex)**

**Gained:** At 14th Level

**Replaces:** Greater banner

**Special:** This ability is a mind-affecting fear effect.

**Standard:** A fell rider can rear up his mount, spreading terror among his enemies. Enemies within
60 feet who can see the fell rider must succeed at a Will save (DC 10 + 1/2 the fell rider's level +
the fell rider's Charisma modifier) or be [shaken](ref/misc/shaken) for 1 round per level the fell
rider possesses. Creatures with half or fewer Hit Dice than the fell rider become
[frightened](ref/misc/frightened) instead. An opponent that succeeds at the saving throw is immune
to that fell rider's terror ability for 24 hours.

**Unstoppable Rampage (Ex)**

**Ability:** A mounted fell rider can overrun up to four creatures as part of a single overrun
combat maneuver. Each attempt made against a creature after the first receives a cumulative -5
penalty (for example, the fourth overrun attempt would be at a -15 penalty). If any overrun attempt
fails, the fell rider cannot make further overrun attempts that round. Attacks made by the fell
rider or his mount as part of the overrun, such as those provided by the Trample feat or the _deadly
rampage_ ability, receive a +4 bonus to hit, and any critical threats from these attacks
automatically confirm.

**Gained:** At 20th Level

**Replaces:** Supreme charge
