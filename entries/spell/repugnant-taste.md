+++
id = "ref/spell/repugnant-taste"
kind = "spell"
title = "Repugnant Taste"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "repugnant_taste", path = "json/spells8.json" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "30"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (mustard seed)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Bard, Hunter, Investigator, Mesmerist, Ranger, Skald\
4: Druid, Shaman, Witch
Casting time: 1 standard action
Components: V, S, M/DF (mustard seed)
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Descriptors: poison
:::

The target creature begins sweating a foul liquid that makes it repugnant to most living creatures.
When a creature deals damage to the affected creature with a bite attack or the swallow whole
ability, it must succeed at a Fortitude saving throw or become nauseated until the end of its next
turn. After a creature has become nauseated by this spell, each subsequent failed saving throw
against the spell instead gives it the sickened condition until the end of its next turn.
