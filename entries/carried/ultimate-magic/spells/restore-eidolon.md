+++
id = "ref/carried/ultimate-magic/spells/restore-eidolon"
kind = "spell"
title = "Restore Eidolon"
source_ids = ["ultimate-magic"]
section = ["Spells"]
tags = ["conjuration", "healing"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Restore Eidolon", path = "ultimate_magic/spell/restore_eidolon.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Summoner", level = 3 },
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
School: conjuration (healing)
Level: 3: Summoner
Casting Time: 1 minute
Components: V, S, M (diamond dust worth 100 gp or 1,000 gp, see text)
Range: touch
Target: eidolon touched
Duration: instantaneous
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_Restoration for an eidolon._

This spell functions as _[restoration](ref/spell/restoration)_, except it only affects an eidolon.
