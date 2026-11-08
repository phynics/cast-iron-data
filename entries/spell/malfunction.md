+++
id = "ref/spell/malfunction"
kind = "spell"
title = "Malfunction"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "malfunction", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/confusion" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "one construct" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Occultist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Area: one construct
:::

**Sources:** Ultimate Magic pg 228

This functions as [confusion](ref/spell/confusion), except it only affects constructs, and instead
of babbling incoherently, the construct takes no actions on its turn (but may still make attacks of
opportunity).
