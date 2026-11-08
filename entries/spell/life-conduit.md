+++
id = "ref/spell/life-conduit"
kind = "spell"
title = "Life Conduit"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "life_conduit", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Healing
:::

**Sources:** Ultimate Combat pg 233

You utilize life conduit to share hit points with your eidolon. While this spell is active, you can
spend a swift action to transfer 1d6 hit points between you and your eidolon, either taking damage
yourself and healing your eidolon or healing yourself and damaging your eidolon. If your eidolon
moves farther than 50 feet from you, this spell ends.
