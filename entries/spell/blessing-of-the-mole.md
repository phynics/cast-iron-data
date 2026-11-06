+++
id = "ref/spell/blessing-of-the-mole"
kind = "spell"
title = "Blessing of the Mole"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blessing_of_the_mole", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "1 creature/level" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Cleric, Hunter, Inquisitor, Oracle, Paladin, Ranger, Warpriest
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes (harmless)
Area: 1 creature/level
:::

**Sources:** Ultimate Magic pg 208

The targets gain [darkvision](ref/rule/darkvision) 30 feet and a +2 competence bonus on Stealth
checks.
