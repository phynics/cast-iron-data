+++
id = "ref/arc-inquisitor/spellbreaker"
kind = "archetype"
title = "Spellbreaker"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Spellbreaker"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellbreaker", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-combat"
page = "52"

[fields]
kind = "archetype"
replaces = ["Monster lore", "Teamwork feats", "Solo tactics", "True judgment"]
replaces_features = ["monster-lore", "solo-tactics", "true-judgment"]
+++

The world is full of dangerous magic, and many recoil in the face of such power. The spellbreaker,
by contrast, learns to recognize and resist certain types of magic, wading through waves of magic to
reach her foes.

**Strong-Willed (Ex)**

**Flavor:** A spellbreaker is able to stand strong against magical effects that seek to control,
compel, or persuade her.

**Gained:** At 1st Level

**Passive:** The spellbreaker rolls twice and takes the best result when making a Will saving throw
against a mind-affecting effect.

**Replaces:** Monster lore

**Defense against Magic (Ex)**

**Gained:** At 3rd Level

**Passive:** A spellbreaker picks a single [wizard school](ref/ability/arcane-schools). She gains a
+1 bonus on saving throws against arcane spells of that school.

**Replaces:** Teamwork feats

**Special:** Each time the spellbreaker picks a new school, the bonuses for the schools she has
already chosen increase by 1.

At 7th level: The spellbreaker picks a 2nd school and gains this bonus against arcane spells of that
school.

At 11th level: The spellbreaker picks a 3rd school and gains this bonus against arcane spells of
that school.

At 15th level: The spellbreaker picks a 4th school and gains this bonus against arcane spells of
that school.

At 19th level: The spellbreaker picks a 5th school and gains this bonus against arcane spells of
that school.

**Foil Casting (Su)**

**Ability:** Furthermore, the spellbreaker knows where to hit foes to foil casting from a distance.
Each time she hits an arcane spellcaster or a creature that uses
[spell-like abilities](ref/umr/spell-like-abilities) with a ranged weapon attack, the DC of any
[concentration](ref/rule/concentration) checks the caster makes increases by 2 for 1 round.

**Gained:** At 3rd Level

**Passive:** When an opponent tries to cast an arcane spell within a spellbreaker's threatened area,
the DC for that caster to cast defensively increases by 2. This increase stacks with the effects of
the [Disruptive](ref/feat/disruptive) feat.

**Replaces:** Solo tactics

**Impervious (Ex)**

**Gained:** At 20th Level

**Passive:** A spellbreaker becomes immune to the effects of a single school of arcane magic. That
school of magic must be the first one she picked for _defense against magic_ (see above). Neither
harmful nor helpful arcane spells of that school have an effect on the spellbreaker. If a spell of
that school is an area of effect spell, the spell goes off as normal, but the spellbreaker is
untouched by its effects.

**Replaces:** True judgment

**Swift:** Once per day, the spellbreaker can grant this imperviousness to all allies in a 60-foot
[burst](ref/misc/burst) for 1 minute.
