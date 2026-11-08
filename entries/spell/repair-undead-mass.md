+++
id = "ref/spell/repair-undead-mass"
kind = "spell"
title = "Mass Repair Undead"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "repair_undead_mass", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/repair-undead" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one undead creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Will half (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will half (harmless)
Spell resistance: yes (harmless)
Targets: one undead creature/level, no two of which can be more than 30 ft. apart
:::

**Sources:** Advanced Class Guide pg 191

This spell functions as [repair undead](ref/spell/repair-undead), except as noted above, and it
cures 1d8 points of damage + 1 point per caster level (maximum +20) on each selected creature.
