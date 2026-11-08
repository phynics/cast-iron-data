+++
id = "ref/spell/deathless"
kind = "spell"
title = "Deathless"
source_ids = ["mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deathless", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Alchemist, Arcanist, Cleric, Inquisitor, Investigator, Medium, Oracle, Psychic, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
:::

**Sources:** Mythic Adventures pg 113

The target's soul is strongly anchored to its body, preventing death from hit point damage. No
matter how low the target's hit points get, it remains alive (though not necessarily conscious).

This spell doesn't prevent death from sources other than hit point damage - such as Constitution
damage or drain, death effects, or energy drain. Spells that cure hit points affect the creature
normally.
