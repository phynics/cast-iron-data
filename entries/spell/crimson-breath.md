+++
id = "ref/spell/crimson-breath"
kind = "spell"
title = "Crimson Breath"
aon = "SpellDisplay.aspx?ItemName=Crimson%20Breath"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crimson_breath", path = "json/spells3.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "160"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Arcanist, Cleric, Druid, Hunter, Investigator, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: no
Target: one creature
:::

When you cast this spell, your salivary glands transform and instantly fill with potent venom. Make
a ranged touch attack against a single target in range; if you hit, the target is affected by a dose
of [breath of the mantis god](ref/eq-poison/breath-of-the-mantis-god). The Fortitude save DC for
this poison is the same as the spell's DC, not the standard save DC for the poison.
