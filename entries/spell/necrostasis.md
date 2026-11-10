+++
id = "ref/spell/necrostasis"
kind = "spell"
title = "Necrostasis"
aon = "SpellDisplay.aspx?ItemName=Necrostasis"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "necrostasis", path = "json/spells7.json" },
]
[[sources]]
publication = "inner-sea-temples"
page = "42"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a finger bone)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one undead creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Inquisitor, Oracle, Shaman, Spiritualist, Warpriest, Witch\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a finger bone)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one undead creature
:::

You drain necromantic energy from an undead creature, inducing a sluggish stupor. The target becomes
staggered. For the duration of the spell, dark wisps of energy seep out of the target creature. If
the target already has the staggered condition (as a zombie does), it becomes dazed for 1 round
instead.
