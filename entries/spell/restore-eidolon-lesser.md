+++
id = "ref/spell/restore-eidolon-lesser"
kind = "spell"
title = "Lesser Restore Eidolon"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "restore_eidolon_lesser", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
]
casting_time = "3 rounds"
components = "V, S"
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
Level: 2: Summoner, Unchained Summoner
Casting time: 3 rounds
Components: V, S
Range: touch
Target: eidolon touched
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Subschool: Healing
:::

**Sources:** Ultimate Magic pg 235

This spell functions as [lesser restoration](ref/spell/restoration-lesser), except it only affects
an eidolon.

### Restore Eidolon

**Sources:** Ultimate Magic pg 235

This spell functions as [restoration](ref/spell/restoration), except it only affects an eidolon.
