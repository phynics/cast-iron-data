+++
id = "ref/carried/ultimate-combat/spells/life-conduit/greater"
kind = "spell"
title = "Life Conduit, Greater"
source_ids = ["ultimate-combat"]
section = ["Spells", "Life Conduit"]
tags = ["conjuration", "healing"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Life Conduit/Greater", path = "ultimate_combat/spell/life_conduit_greater.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Summoner", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
+++

::: statblock
School: conjuration (healing)
Level: 5: Summoner
Casting Time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 1 round/level
:::

_You transfer 3d6 hit points to your eidolon as a swift action._

This spell functions like _[life conduit](ref/spell/life-conduit)_, except you can transfer 3d6 hit
points as a swift action.
