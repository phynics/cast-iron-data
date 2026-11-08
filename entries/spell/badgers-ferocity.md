+++
id = "ref/spell/badgers-ferocity"
kind = "spell"
title = "Badger's Ferocity"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "badgers_ferocity", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/keen-edge" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one weapon/3 levels" },
]
duration = "concentration"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Hunter, Occultist, Ranger, Red Mantis Assassin, Sorcerer, Wizard\
3: Cleric, Druid, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one weapon/3 levels
:::

**Sources:** Ultimate Magic pg 207

This functions like [keen edge](ref/spell/keen-edge), except it affects multiple weapons and
requires your concentration. You select the weapons to be affected, and can only affect one weapon
per creature. If a creature's weapon exceeds the spell's range, the spell ends for that weapon.
