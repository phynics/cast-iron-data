+++
id = "ref/arc-alchemist/mad-scientist"
kind = "archetype"
title = "Mad Scientist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Mad%20Scientist"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mad_scientist", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "horror-adventures"
page = "45"

[fields]
kind = "archetype"
replaces = ["2nd-level discovery", "4th-level discovery"]
alters = ["Alchemy", "Mutagen"]
+++

The mad scientist's colleagues laughed at her insights, mocked her theories, and hounded her from
the halls of academia, simply because they were too weak and frightened to understand her work. They
thought she was finished. They were wrong.

**Mad Genius (Su)**

**Ability:** A mad scientist can deal 1d3 points of [Wisdom damage](ref/rule/ability-damage-drain)
to herself (or 1d6 points of sanity damage if employing the [sanity rules](ref/rule/sanity)) to
create a genius extract as one of her daily 1st-, 2nd-, 3rd-, 4th-, or 5th-level extracts. This
otherwise takes the same amount of time and effort as creating a normal extract of its level, but
instead of her choosing a formula she knows for it to grant, a genius extract has an unpredictable
result. When the alchemist (or an ally, if she has the [infusion](ref/discovery/infusion) discovery)
drinks the extract, it produces a random effect from the list of alchemist formulae of 1 spell level
higher than the extract's spell level. For instance, if she creates a genius extract using a
2nd-level extract, it would produce the effect of a random 3rd-level alchemist formula.

**Alters:** Alchemy

**Gained:** At 2nd Level

**Passive:** There is no way to predict which effect a genius extract will produce before drinking
it. A genius extract's minimum caster level is equal to the minimum caster level of the extract
used, not the effect produced. So, for instance, a genius extract that produced a
[fox's cunning](ref/spell/foxs-cunning) effect would have a minimum caster level of 1 (for the
1st-level extract used) rather than 4 (for the 2nd-level effect).

**Replaces:** 2nd-level discovery

**Special:** There are 111 potential 2nd-level extracts, 89 potential 3rd-level extracts, 63
potential 4th-level extracts, 39 potential 5th-level extracts, and 33 potential 6th-level extracts.

**Mad Mutagen (Su)**

**Ability:** A mad scientist can brew a mad mutagen in place of a normal mutagen. If she does so,
she need not make any decisions about the mutagen (including whether to make it a
[cognatogen](ref/discovery/cognatogen) or another variant mutagen if she has the appropriate
discoveries) when she brews it. When the mad scientist drinks her mad mutagen, she makes those
decisions on the fly, but she also takes 1d4 points of Wisdom damage (or 1d8 points of sanity damage
if using the sanity rules). If anyone else, even another alchemist, drinks a mad mutagen, that
person must succeed at a Will save (with the same DC as for the Fortitude save against nausea) or
she becomes [confused](ref/misc/confused) for 1 hour.

**Alters:** Mutagen

**Gained:** At 4th Level

**Replaces:** 4th-level discovery
