+++
id = "ref/spell/golden-guise"
kind = "spell"
title = "Golden Guise"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "golden_guise", path = "json/spells5.json" },
]
[[sources]]
publication = "agents-of-evil"
page = "31"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (10 gold pieces)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one object weighing no more than 5 lbs./level" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Bard, Skald\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (10 gold pieces)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: one object weighing no more than 5 lbs./level
:::

You cause an object to briefly transform into gold. Affected items gain the properties of gold until
the spell expires. Weapons reduce their [hardness](ref/umr/hardness) by half and gain the
[fragile](ref/misc/fragile) quality, while piercing and slashing weapons take a -2 penalty on damage
rolls (minimum 1 damage). This spell increases the affected item's armor check penalty by 2 and
decreases its armor or shield bonus by 2. Gold armor has hardness 5.
