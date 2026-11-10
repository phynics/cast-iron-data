+++
id = "ref/spell/spellcasting-contract"
kind = "spell"
title = "Spellcasting Contract"
aon = "SpellDisplay.aspx?ItemName=Spellcasting%20Contract"
source_ids = ["pathfinder-29-mother-of-flies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellcasting_contract", path = "json/spells9.json" },
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
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched; see text" },
]
duration = "permanent until discharged (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Cleric, Oracle, Warpriest
Casting time: 10 minutes
Components: V, S, DF
Range: touch
Duration: permanent until discharged (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched; see text
:::

### Spellcasting Contract

This spell functions like [lesser spellcasting contract](ref/spell/spellcasting-contract-lesser),
except if the target has 9 HD or more, you can imbue him with one or two 2nd-level spells and one
3rd-level spell.
