+++
id = "ref/spell/technomancy"
kind = "spell"
title = "Technomancy"
aon = "SpellDisplay.aspx?ItemName=Technomancy"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "technomancy", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-magic" },
]
[[sources]]
publication = "technology-guide"
page = "11"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (oil stirred with a coil of wires)"
range = "60 ft."
effects = [
  { label = "Target", value = "cone-shaped emanation" },
]
duration = "3 rounds/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (oil stirred with a coil of wires)
Range: 60 ft.
Duration: 3 rounds/level
Saving throw: none
Spell resistance: no
Target: cone-shaped emanation
:::

This spell functions as [detect magic](ref/spell/detect-magic), except it detects the presence of
technological objects instead of magical objects. The spell grants you the
[Technologist](ref/feat/technologist) feat for the purposes of attempting Knowledge (engineering)
checks to identify the properties of technological items in your possession. If you already possess
this feat, you gain a +10 bonus on Knowledge (engineering) checks to identify item properties.
