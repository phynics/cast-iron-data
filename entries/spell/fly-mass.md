+++
id = "ref/spell/fly-mass"
kind = "spell"
title = "Mass Fly"
aon = "SpellDisplay.aspx?ItemName=Fly%2C%20Mass"
source_ids = ["core-rulebook", "advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fly_mass", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fly" },
]
[[sources]]
publication = "advanced-players-guide"
page = "223"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Elementalist Wizard", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F (a wing feather)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "10 minutes/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Elementalist Wizard, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a wing feather)
Range: close (25 ft. + 5 ft./2 levels)
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 10 minutes/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Mass Fly

This spell functions as [fly](ref/spell/fly), save that it can target numerous creatures and lasts
longer.
