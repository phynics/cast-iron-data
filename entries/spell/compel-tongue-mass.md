+++
id = "ref/spell/compel-tongue-mass"
kind = "spell"
title = "Mass Compel Tongue"
aon = "SpellDisplay.aspx?ItemName=Compel%20Tongue%2C%20Mass"
source_ids = ["advanced-players-guide", "black-markets", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "compel_tongue_mass", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/compel-tongue" },
]
[[sources]]
publication = "black-markets"
page = "24"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (a wooden block carved with a letter)"
range = "touch"
effects = [
  { label = "Target", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Bard, Skald\
5: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a wooden block carved with a letter)
Range: touch
Target: one creature/level, no two of which can be more than 30 ft. apart
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: yes
:::

### Mass Compel Tongue

This spell functions as [compel tongue](ref/spell/compel-tongue), except it affects multiple
creatures. The same language restriction applies to all creatures, and the same language must be
imparted to all creatures affected by the same casting on this spell.
