+++
id = "ref/spell/darkvision-greater"
kind = "spell"
title = "Greater Darkvision"
source_ids = ["core-rulebook", "ultimate-combat", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darkvision_greater", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/darkvision" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (either a pinch of dried carrot or an agate)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Antipaladin, Arcanist, Hunter, Investigator, Medium, Occultist, Psychic, Ranger, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (either a pinch of dried carrot or an agate)
Range: touch
Target: creature touched
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Darkvision

**Sources:** Ultimate Magic pg 216

This spell functions as [darkvision](ref/spell/darkvision), except the target's darkvision has a
range of 120 feet.
