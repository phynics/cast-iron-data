+++
id = "ref/spell/true-form"
kind = "spell"
title = "True Form"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "true_form", path = "json/spells10.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "251"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "up to one creature/3 levels, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Arcanist, Druid, Hunter, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: up to one creature/3 levels, no two of which can be more than 30 ft. apart
:::

True form removes any polymorph effect from a target creature, returning it to its true form, even
against its will. Against creatures affected by polymorph spell effects (such as baleful polymorph
or giant form), you must make a caster level check (1d20 + caster level, maximum +15) against a DC
of 11 + caster level of the effect. Success means that the polymorph effect immediately ends.

A creature with the supernatural ability to change shape (such as a lycanthrope) must make a Will
saving throw or immediately revert to its true form. If it fails this first saving throw, the
creature can attempt another Will saving throw to overcome the spell as a full-round action that
does not provoke attacks of opportunity. If this save succeeds, the spell ends and the creature is
capable of changing shape once again. If the second save fails, the creature is locked in its true
form for the duration of the spell, preventing any further polymorph effects from changing its
shape.
