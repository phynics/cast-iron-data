+++
id = "ref/spell/destruction"
kind = "spell"
title = "Destruction"
aon = "SpellDisplay.aspx?ItemName=Destruction"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "destruction", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "266"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death"]
levels = [
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 8 },
  { class = "Witch", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, F (holy or unholy symbol costing 500 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 7: Cleric, Oracle\
8: Shaman, Witch
Casting time: 1 standard action
Components: V, S, F (holy or unholy symbol costing 500 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: one creature
Descriptors: death
:::

This spell instantly delivers 10 points of damage per caster level. If the spell slays the target,
it consumes the remains utterly in holy (or unholy) fire (but not its equipment or possessions). If
the target's Fortitude saving throw succeeds, it instead takes 10d6 points of damage. The only way
to restore life to a character who has failed to save against this spell (and was slain) is to use
[true resurrection](ref/spell/true-resurrection), a carefully worded [wish](ref/spell/wish) spell
followed by [resurrection](ref/spell/resurrection), or [miracle](ref/spell/miracle).
