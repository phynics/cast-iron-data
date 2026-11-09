+++
id = "ref/spell/tactical-formation"
kind = "spell"
title = "Tactical Formation"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tactical_formation", path = "json/spells10.json" },
]
[[sources]]
publication = "dwarves-of-golarion"
page = "23"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 4 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "up to one creature/level, no two of which may be more than 30 ft. apart" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Cleric, Oracle, Paladin, Warpriest\
4: Hunter, Ranger
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: up to one creature/level, no two of which may be more than 30 ft. apart
:::

> _In order to prepare this spell, the caster must spend an hour performing a ritual in which he
> beseeches [Torag](ref/faith/torag) (or a member of his family) for the aid of Torag. For 24 hours
> after the ritual, the caster may prepare spells of the requested deity. The caster may only attune
> himself to one additional deity at a time._

This spell increases the effectiveness of a group's formation in battle. When cast, all creatures
under the effect of the spell must be adjacent to one another, forming an unbroken chain of squares
(which may include creatures sharing the same square). This chain does not need to be a straight
line. Each target in the chain receives a +2 deflection bonus to AC as long as the targets stay
adjacent to at least one other creature affected by the spell; moving more than 5 feet from another
target ends the spell with respect to that creature only. For example, a cleric could cast it on
himself and four dwarves blocking a 20-foot-wide corridor; the cleric can move freely from the left
side of the formation to the right side (whether in front of or behind the other targets) and not
break the spell as long as he stays within 5 feet of at least one of them.
