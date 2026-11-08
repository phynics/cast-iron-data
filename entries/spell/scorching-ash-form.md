+++
id = "ref/spell/scorching-ash-form"
kind = "spell"
title = "Scorching Ash Form"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "scorching_ash_form", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/gaseous-form" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["fire"]
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S, M (a bit of gauze and a handful of ashes)"
range = "touch"
effects = [
  { label = "Target", value = "willing corporeal creature touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Arcanist, Investigator, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: S, M (a bit of gauze and a handful of ashes)
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: willing corporeal creature touched
Descriptors: fire
:::

**Sources:** Advanced Race Guide pg 131

> _[Ifrits](ref/race/ifrit) have access to the following spell._

This spell functions like [gaseous form](ref/spell/gaseous-form), except the target becomes a
visible swirl of hot ash and smoke instead of harmless translucent gas. The target gains the fire
subtype. Any creature that begins its turn sharing a space with the target takes 2d6 points of fire
damage and must make a Fortitude save (DC 15, + 1 per previous check) or suffer the effects of
[smoke inhalation](ref/rule/forest-fires).
