+++
id = "ref/spell/heightened-reflexes"
kind = "spell"
title = "Heightened Reflexes"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "heightened_reflexes", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "allies within a 30-ft.-radius burst centered on you" },
]
duration = "1 minute/level or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: 1 minute/level or until discharged
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: allies within a 30-ft.-radius burst centered on you
:::

**Sources:** Advanced Class Guide pg 184

You grant each of your allies within the area a +10 competence bonus on a single Reflex saving
throw. Each ally must decide whether to use the bonus before making the roll to which it applies.
When an ally uses the bonus, the spell ends for that individual.
