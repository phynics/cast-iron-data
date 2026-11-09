+++
id = "ref/spell/halt-undead"
kind = "spell"
title = "Halt Undead"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "halt_undead", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "293"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of sulfur and powdered garlic)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "up to three undead creatures, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Inquisitor, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of sulfur and powdered garlic)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates (see text)
Spell resistance: yes
Targets: up to three undead creatures, no two of which can be more than 30 ft. apart
:::

This spell renders as many as three undead creatures immobile. A nonintelligent undead creature gets
no saving throw; an intelligent undead creature does. If the spell is successful, it renders the
undead creature immobile for the duration of the spell (similar to the effect of
[hold person](ref/spell/hold-person) on a living creature). The effect is broken if the halted
creatures are attacked or take damage.
