+++
id = "ref/arc-investigator/infiltrator"
kind = "archetype"
title = "Infiltrator"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infiltrator", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "advanced-class-guide"
page = "100"

[fields]
kind = "archetype"
replaces = ["Trapfinding", "Poison lore", "Poison resistance"]
+++

An infiltrator specializes in investigating or disrupting groups from within. He uses his
specialized set of skills and alchemical abilities to morph into the shape of the people or
creatures whose company he's infiltrating, or even specific individuals.

**Master of Disguise (Ex)**

**Flavor:** An infiltrator can use disguise with great results.

**Gained:** At 1st Level

**Passive:** When [disguising](ref/skill/disguise) himself as a different gender, race, age
category, or size category, an infiltrator reduces the penalties for each by -2. For example, if the
infiltrator disguises himself as a female two age categories older than himself, he would take a -2
to the check instead of a -6. Also, an infiltrator can disguise himself with 1d3 minutes of work
(instead of the normal 1d3 &times& 10 minutes of work).

**Replaces:** Trapfinding

**Voice Mimicry (Ex)**

**Action:** Ability

**At 8th Level:** The infiltrator gains the effects of its _master of disguise_ class feature on
this special use of the Disguise skill (no penalty for a voice of a different gender, race, or age
category, and only a -3 penalty for a different size category).

**Gained:** At 2nd Level

**Replaces:** Poison lore

An infiltrator learns to mimic voices and sounds around him. Using this ability requires a special
Disguise check, and creatures hearing the voice can make a Perception check to discover the ruse. An
infiltrator can attempt to emulate any creature or other sound he's heard clearly for at least 1
minute. The bonuses or penalties to this special Disguise check are modified in the following ways,
all of which are cumulative.

|Disguised Voice|Check Modifier|
| --- | --- |
|Voice is not your own, but not that of a distinct individual|+5|
|Voice is that of a different gender|-2|
|Voice is that of a different race|-2|
|Voice is that of a different age category|-2|
|Voice is that of a different size category|-5|

Also, the creature making the Perception check gains a bonus based on its familiarity with specific
voices, just as if it were confronted with a normal disguise. This ability is a language-dependent
effect, meaning that if a creature cannot hear or understand what the infiltrator is saying, the
ruse fails. Magic items, feats, and traits that affect typical disguises do not affect this disguise
check.

**Mimic Mastery (Su)**

**Ability:** When an infiltrator uses [disguise self](ref/spell/disguise-self) or any polymorph
extracts on himself, he is treated as 2 investigator levels higher for the purpose of determining
the duration of that extract's effect. He can use these extracts to take the appearance of specific
individuals of the type of form he chooses, gaining a +10 to Disguise checks even if that extract
does not typically grant such a bonus. Furthermore, these extracts grant the infiltrator a +10 bonus
to Disguise checks made as part of his _voice mimicry_ ability.

**Gained:** At 2nd Level

**Replaces:** Poison resistance
