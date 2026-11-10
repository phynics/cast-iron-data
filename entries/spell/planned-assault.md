+++
id = "ref/spell/planned-assault"
kind = "spell"
title = "Planned Assault"
aon = "SpellDisplay.aspx?ItemName=Planned%20Assault"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planned_assault", path = "json/spells7.json" },
]
[[sources]]
publication = "dwarves-of-golarion"
page = "23"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 4 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Cleric, Oracle, Paladin, Warpriest\
4: Hunter, Ranger
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level or until discharged
Saving throw: none
Spell resistance: no
Area: one creature/level, no two of which can be more than 30 ft. apart
:::

> _In order to prepare this spell, the caster must spend an hour performing a ritual in which he
> beseeches [Torag](ref/faith/torag) (or a member of his family) for the aid of
> [Angradd](ref/faith/angradd). For 24 hours after the ritual, the caster may prepare spells of the
> requested deity. The caster may only attune himself to one additional deity at a time._

This spell increases the effectiveness of a planned action. If the targets spend at least 1 minute
studying a situation, they receive bonuses to their first actions in response to the situation. All
targets must declare in advance what their intended actions are. If they perform those actions, they
receive a +2 sacred bonus to AC, saving throws, and checks for the first round. This bonus increases
to +4 at 10th level and +6 at 15th level.

For example, the PCs discover a camp of orcs; the PC cleric casts tactical assault, the group spends
1 minute analyzing the layout of the camp, and then declares its actions. As long as the PCs stick
to the plan, they gain a +2 morale bonus to AC, saving throws, and all actions for the first round.
