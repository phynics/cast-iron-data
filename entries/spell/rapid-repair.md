+++
id = "ref/spell/rapid-repair"
kind = "spell"
title = "Rapid Repair"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rapid_repair", path = "json/spells8.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "234"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "construct touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Occultist\
5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: construct touched
:::

The targeted construct gains [fast healing](ref/umr/fast-healing) 5. This does not stack with any
fast healing the construct already has. Fast healing has no effect on a construct that has been
brought to 0 hit points or destroyed.
