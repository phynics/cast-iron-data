+++
id = "ref/spell/adroit-retrieval"
kind = "spell"
title = "Adroit Retrieval"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "adroit_retrieval", path = "json/spells.json" },
]
[[sources]]
publication = "black-markets"
page = "30"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
:::

You instill the target with the ability to withdraw small items from her pockets or packs with
supernatural swiftness. When the target retrieves an item stored on itself, it can retrieve the item
either as a move action without provoking attacks of opportunity, or as a swift action that provokes
attacks of opportunity. This effect functions only when the target attempts to retrieve a stored
item that weighs less than 1 pound per caster level (maximum 15 pounds).
