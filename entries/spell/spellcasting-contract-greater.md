+++
id = "ref/spell/spellcasting-contract-greater"
kind = "spell"
title = "Greater Spellcasting Contract"
source_ids = ["pathfinder-29-mother-of-flies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellcasting_contract_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spellcasting-contract-lesser" },
]
[[sources]]
publication = "pathfinder-29-mother-of-flies"
page = "68"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent until discharged (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Cleric
Casting time: 10 minutes
Components: V, S, DF
Range: touch
Target: creature touched
Duration: permanent until discharged (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Spellcasting Contract

This spell functions like [lesser spellcasting contract](ref/spell/spellcasting-contract-lesser),
except if the target has 13 HD or more you can imbue him with one or two 4th-level spells and one
5th-level spell.
