+++
id = "ref/carried/ultimate-magic/spells/lend-judgment/greater"
kind = "spell"
title = "Lend Judgment, Greater"
source_ids = ["ultimate-magic"]
section = ["Spells", "Lend Judgment"]
tags = ["divination"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Magic/Spells/Lend Judgment/Greater", path = "ultimate_magic/spell/lend_judgment_greater.json" },
]

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
School: divination
Level: 5: Inquisitor
Casting Time: 1 standard action
Components: V, DF
Range: touch
Target: one ally
Duration: 1 round/level
Saving Throw: Will negates (harmless)
Spell Resistance: yes (harmless)
:::

_Ally receives all your judgments._

This functions as _[lend judgment](ref/spell/lend-judgment)_, except the ally gains the benefit of
all your active judgments.
