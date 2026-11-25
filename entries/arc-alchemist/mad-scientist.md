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
features = [
  { anchor = "mad-genius", level = 2 },
  { anchor = "mad-mutagen", level = 4 },
]
trades = [
  { replaces = "Discovery gained at 2nd level", feature = "discovery", levels = [2], by = ["mad-genius"] },
  { replaces = "Discovery gained at 4th level", feature = "discovery", levels = [4], by = ["mad-mutagen"] },
  { alters = "Alchemy", feature = "alchemy", by = ["mad-genius"] },
  { alters = "The alchemist's mutagen", feature = "mutagen", by = ["mad-mutagen"] },
]
+++

The mad scientist's colleagues laughed at her insights, mocked her theories, and hounded her from
the halls of academia, simply because they were too weak and frightened to understand her work. They
thought she was finished. They were wrong.

## Mad Genius (Su) {#mad-genius}

At 2nd level, a mad scientist can deal 1d3 points of [Wisdom damage](ref/rule/ability-damage-drain)
to herself (or 1d6 points of sanity damage if employing the [sanity rules](ref/rule/sanity) found on
page 12) to create a genius extract as one of her daily 1st-, 2nd-, 3rd-, 4th-, or 5th-level
extracts. This otherwise takes the same amount of time and effort as creating a normal extract of
its level, but instead of her choosing a formula she knows for it to grant, a genius extract has an
unpredictable result. When the alchemist (or an ally, if she has the
[infusion](ref/discovery/infusion) discovery) drinks the extract, it produces a random effect from
the list of alchemist formulae on page 32 of the _Advanced Player's Guide_ of 1 spell level higher
than the extract's spell level. For instance, if she creates a genius extract using a 2nd-level
extract, it would produce the effect of a random 3rd-level alchemist formula. There is no way to
predict which effect a genius extract will produce before drinking it. A genius extract's minimum
caster level is equal to the minimum caster level of the extract used, not the effect produced. So,
for instance, a genius extract that produced a _[fox's cunning](ref/spell/foxs-cunning)_ effect
would have a minimum caster level of 1 (for the 1st-level extract used) rather than 4 (for the
2nd-level effect). There are 29 potential 2nd-level extracts, 23 potential 3rd-level extracts, 18
potential 4th-level extracts, 15 potential 5th-level extracts, and 15 potential 6th-level extracts.

This ability alters alchemy and replaces the discovery gained at 2nd level.

## Mad Mutagen (Su) {#mad-mutagen}

At 4th level, a mad scientist can brew a mad mutagen in place of a normal mutagen. If she does so,
she need not make any decisions about the mutagen (including whether to make it a
[cognatogen](ref/discovery/cognatogen) or another variant mutagen if she has the appropriate
discoveries) when she brews it.

When the mad scientist drinks her mad mutagen, she makes those decisions on the fly, but she also
takes 1d4 points of Wisdom damage (or 1d8 points of sanity damage if using the sanity rules on page
12). If anyone else, even another alchemist, drinks a mad mutagen, that person must succeed at a
Will save (with the same DC as for the Fortitude save against nausea) or she becomes
[confused](ref/misc/confused) for 1 hour.

This ability alters the alchemist's mutagen and replaces the discovery gained at 4th level.
