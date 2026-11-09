+++
id = "ref/spell/bestow-grace-of-the-champion"
kind = "spell"
title = "Bestow Grace of the Champion"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bestow_grace_of_the_champion", path = "json/spells12.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "208"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["good", "lawful"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Paladin", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "lawful good creature touched" },
]
duration = "1 round/level (see text)"
saving_throw = "yes (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Paladin\
7: Cleric, Oracle
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level (see text)
Saving throw: yes (harmless)
Spell resistance: yes
Target: lawful good creature touched
Descriptors: good, lawful
:::

You channel the power of good and law into the target, temporarily giving it powers similar to those
of a paladin. The target gains the ability to use [detect evil](ref/spell/detect-evil) at will as a
[spell-like ability](ref/umr/spell-like-abilities), immunity to disease (suppressing any diseases
currently affecting it), and immunity to fear (ending any fear effects currently affecting it); can
lay on hands (on itself only) once as a paladin of 1/2 your caster level; and can smite evil once as
a paladin of 1/2 your caster level. It adds its Charisma bonus to all its saving throws. It can use
[spell completion](ref/misc/spell-completion), [spell trigger](ref/misc/spell-trigger), or other
magic items that require the ability to cast spells as a paladin. Any abilities not used by the time
the spell expires are lost. This spell has no effect if cast on a paladin.
