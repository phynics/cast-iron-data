+++
id = "ref/spell/stabilize-powder"
kind = "spell"
title = "Stabilize Powder"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stabilize_powder", path = "json/spells9.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "245"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a few drops of liquor)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "1 loaded firearm" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a few drops of liquor)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: 1 loaded firearm
:::

Ammunition currently loaded in the target firearm is less prone to misfire. Decrease the misfire
range by 1 + 1 per five caster levels (maximum +5, minimum misfire 0) for the ammunition currently
loaded into that firearm.
