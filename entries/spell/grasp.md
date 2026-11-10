+++
id = "ref/spell/grasp"
kind = "spell"
title = "Grasp"
aon = "SpellDisplay.aspx?ItemName=Grasp"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grasp", path = "json/spells5.json" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "9"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 0 },
  { class = "Bard", level = 0 },
  { class = "Cleric", level = 0 },
  { class = "Druid", level = 0 },
  { class = "Hunter", level = 0 },
  { class = "Magus", level = 0 },
  { class = "Oracle", level = 0 },
  { class = "Psychic", level = 0 },
  { class = "Skald", level = 0 },
  { class = "Sorcerer", level = 0 },
  { class = "Warpriest", level = 0 },
  { class = "Witch", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 immediate action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 0: Arcanist, Bard, Cleric, Druid, Hunter, Magus, Oracle, Psychic, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 immediate action
Components: V
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
:::

You can cast this spell as an immediate action when you fail a Climb check and would fall. You can
immediately attempt another Climb check as a free action at a -2 penalty. Each successive use of
this spell in a particular situation increases the penalty by 2. If successful, you don't fall, but
you don't progress at climbing.
