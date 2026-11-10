+++
id = "ref/spell/homeward-bound"
kind = "spell"
title = "Homeward Bound"
aon = "SpellDisplay.aspx?ItemName=Homeward%20Bound"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "homeward_bound", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dismissal" },
]
[[sources]]
publication = "planar-adventures"
page = "41"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 minute"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one willing extraplanar creature" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Cleric, Oracle, Warpriest\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S
Range: touch
Target: one willing extraplanar creature
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes
:::

### Homeward Bound

This spell functions as [dismissal](ref/spell/dismissal), except as noted above.
