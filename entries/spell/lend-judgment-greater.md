+++
id = "ref/spell/lend-judgment-greater"
kind = "spell"
title = "Greater Lend Judgment"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lend_judgment_greater", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/lend-judgment" },
]
[[sources]]
publication = "ultimate-magic"
page = "227"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Inquisitor", level = 5 },
]
casting_time = "1 standard action"
components = "V, DF"
range = "touch"
effects = [
  { label = "Target", value = "one ally" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 5: Inquisitor
Casting time: 1 standard action
Components: V, DF
Range: touch
Target: one ally
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Lend Judgment

This functions as [lend judgment](ref/spell/lend-judgment), except the ally gains the benefit of all
your active judgments.
