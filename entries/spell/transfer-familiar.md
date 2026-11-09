+++
id = "ref/spell/transfer-familiar"
kind = "spell"
title = "Transfer Familiar"
source_ids = ["familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "transfer_familiar", path = "json/spells10.json" },
]
[[sources]]
publication = "familiar-folio"
page = "23"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "your familiar and one willing creature" },
]
duration = "1 day/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 day/level (D)
Saving throw: none
Spell resistance: no
Target: your familiar and one willing creature
:::

You temporarily grant control of your familiar to another willing creature. You, your familiar, and
the target creature must all be touching each other when you cast this spell. The target gains all
the benefits and abilities normally associated with having a familiar, including the ability to
share spells, speak with the familiar, and so on. You lose all of these benefits for the duration of
the spell. If the target already has a familiar, the spell fails.
