+++
id = "ref/spell/reinvigorating-wind"
kind = "spell"
title = "Reinvigorating Wind"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reinvigorating_wind", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["air", "mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a flower petal)"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Shaman, Skald\
3: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S, M/DF (a flower petal)
Range: 30 ft.
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: cone-shaped burst
Subschool: Compulsion
Descriptors: air, mind-affecting
:::

**Sources:** Villain Codex pg 177

You exhale deeply, creating a gentle magical wind that invigorates any allies in the affected area,
as follows. Any sleeping allies immediately wake up. Fascinated allies are shaken free of the
fascinate effect. Flat-footed allies no longer count as flat-footed even if they have not acted yet.
The duration of effects that cause any allies to be confused, frightened, paralyzed, slowed, or
stunned is decreased by 1d4 rounds (roll separately for each target). If the duration of any such
effect is reduced to 0 rounds or fewer, the effect ends for that ally. Finally, any allies lying
prone may stand up as an immediate action, provoking attacks of opportunity as normal.
