+++
id = "ref/arc-investigator/forensic-physician"
kind = "archetype"
title = "Forensic Physician"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Forensic%20Physician"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "forensic_physician", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "33"

[fields]
kind = "archetype"
replaces = ["Trapfinding", "Trap sense", "investigator talent gained at 3rd level", "Investigator talent gained at 5th level"]
alters = ["Inspiration"]
+++

A forensic physician specializes in analyzing medical details in order to solve crimes and uncover
evidence. Whether it is a disease, blood work, a poison, or bones, the forensic physician's medical
expertise allows him great insight into his cases, much to the chagrin of criminals who seek to
cover up the nature of their crimes, even those with magical methods at their disposal.

**Medical Expertise (Ex)**

**Ability:** A forensic physician can use _inspiration_ on any [Heal](ref/skill/heal) checks without
expending a use, if he is trained in the skill, but not on any [Linguistics](ref/skill/linguistics)
check. If he later takes the [expanded inspiration](ref/invtalent/expanded-inspiration) investigator
talent, he can use _inspiration_ on Linguistics checks without expending a use, if he is trained in
the skill.

**Alters:** Inspiration

**Gained:** At 1st Level

**Passive:** A forensic physician adds half his investigator level (minimum 1) on Heal checks. This
bonus doubles on Heal checks to notice tampering with medical evidence, such as those used to defeat
[dress corpse](ref/spell/dress-corpse).

**Replaces:** Trapfinding

**Disease Lore (Ex)**

**Ability:** A forensic physician can use [Heal](ref/skill/heal) to identify a disease after only 1
minute of examining the symptoms (DC = the disease's saving throw DC), and he can spend 1 minute and
attempt a Heal check at the same DC to disinfect an infected object or corpse.

**Gained:** At 3rd Level

**Passive:** He receives a +2 bonus on saving throws against diseases.

**Replaces:** Trap sense, investigator talent gained at 3rd level

At 6th level: This bonus +4.

At 9th level: This bonus +6.

At 12th level: This bonus +8.

At 15th level: This bonus +10.

At 18th level: This bonus +12.

**Blood Lore (Ex)**

**Action:** Ability

**Gained:** At 5th Level

**Replaces:** Investigator talent gained at 5th level

A forensic physician can study a sample of blood and learn about its origins by attempting a Heal
check with a DC of 20 for a creature very familiar to the forensic physician (generally common PC
races for a PC forensic physician), 25 if the creature is somewhat familiar to the forensic
physician (typically a commonly known monster, but not the subject of many investigations), and 30
or more for rarer creatures. This allows the forensic physician to identify the race of creature
that spilled the blood, and the creature's age and gender (if any).

If the forensic physician succeeds at the Heal check but might not have heard of the creature's race
before, he can attempt an automatic Knowledge check to see if he knows about the creature. If he
succeeds, he identifies the blood (and gains all other benefits of the Knowledge check); otherwise,
he knows that he succeeded at the Heal check but the blood is not from a creature he recognizes. If
the blood is in its original setting, and the forensic physician exceeds the DC by 5 or more, he can
study the blood to determine a rough estimate of when the blood was shed, and he can study the
bloodstain patterns to get an approximate idea of how the creatures involved were positioned and
moving.
