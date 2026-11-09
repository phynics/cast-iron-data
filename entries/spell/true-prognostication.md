+++
id = "ref/spell/true-prognostication"
kind = "spell"
title = "True Prognostication"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "true_prognostication", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/divination" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "228"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, M (incense and an appropriate offering worth 25 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium\
4: Cleric, Inquisitor, Oracle, Psychic, Shaman, Spiritualist, Warpriest, Witch
Casting time: 10 minutes
Components: V, S, M (incense and an appropriate offering worth 25 gp)
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

### True Prognostication

True prognostication functions as [divination](ref/spell/divination) except that the spell can see
up to 100 years into the future. Because of the extreme unpredictability of the far-distant future,
true prognostication is incredibly cryptic when used to learn about events on such large a scale.
