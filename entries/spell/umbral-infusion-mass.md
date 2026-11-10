+++
id = "ref/spell/umbral-infusion-mass"
kind = "spell"
title = "Mass Umbral Infusion"
aon = "SpellDisplay.aspx?ItemName=Umbral%20Infusion%2C%20Mass"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "umbral_infusion_mass", path = "json/spells11.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/umbral-infusion" },
]
[[sources]]
publication = "blood-of-shadows"
page = "31"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one mindless undead creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 8: Arcanist, Cleric, Oracle, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one mindless undead creature/level, no two of which can be more than 30 ft. apart
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Descriptors: shadow
:::

### Mass Umbral Infusion

This spell functions as [umbral infusion](ref/spell/umbral-infusion), except it can affect multiple
mindless undead creatures.
