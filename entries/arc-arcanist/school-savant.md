+++
id = "ref/arc-arcanist/school-savant"
kind = "archetype"
title = "School Savant"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "school_savant", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "advanced-class-guide"
page = "78"

[fields]
kind = "archetype"
replaces = ["The arcanist exploits gained at 1st, 3rd, and 7th levels"]
+++

Some arcanists specialize in a school of magic and trade flexibility for focus. School savants are
able to prepare more spells per day than typical arcanists, but their selection is more limited.

**School Focus (Su)**

**Action:** Ability

**Gained:** At 1st Level

**Replaces:** The arcanist exploits gained at 1st, 3rd, and 7th levels

A school savant chooses [a school of magic](ref/ability/arcane-schools). The arcanist gains the
abilities granted by that school, as the arcane school class feature of the
[wizard](ref/class/wizard), treating her arcanist level as her wizard level for these abilities. She
can also further specialize by selecting a subschool. In addition, the arcanist can prepare one
additional spell per day of each level she can cast, but this spell must be chosen from the selected
school.

Finally, the arcanist must select two additional schools of magic as her opposition schools.
Whenever she prepares spells from one of her opposition schools, the spell takes up two of her
prepared spell slots. In addition, a school savant takes a -4 penalty on any skill checks when
crafting a magic item that has a spell from one of her opposition schools as a prerequisite. A
school savant cannot select the [school understanding](ref/exploit/school-understanding) arcanist
exploit.
