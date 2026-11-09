+++
id = "ref/spell/spindrift-spritz"
kind = "spell"
title = "Spindrift Spritz"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spindrift_spritz", path = "json/spells9.json" },
]
[[sources]]
publication = "elemental-masters-handbook"
page = "14"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["water"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Hunter, Paladin, Ranger\
2: Cleric, Druid, Inquisitor, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 immediate action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
Subschool: Healing
Descriptors: water
:::

You can cast this spell only as a response to a target attempting a saving throw against an effect
that would cause the fatigued, shaken, sickened, or staggered conditions. The target can roll its
saving throw twice and take the higher result.
