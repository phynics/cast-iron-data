+++
id = "ref/spell/protective-penumbra"
kind = "spell"
title = "Protective Penumbra"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protective_penumbra", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Cleric, Occultist, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: creature touched
Descriptors: darkness
:::

**Sources:** Ultimate Magic pg 233

This spell keeps the target slightly in shadow. A target with light blindness, light sensitivity, or
vulnerability to sunlight (such as vampires and wraiths) may ignore penalties from those qualities.
The spell gives the target a +2 bonus on saving throws against nonmagical hazards related to bright
light, such as glare or sunburn.
