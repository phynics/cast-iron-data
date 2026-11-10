+++
id = "ref/arc-sorcerer/umbral-scion"
kind = "archetype"
title = "Umbral Scion"
aon = "ArchetypeDisplay.aspx?FixedName=Sorcerer%20Umbral%20Scion"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "umbral_scion", path = "json/archetypes_sorcerer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/sorcerer" },
]
[[sources]]
publication = "blood-of-shadows"
page = "19"

[fields]
kind = "archetype"
replaces = ["1st-level bloodline power", "7th-level bloodline feat", "13th-level bloodline feat"]
alters = ["Spellcasting"]
+++

Umbral scions are sorcerers who are able to expertly control their especially potent shadow
heritage. The majority of umbral sorcerers hail from the Darklands.

**Prerequisites:** [Shadow](ref/sorcbloodline/shadow) bloodline

**Diminished Spellcasting**

**Alters:** Spellcasting

**Info:** An umbral scion can cast one fewer spell per day of each level than normal. If this
reduces the number to 0, she can cast spells of that level only if her Charisma score grants her
[bonus spells](ref/rule/determine-bonuses) of that level.

**Shrouded Spells (Su)**

**Flavor:** An umbral scion is enveloped by wisps of shadow whenever she casts a spell.

**Passive:** The DC to identify spells cast by an umbral scion increases by 2. If the spell is being
cast within an area of [dim light](ref/rule/vision-and-light) or darkness, the DC increases by 5
instead.

**Encroaching Darkness (Su)**

**Flavor:** An umbral scion is capable of influencing light around her.

**At 14th Level:** The veil increases to 60 feet and grants any creature within it
[cover](ref/rule/cover) (even against senses normally able to penetrate total darkness, such as the
[see in darkness](ref/umr/see-in-darkness) ability).

**At 7th Level:** The veil increases to a 30-foot radius.

**At 8th Level:** The veil decreases the light level by two steps. If the light level is decreased
past darkness, the veil is treated as [deeper darkness](ref/spell/deeper-darkness).

**Replaces:** 1st-level bloodline power

**Standard:** She can produce a 10-foot-radius veil centered on a creature or object within 30 feet.
This veil decreases the [light level](ref/rule/vision-and-light) by one step and remains for a
number of rounds equal to the sorcerer's Charisma modifier.

**Usage:** Charisma3 modifier times/day

**Potent Shadows (Su)**

**Gained:** At 7th Level

**Passive:** When an umbral scion casts a spell of the
[shadow subschool](ref/spelldef/shadow-subschool) or a spell with the
[darkness](ref/spelldef/darkness) or [shadow descriptor](ref/spelldef/shadow-descriptor) within an
area of dim light or darkness, she treats her caster level as 1 higher. Only the sorcerer herself
needs to be in dim light or darkness.

**Replaces:** 7th-level bloodline feat

At 11th level: This bonus +2.

At 15th level: This bonus +3.

At 19th level: This bonus +4.

**Crippling Darkness (Su)**

**At 18th Level:** This bonus increases by 1.

**Gained:** At 13th Level

**Passive:** When an umbral scion targets a creature within an area of dim light or darkness with a
spell of the shadow subschool or a spell with the darkness or shadow descriptor, the DC for the
spell increases by 1.

**Replaces:** 13th-level bloodline feat
