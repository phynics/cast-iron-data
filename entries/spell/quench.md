+++
id = "ref/spell/quench"
kind = "spell"
title = "Quench"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "quench", path = "json/spells8.json" },
]
[[sources]]
publication = "core-rulebook"
page = "329"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area or Target", value = "one 20-ft. cube/level (S) or one fire-based magic item" },
]
duration = "instantaneous"
saving_throw = "none or Will negates (object)"
spell_resistance = "no or yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Druid, Hunter
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: none or Will negates (object)
Spell resistance: no or yes (object)
Area or Target: one 20-ft. cube/level (S) or one fire-based magic item
:::

Quench is often used to put out forest fires and other conflagrations. It extinguishes all
nonmagical fires in its area. The spell also dispels any fire spells in its area, though you must
succeed on a dispel check (1d20 +1 per caster level, maximum +15) against each spell to dispel it.
The DC to dispel such spells is 11 + the caster level of the fire spell.

Each creature with the fire subtype within the area of a quench spell takes 1d6 points of damage per
caster level (maximum 10d6, no save allowed).

Alternatively, you can target the spell on a single magic item that creates or controls flame. The
item loses all its fire-based magical abilities for 1d4 hours unless it succeeds on a Will save.
Artifacts are immune to this effect.
