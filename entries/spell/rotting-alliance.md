+++
id = "ref/spell/rotting-alliance"
kind = "spell"
title = "Rotting Alliance"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rotting_alliance", path = "json/spells8.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "61"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse", "disease"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 8 },
  { class = "Witch", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature/level, no two of which can be more than 60 feet apart" },
]
duration = "permanent"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Inquisitor, Occultist\
8: Cleric, Druid, Oracle, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: permanent
Saving throw: Fortitude negates
Spell resistance: yes
Target: one living creature/level, no two of which can be more than 60 feet apart
Descriptors: curse, disease
:::

You curse two or more creatures to sicken and waste away while in each others' company. Each target
that fails a Fortitude save becomes cursed with a wasting sickness. The disease has no onset period,
and those who contracted it must attempt a second Fortitude save immediately. A target that fails
this second saving throw takes 1d6 points of Constitution damage and 1d6 points of Charisma damage.
Every day thereafter, each target that was within 100 feet of another target during the previous 24
hours takes 1d6 points of Constitution damage and 1d6 points of Charisma damage (reroll to determine
the specific amount of damage each day). A successful Fortitude save negates the damage for that day
only.

A target cannot be healed of damage from this disease (naturally or by magic) while the target is
within 100 feet of another target. If healed of such damage while away from other targets, a target
might take damage again the day they reconvene. This disease is a curse, and can never be cured by
successful saving throws. The spell can be ended on a single target only with a successful casting
of [remove curse](ref/spell/remove-curse) followed by a successful casting of
[remove disease](ref/spell/remove-disease) while the target is within 100 feet of at least one other
target. When the curse remains on only one target, it ends automatically.
