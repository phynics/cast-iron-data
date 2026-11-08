+++
id = "ref/spell/speak-with-waves"
kind = "spell"
title = "Speak with Waves"
source_ids = ["core-rulebook", "elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "speak_with_waves", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/stone-tell" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 7 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 6: Druid, Hunter, Psychic\
7: Shaman
Casting time: 10 minutes
Components: V, S, DF
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
:::

### Speak with Waves

**Sources:** Elemental Master's Handbook pg 14

This spell functions as [stone tell](ref/spell/stone-tell) but allows conversations only with a body
of standing or flowing fresh water at least as large as you are. Flowing water can generally speak
about events happening upstream but not events happening downstream.
