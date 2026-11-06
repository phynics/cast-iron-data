+++
id = "ref/spell/pressure-adaptation"
kind = "spell"
title = "Pressure Adaptation"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pressure_adaptation", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (slime from a cephalopod)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Alchemist, Bloodrager, Cleric, Druid, Hunter, Investigator, Oracle, Psychic, Ranger, Shaman, Summoner, Unchained Summoner, Warpriest
Casting time: 1 standard action
Components: V, S, M (slime from a cephalopod)
Range: touch
Duration: 1 hour/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

**Sources:** Aquatic Adventures pg 61

The target adapts incredibly quickly to [changes in pressure](ref/rule/oceanic-zones), adjusting to
100 feet of new pressure (or the entire shift, in the case of an instantaneous shift within its
native range) after just one successful Fortitude saving throw instead of the usual five.
