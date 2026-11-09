+++
id = "ref/spell/restore-eidolon"
kind = "spell"
title = "Restore Eidolon"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "restore_eidolon", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/restoration" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
]
casting_time = "1 minute"
components = "V, S, M (diamond dust worth 100 gp or 1,000 gp, see text)"
range = "touch"
effects = [
  { label = "Target", value = "eidolon touched" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Summoner, Unchained Summoner
Casting time: 1 minute
Components: V, S, M (diamond dust worth 100 gp or 1,000 gp, see text)
Range: touch
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: eidolon touched
Subschool: Healing
:::

### Restore Eidolon

**Sources:** Ultimate Magic pg 235

This spell functions as [restoration](ref/spell/restoration), except it only affects an eidolon.
