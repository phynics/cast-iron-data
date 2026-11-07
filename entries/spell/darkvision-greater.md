+++
id = "ref/spell/darkvision-greater"
kind = "spell"
title = "Greater Darkvision"
source_ids = ["core-rulebook", "ultimate-combat", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "darkvision_greater", path = "json/spells3.json" },
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

## Darkvision

**Sources:** PRPG Core Rulebook pg 264

The subject gains the ability to see 60 feet even in total darkness.
[Darkvision](ref/rule/darkvision) is black and white only but otherwise like normal sight.

[Darkvision](ref/rule/darkvision) can be made permanent with a [permanency](ref/spell/permanency)
spell.

### Communal Darkvision

**Sources:** Ultimate Combat pg 226

This spell functions like [darkvision](ref/rule/darkvision), except you may divide the duration in
1-hour intervals among the creatures touched.

### Greater Darkvision

**Sources:** Ultimate Magic pg 216

This spell functions as [darkvision](ref/rule/darkvision), except the target's darkvision has a
range of 120 feet.
