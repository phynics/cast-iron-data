+++
id = "ref/spell/watchful-eye"
kind = "spell"
title = "Watchful Eye"
aon = "SpellDisplay.aspx?ItemName=Watchful%20Eye"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "watchful_eye", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/shield-other" },
]
[[sources]]
publication = "dwarves-of-golarion"
page = "23"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F (a pair of silver or gold rings worth 10 gp, worn by both you and the target)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, F (a pair of silver or gold rings worth 10 gp, worn by both you and the target)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
:::

> _In order to prepare this spell, the caster must spend an hour performing a ritual in which he
> beseeches [Torag](ref/faith/torag) (or a member of his family) for the aid of
> [Folgrit](ref/faith/folgrit). For 24 hours after the ritual, the caster may prepare spells of the
> requested deity. The caster may only attune himself to one additional deity at a time._

This spell emulates Folgrit's motherly protection. It functions as
[shield other](ref/spell/shield-other), except as noted above, and you must maintain line of effect
to the target.
